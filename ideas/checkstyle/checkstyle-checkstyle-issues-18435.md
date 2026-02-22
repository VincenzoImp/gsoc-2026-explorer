# issue

**Parent:** checkstyle — Project Ideas
**Source:** https://github.com/checkstyle/checkstyle/issues/18435
**Scraped:** 2026-02-22T23:28:47.591724

---

## Fix xdocs Examples AST Consistency Test (Reduce suppressions list)

**Labels:** approved, miscellaneous, good second issue


## Overview

The `XdocsExamplesAstConsistencyTest` validates that xdocs example files maintain consistent code structure (differing only in comments and configuration). Currently, we have **228 examples** in the suppression list that need to be reviewed and fixed.

## Goal

Reduce or eliminate entries from the `SUPPRESSED_EXAMPLES` list by fixing the underlying AST issues in example files.

## What Needs to Be Done

Each suppressed example needs investigation to determine:

1. **Is the code actually different?** → Fix the code to match other examples
2. **Should the code be different?** → Mark it as independent (different use case)

Please read and looks at images at https://github.com/checkstyle/checkstyle/issues/13345 that shows what is allowed difference between ExampleX classes. 

## Example: suppresswarningsholder (Already Fixed )

**Before:**
- `SUPPRESSED_EXAMPLES` contained: `Example2`, `Example3`, `Example4`
- These examples were failing validation

**Investigation revealed:**
- Example1 = showcase broad suppression (different/Specific use case)
- Example2, 3, 4 = showcase aliasList variations (should match)

**Fix applied:**
1. Marked Example1 as independent (it has different code intent)
2. Fixed Example2's code to match Example3 and Example4
3. Removed all 3 examples from suppression list kept Example1 as it has specific usecase

**Result:**  Test now passes.

## Current Suppression List (check master HEAD version for latest state)

https://github.com/checkstyle/checkstyle/blob/78f9db1cb555aeb2d37531cb6d49be0448d2c624/src/test/java/com/puppycrawl/tools/checkstyle/internal/XdocsExamplesAstConsistencyTest.java#L88-L91


## How to Help

### Pick a check from the list above

Example: `checks/annotation/annotationonsameline`

### Investigate the examples

1. Navigate to: `src/xdocs-examples/resources/com/puppycrawl/tools/checkstyle/checks/annotation/annotationonsameline/`
2. Look at all `Example*.java` files
3. Read the comments to understand what each example demonstrates
4. Compare the code between examples

### Determine the issue

**Question**: Should these examples have the same code structure or different code structures?

- **Same structure** = They demonstrate the same check with different configuration
- **Different structure** = They demonstrate different use cases of the check

### Apply the fix

**If examples should have the same code:**
- Fix the code so all examples match structurally
- Only comments and configuration values should differ

**If an example legitimately has different code:**
- No code change needed
- The test framework will handle it appropriately, just add in the suppression list.

### Run the test

```bash
mvn clean test -Dtest=XdocsExamplesAstConsistencyTest
```

Verify that your changes resolve the suppression.

### Submit your PR

 **Each check can be fixed independently! Pick one and create one PR, for a single check at a time.**

Example can be found here: https://github.com/checkstyle/checkstyle/commit/040a44c300cd8a692c5ba690f9f3fb0020c5da6b
link to actual issue: #17177 

Example of Pull Request on expected update:
https://github.com/checkstyle/checkstyle/pull/18472
Example of Pull Request with diff image to prove that content of examples is same https://github.com/checkstyle/checkstyle/pull/18505

One more example https://github.com/checkstyle/checkstyle/pull/18572 where contributor shared diffcheker links to prove that all examples are same bu java structure.

