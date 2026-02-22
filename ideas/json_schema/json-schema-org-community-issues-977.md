# 977

**Parent:** JSON Schema — Project Ideas
**Source:** https://github.com/json-schema-org/community/issues/977
**Scraped:** 2026-02-22T23:28:47.586224

---

## GSOC 2026: Add Support for Reporting on the Annotation Test Suite

**Labels:** gsoc, Status: Accepted

**Project Title**
Add Support for Reporting on the Annotation Test Suite

**Brief Description**
The official JSON Schema Test Suite now includes a reasonably complete suite for **Annotations** (metadata), but Bowtie currently only supports reporting on **Validation** (boolean pass/fail).

This project aims to implement full support for running and reporting on the Annotation Test Suite. Based on the original feature request by @jdesrosiers in [Issue #2006](https://github.com/bowtie-json-schema/bowtie/issues/2006), this is a full-stack engineering challenge that requires updates across three distinct layers of Bowtie:

1.  **The UI Level:** Creating a new "Annotations" report page in the React frontend.
2.  **The Report Level:** Upgrading the internal report format to store arbitrary comparison results. Unlike validation (which is binary `valid`/`invalid`), annotations return sets of values that must be compared against an expected set.
3.  **The Protocol Level:** Updating how Bowtie’s runner talks to test harnesses to support the specific definitions of the annotation test suite.

**Expected Outcomes**
* **Protocol Update:** The Bowtie runner is capable of executing the official Annotation Test Suite against supported implementations.
* **Data Model Upgrade:** The report schema is updated to persist annotation results (sets of values) alongside standard validation results.
* **New Reporting UI:** A fully functional, interactive page on the Bowtie report site dedicated to visualizing annotation conformance.
* **Component Reusability:** Extraction of shared UI logic to ensure the new Annotation page remains consistent with the existing Validation page.

**Skills Required**
* **Python:** For updating the runner protocol and report data handling.
* **React & TypeScript:** For building the new reporting interface.
* **JSON Schema:** Understanding the specific mechanics of Annotations vs. Validation.

**Mentors**
@Julian and @AgniveshChaubey

**Expected Difficulty**
Medium

**Expected Time Commitment**
175 hours

