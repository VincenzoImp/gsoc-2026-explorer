# issue tracker

**Parent:** omegaUp — Project Ideas
**Source:** https://github.com/omegaup/omegaup/issues
**Scraped:** 2026-03-10T16:58:40.249928

---

## #9492: [FEATURE] Batch inserts in insert_school_of_the_month_candidates to reduce database round-trips

**Labels:** feature-request

## Description

While looking through `stuff/cron/school_of_the_month.py`, I noticed that the function `insert_school_of_the_month_candidates` inserts rows into `School_Of_The_Month` using a loop that executes one `INSERT` query per candidate.

Currently the code follows this pattern:

```python
for index, row in enumerate(candidates):
    cur.execute(...)
```

This means one database call is made for every candidate.
In practice the list is limited to 100 entries, but it still results in multiple database round-trips when the cron runs.

## Proposed Improvement

Instead of executing one query per row, the inserts could be batched using `executemany()`.

The idea would be to collect the parameters first and then execute the insert in a single batch:

```rows = [
    (row.school_id, first_day_of_next_month, index + 1, row.score)
    for index, row in enumerate(candidates)
]

cur.executemany(SQL_QUERY, rows)
```
This keeps the SQL exactly the same while reducing the number of database round-trips.This keeps the SQL exactly the same while reducing the number of database round-trips.

### Why this might help

- Fewer database calls during the cron execution
- Simpler insert logic
- No change in behavior or ranking logic

---

## #9489: [BUG]:Docker dev environment: db-migrate.py fails because /.my.cnf is missing for non-ubuntu users

**Labels:** bug

## Checklist

- [x] I have searched existing issues and confirmed this is not a duplicate (Required)

## Current Behavior

When running the Docker development environment on macOS with `docker compose up`, the `developer-environment` supervisor program fails because it cannot find `~/.my.cnf`. The Dockerfile copies the MySQL config to `/home/ubuntu/.my.cnf`, but when the container runs as `UID_GID` (e.g., `501:20` on macOS), `$HOME=/`. The file `/.my.cnf` does not exist, so `db-migrate.py` and all MySQL commands in `developer-environment.sh` fail. This results in database migrations never running, missing tables (e.g., `Coder_Of_The_Month`), and HTTP 400/500 errors when accessing `localhost:8001`.

## Expected Behavior

The Docker development environment should work out of the box on macOS. Database migrations should run successfully on first boot regardless of the container user's `$HOME` directory, and the site should be accessible at `localhost:8001` without manual intervention.

## Steps to Reproduce

1. Clone the omegaup repo on macOS
2. Run `docker compose up`
3. Wait for all services to start
4. Visit `localhost:8001` — observe HTTP 400 Bad Request
5. Run `docker compose exec frontend cat /home/ubuntu/.my.cnf` — file exists
6. Run `docker compose exec frontend bash -c 'echo $HOME'` — outputs `/`
7. Run `docker compose exec frontend cat /.my.cnf` — file not found

**Root cause:** In `stuff/docker/Dockerfile.dev-php`, line 70:
```dockerfile
COPY ./my.cnf /home/ubuntu/.my.cnf

---

## #9482: [BUG]Node version mismatch during local setup causes yarn install failure

**Labels:** bug

## Problem

While setting up omegaUp locally using Docker, I encountered a Node.js version mismatch during `yarn install`.

The project documentation suggests using Node 18, but some dependencies (such as Cypress) expect Node >=20.

This caused the following error:

error cypress@15.7.0: The engine "node" is incompatible with this module.
Expected version "^20.1.0 || ^22.0.0 || >=24.0.0".
Got "18.17.1"

Because of this, `yarn install` fails during the container setup.

## Steps to reproduce

1. Clone the repository
2. Run:

docker compose up

3. The frontend container runs `yarn install`
4. Installation fails due to Node version mismatch.

## Workaround

Running the following command allowed the installation to continue:

yarn install --ignore-engines

However, this is only a workaround and may not be the ideal solution.

## Possible solution

- Update the recommended Node version in the setup documentation
- Or adjust dependency engine requirements

## Environment

OS: Windows 11  
Node version used: v22.12.0 (host)  
Node version inside container: v18.17.1

## Additional context

This issue may affect new contributors setting up the project locally for the first time.

@Yashagarwal9798

---

## #9478: [BUG] AI editorial worker crash-loops in frontend container due to missing Python dependencies

**Labels:** bug

## Checklist

- [x] I have searched existing issues and confirmed this is not a duplicate (Required)

## Current Behavior

When running `docker compose up` with the default setup, the `ai-editorial-worker` program inside the `frontend` container enters an infinite crash loop, flooding the logs with:

`frontend-1 | ModuleNotFoundError: No module named 'anthropic'`
`frontend-1 | INFO exited: ai-editorial-worker (exit status 1; not expected)`
`frontend-1 | INFO spawned: 'ai-editorial-worker' with pid ...`

This happens because:
1. `stuff/docker/etc/supervisor/supervisord.conf` defines `[program:ai-editorial-worker]` which runs `worker.py` inside the frontend container using the venv at `/opt/omegaup/stuff/venv`.
2. `stuff/docker/usr/bin/developer-environment.sh` only installs from `stuff/requirements.txt`  it never installs `stuff/ai_editorial_worker/requirements.txt`.
3. The AI worker dependencies (`anthropic`, `openai`, `google-generativeai`, `redis`) are thus missing from the venv.
4. Supervisor is set to `autorestart=true`, causing it to endlessly respawn the crashing process.

## Expected Behavior

The `ai-editorial-worker` should either start successfully inside the frontend container or not crash-loop. All required Python dependencies (including AI worker requirements) should be installed during the initial Docker environment setup.

## If necessary, add the following information (otherwise delete this section):

**Steps to Reproduce:**
1. Clone the repository using `git clone --recurse-submodules https://github.com/omegaup/omegaup`
2. Run `docker compose up`
3. Observe the repeated `ModuleNotFoundError: No module named 'anthropic'` in the `frontend-1` logs.

**Suggested Fix:**
Add the following line after in `stuff/docker/usr/bin/developer-environment.sh` to ensure the AI dependencies are installed:
`python3 -m pip install -r /opt/omegaup/stuff/ai_editorial_worker/requirements.txt`

_Relevant details about the environment in which you encountered this bug:_
* **Browser name:** N/A (Backend/Docker issue)
* **Operating System and version:** Any (Docker-based dev environment)
* **Link to the site where this issue occurs:** Localhost Docker environment
* **Files involved:** `supervisord.conf`, `developer-environment.sh`, `requirements.txt`

---

## #9477: [ENHANCEMENT] Mobile UI: Course search input appears cramped and placeholder text gets truncated

## Current Behavior
On mobile view, the search input field in the **Courses → Enrolled courses** page appears cramped. The placeholder text inside the search box is truncated (for example, it shows **"Course nar"** instead of the full text), which makes it harder to understand the purpose of the input field.

This occurs when viewing the page on small screen sizes such as **iPhone SE (375 × 667)** using browser developer tools.

## Expected Behavior
The search input field should have enough width so the placeholder text is fully visible and readable on mobile devices. The layout should adjust responsively so that the search box does not appear compressed.

## Steps to Reproduce
1. Open the **Courses** page.
2. Navigate to **Enrolled courses**.
3. Enable mobile view in the browser (e.g., iPhone SE – 375 × 667).
4. Observe the search input field.

## Environment
- Device: Mobile (tested using Chrome DevTools)
- Screen size: 375 × 667
- Browser: Chrome

## Possible Improvement
- Increase the width of the search input on small screens.
- Adjust responsive styling so the placeholder text is not truncated.

## Screenshot

<img width="1610" height="881" alt="Image" src="https://github.com/user-attachments/assets/03ffca0d-5b54-4a8f-8f46-96e74ee40ca9" />

---

## #9472: Performance: Enhance Scoreboard Performance using SQL Window Functions

## Description:

Currently, the scoreboard generation in Scoreboard.php and Runs.php fetches all submissions for a problemset and processes them within PHP to find the best run per user. This leads to high memory consumption and slow response times in large contests with thousands of submissions.

## Proposed Solution:
    1. SQL Optimization: Refactored Runs::getProblemsetRuns to use MySQL 8.0 Window Functions (ROW_NUMBER()). This allows the database to return only the best run per identity per problem, significantly reducing the data transferred to PHP.
    2. Logic Simplification: Simplified the loops in Scoreboard::getScoreboardFromRuns and Scoreboard::calculateEvents to reflect that incoming data is already pre-filtered and ranked by the database.

## Database Indexing:
To maximize the performance of the PARTITION BY and ORDER BY operations within the Window Functions, I recommend adding a composite index on the Submissions table. This will allow the database engine to perform an index scan instead of a full table scan:

