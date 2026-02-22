# JabRef e.V. — Project Ideas

**Source:** https://jabref.github.io/GSoC/projects/
**Scraped:** 2026-02-22T23:28:47.605262

---

# Projects

### Improved Journal Abbreviations

Currently, JabRef has a single list of journal abbreviations. This list is a combined list of the `.csv`

files at [https://github.com/JabRef/abbrv.jabref.org/tree/main/journals](https://github.com/JabRef/abbrv.jabref.org/tree/main/journals). Instead of the dropdown of JabRef should not show a single “JabRef built in list”, but should show the various lists we offer: built-in lists, external lists, custom lists. Then, one can enable and disable with a click. This eases the users to find issues in abbreviation lists and allows users to customize the lists according to their field (e.g., physics, information science, …).

Fore more context, see: [https://github.com/JabRef/jabref/issues/12364](https://github.com/JabRef/jabref/issues/12364) and list of all abbreviation issues: [https://github.com/jabref/jabref/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22component%3A%20journal%20abbreviations%22](https://github.com/jabref/jabref/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22component%3A%20journal%20abbreviations%22). Please also check existing pull requests and comments on them.

**Skills required:**

- Java, JavaFX

**Expected Outcome:**

A UI view which allows selecting/including journal abbreviations by category.

**Possible Mentors:**

**Project size:**

- 90h (small) to medium

### Improved LibreOffice-JabRef integration

**Description:**

JabRef can connect to LibreOffice to offer premier reference management by allowing users to cite library entries directly into the document, and then generate bibliographies based on the cited entries. See [JabRef LibreOffice Integration](https://docs.jabref.org/cite/openofficeintegration).

We have a collection of independent projects available for the LibreOffice/OpenOffice integration feature of JabRef.

**BST style support:**Currently, custom styles (JStyles) and CSL styles are supported. In the LaTeX-world, BST styles (specified via`.bst`

files) are still popular. JabRef already has BST support, but it is currently not accessible via the UI.- Expected deliverable: It should be possible to select a
`.bst`

file, which is then used for rendering into the LibreOffice document. [Details:[#624](https://github.com/JabRef/jabref/issues/624)]

- Expected deliverable: It should be possible to select a
**Improved support for CSL styles:**Support for CSL styles in the LibreOffice integration has been a popular new feature in JabRef that[users look forward to](https://discourse.jabref.org/t/error-when-connecting-to-libreoffice/5431/14?u=subhramit). This project aims to enhance the integration further by introducing**Footnote-based citation support for CSL styles**. Currently, using CSL styles in footnotes of the LibreOffice document causes unexpected behavior, especially for numeric styles. There should be a proper definition of the “global order” of the citations so that they can be used in footnotes. This problem is already solved for JStyles (see a high-level overview[here](https://devdocs.jabref.org/code-howtos/openoffice/order-of-appearance.html)), so the solution needs to be extended/adapted for CSL styles (and BST styles, if project 1 is also undertaken).- Expected deliverable: It is possible to use CSL styles in the footnotes of the documents, without any unexpected/broken ordering in the bibliography or numeric citations. [Tracking issue:
[#12484](https://github.com/JabRef/jabref/issues/12484)]

- Expected deliverable: It is possible to use CSL styles in the footnotes of the documents, without any unexpected/broken ordering in the bibliography or numeric citations. [Tracking issue:
**Cross-compatibility with other reference management software**: In case of CSL styles, reference management software like[Zotero](https://www.zotero.org/)and[Mendeley](https://www.mendeley.com/)can read each other’s citations in LibreOffice. This is made possible by following a specific format of document annotations, embedding information in CSL JSON. In JabRef, the internal format of references is currently a JabRef-custom format. It should be changed to a format used by Zotero, so that cross-compatibility can be ensured. See the discussion at[https://github.com/JabRef/jabref/issues/2146#issuecomment-891432507](https://github.com/JabRef/jabref/issues/2146#issuecomment-891432507)for details. This includes: i) Implementation of that format, ii) Implementation of a converter from the “old” JabRef-Format to the new one. The converter could be implemented within OpenOffice (similar to[JabRef_LibreOffice_Converter](https://github.com/teertinker/JabRef_LibreOffice_Converter?tab=readme-ov-file#jabref_libreoffice_converter)).- Expected deliverable: One can seamlessly switch working with LibreOffice documents having citations from Zotero and JabRef.

**Seamless citation style type switching:**JabRef in LibreOffice should support auto-updation of references when switching from CSL-based formats to JStyle (or BST)-based formats and back. Currently, if the user messes up and realizes that they had to use another style family, the workaround is to re-cite all entries again with the new style, then refresh the bibliography. This may not be very user-friendly when citation styles need to be updated when submitting papers to different journals (one use-case), or simply because of last-minute change in decisions. For this project, the starting step will be unifying the “reference mark” (document annotation) format for all these style types, so that the entry information can be parsed across styles. This project thus goes very well coupled with Project 1 and Project 3.- Expected deliverable: On changing style type (CSL/BST/JStyle), all references in the documents should seamlessly adapt to the new style.


**Skills required:**

- Java, JavaFX

**Possible Mentors:**

**Project size:**

**350h (large)**: If (Project 1 + Project 2 + Project 3 + Project 4)**175h (medium)**: If (Project 1 + Project 2)**OR**(Project 2 + Project 3)**OR**(Project 1 + Project 3)**90h (small)**: If Project 1**OR**Project 2**OR**Project 3

### Improve handling of older documents by OCR and AI

JabRef, comprehensive literature management software, currently supports both handling metadata and text-based PDF documents. However, a significant limitation arises with scanned PDFs, particularly historical articles, which are not text-searchable due to their image-based format. This project aims to bridge this gap by integrating advanced OCR (Optical Character Recognition) technology, enabling full-text search in scanned PDFs.

**Useful links:**

[OCR Integration in JabRef - Meta Issue](https://github.com/JabRef/jabref/issues/13267)- A Document AI Package: https://github.com/deepdoctection/deepdoctection
- Hand-written text recognition in historical documents: https://github.com/githubharald/SimpleHTR#handwritten-text-recognition-with-tensorflow
- Java OCR with Tesseract:
[Baeldung Guide](https://www.baeldung.com/java-ocr-tesseract) - Tesseract OCR Library:
[Official Documentation](https://tesseract-ocr.github.io/) - OCRmyPDF Installation and Usage:
[GitHub Repository](https://github.com/ocrmypdf/OCRmyPDF#installation) - ChatOCR and ChatGPT Integration:
[Blog Article](https://www.blogmojo.de/chatgpt-plugin/chatocr/) - AI-Powered OCR:
[Addepto Blog](https://addepto.com/blog/ai-powered-ocr-optical-character-recognition-enhancing-accuracy-and-efficiency-in-document-analysis/) - Tika OCR Integration:
[Apache Tika Wiki](https://cwiki.apache.org/confluence/display/tika/tikaocr) - Surya AI powered OCR, apparently better than Tesseract, but coded in python
[VikParuchuri/Surya](https://github.com/VikParuchuri/surya) - SOTA (October 2025) language model for OCR:
[PaddleOCR-VL](https://huggingface.co/PaddlePaddle/PaddleOCR-VL); Supported by[llama.cpp with PR 16701](https://github.com/ggml-org/llama.cpp/pull/16701)

**Some aspects:**

- Add an option to call an OCR engine from JabRef, e.g., cloud based or local installs
- Define a common interface to support multiple OCR engines
- Provide a good default set of settings for the OCR engines
- Support expert configuration of the settings
- Add the extracted text as a layer to the pdf so that Apache Lucene can parse it
- Add an option to further process the text with Grobid for training and metadata extraction

**Expected outcome:**

A) Develop a common interface within JabRef to accommodate multiple OCR engines, ensuring flexibility and expandability. B) Enable expert users to fine-tune OCR settings, catering to specific needs or document formats.

C) Incorporate the OCR-extracted text as a searchable layer in PDFs, allowing Apache Lucene to index and look for the content.

**Skills required:**

- Proficiency in Java programming.
- A keen interest and curiosity in document processing and AI technologies.

**Possible mentors:**

[@Siedlerchr](https://github.com/Siedlerchr), [@InAnYan](https://github.com/InAnYan/), [@calixtus](https://github.com/calixtus), [@subhramit](https://github.com/subhramit)

**Project size:**

90h (small)

### JabRef components as native images

JabRef consists of multiple parts: JabKit, JabLS, JabSrv, and JabRef (the GUI).

JabKit is the command-line tool of JabRef offering all the “cool” functionality using a command-line interface. Currently, JabKit is distributed by jpackage and JBang. JPackage creates an installer and portable version. The startup time is way too long for a CLI application. While the installer and portable version include a JDK, JBang downloads the JRE for itself and “just” downloads the Maven artifact jablib to enable execution.

In the Java compiler space, there is the option of [GraalVM and “native image”](https://www.graalvm.org/latest/reference-manual/native-image/). This enables generating an executable file (.exe on Windows) which promises a faster startup.

This GSoC project has two phases:

- Phase 1: Adapt JabKit+jablib to be compatible with
`graalvm-native`

- Phase 2: Adapt JabGui to be compatible with
`graalvm-native`

- Phase 3: Adapt JabLS to be compatible with
`graalvm-native`

- Phase 4: Adapt JabSrv to be compatible to
`graalvm-native`


Especially phase 2 might require exchanging libraries in JabRef.

**Why is this a nice project?**

One can learn about fields of Java known to a little group of developers only. One touches areas very new in the Java space. Finally, one can learn about [WASM-compiling of Java](https://github.com/oracle/graal/issues/3391).

**Expected outcomes:**

- jabkit.exe (JabRef’s CLI tool)
- jabref.exe (JabRef GUI)
- jabls.exe
- jabsrv.exe

**Skills required:**

- Strong Java-coding skills
- Endurance, because this project might include much trial-and-error

**Possible Mentors:**

**Links:**

- Source of JabKit:
[https://github.com/JabRef/jabref/tree/main/jabkit](https://github.com/JabRef/jabref/tree/main/jabkit) - Initial PR trying it:
[https://github.com/JabRef/jabref-koppor/pull/693](https://github.com/JabRef/jabref-koppor/pull/693) - JBang runner for JabKit:
[https://github.com/JabRef/jabref/tree/main/.jbang#running-jabkit](https://github.com/JabRef/jabref/tree/main/.jbang#running-jabkit) - Way to have a single binary running on multiple platforms:
[https://github.com/oracle/graal/pull/12865](https://github.com/oracle/graal/pull/12865)

**Project size:**

175h (medium)

### Use PostgreSQL as full GUI data backend for JabRef

Currently, JabRef GUI holds all entries in memory. It even converts LaTeX to Unicode and vice versa to support better search. While this is a great UX, this leads to a huge memory consumption. The more “proper” way is to use a database (such as PostgreSQL) to store the entries. Then, not all entries need to be loaded in memory. The first step is to introduce a data-access layer: The maintable should read from SQL database, not from all in-memory. Possible future work may be: [https://www.zotero.org/support/dev/client_coding/direct_sqlite_database_access](https://www.zotero.org/support/dev/client_coding/direct_sqlite_database_access) and [https://github.com/zotero/zotero/blob/main/resource/schema/userdata.sql](https://github.com/zotero/zotero/blob/main/resource/schema/userdata.sql).

There can be an initial phase to evaluate whether PostgreSQL is the right DBMS as backend for JabRef. For instance, DuckDB and SQLite were also discussed. Currently, PostgeSQL turned out best (especially for handling regular expression search on the database itself), but things may have changed in 2026.

This is issue [https://github.com/JabRef/jabref/issues/12708](https://github.com/JabRef/jabref/issues/12708).

**Skills required:**

- PostgreSQL, Java, JavaFX

**Code places to start to look at:**

- org.jabref.gui.maintable.MainTableFieldValueFormatter#formatFieldsValues

**Starting points:**

- Document the maintable of JabRef using Markdown and UML (starting point:
`org.jabref.gui.util.ValueTableCellFactory`

)

**Possible Mentors:**

**Project size:**

175h (medium)

### Improved SLR Support

With the ever-growing number of publications in computer science and other fields of research, conducting secondary studies becomes necessary to summarize the current state of the art. For software engineering research, Kitchenham popularized the systematic literature review (SLR) method to address this issue. The main idea is to systematically identify and analyze the majority of relevant publications on a specific topic. This is usually an activity that takes extensive manual effort. Some tool support does exist, but the full potential of tools has not been exploited yet. JabRef also offers basic functionality for systematic literature reviews that is used by a number of researchers to systematically “harvest” related work based on the fetching capabilities of JabRef. While using the feature, various additional feature requests came up. For instance, created search queries are currently transformed internally by JabRef to the query format of the publisher. It should also be possible to directly input a query at the publisher site, e.g., for IEEE or ACM.

More background information: [Paper: Systematic Literature Tools: Are we there yet?](https://ceur-ws.org/Vol-2839/paper13.pdf); ** Presentation**.

One key aspect would be the improvement of the fetcher infrastructure in JabRef to better adapt to new and changing Publisher/Journal websites and to offer a more direct integration. As an inspiration, see [BibDesk](https://bibdesk.sourceforge.io/).

Example SLRs: [https://dl.acm.org/doi/full/10.1145/3690632](https://dl.acm.org/doi/full/10.1145/3690632)

**Expected outcome:**

An advanced SLR functionality, where a researcher is supported to execute a systematic-literature-review.

We did an initial project organization at [https://github.com/users/koppor/projects/2](https://github.com/users/koppor/projects/2).

**Skills required:**

- Java, JavaFX

**Possible mentors:**

[@koppor](https://github.com/koppor), [@calixtus](https://github.com/calixtus), [@subhramit](https://github.com/subhramit)

**Project size:**

175h (medium)

### Sync with Zotero Storage

Zotero is an alternative to JabRef with features focused on collaboration (and less on BibTeX quality). Zotero offers a [Storage](https://www.zotero.org/storage). It would be great if JabRef could synchronize with the storage.

Zotero offers an [API](https://www.zotero.org/support/dev/web_api/v3/start) to access the data. It should be used to synchronize data from and to Zotero.

Special attention should be put on synchronization of data if the local BibTeX file changes in parallel. Different scenarios of synchronization should be regarded. This knowledge should also be used to enhance the git support and OneDrive/Dropbox support.

**Possible Mentors:**

[@koppor](https://github.com/koppor), [@InAnYan](https://github.com/InAnYan/), [@calixtus](https://github.com/calixtus), [@subhramit](https://github.com/subhramit)

**Project size:**

175h (medium)

### More Generic Preferences

JabRef’s strength is that everything is configurable. There are more than 100 parameters to tweak. This is loved and hated by users at the same way.

Two major pain points exist.

- In the BibTeX (.bib) file, the preferences are stored using a custom format.
- Some preferences can be configured for each Bib file, but not all.

In this project, two things should be tackled:

- Rewrite preferences storage in the BibTeX file to JSON
[#10371](https://github.com/JabRef/jabref/issues/10371) - Offer preferences to be configured in the library.
[#8701](https://github.com/JabRef/jabref/issues/8701)

Note that 2 does NOT mean that all preferences should be stored in the library; only the ones the user wants to store.

**Possible Mentors:**

**Project size:**

350h (large)

### {Your own project}

The list of projects is by no means a closed list. You can propose other projects. JabRef offers various places where it can be improved. Think as a user or talk to other users. The following places are a good start:

- Big projects:
[https://github.com/JabRef/jabref/issues?q=sort%3Aupdated-desc+state%3Aopen+label%3A%22size%3A+big%22](https://github.com/JabRef/jabref/issues?q=sort%3Aupdated-desc+state%3Aopen+label%3A%22size%3A+big%22) - General list of feature requests:
[https://discourse.jabref.org/c/features](https://discourse.jabref.org/c/features) - Candidates of university projects, the large ones:
[https://github.com/orgs/JabRef/projects/3/views/3?filterQuery=status%3A%22free+to+take%22+size-of-project%3Alarge&sortedBy%5Bdirection%5D=desc&sortedBy%5BcolumnId%5D=8246261](https://github.com/orgs/JabRef/projects/3/views/3?filterQuery=status%3A%22free+to+take%22+size-of-project%3Alarge&sortedBy%5Bdirection%5D=desc&sortedBy%5BcolumnId%5D=8246261) - Issues tagged with GSoC:
[https://github.com/JabRef/jabref/issues?q=sort%3Aupdated-desc+state%3Aopen+label%3A%22project%3A+gsoc%22](https://github.com/JabRef/jabref/issues?q=sort%3Aupdated-desc+state%3Aopen+label%3A%22project%3A+gsoc%22) - The
[GitHub issue tracker](https://github.com/JabRef/jabref/issues)might serve as an additional source of inspiration) - Switch to Apache Velocity:
[https://github.com/JabRef/jabref/issues/12418](https://github.com/JabRef/jabref/issues/12418)
