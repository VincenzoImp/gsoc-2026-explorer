# 983

**Parent:** JSON Schema — Project Ideas
**Source:** https://github.com/json-schema-org/community/issues/983
**Scraped:** 2026-02-22T23:28:47.586290

---

## GSOC 2026: Enhanced Interaction and Navigation in JSON Schema Studio

**Labels:** gsoc, Status: Accepted

**Enhanced Interaction and Navigation in [JSON Schema Studio](http://studio.ioflux.org/)**

**Brief Description**
**JSON Schema Studio** is an open-source tool that visualizes JSON Schemas as interactive graphs, helping developers understand and debug complex schemas. This project was part of GSoC 2025, and we successfully released the first beta this year, receiving strong and positive feedback from the community. There remains significant scope for further improvements and feature additions.

This GSoC 2026 project focuses on improving interactivity, navigation, and rendering correctness by enhancing dependency ordering, editor synchronization, collision handling, and user-driven exploration features, including collapsible nodes, bidirectional editing, and focused graph navigation.

**Expected Outcomes**
- **Topologically sorted rendering of `$defs` dependencies**: Ensure `$defs` schemas are rendered in dependency order to handle chained and recursive references correctly.
- **Validation error navigation**: When schema validation errors occur, clicking an error highlights and scrolls to the corresponding line number in the editor.
- **Edge collision resolution**: Reduce edge overlappings to improve readability in large graphs.
- **Edge-based navigation controls**: On hovering over an edge, display navigation buttons that allow users to:
  - Focus and center the source node
  - Focus and center the target node
- **Fix handle misalignment on live edits**: Ensure node sourcehandles remain correctly positioned when schemas are edited dynamically in the editor. 
- **Distinct visualization for multi-type schemas**: Clear and intuitive rendering for nodes with multiple types (e.g. `["string", "null"]`) using visual elements such as segmented styles, badges, or patterns.
- **File upload support**: Allow users to upload JSON Schema files directly into the application for instant visualization.
- **Downloadable visualization output**: Enable exporting the visualization as an image or file for documentation and sharing.

**Skills Required**
- JavaScript/TypeScript
- Reactjs
- Understanding of visualization library ([ReactFlow](https://reactflow.dev/))
- Understanding of JSON Schema

**Mentors**
@AgniveshChaubey

**Expected Difficulty**
Small

**Expected Time Commitment**
90 hrs