SQL
ALTER TABLE Submissions 
ADD INDEX idx_problemset_ranking (problemset_id, status, type, identity_id, problem_id, submission_id);

## Expected Impact:
    1. Time Complexity: Reduced from $O(N)$ processing in PHP (where $N$ is total runs) to $O(M)$ (where $M$ is total unique student-problem pairs).
    2. Memory Footprint: Significant reduction in RAM usage for the web server during scoreboard updates.


## Update:
I have refactored the SQL queries in getProblemsetRuns to ensure full compatibility with MySQL's only_full_group_by mode, which was causing the CI failures.
    - The optimized path now uses a subquery to rank submissions before selecting specific columns.
    - The standard path has also been updated to avoid incorrect grouping.
    - All scoreboard-related calls now correctly utilize the onlyBest parameter for maximum performance.

---

## #9470: [FEATURE] Improve performance of update_user_rank in update_ranks.py

**Labels:** feature-request

# Improve performance of `update_user_rank` in `update_ranks.py`

While going through `stuff/cron/update_ranks.py`, I noticed something in `update_user_rank()` (and similarly `update_author_rank()`) that might be worth revisiting from a performance perspective.

Right now, the function:

- Computes ranking information in Python.
- Iterates over all ranked users.
- Executes one `INSERT ... ON DUPLICATE KEY UPDATE` per user.
- Commits at the end.

So effectively, if there are **N ranked users**, we end up doing **N individual database writes from Python**.

This works correctly, but as the number of users grows, this could become expensive. For large installations with tens of thousands of users, this results in a large number of round-trips between Python and MySQL during a single cron execution.

## Possible Improvement

Since the ranking logic is already computed in Python, the database writes could potentially be **batched** instead of executing one query per user.

For example, instead of executing one query per row from Python, the writes could potentially be batched using `executemany()` while keeping the SQL and ranking logic unchanged.

This could reduce the number of database round-trips and improve cron execution time for installations with many users.

---

## #9469: [ENHANCEMENT] Improve mobile responsiveness of submissions table to avoid horizontal scrolling

## Current Behavior

On the `/submissions` page, the submissions are displayed in a wide table layout.  
On smaller screens (for example 375px mobile width), the table overflows the viewport and requires horizontal scrolling to view all columns.

This makes it difficult for users to quickly read submission details on mobile devices.

## Expected Behavior

On smaller screens, the submissions list should adapt to a mobile-friendly layout instead of requiring horizontal scrolling.

Each submission row could be displayed as a stacked **card layout**, where the information is presented vertically. For example:

-----------------------------
Date & Time: 3/7/2026, 9:15 PM  
Coder: JM13-1  
Problem: A + B LL  
Language: C++  
Verdict: Accepted  
-----------------------------

This card-style layout would allow users to view all important information clearly without horizontal scrolling and improve readability on mobile devices.

## Steps to Reproduce

1. Open the `/submissions` page
2. Open browser developer tools
3. Switch to a mobile viewport (e.g., 375px width or iPhone SE)
4. Observe that the table requires horizontal scrolling

## Environment

- Device width: ~375px
- Browser: Chrome
- Page: `/submissions`

## Possible Improvement

- Convert table rows into stacked cards on small screens
- Alternatively hide less important columns on smaller viewports

## Screenshot

<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/db91db46-ca95-45cf-a032-2c889f37f594" />

---

## #9468: [BUG] Edit Contest page: browser back button changes URL hash but doesn't update page content

**Labels:** bug

## Checklist

- [x] I have searched existing issues and confirmed this is not a duplicate (Required)

## Current Behavior

On the **Edit Contest** page (`/contest/{alias}/edit/`), clicking the navigation tabs (Edit, Add Problems, Admission Mode, Contestants, Admins, Links, Clone, Archive, Certificates) updates the page content and changes the URL hash correctly. However, when pressing the **browser back button**, only the URL hash changes  the page content remains stuck on the last tab that was clicked.

## Expected Behavior

When the browser back button is pressed, the page content should update to match the URL hash, just like when clicking a tab directly.

## If necessary, add the following information (otherwise delete this section):

**Steps to reproduce:**

1. Go to any contest's edit page (`/contest/{alias}/edit/`)
2. Click on the **"Clone"** tab → content changes to Clone, URL becomes `#clone`
3. Click on the **"Links"** tab → content changes to Links, URL becomes `#links`
4. Press the **browser back button** → URL changes back to `#clone`, but the page still shows the **Links** tab content

## Additional Context
A similar issue was previously fixed in another part of the platform.

Reference issue:
https://github.com/omegaup/omegaup/issues/9392

Reference PR:
https://github.com/omegaup/omegaup/pull/9396

The solution implemented there can be used as a reference.


https://github.com/user-attachments/assets/9078add9-07ac-4743-bfb3-c74c64b2e40d

---

## #9466: [FEATURE] Table layout breaks on mobile in school profile page

**Labels:** feature-request

## Description
On the school profile page (`/schools/profile/{id}`), the users table does not render properly on small screens. When viewed on mobile devices, the table layout collapses and the **"Place" column header appears vertically stacked**, making the UI difficult to read.

## Steps to Reproduce
1. Open https://omegaup.com/schools/profile/{id}/
2. Enable mobile view in the browser (e.g., iPhone SE – 375px width using Chrome DevTools).
3. Scroll to the **"Users who belong to this school"** section.

## Current Behavior
- The table becomes poorly formatted on small screens.
- The **"Place" column header breaks into multiple lines**, showing each letter vertically.
- Overall table readability is reduced and the layout appears broken.

## Expected Behavior
The table should remain readable on small screens. Column headers should not collapse vertically and the layout should adjust responsively to fit mobile devices.

## Possible Cause
This may be due to insufficient responsive styles for the table layout or column width constraints on small screen sizes.

## Screenshot

<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/b9a91d49-8fb9-4873-88d6-435fd14729ed" />

---

## #9465: [FEATURE] Score column overflows container on small screens in school rankings page

**Labels:** feature-request

## Description
On the **school rankings page** (`/rank/schools`), the **Score column appears too close to the right edge of the container on small screens**, causing the values to look cramped and partially outside the card container.

## Steps to Reproduce
1. Open https://omegaup.com/rank/schools
2. Enable mobile view in the browser (for example **iPhone SE – 375px width** using Chrome DevTools).
3. Observe the **Score** column in the ranking table.

## Current Behavior
The score values (e.g., `135823.00`, `51093.00`) appear too close to the right edge of the container and look misaligned or slightly overflowing outside the card on smaller screens.

## Expected Behavior
The **Score column should stay properly aligned within the container**, with enough right padding so that the values do not appear cramped or overflow on mobile devices.

## Possible Cause
This may be due to insufficient padding or responsiveness issues in the table layout for smaller screen widths.

## Screenshot

<img width="1634" height="771" alt="Image" src="https://github.com/user-attachments/assets/90f20316-ac2d-4238-b2ed-a603a68ab8a7" />

---

## #9462: [BUG] Course arena assignment navigation shows '-' when no previous/next assignment exists

## Checklist

- [x] I have searched existing issues and confirmed this is not a duplicate (Required)

## Current Behavior

<img width="1253" height="910" alt="Image" src="https://github.com/user-attachments/assets/8864a8fd-ec7d-4343-b5e4-bea7888c3c7e" />

When a student views the **first assignment** in a course via the old arena (`/course/<alias>/assignment/<alias>#problems`), the **previous assignment navigation button** is rendered as a **disabled button with the text `-`** (a dash). Similarly, the last assignment shows a `-` button for the next assignment.

Additionally, the **breadcrumb** in the left sidebar (`NavbarProblems.vue`) uses inline `>` characters as separators. In the narrow sidebar layout these separators wrap onto their own lines, making the breadcrumb appear visually broken (separator floats alone on a line with nothing beside it).

There is also a potential problem: `NavbarAssignments.vue` line 8 has:
```js
@click="$emit('navigate-to-assignment', previousAssignment.alias)"
```
Even though the button is `:disabled`, accessing `.alias` on a `null` value is unsafe.

## Expected Behavior

