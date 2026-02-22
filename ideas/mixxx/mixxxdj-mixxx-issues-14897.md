# Last years project description

**Parent:** Mixxx — Project Ideas
**Source:** https://github.com/mixxxdj/mixxx/issues/14897
**Scraped:** 2026-02-22T23:28:47.631410

---

## [GSoC 2025 Antonio Giordano] Multi-Genre & Autocompletion Support Implementation (Detailed Project Overview)

## Project Summary

The goal of this project was to implement a robust and flexible system for managing multiple genres per track within Mixxx. Currently, Mixxx allows only a single genre per track, which is limiting for detailed and personal music cataloging. This project will introduce the ability for Mixxx to understand what "a genre is" in order to associate multiple genres with each track, manage these genres centrally and integrate these features into the user interface mechanisms. The changes will be based on Mixxx's existing architecture, with a focus on backward compatibility and usability, addressing needs identified in the [community survey](https://mixxx.zulipchat.com/#narrow/channel/109122-general/topic/.5BSuvey.5D.20Improving.20Genre.20Management/with/520183015).

## Progress Track Table
*(**Tasks** implemented via separate Pull Requests, linked here in the track progress table below.)*
*(**Test** implemented in a single PR, linked here below in the track progress table.)*

(**Please note that every PRs depends on the first one** -> [PR#1](https://github.com/mixxxdj/mixxx/pull/14898)

---

| Phase                                                        | Sub-Phase ID | Task Description                                                                                                                                                                                                                                                                                                                        | Status    | PR Link(s)     |
| :----------------------------------------------------------- | :----------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------- | :------------- |
| **Backend Foundation** | ---          | *Establish the database schema and a robust Data Access Object (DAO) layer for all multi-genre operations.* |           |                |
|                                                              | **1.1** | **Database Schema Definition & Initial Migration** | `✅ Done` | [`PR#1`](https://github.com/mixxxdj/mixxx/pull/14898) |
|                                                              | **1.2** | **Core `TrackDAO` Extensions for Multi-Genre CRUD** | `✅ Done` | [`PR#2`](https://github.com/mixxxdj/mixxx/pull/15145) |
|     **Final Test**                                                | **v1.0** | **Development/testing branch** | `✅ Done` | [`PR#5`](https://github.com/mixxxdj/mixxx/pull/15182)  |
|     **Newspost**                                                |  | **The Final Blog Post on** [Mixxx Official Website](https://github.com/mixxxdj/mixxx/issues/mixxx.org) | `✅ Done` | [`PR#6`](https://github.com/mixxxdj/website/pull/403)  |

# What We Did

## 1.1 Data Model & Schema (`schema.xml`)

Before touching the backend and UI, we aligned the **schema** to support feature end-to-end.

### 1.1.1 Covered schema Requirements

- **Stable Genre ID:** Each genre has a unique integer ID, used in RAW placeholders `##id##`. This allows renaming/restructuring without breaking track references.
- **Hierarchy (multi-level names):** Each genre may have a `parent` (tree). We support **multi-level names** to facilitate importing external models (e.g., **Discogs**), which is already integrated.
- **Lookup & Uniqueness:** Display names are unique; dedicated indexes enable efficient **autocomplete** and **name→id** mapping.
- **Backward Compatibility:** The `library.genre` field remains a **string**: it can contain `##id##` placeholders **and** unmapped literals. Migration is **gradual**.
- **Gradual migration:** Utilities (e.g., *Edit Orphan Genres*) let users convert legacy strings to IDs **without blocking** workflows.
- **Join table for performance:** We use the association table **`genre_tracks`** because indexing **multiple values** inside a **string** (e.g., `library.genre`) is not well supported by SQLite. Indexing **IDs** in a join table is **much faster** and improves UX (filters, counts, tree).

### 1.1.2 RAW genre format in track records

In **TrackRecord**, the `genre` field is a `;`-separated string whose tokens are:

- `##<id>##` if the genre exists in the tree (mapped),
- a **literal** if it is not yet mapped.

**Example:**

`##12##`; `##34##`; `Italo Disco`

This ensures **stable persistence** (IDs don’t change), while the UI continues to show **human-readable names** **through the table delegates**.

**Normalization (ingress/egress):**

- split on `;`, trim, **case-insensitive dedup**, and preserve **order** where meaningful.

---

## 1.2 Backend [GenreDao and Domain Rules]

All mapping/normalization logic is centralized in **GenreDao** and the **`genre_tracks`** join table. The UI does not duplicate rules; visual formatting is handled by the Track Table’s **delegates**.

### 1.2.1 DAO APIs & responsibilities

- **Autocomplete:** `getGenreNameList()` → list of names for `QCompleter`.
- **Name→ID:** `getGenreId(name)` → case-insensitive resolution; returns **1** if not found.
- **RAW→Display:** `getDisplayGenreNameForGenreID(raw)` → converts RAW (mix of `##id##` + literals) to **user names** joined by `;` (used by **delegates**).
- **Display→RAW:** where needed (e.g., single-track dialog) we convert display names to ID placeholders when available, keeping literals for orphans.

**Why DAO + table delegates**

- **Single source of truth** for data/rules: no divergence between dialogs and the tree.
- **Delegates** control presentation (consistent human names everywhere).
- We can change caching/lookup without touching UI code.

### 1.2.2 RAW codec (algorithm)

**Deserialization (RAW→display):**

1. `split(';')`, `trim()`, drop empties;
2. for each token:
    - if `##n##` → resolve `n` to a name via DAO;
    - else keep the **literal**;
3. **case-insensitive dedup**, rejoin with `"; "`.

**Serialization (display→RAW):**

1. `split(';')`, `trim()`, drop empties;
2. for each name: `id = getGenreId(name)`
    - if `id != -1` → emit `##id##`;
    - else emit the **literal**;
3. **case-insensitive dedup**, rejoin with `";"`.

### 1.2.3 Orphans: discovery and resolution

At startup (or when validating), every token in the `genre` field **not resolved** to an ID is treated as an **orphan**. Flow (**right-click** the tree root → **Edit Orphan Genres**):

- We show detected orphans. For a string `"part1 part2 part3"`, we show **both** the full string **and** tokens `"part1"`, `"part2"`, `"part3"`.
- **If we want to keep the full string** as a genre, we **add that first** and apply → the tokens disappear (the string now has an ID).
    
    **Additionally**: the string in `library.genre` is **rewritten**, replacing literals with **`##genre_id##`** placeholders.
    
- When **new tracks** arrive with plain strings in the `genre` field, the **orphan detector** helps quickly link them to the correct genres (Add/Link).

**Supported actions:**

- **Add:** creates a new genre in the tree → rewrites RAW, replacing literals with `##id##`.
- **Link:** links an orphan to an existing genre → same rewrite.

### 1.2.4 Tree model and related operations

- **Track selection → highlighting:** when a track is selected, the genres containing it are shown in **bold** (crate-like UX).
- **Counts and duration:** each genre displays **track count** and **aggregated duration**.
- **Drag & Drop:** dragging tracks from the Tracklist onto a node **assigns** the genre (DAO serializes with `##id##` and updates `genre_tracks`).
- **Context menu → Tracks → Genres:** quick (de)selection in a crate-like fashion, consistent with DAO/`genre_tracks`.
- **F2 rename** on a node: changes the **name**, **not** the ID. After pressing *Enter*, for index/counter consistency, the relevant **`genre_tracks`** rows are **regenerated** (delete+recreate), **without** rewriting files or losing ID associations.
- **Genre node context actions (right-click on a genre):**
    - **Edit genre:** set multilevel relationships (parent/child), toggle **is_visible**, and define the **concatenated display name**.
    - **Make all genres visible:** one-click operation to set **is_visible = true** for the entire tree.
    - **Edit multiple genres:** bulk-edit **visibility** and **display_group** for selected genres.
    - **Model-defined flag:** **is_model_defined** (for genres imported from external models) is **read-only** and **cannot be changed**.

---

## 1.3 UI [Consistent Tag Editor (Single & Multi)]

### 1.3.1 Single-track (`DlgTrackInfo`)

- **Control architecture:** The `.ui` container `txtGenre` hosts a horizontal `QScrollArea` with **fixed height** and a **thin scrollbar**; inside, a `QWidget` with `QHBoxLayout` containing **chips**: `QFrame#genreChip` + `QLabel(name)` + `QToolButton("×")`.
- **Style/visual parity:** Palette and metrics aligned (padding/radius/spacing), with a white **×** and subtle hover/pressed feedback.
- **Behavior:** Autocomplete via `QCompleter` (DAO); Add/Remove; saving **display→RAW** with placeholders when IDs exist; **case-insensitive dedup** and order preservation.
- **Name formatting:** In the track table, presentation is handled by **table delegates** (consistent human names).

### 1.3.2 Multi-track (`DlgTrackInfoMulti`) **Experimental**

- **Visual parity with single-track.** Same layout, palette, scrollbar, and tags:
    - same metrics (padding, radius, spacing),
    - same thin scrollbar,
    - same chips (look & feel, “×” hover/pressed).
- **Batch semantics:** On open, we show the **intersection** of common genres (case-insensitive). User actions accumulate:
    - `m_pendingAdd` (lowercase set),
    - `m_pendingRemove` (lowercase set).
        
        On **Apply/OK**, for each track: RAW→display (DAO) → `−pendingRemove` → `+pendingAdd` (dedup) → **display→RAW** (DAO) and update `genre_tracks`.
        
- **Modes:**
    - **Add:** union with existing genres;
    - **Replace:** full replacement.
- **Legacy combobox variant:** We also keep a variant with the **legacy combobox** (crate-style selections) as an **open question for the community** from a UX standpoint.

### 1.3.3 Edit Orphan Genres flow (UI)

- **Access:** Right-click the **tree root** → **Edit Orphan Genres**.
- **View:**Orphan list; multi-word strings appear both as full strings and as tokens.
- **UX note:** If you need the full string, **add it first** and apply; tokens disappear.
- **Actions:** **Add** (create new genre) or **Link** (map to existing); both rewrite RAW with `##id##` and update `genre_tracks`.

---

## 1.4 Technical rationale and trade-offs

- **`##genre_id##` placeholders.**
    
    **Pros:** renames/restructures do not break metadata; **incremental migration**; easy debugging.
    
    **Cons:** RAW is less human-readable; mitigated because the UI always shows **names** via **table delegates**.
    
    **Note:** the placeholder format is **open for discussion** if the community prefers alternatives.
    
- **Why `genre_tracks`.**
    
    Indexing **IDs** in a join table is **robust and fast**; indexing **tokens** inside `library.genre` (a string) is fragile/slow in SQLite. Using `genre_tracks` improves filters, counts, and the **TreeModel** (which now relies on it directly).
    
- **DAO + Delegates.**
    
    Rules remain centralized in the **DAO** consistent **presentation** comes from **delegates** in the table. This cleanly separates data from UI and reduces duplication.
    
- **UI choices.**
    - Visual parity between single and multi reduces cognitive friction.
    - The **thin scrollbar** and  “×” improve live ergonomics.
    - The **horizontal chip layout** scales better with many genres, avoiding intrusive text wrap.

# Current State of The Project

## Before vs. Now (Brief Overview)

**Before**

Mixxx accepted multiple genres in a **single text field**. Everything was treated as a **flat string**:

- no notion of **individual tags** (e.g., “Dance” distinct from “Electronic”);
- no **structured genre database**;
- impossible to **query/filter/validate** individual genres;
- cumbersome editing: removing one genre meant editing the entire string;
- no **autocomplete** or **normalization** (e.g., “Electronic” vs “electronic”).

**Now**

We introduced **stable IDs**, a **hierarchical tree**, a **DAO** for mapping, and a **chip-based UI** (single & multi) with **gradual** migration from string literals.

In practice: Mixxx **understands** genres, **manages** them as entities, and **uses** them throughout (tree, dialogs, drag & drop, counts) without breaking compatibility.

---

## 2.1 Data & Schema (current)

- **Stable IDs + hierarchy:** Each genre has a unique ID and an optional **parent** (tree, multi-level supported).
- **Join table `genre_tracks`:** All *track ↔ genre* relations are normalized and indexed by ID → **fast** queries and counts.
- **Compatibility.** The `library.genre` field remains a **string**: it can contain both **`##id##` placeholders** and **unmapped literals** (gradual migration).
- **Consolidated RAW format.** `;` as separator; token = `##<id>##` (mapped) **or** literal (orphan).
    - Example: `##12##; ##34##; Italo Disco`.
    - Normalization: split/trim, **case-insensitive dedup**, preserve order.

---

## 2.2 Backend (operational state)

- **GenreDao = single source of truth.**
    - **Autocomplete:** provides the name list (for `QCompleter`).
    - **Name→ID:** case-insensitive resolution.
    - **RAW→Display / Display→RAW:** centralized codec (emit placeholders when an ID exists, otherwise keep literals), with normalization rules.
- **Orphan detector:** Unmapped strings are **orphans**: handled by the “Edit Orphan Genres” flow (Add/Link), which **rewrites** RAW with `##id##` where possible.
- **Performance:** The TreeModel and filters operate on `genre_tracks` (IDs), not string parsing → better **responsiveness**.

---

## 2.3 Tree Model & Interactions (current)

- **Backed by `genre_tracks`:** The tree reads hierarchy and associations via the join table.
- **Track-genre highlighting.** When a track is selected, the genres that contain it are shown in **bold** (crate-like UX).
- **Counts and duration.** Each node shows **track count** and **aggregated duration**.
- **Drag & Drop from Tracklist.** Dropping tracks onto a genre **assigns** the ID (DAO serializes to placeholders, join table updated).
- **Context menu (Tracks → Genres).** Quick (de)selection consistent with DAO/`genre_tracks`.
- **Rename (F2).** Changes **only the name**; the ID stays the same. On confirm, relevant `genre_tracks` rows are **regenerated** (delete+recreate) to keep counts/indexes aligned, without touching files. The completer works for every new start of a genre, if you want to add 3 genres you'll have 3 times the QCompleter

<img width="449" height="267" alt="Image" src="https://github.com/user-attachments/assets/a0f496bf-a128-4975-ab53-67df17e95794" />
<img width="441" height="433" alt="Image" src="https://github.com/user-attachments/assets/bbc00668-b04f-4b59-adfa-1574aecee79a" />
<img width="446" height="432" alt="Image" src="https://github.com/user-attachments/assets/871aa649-b386-4d1b-b623-ed05a3c00770" />

---

## 2.4 UI Single-track (`DlgTrackInfo`) (current)

- **Tag editor:** The `txtGenre` host contains a horizontal `QScrollArea` with **fixed height** and a **thin scrollbar**; inside, compact chips (label + white “×”, subtle hover/pressed).
- **Operational features.**
    - **Autocomplete** with `QCompleter` (fed by the DAO).
    - **Add/Remove** tags.
    - **Save** using the **Display→RAW** codec (placeholder when the ID exists; literal otherwise).
    - **Delegates:** the Track Table consistently shows **names** everywhere.

<img width="1280" height="712" alt="Image" src="https://github.com/user-attachments/assets/acd3d6e4-f285-4a0f-bda3-b2fa319c2628" />

<img width="388" height="297" alt="Image" src="https://github.com/user-attachments/assets/9fb5e5e0-c62e-402a-9328-d4e2a0d934a6" />

<img width="570" height="420" alt="Image" src="https://github.com/user-attachments/assets/4c577dfe-a51a-4a28-ad62-35877f781d43" />

<img width="573" height="335" alt="Image" src="https://github.com/user-attachments/assets/ca3d8dc2-f155-48bb-b2ac-0583b9252185" />

---

## 2.5 UI  Multi-track (`DlgTrackInfoMulti`) **[Experimental]** (current)

- **Visual parity with single.** Same layout, palette, metrics, scrollbar, and “×”.
- **Batch semantics.**
    - On open, we show the **intersection** of genres **common** to all selected tracks.
    - User actions produce `m_pendingAdd` / `m_pendingRemove` (lowercase).
    - **Apply/OK:** for each track → DAO **RAW→Display** → `−pendingRemove` → `+pendingAdd` (**dedup**) → **Display→RAW** (DAO) → update `genre_tracks`.
- **Modes.** **Add** (union) and **Replace** (total replacement).
- **Legacy combobox variant.** Available as an **experimental option** for community feedback.

<img width="1276" height="735" alt="Image" src="https://github.com/user-attachments/assets/b8329960-b7df-41a5-8a01-62f4ca18cdf1" />
<img width="567" height="357" alt="Image" src="https://github.com/user-attachments/assets/e68f6e89-3913-4c21-aab6-bf0aae7c0aee" />
<img width="715" height="178" alt="Image" src="https://github.com/user-attachments/assets/58f4ffbd-6e47-4cf4-86df-d72e5efa69e8" />

---

## 2.6 Orphan Genres (current flow)

- **Active detection.** Unmapped tokens are listed as **orphans**.
- **Edit Orphan Genres UI:** Access via **right-click** on the tree root.
- **Multi-word tokenization:** For “part1 part2 part3” we show both the full string and the individual tokens.
- **Actions.**
    - **Add:** creates a new genre and **rewrites** RAW to `##id##`.
    - **Link:** links to an existing genre with the same rewrite.

<img width="417" height="263" alt="Image" src="https://github.com/user-attachments/assets/59f23ef5-c529-4a20-92ec-86488c34e7c5" />
<img width="796" height="179" alt="Image" src="https://github.com/user-attachments/assets/ac3d344d-d0b6-4392-8f13-b3ebd2dfdb2e" />
<img width="792" height="193" alt="Image" src="https://github.com/user-attachments/assets/7eebb69c-2701-4e97-a9ba-4f2b3367253f" />
<img width="792" height="193" alt="Image" src="https://github.com/user-attachments/assets/91eb52af-ae72-49a8-bd9f-6b4e277658bf" />
<img width="875" height="707" alt="Image" src="https://github.com/user-attachments/assets/e90e9f6b-89ba-4059-9ce7-b3719c9fb4b3" />

---

## 2.7 Compatibility & Migration (current)

- **Zero lock-in:** Legacy strings **keep working**; migration to `##id##` happens **incrementally** via Add/Link and the new editors.
- **External model import:** **Multi-level names** enable importing external models (e.g., Discogs) consistent with the tree.

---

## 2.8 What’s “done” vs. “experimental”

### Done

- schema + join table;
- DAO + RAW codec;
- TreeModel on `genre_tracks`; on `genres` for structure, on `genre_tracks` for members
- highlighting, counts, duration;
- drag & drop;
- context menu;
- single-track tag editor;
- orphan flow;
- normalization and placeholders;
- delegates for consistent display.

### Experimental

- **multi-track** editor (same layout, batch semantics);
- `##id##` placeholder format (if the community prefers alternatives).

# Challenges and Important Things We Learned

This project wasn’t “just code”: we had to make architectural decisions, solve unforeseen issues, and adjust our approach as the scope solidified.

## Key Challenges

### 1) Defining the right architecture (scope and layering)

- **Challenge:** Moving Mixxx from a single free-text field to a **multi-value, hierarchical genre system** required solid foundations. Jumping straight into full hierarchy increased risk and testing complexity.
- **Decision:** We adopted an **incremental path** started with flat simple table: extend the data model (stable IDs + join table), use `##id##` placeholders in RAW for compatibility, introduce a **DAO** as the source of truth and **table delegates** for presentation; then ship the single-track chip UI and, finally, the “experimental” multi-track editor.
- **Outcome:** A clear layering (schema → DAO → tree/operations → dialogs) that lets us evolve (hierarchies, model import) without constant refactors.

### 2) Schema migration and database design

- **Challenge:** Support multiple genres per track with performance and consistency.
- **Decision:** Introduce `genres` (unique IDs, optional parent, multilevel names) and the **join table `genre_tracks`** to normalize *track↔genre*. Keep `library.genre` as a **string** for **backward compatibility**, with `##id##` tokens and/or literals.
- **Technical rationale:** In SQLite, indexing **tokens inside a string** is weak; indexing **IDs** in a relational table is **robust and fast** (filters, counts, tree).
- **Result:** Safe migration, responsive queries, and a solid base for tree features (counts, duration, highlighting).

### 3) Normalization and mapping in the **DAO**

- **Challenge:** Avoid duplicating logic across the UI and model, ensuring a single set of rules for: splitting on `;`, trimming, **case-insensitive dedup**, preserving order; **RAW→display** and **display→RAW** (placeholders when an ID exists).
- **Decision:** Centralize everything in **GenreDao**:
    - `getGenreNameList()` for autocomplete;
    - `getGenreId(name)` (case-insensitive resolution);
    - `getDisplayGenreNameForGenreID(raw)` (RAW→names codec);

### 4) Orphan detection & rewriting

- **Challenge:** Recognize legacy strings in `genre` and offer an “adoption” flow without blocking workflows.
- **Decision:** Implement **Edit Orphan Genres** to ****detect unmapped tokens, handle multi-word strings by showing the **full string** and its **parts**; support **Add** (create genre) and **Link** (map to existing), rewriting RAW with `##id##` and updating `genre_tracks`.
- **Outcome: Gradual migration**, guided UX, and a tree that stays consistent over time.

### 5) Integrating with the **TreeModel** and operations

- **Challenge:** Drive the tree from `genre_tracks` while keeping UX
- **Decisions:**
    - The tree is backed by `genre_tracks` (not by parsing `library.genre`).
    - **F2 rename** changes only the **name**; the **ID** is stable. On confirmation, relevant `genre_tracks` rows are **regenerated** (delete+recreate) to keep counts/indexes consistent: without touching files.
    - **Edit genre** (right-click on a genre): set multilevel names, **is_visible**, and the **concatenated name**; bulk actions (**make all genres visible**, **edit multiple genres** for `is_visible` and `display_group`). `is_model_defined` (for model-imported genres) **cannot** be changed.
- **Outcome:** Coherent, fast operations with a crates-like UX.

### 6) Dialog UX (single and multi)

- **Challenge:** Build a **tag-based tag editor** that is readable, unobtrusive, and consistent across single- and multi-track; in multi-track, avoid overwriting genres that are unique to certain tracks.
- **Decisions:**
    - **Single-track:** host `txtGenre` → horizontal `QScrollArea` (fixed height, thin scrollbar) → compact chips (label + **×**).
    - **Multi-track (experimental):** **visual parity** with single-track, but **batch semantics**: show the **intersection** of genres; maintain `m_pendingAdd`/`m_pendingRemove`; on **Apply/OK** do per-track application (RAW→display → −remove → +add → display→RAW), updating `genre_tracks`. Modes **Add**/**Replace**.
    - Keep a **legacy combobox** variant as an option for community feedback.
- **Outcome:** Consistent, ergonomic UI ready for iterative feedback.

---

## Important Things We Learned

- **A single source of truth pays off.**
    
    Using a **DAO** for rules and **delegates** for presentation eliminated duplication and made dialogs thinner (less local logic, more reliability).
    
- **Separate compatibility from correctness.**
    
    `##id##` placeholders in RAW give **stability** (renames/restructures don’t break references) while keeping **backward compatibility** with existing strings and enabling **gradual** migration via the orphan flow.
    
- **Performance: design for indexes, not for parsing.**
    
    Moving relationships to `genre_tracks` simplified queries and counts, improving **responsiveness** of the tree and actions (drag&drop, filters).
    
- **Tree operations with stable IDs = less I/O, more safety.**
    
    With stable IDs, **F2 rename** doesn’t touch files; we only regenerate `genre_tracks` to keep counts consistent. It’s a **safe**, fast compromise.
    
- **Tooling as an ally.**
    
    Working with CI, clang-tidy, and clazy improved code quality and reduced regressions, making the refactor more sustainable.

# What More is Needed

We’ve laid the foundations (stable IDs, `genre_tracks`, DAO, RAW codec, tree & chip-UI). The next step is to **refine the experience**, close the loop with the wider ecosystem, and scale to real-world hierarchical structures. Below is a **concrete but lightweight** roadmap, intended to be discussed and prioritized with the community.

## 1) A truly hierarchical (multi-level) tree

Bring the tree fully in line with **multi-level names**: enable drag & drop across levels, create/move sub-genres, and edit attributes (visibility, display group) consistently across the hierarchy.

**Goal:** natural navigation and maintenance for deep trees.

## 2) Feedback-driven dialog improvements

Polish the single/multi dialogs based on community input:

- confirm or revisit the **legacy combobox** variant in multi (currently “experimental”);
- improve **accessibility** and **shortcuts** (keyboard-only flows, focus ring, textual announcements);
- micro-UX for add/remove, placeholders, and completer behavior.

## 3) Search across `genres.names`

Extend the **search bar/filters** to include **genre names** (and concatenated names) in addition to track columns.

**Impact:** find tracks and genres when starting from the taxonomy itself.

## 4) Correct multi-genre separators when exporting tags to files

When writing metadata via TagLib, ensure the **format-correct** separator/encoding:

- ID3v2 (multiple frames vs single frame with separators),
- Vorbis/Opus/FLAC (repeated keys),
- MP4/M4A (multiple atoms).

Align what Mixxx shows with what actually gets written **to files**.

## 5) Preference for the tag separator in track metadata

Add a setting to choose the **preferred separator** (e.g., `;`, `/`, or true multiple frames/atoms where supported), with per-format mapping. This lets export adapt to user habits and external tooling.

## 6) Conversion logic for external taggers (Picard/MusicBrainz, Mp3tag/Discogs)

Introduce **normalized import** rules/heuristics:

- recognize separators used by taggers,
- immediately map to known **IDs** (placeholders) when possible,
- handle variants/synonyms (e.g., “EDM” ↔ “Electronic Dance Music” when defined by the model).

## 7) Optional automation on import

New preference: during **library scans**, if a genre token matches the table, automatically convert it to a `##id##`**placeholder** (instant adoption). Alternatively, a “suggest & confirm” mode.

## 8) Import/Export of the genre structure

Extend import/export (CSV/JSON) to share **genre trees** between users:

- merge strategies (add/union/ignore),
- preserve attributes (visibility, display group; keep `is_model_defined` immutable),
- version and document the format.

## 9) QCompleter with fuzzy match (Levenshtein)

Make autocomplete **typo-tolerant** (“dacn” → **dance**) without losing current prefix/substring capabilities.

## My Experience with Mixxx

### Why Mixxx?

I come from DJing and music production: I wanted a project where code has a **tangible impact** on how music is **played** and **organized**. GSoC was the perfect excuse to stop watching from the sidelines and really dive into open source. Mixxx convinced me because it’s **technical**, **demanding**, and at the same time **close to real-world use**: every architectural choice lands straight on the DJ booth, with real workflows, tight timing, and the need for reliability.

### Collaboration & reviews

Working with my mentor and the community pushed me to justify every decision, not just the **how**, but the **why**. I learned to:

- write **narrative PRs**, explaining what changes, how to test it, and which regressions are avoided;
- iterate quickly on feedback while balancing robustness and delivery time;
- maintain consistent style and quality, treating quality tools as allies rather than obstacles.

### How I plan to keep contributing

This experience was a **springboard** into open source and, especially, into the Mixxx community. It was a great opportunity to get involved, and even after GSoC I want to **stay active** and have a role in this organization.

I know I still have a lot to learn on the programming side, and I’m **sure** this is the right place to grow. I also know I can bring value **beyond code**.

I’m ready to **keep contributing** and to take on growing responsibility across different areas, with the same care I put into preparing a DJ set: attention to detail, a steady pace, and rock-solid reliability.