- When there is no previous (or next) assignment, the navigation button should be **hidden entirely**, not shown as a disabled `-` button. The newer `Coursev2.vue` already does this correctly with `v-if="previousAssignment"`.
- The breadcrumb should render correctly in narrow widths - use CSS-based separators (`::before` pseudo-element or Bootstrap's `.breadcrumb` component) instead of inline `>` text characters.

## Steps to Reproduce

1. Open a course that has assignments as a student
2. Navigate to the **first assignment**: `/course/<alias>/assignment/<first-assignment-alias>#problems`
3. In the left sidebar, observe the navigation buttons at the bottom
4. The left (previous) button shows only **`-`** with no label and no icon

## Relevant details

- File: Already mentioned above.- Browser: Chrome / Firefox (any)
- URL: `http://localhost:8001/course/<alias>/assignment/<first-assignment-alias>#problems`

---

## #9461: [FEATURE] Show per-problem solve count in contest arena Scoreboard

## Checklist

- [x] I have searched existing issues and confirmed this is not a duplicate (Required)

As a **contest participant**, I want **to see how many contestants have solved each problem in the scoreboard header** so that **I can gauge the relative difficulty of problems and make better strategic decisions during a contest**.

## Context

<img width="1903" height="331" alt="Image" src="https://github.com/user-attachments/assets/192aff58-6453-48e8-adbc-a02009172ce0" />

In most competitive programming platforms (Codeforces, ICPC), the scoreboard header for each problem column shows the number of accepted submissions (e.g. **"A (147 AC)"**). This helps contestants quickly identify which problems are easier (many solves) or harder (few solves) without leaving the scoreboard.

Currently, `frontend/www/js/omegaup/components/arena/Scoreboard.vue` renders problem columns using only the alias (line 60):

```vue
<th v-for="(problem, index) in problems" :key="problem.alias">
```

The `Scoreboard` type in `api_types.ts` exposes `problems: { alias: string; order: number }[]` - there is no `accepted_count` field. Neither the API response for `/api/contest/scoreboard/` nor the `Scoreboard` TypeScript interface includes per-problem acceptance counts.

### How has this issue affected you?

- During a contest, it is impossible to tell which problems are widely solved vs. unsolved without individually opening each problem
- This information is already computed server-side (the DB tracks accepted submissions per problem) but is not in the scoreboard

### Files involved:

- `frontend/www/js/omegaup/components/arena/Scoreboard.vue` - render solve count in `<th>`
- Backend: `Scoreboard` API response and `types.Scoreboard` interface - add `accepted_count` per problem

---

## #9460: [BUG] [Urgent] After creating a problem, HTTP/1.1 400 - Bad Request

**Labels:** bug

## Checklist

- [x] I have searched existing issues and confirmed this is not a duplicate (Required)

## Current Behavior
After creating a problem, We are getting : HTTP/1.1 400 - Bad Request

Curl request:

```
curl 'https://omegaup.com/problem/aaaaaaaaa44/edit/' \
  -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8' \
  -H 'accept-language: en-US,en;q=0.8' \
  -H 'cache-control: max-age=0' \
  -b 'github_oauth_state=hveyFrXEA5nbrmK5; PHPSESSID=44gb45i7bu3hqqvcolr1j6ir32; has-visited-signup=true; has-visited-login=true; g_state={"i_l":0,"i_ll":1772875682647,"i_e":{"enable_itp_optimization":17}}; ouat=e87b69afb86275cf4eba0d8dcb3d94-320273-c9d5b2d748fd6e9c58f1cc8b74868baad61a8973f3f40a6a37c8a754d9adadb9; has-visited-problem-creator=true; has-visited-code-tab=true; has-visited-cases-tab=true; has-visited-solution-tab=true; has-visited-create-problem=true' \
  -H 'priority: u=0, i' \
  -H 'referer: https://omegaup.com/problem/new/' \
  -H 'sec-ch-ua: "Not:A-Brand";v="99", "Brave";v="145", "Chromium";v="145"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  -H 'sec-fetch-dest: document' \
  -H 'sec-fetch-mode: navigate' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-fetch-user: ?1' \
  -H 'sec-gpc: 1' \
  -H 'upgrade-insecure-requests: 1' \
  -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36'
```

https://github.com/user-attachments/assets/b0263eb4-0005-4452-a831-cfa5355398cc

_Describe what happened instead of what was expected._

## Expected Behavior
After creating a new problem , We should go to edit problem page.
_Describe what you were originally trying to do and how you expected the platform to behave._

## If necessary, add the following information (otherwise delete this section):

[https://omegaup.com/problem/new](https://omegaup.com/problem/new)

_Provide a link to an example, or a detailed list of steps to reproduce this bug._

    1. Go to problem new page. 
    2. Fill up the form and hit submit.
    3. Currently api fails and error page appears.

---

## #9458: [FEATURE] Show assignment deadline and overdue badge in student's AssignmentCard

## Description

As a **student**, I want to see the **deadline (due date)** for each assignment directly on the course homepage so that I can prioritize my work and never miss a submission deadline.

## Context
### Student View:
<img width="1508" height="884" alt="Image" src="https://github.com/user-attachments/assets/c9e9ddc3-38cf-438b-bc6d-7f83e4f72006" />

### Admin View:
<img width="1454" height="523" alt="Image" src="https://github.com/user-attachments/assets/52275e90-d618-4968-b8fb-29078a95fac3" />

The API `/api/course/listAssignments/` already returns `finish_time` for every assignment. However, the `AssignmentCard.vue` component , which renders each assignment as a card on the student's course homepage **does not display this date at all**.

Currently `AssignmentCard.vue` receives a `studentProgress` prop and shows a progress bar, but has no `finish_time` prop and renders no deadline information. Students have no way to know when an assignment is due without clicking into it.

### How has this issue affected you?

- Students cannot tell which assignments are overdue vs. still open from the course homepage
- Two assignments that are already past their deadline (`finish_time < now`) look identical to open ones
- There is no visual badge or indicator for "Overdue" assignments

## Proposed Solution

In `frontend/www/js/omegaup/components/course/AssignmentCard.vue`:

1. Add a `finishTime: Date` prop
2. Display the due date below the assignment name (e.g. _"Due: Mar 13, 2026 at 2:19 PM"_)
3. Add an **"Overdue"** badge (e.g. `badge badge-danger`) when `finishTime < now`

## Files Involved

- `frontend/www/js/omegaup/components/course/AssignmentCard.vue` : add `finishTime` prop and deadline display
- `frontend/www/js/omegaup/course/student.ts`  : pass `finish_time` from API response to component

## Verification

Visit any enrolled course as a student:- the assignment cards show **no due date**, even though the API returns `finish_time` for all assignments.

```
GET /api/course/listAssignments/?course_alias=<alias>
-> assignments[].finish_time  ,, exists in API, missing in UI
```

---

## #9455: [BUG] "Or upload the file" label and file input break onto separate lines on mobile

**Labels:** bug

## Current Behavior

On the Problem Creator page (`/problem/creator/`), when viewing the Code tab on mobile (e.g., iPhone 12 Pro, 390px width), the **"Or upload the file"** label and the **"Choose File"** button are on **separate lines** instead of sitting next to each other on the same line.

This happens because the label uses `col-12` for small screens, which forces it to take the full width and pushes the file input below it.

In `CodeTab.vue` (lines 42–57):
```html
<div class="form-group row mt-3 align-items-center">
  <label class="col-12 col-sm-auto ...">    <!-- col-12 = full width on mobile -->
    Or upload the file
  </label>
  <div class="col-12 col-sm-auto ...">       <!-- also col-12 = drops to next line -->
    
  </div>
</div>
```

On desktop (`col-sm-auto`), both sit side by side. On mobile (`col-12`), each takes the full row width, so they stack vertically.

## Expected Behavior

The label ("Or upload the file") and the file input ("Choose File") should appear on the **same line** on all screen sizes, just like the "Language" label and its dropdown above it.

## If necessary, add the following information (otherwise delete this section):

1. Go to `omegaup.com/problem/creator/`
2. Click the "Code" tab
3. Open browser DevTools and switch to a mobile view (e.g., iPhone 12 Pro, 390px)
4. Scroll down to the "Or upload the file" section
5. Notice that the label and file input are stacked on two lines instead of one

*Relevant details about the environment in which you encountered this bug:*

* Happens on mobile screen widths (below 576px where `col-sm` breakpoint kicks in)
* File: `frontend/www/js/omegaup/components/problem/creator/code/CodeTab.vue` (lines 42–57)


<img width="1069" height="1021" alt="Image" src="https://github.com/user-attachments/assets/d9531880-bba1-4964-92f4-cd54ed7db692" />

---

## #9454: [BUG] Tab navigation wraps to two lines on Female Coder of the Month page

**Labels:** bug, Good first issue

## Current Behavior

On the Female Coder of the Month page (`/coderofthemonth/female/`), the tab navigation bar wraps to **two lines** because the female-specific tab titles are longer than the overall page titles. The third tab ("List of candidates to female coder of the month") gets pushed to a second row, breaking the visual layout.

On the Overall Coder of the Month page (`/coderofthemonth/`), all three tabs fit on a single line without issue.

**Tab title comparison (English):**

| Tab | Overall page | Female page |
|-----|-------------|-------------|
| Tab 1 | "Coders of the Month" (19 chars) | "Female coders of the Month" (26 chars) |
| Tab 2 | "Top 100 coders of the previous month" (36 chars) | "Top 100 coders of the previous month" (36 chars) |
| Tab 3 | "List of candidates to coder of the month" (40 chars) | "List of candidates to female coder of the month" (48 chars) |

The tab container (`.ranking-width`) has `max-width: 55rem`, and the `.nav-link` has `padding: 0.65rem 1rem`. The longer female titles push the total width past the container, causing the third tab to wrap.

The CSS in `List.vue` (lines 141–163) does not handle this overflow scenario  there is no `flex-wrap: nowrap`, `overflow-x: auto`, `font-size` adjustment, or responsive `padding` reduction.

## Expected Behavior

All three tabs should fit on a single line on both the Overall and Female Coder of the Month pages, matching the visual layout consistently.

## If necessary, add the following information (otherwise delete this section):

1. Go to `omegaup.com/coderofthemonth/female/`
2. Observe that "List of candidates to female coder of the month" wraps to a second line
3. Compare with `omegaup.com/coderofthemonth/` where all three tabs fit on one line

*Relevant details about the environment in which you encountered this bug:*

* Reproducible on standard desktop browser widths
* File: `frontend/www/js/omegaup/components/coderofthemonth/List.vue` (lines 141–163, scoped styles)

<img width="1900" height="708" alt="Image" src="https://github.com/user-attachments/assets/23bac59f-0b1f-4c07-affa-353278a41b92" />

---

## #9453: [BUG] Double back-button required to exit Coder of the Month page

**Labels:** bug, Good first issue

## Current Behavior

When navigating to the Coder of the Month page from the OmegaUp main page, the user must click the browser's Back button **twice** to return to the main page. This affects **both** pages:
- **Overall Coder of the Month** → `/coderofthemonth/`
- **Coder of the Month (Her)** → `/coderofthemonth/?category=female`

Both pages share the same entry point: `frontend/www/js/omegaup/coderofthemonth/index.ts` (lines 13-15), which automatically sets a default hash on the URL when the page loads without one:
```typescript
  const locationHash = window.location.hash.substring(1).split('/')[0];
  const selectedTab = getSelectedValidTab(locationHash);
  if (selectedTab !== locationHash) {
    window.location.hash = selectedTab; // ← Pushes a new history entry
  }
```
Setting `window.location.hash` directly forces the browser to push a new entry to the session history. This means immediately upon loading either page, the history becomes:
1. `omegaup.com`
2. `omegaup.com/coderofthemonth/`
3. `omegaup.com/coderofthemonth/#codersOfTheMonth`

Clicking Back once only resolves the hash (returning to step 2). A second click is needed to return to the main page.

## Expected Behavior

Navigating to either Coder of the Month page should only create a single history entry. Clicking the Back button once should return the user to the previous page.

## If necessary, add the following information (otherwise delete this section):

**Reproduce on Overall Coder of the Month:**
1. Go to `omegaup.com`
2. Navigate to the Overall Coder of the Month page 
3. Notice the URL instantly changes to append `#codersOfTheMonth`
4. Click the browser's Back button once — notice you are still on the Coder of the Month page
5. Click Back a second time to actually return to the previous page

**Reproduce on Coder of the Month (Her):**
1. Go to `omegaup.com`
2. Navigate to the Coder of the Month (Her) page 
3. Same behavior — the URL gets `#codersOfTheMonth` appended, and Back must be clicked twice


https://github.com/user-attachments/assets/bc7201c9-5735-44f1-a84f-abcf25f3af72

---

## #9452: [BUG] `renderMermaidDiagrams` returns `void` instead of `Promise`, silently swallowing errors

**Labels:** bug

## Current Behavior

The `renderMermaidDiagrams` method in `markdown.ts` (line 585) returns `void` instead of `Promise<void>`. It starts an `import('mermaid')` promise on line 595 but does **not** return it:

```typescript
public renderMermaidDiagrams(container: HTMLElement): void {
  // ...
  import('mermaid')        // ← promise NOT returned
    .then((mermaidModule) => { /* ... */ })
    .catch((error) => { console.error(...); });
}
```

In `ProblemMarkdown.vue` (lines 169–175), the caller tries to `await` this method:

```typescript
private async renderMermaid(): Promise<void> {
  try {
    await this.markdownConverter.renderMermaidDiagrams(this.root);
    // ↑ await gets `undefined`, resolves immediately
  } catch (error) {
    console.error('Error rendering Mermaid diagrams:', error);
    // ↑ This NEVER catches mermaid errors
  }
}
```

Since the method returns `void`, the `await` resolves immediately with `undefined`. If Mermaid fails to load or render, the error is only logged inside `markdown.ts` and never reaches the caller's `catch` block.

## Expected Behavior

Errors from Mermaid loading/rendering should propagate to the caller so they can be properly caught and handled by `ProblemMarkdown.vue`.



*Relevant details about the environment in which you encountered this bug:*

* Not environment-specific  this is a code-level bug
* Files: `frontend/www/js/omegaup/markdown.ts` (lines 585, 590–591, 595) and `frontend/www/js/omegaup/components/problem/ProblemMarkdown.vue` (lines 169–175)

---

## #9451: [BUG] `preview` prop in ProblemMarkdown.vue is a no-op (hardcoded to `false`)

**Labels:** bug, Good first issue

## Current Behavior

The `ProblemMarkdown.vue` component accepts a `preview` prop on **line 44**, but the markdown converter on **line 49** ignores it and hardcodes `preview: false`:

- Line 44 declares the prop:
  ```typescript
  @Prop({ default: false }) preview!: boolean;
  ```
- Line 49 hardcodes it:
  ```typescript
  markdownConverter = new markdown.Converter({ preview: false });
  ```

When a parent passes `preview=true`, the converter still renders full download panels (`panel panel-default` divs) instead of the simpler icon-based preview format defined in [markdown.ts](https://github.com/omegaup/omegaup/blob/main/frontend/www/js/omegaup/markdown.ts) (lines 66–72). The prop is silently ignored.

## Expected Behavior

When `preview=true` is passed, the converter should use the simplified icon-based templates (e.g., a `<code class="libinteractive-download">` element with a download glyph icon) instead of the full panel HTML.


*Relevant details about the environment in which you encountered this bug:*

* Not environment-specific — this is a code-level bug
* File: `frontend/www/js/omegaup/components/problem/ProblemMarkdown.vue` (lines 44, 49)

---

## #9448: [BUG] Fix signup redirect when accessing a course via shared URL

**Labels:** bug

## Current Behavior
When a user opens a course using a **shared URL** while not logged in, the page correctly displays the course description and a **Log in** option.

However, the **Sign up** option is not clearly presented.

If the user proceeds with the signup process, they are always redirected to the **Profile page** instead of returning to the course page they originally opened.

https://github.com/user-attachments/assets/55463a9c-94f4-4805-a495-b51ba1772d27

## Expected Behavior
When a user signs up after accessing a course through a shared URL, they should be redirected back to the course page so they can proceed with the enrollment process.

Additionally, the interface should clearly provide both **Log in** and **Sign up** options.

## Steps to Reproduce

1. As a course organizer, create a new course.
2. In the Admission Mode, select the option to allow access via Shared URL.
3. Copy the generated course URL.
4. Open the shared URL in a browser while not logged in.
5. Click Sign up.
6. Complete the registration process.
7. Observe the page where the user is redirected after signing up.

---

## #9447: [FEATURE] Improve empty state for student list in courses

**Labels:** feature-request, Good first issue

## Description
As a course administrator, I want a clearer interface when a course has no students yet so that I understand how to add them.

## Context
When there are no students enrolled in a course, the interface could display an **empty state** that includes:

- An icon
- A title
- A short explanation
- A centered button to add students

This pattern would match the improved empty states proposed in other parts of the course interface similar Github does in some sections
<img width="790" height="449" alt="Image" src="https://github.com/user-attachments/assets/aaef36c0-b297-4a64-9b90-ea2de89f51bb" />

---

## #9446: [FEATURE] Improve empty state when no problems are added to course content

**Labels:** feature-request, Good first issue

## Description
Currently, when editing the content of a course (such as an assignment or test), the **Add problem** button appears in the bottom-right corner of the interface.

When there are already problems in the list, this placement works well. However, when the content has no problems yet, the interface looks empty and the button can be easy to miss.

As a suggestion we can display an empty state similar to Github does in some sections:

- Show a centered placeholder inside the card.
- Include a short title explaining that there are no problems yet.
- Include a brief description encouraging the user to add the first problem.
- Display the Add problem button centered in this empty state.

<img width="790" height="449" alt="Image" src="https://github.com/user-attachments/assets/aaef36c0-b297-4a64-9b90-ea2de89f51bb" />


Once the user adds the first problem, the interface should return to the current layout, where the button appears in the bottom-right corner.

---

## #9445: [Bug] Browser back button does not update displayed tab on edit course page

**Labels:** feature-request, Good first issue

## Current Behavior
When navigating between tabs in the **Edit course** page, using the browser's **Back button** does not update the visible tab correctly.

## Expected Behavior
Using the browser's Back button should correctly update the displayed tab.

## Additional Context
A similar issue was previously fixed in another part of the platform.

Reference issue:
#9392

Reference PR:
#9396

The solution implemented there can be used as a reference.

---

## #9444: [Bug] Warn users about unsaved problems when leaving the “Add course content” page

**Labels:** feature-request, Good first issue

## Current Behavior
When adding problems to course content, users can select problems but they are not saved until they click the **Add content** button.

If the user leaves the page before clicking that button, the selected problems are lost without any warning.

## Expected Behavior
If problems have been selected but the **Add content** button has not been clicked, the browser should warn the user before leaving the page.

This can be implemented using the browser's native **unsaved changes warning**.

---

## #9443: [FEATURE] Improve empty course content state by centering the “Add content” button

**Labels:** feature-request, Good first issue

## Description
As a course administrator, I want a clearer interface when a course has no content so that I know how to start adding material.

## Context
When a course does not yet contain any content, the **Add content** button appears in the bottom-right corner.

This can make it less visible for new users.

A better empty state could include:

- A centered **Add content** button
- A short title
- A brief description explaining what to do

This approach is similar to how GitHub displays empty states in some sections:
<img width="790" height="449" alt="Image" src="https://github.com/user-attachments/assets/aaef36c0-b297-4a64-9b90-ea2de89f51bb" />

---

## #9442: [FEATURE] Add Markdown editor (Pagedown controls) to course description and objectives

**Labels:** feature-request, Good first issue

## Description
As a course creator, I want formatting controls when writing course descriptions and objectives so that I can structure the content more easily.

## Context
The fields for **course description** and **course objectives** are currently plain textareas.

Adding **Pagedown controls** would allow course creators to format their content more easily while writing it:

<img width="777" height="257" alt="Image" src="https://github.com/user-attachments/assets/bc80ff04-2c88-48cd-8d40-0304ca927419" />

---

## #9441: [FEATURE] Add Markdown editor (Pagedown controls) to contest description field

**Labels:** feature-request, Good first issue

## Description
As a contest organizer, I want formatting controls when writing a contest description so that I can structure the content more easily.

## Context
Currently, the **contest description field** in the create/edit contest form is displayed as a plain textarea.

While the content already supports basic Markdown when displayed, the editor itself does not provide formatting controls.

Adding **Pagedown controls** like the ones used in problem statements: 

<img width="777" height="257" alt="Image" src="https://github.com/user-attachments/assets/bc80ff04-2c88-48cd-8d40-0304ca927419" />

would improve the authoring experience.

---

## #9440: [FEATURE] Create reusable modern styles for modal forms

**Labels:** feature-request, Good first issue

## Description
As a developer, I want reusable modern styles for modal forms so that UI components across the platform look consistent and easier to maintain.

## Context
The modal used to **report problems** currently looks outdated and uses a very basic layout.

<img width="956" height="729" alt="Image" src="https://github.com/user-attachments/assets/446f7f9c-1950-44a5-b5d0-3316996a4425" />

Instead of updating only that modal, the goal is to create **general reusable styles** that can be applied to similar forms across the platform.

These styles could modernize the layout and improve the visual consistency of modal forms.

---

## #9439: [BUG] Fix login redirect after logging out

**Labels:** bug, Good first issue

## Current Behavior
When a user logs out, they are redirected to the homepage. However, the URL might still contains the `logout` path when the platform responds slow.

If the user immediately clicks **Log in**, the current URL is passed as the redirect parameter.

After logging in successfully, the system redirects the user to the `logout` route again, effectively logging them out and returning them to the homepage.

## Expected Behavior
After logging out, the login flow should not redirect back to the `logout` route.

The user should be able to log in normally and remain authenticated.

## Steps to Reproduce
This issue is easier to reproduce when the page loads slowly.

1. Log out of your account.
2. Immediately click **Log in** from the homepage.
3. After logging in, notice that you are redirected to the `logout` route and returned to the homepage without being logged in.

If it is difficult to reproduce due to normal page speed, you can simulate the behavior by manually adding `logout` as the redirect parameter in the URL.

For example:

https://github.com/user-attachments/assets/1d41a4d3-c0ed-4d25-be1f-96a33e1c3580

---

## #9438: [FEATURE] Add useful tools to the Resources menu

**Labels:** feature-request, Good first issue

## Description
As a user, I want quick access to commonly used learning tools from the Resources menu so that I can easily find them while using the platform.

## Context
The current **Resources** menu contains links such as tutorials, the Discord server, the blog, and some algorithm books.

It would be helpful to add direct links to some existing tools in the platform:

- `/problem/statement/` (Problem statement editor)
- `/grader/ephemeral/` (Ephemeral grader / isolated IDE)
- `/karel.js/` (Legacy Karel environment)

These tools already exist but are not easily discoverable from the main navigation.

---

## #9430: [BUG] Difficulty and Quality filter labels break mid-word on mobile viewports in problem collection pages

**Labels:** bug, 📍 Assigned

## Current Behavior

On the problem collection pages (e.g., `/problem/collection/problemLevelIntermediateMathsInProgramming/`), the **Difficulty** and **Quality** filter sidebar labels break mid-word on mobile/tablet viewports (e.g., "Difficu lty", "Qualit y"), making them unreadable. The radio button options also appear cramped and misaligned.

## Expected Behavior

The "Difficulty" and "Quality" headings and their radio button options should display correctly without word-breaking, regardless of screen size.

## Root Cause

The root `<div>` elements in both [FilterDifficulty.vue](cci:7://file:///c:/Users/BIT/Desktop/omegaup/frontend/www/js/omegaup/components/problem/FilterDifficulty.vue:0:0-0:0) and [FilterQuality.vue](cci:7://file:///c:/Users/BIT/Desktop/omegaup/frontend/www/js/omegaup/components/problem/FilterQuality.vue:0:0-0:0) use Bootstrap grid column classes (`col-6 col-sm-3 col-lg-12`) that were designed for a Bootstrap `row` parent. However, in [CollectionList.vue](cci:7://file:///c:/Users/BIT/Desktop/omegaup/frontend/www/js/omegaup/components/problem/CollectionList.vue:0:0-0:0), these components are placed inside a `filters-sidebar` div (a fixed 250px flexbox container, **not** a Bootstrap row).

On smaller viewports, `col-sm-3` restricts the width to 25% of the parent (~62px), which is far too narrow for the content causing the text to wrap mid-word.

**Affected files:**
- [frontend/www/js/omegaup/components/problem/FilterDifficulty.vue](cci:7://file:///c:/Users/BIT/Desktop/omegaup/frontend/www/js/omegaup/components/problem/FilterDifficulty.vue:0:0-0:0) (line 2)
- [frontend/www/js/omegaup/components/problem/FilterQuality.vue](cci:7://file:///c:/Users/BIT/Desktop/omegaup/frontend/www/js/omegaup/components/problem/FilterQuality.vue:0:0-0:0) (line 2)

## Steps to Reproduce

1. Go to **Problems → Browse Problem Collections**
2. Click on any collection (e.g., "Intermediate Level – Mathematics in Programming")
3. View the page on a mobile viewport (or use browser DevTools to emulate a device like iPhone 12 Pro)
4. Observe the **Difficulty** and **Quality** filter sections in the left sidebar


<img width="1067" height="913" alt="Image" src="https://github.com/user-attachments/assets/d93c2fd3-41e7-42e2-9726-184b6c124897" />

---

## #9426: [BUG] Incorrect color scheme used in verdicts section of the profile

**Labels:** bug

## Current Behavior
In competitive programming, Green is used to signify AC and any other error we can use red color
But on my profile WAs are shown in green color. Currently we are using Blue for ACs and Green for WAs.
I understand this is not technically a bug, but it does feel a bit out of picture.
Is there some specific color scheme we are using strictly?

<img width="1125" height="821" alt="Image" src="https://github.com/user-attachments/assets/312898b7-4b42-4284-955e-020a2282a636" />

## Expected Behavior

I feel AC should be green, WA be red, other errors can get yellow/black shade. 

## Steps to reproduce this bug
	1. Just navigate to the my profile section on omegaup after logging in and scroll down to the bar graph.
	
Relevant details about the environment in which I encountered this bug:
	* Browser name: Chrome
	* Operating System: Windows 11
	* Link to the [site](https://omegaup.com/profile/#charts) where this issue occurs.

---

## #9423: [BUG] 5 console.log() debug statements left in production code

**Labels:** bug, 📍 Assigned

## Current Behavior

*Five [console.log()](vscode-file://vscode-app/c:/Users/akhil/AppData/Local/Programs/Microsoft%20VS%20Code/0870c2a0c7/resources/app/out/vs/code/electron-browser/workbench/workbench.html) debug statements are left in production frontend code, leaking internal data structures to the browser console:*
  *1.[course/edit.ts line 332](vscode-file://vscode-app/c:/Users/akhil/AppData/Local/Programs/Microsoft%20VS%20Code/0870c2a0c7/resources/app/out/vs/code/electron-browser/workbench/workbench.html) — Logs [data.solutionStatus](vscode-file://vscode-app/c:/Users/akhil/AppData/Local/Programs/Microsoft%20VS%20Code/0870c2a0c7/resources/app/out/vs/code/electron-browser/workbench/workbench.html) (API response field) every time a problem is added to a course assignment:*

      console.log(data.solutionStatus);

*2.[arena/coursev2.ts line 56](vscode-file://vscode-app/c:/Users/akhil/AppData/Local/Programs/Microsoft%20VS%20Code/0870c2a0c7/resources/app/out/vs/code/electron-browser/workbench/workbench.html) — Logs the full [SubmissionRequest](vscode-file://vscode-app/c:/Users/akhil/AppData/Local/Programs/Microsoft%20VS%20Code/0870c2a0c7/resources/app/out/vs/code/electron-browser/workbench/workbench.html) object (containing run GUID) when a user clicks "show run details":*

          console.log(request);

*3[arena/coursev2.ts line 59](vscode-file://vscode-app/c:/Users/akhil/AppData/Local/Programs/Microsoft%20VS%20Code/0870c2a0c7/resources/app/out/vs/code/electron-browser/workbench/workbench.html) — Logs the full [runDetails](vscode-file://vscode-app/c:/Users/akhil/AppData/Local/Programs/Microsoft%20VS%20Code/0870c2a0c7/resources/app/out/vs/code/electron-browser/workbench/workbench.html) API response (containing source code, verdict, runtime, memory) immediately after:.*

    console.log(runDetails);

*4 .[arena/events_socket.ts line 310](vscode-file://vscode-app/c:/Users/akhil/AppData/Local/Programs/Microsoft%20VS%20Code/0870c2a0c7/resources/app/out/vs/code/electron-browser/workbench/workbench.html) — Logs the WebSocket connection error object when the socket fails and falls back to polling:*

      console.log(e);

*5.  [components/admin/Support.vue line 473](vscode-file://vscode-app/c:/Users/akhil/AppData/Local/Programs/Microsoft%20VS%20Code/0870c2a0c7/resources/app/out/vs/code/electron-browser/workbench/workbench.html) — Logs every DOM [Event](vscode-file://vscode-app/c:/Users/akhil/AppData/Local/Programs/Microsoft%20VS%20Code/0870c2a0c7/resources/app/out/vs/code/electron-browser/workbench/workbench.html) object when the admin support textarea is resized:*

      console.log(event);

## Expected Behavior

*No [console.log()](vscode-file://vscode-app/c:/Users/akhil/AppData/Local/Programs/Microsoft%20VS%20Code/0870c2a0c7/resources/app/out/vs/code/electron-browser/workbench/workbench.html) calls should exist in production code. Debug output in the browser console confuses users, leaks internal data structures, and increases noise when developer

*[truncated]*

---

## #9422: [FEATURE]Add proper pagination to Contest List

**Labels:** feature-request

## Title
As a competitive programmer, I want the contest list summary view to show all available contests (not just 10) so that I can discover and join contests without missing any.

## Context
The contest listing page (/arena/) has two view modes:
     1.Summary view (default) — shows contests in a horizontal scrollable row per tab (Current / Future / Past)
      2." View All" grid view — a full paginated grid with "Load More"

The summary view hard-codes .slice(0, 10) at [ContestList.vue:209](vscode-file://vscode-app/c:/Users/akhil/AppData/Local/Programs/Microsoft%20VS%20Code/0870c2a0c7/resources/app/out/vs/code/electron-browser/workbench/workbench.html), silently hiding any contests beyond the first 10 per tab. This means:

-->Users are unaware contests exist beyond the visible 10. There is no count indicator (e.g., "Showing 10 of 47")     and no visual cue that more data is available.
-->The horizontal scroll arrows ([lines 187-193](vscode-file://vscode-app/c:/Users/akhil/AppData/Local/Programs/Microsoft%20VS%20Code/0870c2a0c7/resources/app/out/vs/code/electron-browser/workbench/workbench.html), [ContestList.vue:285-291](vscode-file://vscode-app/c:/Users/akhil/AppData/Local/Programs/Microsoft%20VS%20Code/0870c2a0c7/resources/app/out/vs/code/electron-browser/workbench/workbench.html)) suggest all content is visible once you scroll to the end, but 37 contests may be hidden.
-->The "View All" button exists per tab, but users who rely on the summary view (the default landing experience) will never know they're missing contests.
-->Search/filter in summary view still caps results to 10 — if your search matches 15 contests, 5 are silently dropped.
The grid/"View All" view already has proper pagination with loadMoreContests() ([line 714](vscode-file://vscode-app/c:/Users/akhil/AppData/Local/Programs/Microsoft%20VS%20Code/0870c2a0c7/resources/app/out/vs/code/electron-browser/workbench/workbench.html)) and pageSize prop ([line 528](vscode-file://vscode-app/c:/Users/akhil/AppData/Local/Programs/Microsoft%20VS%20Code/0870c2a0c7/resources/app/out/vs/code/electron-browser/workbench/workbench.html)), but the summary view does not leverage any of this.

## Impact
This affects every user who visits the contests page. On a platform with active contest creation, users routinely miss contests they could participate in, reducing engagement and contest participation rates.

## Proposed Solution
-->Remove the .slice(0, 10) hard cap at [ContestList.vue:209](vscode-file://vscode-app/c:/Users/akhil/AppData/Local/Programs/Microsoft%20VS%20Code/0870c2a0c7/resources/app/out/vs/code/electron-browser/workbench/workbench.html) — either show all fetched contests in the horizontal scroll, or use the existing pageSize prop to control the limit dynamically.
-->Add a contest count badge next to each tab header (e.g., "Current (23)") using the existing countContests prop ([line 519](vscode-file://vscode-app/c:/Users/akhil/AppData/Local/Programs/Microsoft%20VS%20Code/0870c2a0c7/r

*[truncated]*

---

## #9417: [FEATURE]  MonacoEditor for Ephemeral Grader

**Labels:** feature-request, 📍 Assigned

# MonacoEditor Component

An isolated, highly responsive UI wrapper for the Monaco Editor instance, designed specifically for the Ephemeral runner layout. This component provides a clean, accessible interface for code interaction with built-in state management.

## Key Features

* **Dynamic Environment:** Seamlessly integrates with the global Vuex store to reactively update themes (Dark/Light), languages, and active file contexts.
* **Smart Toolbar Controls:**
  * **Font Size Adjustment:** Quick dropdown for dynamic font scaling (12px - 20px).
  * **Smart Copy:** 1-click clipboard copying with visual feedback. Automatically hides if the editor is empty.
  * **State Reset:** Detects if the user has modified the code (`hasChanges`) and provides a quick-reset button to revert to the default state. Includes a confirmation modal to prevent accidental data loss.
  * **Fullscreen Toggle:** Expands the editor to fill the viewport for focused coding, utilizing keyboard shortcuts (F11/Esc).
* **Performance Optimized:** Uses native JavaScript debouncing for state updates and `ResizeObserver` for fluid layout adjustments without locking the main thread.
* **Accessible:** Fully equipped with ARIA labels, screen-reader-only text, and semantic HTML to ensure usability for all developers.

---

## #9413: [BUG] Navbar dropdowns ("My Content") cannot be closed via click due to CSS hover conflict

**Labels:** bug, Good first issue, 📍 Assigned

## Current Behavior
There is a conflicting behavior in the navigation bar dropdowns (specifically "My Content" ) caused by CSS hover rules fighting with Bootstrap's collapse toggle. 

1. **Bug 1:** Simply hovering over the "My Content"  area immediately displays the sub-menu without requiring a click on the arrow toggle.
2. **Bug 2:** When the sub-menu is open, clicking the arrow toggle does not close the dropdown. The element briefly collapses, but the active CSS `:hover` rule immediately overrides Bootstrap's `display: none` by forcing `display: block`, keeping the menu open.

## Expected Behavior
* Hovering over the menu items should *not* automatically open the sub-menu. 
* The sub-menu should rely purely on Bootstrap's toggle functionality. It should only open when the arrow button is explicitly clicked, and successfully close when the arrow button is clicked a second time.

## **Steps to reproduce this bug:**
1. Log into the platform and view the top navigation bar (desktop viewport).
2. Hover your mouse over the "My Content" section. Note that the sub-menu opens automatically.
3. While the mouse is still hovering, click the arrow toggle button. 
4. Note that the menu fails to close and remains forced open.

**Technical Context :**
This is a great first issue! The root cause is a CSS rule overriding the Bootstrap `data-toggle="collapse"` behavior. 
* In `Navbar.vue` (around line 635), the `.nav-user .collapse-submenu:is(:hover, :focus-within) .collapse-links { display: block; }` rule forces the menu open.
* The exact same pattern exists in `NavbarItems.vue` (around line 130) for the `.nav-problems` class.

**Proposed Fix:**
Remove the conflicting CSS `:hover` rules for these sub-menus in file so that the visibility is controlled entirely by Bootstrap's collapse toggles.

* Browser name: All modern browsers
* Operating System: Desktop viewports (≥992px)

https://github.com/user-attachments/assets/9c2d6d50-b435-418c-86d5-d9441800060c

---

## #9409: [FEATURE]Enforce strict U13 signup contract (birth date + parent email)

**Labels:** feature-request

## Title

_As a platform administrator, I want the signup flow to strictly enforce birth date collection and conditional parent email requirement so that U13 (under-13) accounts are always properly flagged and receive mandatory parental verification_


## Context

How has this issue affected you?
The current user registration system has three interrelated gaps that undermine child-safety compliance (COPPA-like protections):

1. _birth_date is fully optional — The CreateUserParams constructor ([CreateUserParams.php:119-120]) stores birth_date as null when not provided, with an explicit TODO:._

      <?php
     // TODO: Assert that the birth date is always passed, and if and only if the user is U13,
      // the parent email is passed.
        $this->birthDate = $params['birth_date'] ?? null;

*This means users can create accounts without ever declaring their age.*

2. Null birth date silently becomes epoch (1970-01-01) — In User::createUser() ([User.php:195-199], when birthDate is null, intval(null) returns 0, causing toMySQLTimestamp(0) to store 1970-01-01 in the database:

      <?php
      'birth_date' => \OmegaUp\DAO\DAO::toMySQLTimestamp(
    intval($createUserParams->birthDate)  // null → 0 → 1970-01-01
    ),

---

## #9408: [BUG]Rejudge debug flag is silently ignored (always false)

**Labels:** bug, 📍 Assigned

## Current Behavior

*The rejudge() method accepts a bool $debug parameter but hardcodes ['debug' => false](vscode-file://vscode-app/c:/Users/akhil/AppData/Local/Programs/Microsoft%20VS%20Code/072586267e/resources/app/out/vs/code/electron-browser/workbench/workbench.html) in the grader request. This means debug rejudges never work even when explicitly requested.*

## Expected Behavior

## Current Code

    <?php
     public function rejudge(array $runs, bool $debug): void {
    // ...
    $this->curlRequest(
        OMEGAUP_GRADER_URL . '/run/grade/',
        self::REQUEST_MODE_JSON,
        [
            'run_ids' => array_map(...),
            'rejudge' => true,
            'debug' => false, // TODO(lhchavez): Re-enable with ACLs.
        ]
    );
     }
## Implementation:
      <?php
      public function rejudge(array $runs, bool $debug): void {
    if (self::$OMEGAUP_GRADER_FAKE) {
        return;
    }
    $this->curlRequest(
        OMEGAUP_GRADER_URL . '/run/grade/',
        self::REQUEST_MODE_JSON,
        [
            'run_ids' => array_map(
                fn (\OmegaUp\DAO\VO\Runs $r) => intval($r->run_id),
                $runs
            ),
            'rejudge' => true,
            'debug' => $debug,
        ]
    );
      }


*Then add an ACL gate at the caller site (e.g. in the Contest/Problem controller where rejudge is invoked.*

      <?php
     $debug = $r->ensureOptionalBool('debug') ?? false;
    if ($debug && !\OmegaUp\Authorization::isSystemAdmin($r->identity)) {
    throw new \OmegaUp\Exceptions\ForbiddenAccessException('userNotAllowed');
       }
         $grader->rejudge($runs, $debug);    



*Tests to add: Unit test asserting the debug flag propagates to the curl request body, and an auth test that non-admins cannot use [debug=true].*

---

## #9406: [FEATURE] Add missing unit tests for Vue components (tracking issue)

**Labels:** feature-request

_As a **developer**, I want **unit tests for all Vue components that currently lack test coverage** for **preventing regressions and improving code reliability**_


## Context

An audit of the frontend codebase reveals that **88 out of 250 Vue components (35.2%)** have no unit tests. This tracking issue covers the most important ones  prioritized by testable logic density, line count, and user flow criticality.

Each checkbox below will be addressed in a **separate PR** adding a [.test.ts](cci:7://file:///c:/Users/BIT/Desktop/omegaup/frontend/www/js/omegaup/ui.test.ts:0:0-0:0) file for that component.

### Current test coverage
- **Total Vue components**: 250
- **Components with tests**: 162 (64.8%)
- **Components missing tests**: 88

---

## Checklist

###  Priority  High (critical user flows, largest components)

- [ ] **[login/Signup.vue](cci:7://file:///c:/Users/BIT/Desktop/omegaup/frontend/www/js/omegaup/components/login/Signup.vue:0:0-0:0)** (495 lines) - User registration with age verification, reCAPTCHA, parental consent, password validation. Largest untested component.
- [ ] **[problem/ProblemMarkdown.vue](cci:7://file:///c:/Users/BIT/Desktop/omegaup/frontend/www/js/omegaup/components/problem/ProblemMarkdown.vue:0:0-0:0)** (463 lines) - Problem statement rendering with MathJax, Mermaid diagrams, template injection/cleanup. Used on every problem page.
- [ ] **[user/Chartsv2.vue](cci:7://file:///c:/Users/BIT/Desktop/omegaup/frontend/www/js/omegaup/components/user/Chartsv2.vue:0:0-0:0)** (408 lines) - Submission statistics with 10 computed properties doing data transformation for Highcharts.
- [ ] **[course/Statistics.vue](cci:7://file:///c:/Users/BIT/Desktop/omegaup/frontend/www/js/omegaup/components/course/Statistics.vue:0:0-0:0)** (351 lines) - Course statistics with 14 methods: 9 chart option getters, verdict aggregation, stat extraction.
- [ ] **[contest/Intro.vue](cci:7://file:///c:/Users/BIT/Desktop/omegaup/frontend/www/js/omegaup/components/contest/Intro.vue:0:0-0:0)** (339 lines) - Contest entry page with registration flow, countdown, 11 computed properties, user info validation.
- [ ] **[login/Login.vue](cci:7://file:///c:/Users/BIT/Desktop/omegaup/frontend/www/js/omegaup/components/login/Login.vue:0:0-0:0)** (310 lines) - Authentication entry point with GitHub OAuth CSRF token generation, Google Sign-In, intro.js walkthrough.
- [ ] **[common/NavbarItems.vue](cci:7://file:///c:/Users/BIT/Desktop/omegaup/frontend/www/js/omegaup/components/common/NavbarItems.vue:0:0-0:0)** (304 lines) - Global navigation on every page. Auth-conditional rendering, role-based links, lockdown mode.
- [ ] **[arena/RunDetailsPopup.vue](cci:7://file:///c:/Users/BIT/Desktop/omegaup/frontend/www/js/omegaup/components/arena/RunDetailsPopup.vue:0:0-0:0)** (299 lines) - Run results display with expandable test case groups, diff view, compile errors.
- [ ] **[arena/RunSubmitPopup.vue](cci:7://file:///c:/Users/BIT/Desktop/omegaup/frontend/www/js/omegaup/componen

*[truncated]*

---

## #9401: [FEATURE] Cross-tab authentication state synchronization improvement

**Labels:** feature-request

Currently, when a user logs out in one browser tab, other open tabs of the same application continue to display authenticated UI until a navigation event or API request occurs. This creates a temporary inconsistent state where the UI appears logged in even though the session has already been invalidated.

Additionally, during contests, if multiple accounts are used sequentially in different tabs within the same browser session, the most recent login overrides the previous session. Because browser cookies are shared across tabs, both tabs may end up operating under the latest authenticated user. This can make it appear as though submissions from a previous account are visible while another user is logged in, which may confuse users about which account is currently active.

The goal is to ensure that authentication state changes (such as login or logout) are synchronized across all open tabs immediately. This would:

* Prevent stale authenticated UI states
* Avoid confusion about which account is currently active
* Improve clarity during contest participation
* Align session behavior with modern web application standards

This enhancement focuses on improving user experience and session consistency without altering backend authentication logic.

![Image](https://github.com/user-attachments/assets/ecd0ff2d-73c7-4b3f-841c-32462b8998d5)

![Image](https://github.com/user-attachments/assets/4f3f1e37-569a-451d-a5f6-a1e3c5ed84c5)

---

## #9398: [BUG] Release workflows can report success even if merge API fails.

**Labels:** bug, 📍 Assigned, 🔔 reminder-sent

## Current Behavior
curl is used without --fail/status checks; 4xx/5xx can pass silently.

## Expected Behavior
fail on non-2xx and parse response to verify merge happened

## Files
daily-release.yml (line 41), weekly-release.yml (line 33)

---

## #9390: [FEATURE] Optimize Coder_Of_The_Month query using index and removing correlated subquery

**Labels:** feature-request

## Problem
The `getCodersOfTheMonth` / `get_last_12_coders_of_the_month` query shows poor performance:
- EXPLAIN: `Using where; Using join buffer (hash join)`, type `ALL` on join tables
- Correlated NOT EXISTS runs per row
- Emails join uses `user_id` instead of main email

## Solution
1. Add covering index `idx_category_time_selected` on `(category, time, selected_by)` 
2. Replace correlated NOT EXISTS with LEFT JOIN to precomputed derived table
3. Fix Emails join to use `main_email_id` (one row per user, aligns with other COTM queries)

---

## #9389: [BUG] user/mailingListBackfill accessible via HTTP GET

## Current Behavior

`GET /api/user/mailingListBackfill/` returns HTTP 200 and executes the backfill logic instead of returning 405 Method Not Allowed. This is another instance of the same pattern-matching gap described in #9385- the word `backfill` is not in the `$mutatingPatterns` list in `frontend/server/src/ApiCaller.php`.

## Expected Behavior

The endpoint should return 405 for GET requests since it performs bulk user data updates. Only POST should be accepted, consistent with other mutating endpoints.

---

## #9388: [BUG] User system roles lookup ignores group-based roles (GroupRoles)

## Current Behavior

When fetching a user's system roles in `User::apiExtraInformation`, only direct `UserRoles` assignments are checked. Group-based role assignments (`GroupRoles`) are completely ignored. A user who has been granted a system role through a group membership will not have that role reflected in their role list.

The TODO comment in `frontend/server/src/Controllers/User.php` line also acknowledges this:
## Expected Behavior

`getSystemRoles` (or the code calling it) should also check `GroupRoles` so that group-inherited system roles are included in the result, consistent with how authorization checks work elsewhere in the codebase (e.g. `Authorization.php` already queries `GroupRoles::hasRole` for permission checks).

---

## #9387: [BUG] page parameter accepts negative values in contest/list and problem/list without returning 400

## Current Behavior

Passing a negative value for the `page` parameter in `GET /api/contest/list/` or `GET /api/problem/list/` returns HTTP 200 and silently treats it as page 1, with no validation error.

`GET /api/contest/list/?page=-5` returns HTTP 200 with results.
`GET /api/problem/list/?page=-1` returns HTTP 200 with results.

In contrast, `page_size` on the same `contest/list` endpoint is validated with `lowerBound: 1`:

`GET /api/contest/list/?page_size=-1` returns HTTP 400 with a `parameterNumberTooSmall` error.

The inconsistency is in `frontend/server/src/Controllers/Contest.php` around line 136-141:

```php
$page = $r->ensureOptionalInt('page') ?? 1;              // no lowerBound
$pageSize = $r->ensureOptionalInt(
    key: 'page_size',
    lowerBound: 1,                                        // validated
    upperBound: 100
) ?? self::CONTEST_LIST_PAGE_SIZE;
```

## Expected Behavior

`page` should be validated with `lowerBound: 1` the same way `page_size` is, and return HTTP 400 for negative or zero values instead of silently falling back to page 1.

---

## #9386: [BUG] Clarification::apiCreate always returns null for contest_alias

## Current Behavior

POST /api/clarification/create/ always returns contest_alias: null in the response, even when the clarification was created for a specific contest. The variable $contestAlias is set correctly inside the function but is never written into the return array (frontend/server/src/Controllers/Clarification.php line 211 hardcodes null).

## Expected Behavior

The response should include the actual contest alias when the clarification belongs to a contest, so callers can identify which contest the clarification was created for without needing a separate fetch.

## If necessary, add the following information

Steps to reproduce:

1. Log in as any user
2. POST /api/clarification/create/ with a valid contest_alias, problem_alias, and message
3. Inspect the response - contest_alias field is always null

The frontend currently works around this by ignoring the create response and refreshing the full list, so there is no visible breakage now.

---

## #9385: [BUG] isMutatingMethod() missing patterns — contest/clone and course/clone can be triggered via GET

## Current Behavior

`GET /api/contest/clone/` and `GET /api/course/clone/` both return HTTP 200 and actually create contests/courses in the database, instead of returning 405.

```bash
GET /api/contest/clone/?contest_alias=foo&alias=bar&title=x&start_time=1234&description=y
# HTTP 200 - {"alias":"bar","status":"ok"}  <- real contest created

GET /api/course/clone/?course_alias=foo&alias=bar&name=x&start_time=1234
# HTTP 200 - {"alias":"bar","status":"ok"}  <- real course created

GET /api/contest/open/?contest_alias=foo
# HTTP 200 - records first-time access in DB

GET /api/user/acceptPrivacyPolicy/?privacy_git_object_id=x&statement_type=y
# HTTP 404 - processes the request (not 405)
```

## Expected Behavior

All these endpoints should return 405 Method Not Allowed for GET requests, the same way `contest/create` and `user/update` do.

## Root Cause

`isMutatingMethod()` in `frontend/server/src/ApiCaller.php` uses substring pattern matching to block GET on mutating methods. The `$mutatingPatterns` array is missing: `clone`, `open`, `accept`.

The fix is to add those three to the array. Test cases can be added to `ApiCallerGetRejectionTest.php`.

---

## #9384: [BUG]  Authorization bypass in `/api/run/download` using `show_diff` allows hidden test .out exfiltration in contest

**Labels:** bug, 📍 Assigned, 🔔 reminder-sent

# Critical: Authorization bypass in `/api/run/download` using `show_diff` allows hidden test input exfiltration during contest

## Current Behavior

In production,

A non-admin contestant can directly call the run download endpoint with `show_diff=true` and successfully download `files.zip` for their own run, even when they are not a problem admin.

This bypasses intended authorization checks and can expose outputs generated from hidden/private test cases. In practice, a contestant can submit code that echoes input and then recover hidden-case content from downloaded `.out` files.

In Local :-

i got zip file but empty 

## Expected Behavior

The backend should enforce authorization server-side and reject non-admin access to run artifact downloads, regardless of user-controlled request parameters.


## If necessary, add the following information (otherwise delete this section):

_Provide a link to an example, or a detailed list of steps to reproduce this bug._

    1. Create or use a problem with hidden/private test cases.
    2. Log in as a normal contestant (not problem admin) and submit a solution .
    3. Obtain the run alias (guid) from the submissions page/network requests.
    4. While authenticated as the same contestant, request:
       `/api/run/download/run_alias/[guid]/show_diff/true/`
    5. Observe that the server returns a zip file (`files.zip`) instead of a forbidden response.
    6. Extract `.out` files and observe hidden-case input can be accessed.


## PoC submission code (C++):

```cpp
#include <iostream>
#include <string>

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);

    std::string line;
    while (std::getline(std::cin, line)) {
        std::cout << line << '\n';
    }
    return 0;
}
```

---

## #9382: [FEATURE] Optimize inefficient QualityNominations queries (Using temporary; Using filesort; join buffer)

**Labels:** feature-request

## Problem
Two QualityNominations queries show poor performance in EXPLAIN:
1. **getNominations** (DAO/QualityNominations.php ~L299): `Using temporary; Using filesort`, `ALL` – full table scan and sort
2. **getVotesForNomination** (DAO/QualityNominations.php ~L200): `Using join buffer (hash join)`, `ALL` – correlated subquery per row

## Solution
- Add `idx_nomination_qualitynomination` on QualityNominations to support filter + ORDER BY
- Add `idx_qnc_nomination_user_comment` on QualityNomination_Comments for last-vote lookup
- Replace correlated subquery in getVotesForNomination with derived table (runs once per invocation)

---
