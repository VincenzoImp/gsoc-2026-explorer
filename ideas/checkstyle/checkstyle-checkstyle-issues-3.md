# javadoc issues on github

**Parent:** checkstyle — Project Ideas
**Source:** https://github.com/checkstyle/checkstyle/issues?labels=javadoc&page=1&state=open
**Scraped:** 2026-03-10T16:58:40.260429

---

## #19162: LeftCurly: False Negative  when multiple blocks start on a single line

I have read check documentation: https://checkstyle.org/checks/blocks/leftcurly.html
I have downloaded the latest checkstyle from: https://checkstyle.org/cmdline.html#Download_and_Run
I have executed the cli and showed it below, as cli describes the problem better than 1,000 words

```bash
/var/tmp $ javac LeftCurlyTest.java
# [[SUCCESSFULLY COMPILED]]

/var/tmp $ cat config.xml
<?xml version="1.0"?>
<!DOCTYPE module PUBLIC "-//Checkstyle//DTD Checkstyle Configuration 1.3//EN" "https://checkstyle.org/dtds/configuration_1_3.dtd">
<module name="Checker">
  <module name="TreeWalker">
    <module name="LeftCurly">
      <property name="option" value="eol"/>
    </module>
  </module>
</module>

/var/tmp $ cat LeftCurlyTest.java
/** Javadoc */
public class LeftCurlyTest {
    // FN Case: CLASS_DEF curly should be at the end of the line, but it's followed by CTOR_DEF.
    // Checkstyle stays silent because the line ends with another '{' from CTOR_DEF.
    public class FNCase { public FNCase() {
        System.out.println("No violation reported for the first brace.");
    } }

    // TP Case: Reported correctly as the line does not end with a brace.
    public void tpMethod() { int x = 0;
        System.out.println(x);
    }
}

/var/tmp $ RUN_LOCALE="-Duser.language=en -Duser.country=US"
/var/tmp $ java $RUN_LOCALE -jar checkstyle-13.3.0-all.jar -c config.xml LeftCurlyTest.java
Starting audit...
[WARN] LeftCurlyTest.java:13:28: '{' at column 28 should have line break after. [LeftCurly]
Audit done.
```

**Describe what you expect in detail.**
Checkstyle should report a LeftCurly violation for the brace at column 25 (the CLASS_DEF brace) on line 6.

---

**Actual Behavior:**
On line 6: public class FNCase { public FNCase() {, there are two LCURLY tokens. The first one belongs to CLASS_DEF, and the second belongs to CTOR_DEF. The first brace is clearly NOT at the end of the line. However, Checkstyle fails to report a violation for the first brace.

---

## #19156: VariableDeclarationUsageDistance: no violation on variable used in inner class

**Labels:** approved

from https://github.com/checkstyle/checkstyle/issues/13011#issuecomment-3996360057
```
$ cat config.xml 
<?xml version="1.0"?>
<!DOCTYPE module PUBLIC
          "-//Checkstyle//DTD Checkstyle Configuration 1.3//EN"
          "https://checkstyle.org/dtds/configuration_1_3.dtd">

<module name = "Checker">
    <module name="TreeWalker">
        <module name="VariableDeclarationUsageDistance">
          <property name="validateBetweenScopes" value="true"/>
          <property name="allowedDistance" value="1"/>
          <property name="ignoreFinal" value="false"/>
        </module> 
    </module>
</module>

$ cat Test.java 
package com.puppycrawl.tools.checkstyle.checks.coding.variabledeclarationusagedistance;

import java.util.ArrayList;
import java.util.List;

public class Test {

    void nothing() {
    }

    class Parent {
        void mm() {
        }
        <T> void xx(List<T> m){}
    }

    public void method7() {
        // until this issue, not violation, the below distance is 3
        Integer t = 5;
        nothing();
        System.out.println();
        class BClass extends Parent {
            @Override
            void mm() {
                System.out.println(t);
            }
        }
    }
}

$ java -jar checkstyle-13.3.0-all.jar -c config.xml Test.java 
Starting audit...
Audit done.

```


Expected: violation on `t` as distance is 3, allowed distance is 1.

---

## #19154: JavadocStyle format property to control allowed Javadoc formats: traditional, markdown 

**Labels:** blocked

Dependent on https://github.com/checkstyle/checkstyle/issues/16100

Add a "format" property to the [JavadocStyle check](https://checkstyle.sourceforge.io/checks/javadoc/javadocstyle.html) to control allowed Javadoc formats

- any (default)
- traditional
- markdown

```xml
<module name="Checker">
  <module name="TreeWalker">
    <module name="JavadocStyle">
      <property name="format" value="markdown"/>
    </module>
  </module>
</module>
```

---

## #19150: update WriteTagCheck to use AST of javadoc

**Labels:** approved, good fifth issue

we introduced new javadoc AST in scope of https://github.com/checkstyle/checkstyle/issues/17514

Now it is time to migrate [WriteTagCheck](https://github.com/checkstyle/checkstyle/blob/master/src/main/java/com/puppycrawl/tools/checkstyle/checks/javadoc/WriteTagCheck.java) Check to use AST, rather than regexp for parsing of javadoc.

Whole design should stay as is, same properties.
But check should extend ` extends AbstractJavadocCheck` and do all logic based on AST nodes.
There are already bunch of Checks that doing this, so look around for examples.

remove suppresion that is mentioned at https://github.com/checkstyle/checkstyle/issues/11166

---

## #19149: update MissingJavadocTypeCheck to use AST of javadoc

**Labels:** approved, good fifth issue

we introduced new javadoc AST in scope of https://github.com/checkstyle/checkstyle/issues/17514

Now it is time to migrate [MissingJavadocTypeCheck](https://github.com/checkstyle/checkstyle/blob/master/src/main/java/com/puppycrawl/tools/checkstyle/checks/javadoc/MissingJavadocTypeCheck.java) Check to use AST, rather than regexp for parsing of javadoc.

Whole design should stay as is, same properties.
But check should extend ` extends AbstractJavadocCheck` and do all logic based on AST nodes.
There are already bunch of Checks that doing this, so look around for examples.

remove suppresion that is mentioned at https://github.com/checkstyle/checkstyle/issues/11166

---

## #19148: update MissingJavadocMethodCheck to use AST of javadoc

**Labels:** approved, good fifth issue

we introduced new javadoc AST in scope of https://github.com/checkstyle/checkstyle/issues/17514

Now it is time to migrate [MissingJavadocMethodCheck](https://github.com/checkstyle/checkstyle/blob/master/src/main/java/com/puppycrawl/tools/checkstyle/checks/javadoc/MissingJavadocMethodCheck.java) Check to use AST, rather than regexp for parsing of javadoc.

Whole design should stay as is, same properties.
But check should extend ` extends AbstractJavadocCheck` and do all logic based on AST nodes.
There are already bunch of Checks that doing this, so look around for examples.

remove suppresion that is mentioned at https://github.com/checkstyle/checkstyle/issues/11166

---

## #19147: update JavadocVariableCheck to use AST of javadoc

**Labels:** approved, good fifth issue

we introduced new javadoc AST in scope of https://github.com/checkstyle/checkstyle/issues/17514

Now it is time to migrate [JavadocVariableCheck](https://github.com/checkstyle/checkstyle/blob/master/src/main/java/com/puppycrawl/tools/checkstyle/checks/javadoc/JavadocVariableCheck.java) Check to use AST, rather than regexp for parsing of javadoc.

Whole design should stay as is, same properties.
But check should extend ` extends AbstractJavadocCheck` and do all logic based on AST nodes.
There are already bunch of Checks that doing this, so look around for examples.

remove suppresion that is mentioned at https://github.com/checkstyle/checkstyle/issues/11166

---

## #19146: update JavadocTypeCheck to use AST of javadoc

**Labels:** approved, good fifth issue

we introduced new javadoc AST in scope of https://github.com/checkstyle/checkstyle/issues/17514

Now it is time to migrate [JavadocTypeCheck](https://github.com/checkstyle/checkstyle/blob/master/src/main/java/com/puppycrawl/tools/checkstyle/checks/javadoc/JavadocTypeCheck.java) Check to use AST, rather than regexp for parsing of javadoc.

Whole design should stay as is, same properties.
But check should extend ` extends AbstractJavadocCheck` and do all logic based on AST nodes.
There are already bunch of Checks that doing this, so look around for examples.

remove suppresion that is mentioned at https://github.com/checkstyle/checkstyle/issues/11166

---

## #19145: update JavadocStyleCheck to use AST of javadoc

**Labels:** approved, good fifth issue

we introduced new javadoc AST in scope of https://github.com/checkstyle/checkstyle/issues/17514

Now it is time to migrate [JavadocStyleCheck](https://github.com/checkstyle/checkstyle/blob/master/src/main/java/com/puppycrawl/tools/checkstyle/checks/javadoc/JavadocStyleCheck.java) Check to use AST, rather than regexp for parsing of javadoc.

Whole design should stay as is, same properties.
But check should extend ` extends AbstractJavadocCheck` and do all logic based on AST nodes.
There are already bunch of Checks that doing this, so look around for examples.

remove suppresion that is mentioned at https://github.com/checkstyle/checkstyle/issues/11166

---

## #19144: update JavadocMethod to use AST of javadoc

**Labels:** approved, good fifth issue

we introduced new javadoc AST in scope of https://github.com/checkstyle/checkstyle/issues/17514

Now it is time to migrate [JavadocMethod](https://github.com/checkstyle/checkstyle/blob/master/src/main/java/com/puppycrawl/tools/checkstyle/checks/javadoc/JavadocMethodCheck.java) Check to use AST, rather than regexp for parsing of javadoc.

Whole design should stay as is, same properties.
But check should extend ` extends AbstractJavadocCheck` and do all logic based on AST nodes.
There are already bunch of Checks that doing this, so look around for examples.

remove suppresion that is mentioned at https://github.com/checkstyle/checkstyle/issues/11166

---

## #19087: Add instruction to exclude resources files for IntelliJ Idea

**Labels:** approved

Currently the [IntelliJ Setup Guide](https://checkstyle.org/idea.html) does not describe the step to exclude resource files from compilation, which is an unavoidable step if we wish to debug via IntelliJ's interface, as described by this [comment](https://github.com/checkstyle/checkstyle/issues/18939#issuecomment-3905316544). 

During onboarding, I tried to run tests via IntelliJ Idea's interface (clicking the green triangle) but received build errors stemming from input files. After wasting hours I realized I should exclude these input files as they should not be compiled at all. Below are my Excludes settings:

<img width="1476" height="1306" alt="Image" src="https://github.com/user-attachments/assets/517afaf6-4cbd-4989-a928-cb7cdbf77714" />

I believe many newcomers like me start off running tests via Intellij's GUI (which is also demonstrated in this [tutorial video](https://www.youtube.com/watch?v=VnenZbbh1WU&list=PLHM9s_lN4X0hzOQ0sUmGdroxW0HfREAqj&index=12)), therefore I propose to provide detailed instructions for smoother onboarding experience.

---

## #19064: XpathRegressionXxxxxxXxxxxxTest should have 3 test methods

**Labels:** approved, miscellaneous, good fourth issue

we have rule to have 3 tests in XpathRegressionXxxxxxXxxxxxxTest
But as it is not automated we always loose time on this.

examples of missed: 
https://github.com/checkstyle/checkstyle/pull/18657#discussion_r2859017125
https://github.com/checkstyle/checkstyle/pull/18312#issuecomment-3967872333

Find a way to make junit test or Checkstyle Xpath test to make sure that all  
under https://github.com/checkstyle/checkstyle/tree/master/src/it/java/org/checkstyle/suppressionxpathfilter
should 3 methods with `@Test`  and in error message we should mention that we need 3 test that generates xpath different by nodes (structure).

Demand for 3 tests were added at https://github.com/checkstyle/checkstyle/pull/19074

Goal of this issue is to remove suppressions at 
https://github.com/checkstyle/checkstyle/blob/4fdd0fc8ecaf50644660575248e73438b32ad771/config/checkstyle-non-main-files-suppressions.xml#L413

Each file should be removed in separate PR

---

## #19063: Trailing comment alignment test fails with tab-based indentation in test input files

I have read check documentation: https://checkstyle.org/checks/xxxxxx/nameofaffectedcheck.html
I have downloaded the latest checkstyle from: https://checkstyle.org/cmdline.html#Download_and_Run

### Description

When adding a tab-based regression test file for `IndentationCheck`,
the JUnit test `IndentationTrailingCommentsVerticalAlignmentTest` fails due to trailing comment alignment mismatch.

The regression input file intentionally contains tab characters to verify tab-based indentation handling.

However, `IndentationTrailingCommentsVerticalAlignmentTest` enforces that all trailing comments (`//indent:... exp:...`) must align at the same expanded column across the file.

This causes failures for files that intentionally use tabs.

### How to Reproduce

Add a regression input file containing tabs in:
`
src/test/resources/com/puppycrawl/tools/checkstyle/checks/indentation/indentation/
`

**ATTENTION** : should be tabs and not spaces(IDE'sare tend to convert tabs to spaces)

Run:
`
mvn -Dtest=IndentationTrailingCommentsVerticalAlignmentTest test
`
### Input
```
public class InputIndentationTryCtorParamsTabsWrong {                        //indent:0 exp:0

	private InputIndentationTryCtorParamsTabsWrong client;                   //indent:4 exp:4

	private InputIndentationTryCtorParamsTabsWrong(String string) {          //indent:4 exp:4
	}                                                                        //indent:4 exp:4

	private void test() {                                                    //indent:4 exp:4
		try {                                                                //indent:8 exp:8
			client =                                                         //indent:12 exp:12
            new InputIndentationTryCtorParamsTabsWrong(null);                //indent:8 exp:16
		}                                                                    //indent:8 exp:8
		catch (Exception e) {                                                //indent:8 exp:8
		}                                                                    //indent:8 exp:8
	}                                                                        //indent:4 exp:4
}
```
(Initialized gaps are tabs and not spaces to trigger a particular error for test)

### Failing Output
```
Trailing comment alignment mismatch in file:
InputIndentationTryCtorParamsTabsWrong.java on line 23
expected: 77
but was : 71
```
### Expected Behavior

Tab-based regression test files should not fail due to global trailing comment alignment enforcement.

### Actual Behavior

Trailing comment alignment validation fails even though the file is intentionally tab-indented for indentation testing.

### Suggested Direction

Allow a hardcoded list of tab-based test files where vertical alignment enforcement is skipped in `IndentationTrailingCommentsVerticalAlignmentTest`

---

## #19036: Improve onboarding flow for first-time contributors with a minimal step-by-step path

While trying to start as a first-time contributor, I found it difficult to identify a clear minimal end-to-end path for the first successful contribution.

All required information exists in the documentation, but it is distributed across multiple pages and assumes prior open-source experience.

From a beginner’s perspective, the main difficulties are:

1. Understanding the first practical step after forking the repository
2. Knowing how to select a safe first issue for documentation contribution
3. Understanding when discussion/approval is required before implementation
4. What a minimal successful first contribution looks like

I propose adding a short “First Contribution Walkthrough” section that:

- provides a minimal ordered path for new contributors
- focuses on documentation-type contributions
- clearly explains the issue → approval → implementation workflow

This can reduce the entry barrier for new contributors.

I would like to work on this improvement if the idea is approved.

---

## #19004: Add xdocs tests for TextBlockGoogleStyleFormatting

**Description:**

Add xdocs  corresponding test for TextBlockGoogleStyleFormatting check to ensure documentation examples are validated by regression tests.

This improves consistency between documentation and check behavior.

**Explanation:**

Add test and name will be  `TextBlockGoogleStyleFormattingCheckExamplesTest` For Xdocs Example.

Ensure examples are covered by verifyWithInlineConfigParser.

**Example:**
`    @Test
    public void testExample1() throws Exception {
        final String[] expected = CommonUtil.EMPTY_STRING_ARRAY;

        verifyWithInlineConfigParser(getPath("Example1.java"), expected);
    }`
create a new class in: `xdocs-examples/java/com/puppycrawl/tools/checkstyle/checks/coding`
Class name will be: `TextBlockGoogleStyleFormattingCheckExamplesTest` 
And  add test for All the  xdocs Examples of  `textblockgooglestyleformatting`

---

## #19001: JavadocCommentsParser: quoted format specifier in {@value} tag is not parsed

**Labels:** approved, antlr-javadoc

https://www.javaspecialists.eu/archive/Issue308-Formatting-Inlined-value-in-Javadocs.html described this javadoc new syntax

## Checkstyle version
13.3.0-SNAPSHOT

## Description
Since Java 20, the `{@value}` inline tag supports a quoted format string to control 
how a constant value is displayed. For example, from `java.lang.reflect.AccessFlag`:

```java
/**
 * The access flag {@code ACC_MANDATED} with a mask value of
 * <code>{@value "0x%04x" Modifier#MANDATED}</code>.
 */
public static final int MANDATED = 0x8000;
```

Running Checkstyle's Javadoc AST printer on this input throws a parse error:

```
java -jar checkstyle-13.3.0-SNAPSHOT-all.jar -j src/Test.java

Exception in thread "main" java.lang.IllegalArgumentException:
[ERROR:4] Javadoc comment at column 55 has parse error. Details:
mismatched input '%04x' expecting JAVADOC_INLINE_TAG_END while parsing INLINE_TAG
```

The current lexer rule in `JavadocCommentsLexer.g4` only supports bare unquoted format specifiers:

```
FORMAT_SPECIFIER
    : '%' [#+\- 0,(]* [0-9]* ('.' [0-9]+)? [a-zA-Z]
    ;
```

The grammar needs to be updated to support the quoted form (`"0x%04x"`) introduced in Java 20.

## Related
Part of #17882

---

## #18971: NoGetMessageInThrow: New check to not put caught exception message to exception that we are going to throw.

Describe the problem in detail:

Exception messages should not include ex.getMessage() when the exception is
already passed as a cause, as this leads to duplicate information in stack
traces and logs.

/var/tmp $ cat Test.java
```
public class Test {
  void method1() {
    try {
      riskyOperation();
    }
    catch (IOException ex) {
      throw new RuntimeException("unable to process "
          + ex.getMessage(), ex); // violation
    }
  }
```

```
  void method2() {
    try {
      riskyOperation();
    }
    catch (IOException ex) {
      throw new RuntimeException("unable to process file", ex); // ok
    }
  }
```

should method3 considered a violation or not for our new check?

```
  void method3() {
    try {
      riskyOperation();
    }
    catch (IOException ex) {
      throw new RuntimeException("unable to process "
          + ex.getMessage()); // ok, ex is not passed as cause
    }
  }
}
```


Test.java:8: warning: [NoGetMessageInThrow] Avoid using '.getMessage()'
in throw statement.

Describe how the new check will solve the problem:
The check NoGetMessageInThrow will detect when a throw statement
creates a new exception that includes a call to .getMessage() on a
caught exception. The cause exception and its message are already
available in the stack trace, so including getMessage() leads to
duplicate information in logs.

detected at #13023

---

## #18952: review suppresions of org.openrewrite.staticanalysis.CodeCleanup

continuation of https://github.com/checkstyle/checkstyle/issues/18673

we need to review all commented out rules.

if rule needs to be permanently disabled, we should put comment above it to explain reason
or
activate rule.

---

## #18931: New Check: LargeConstantCollection

I am proposing a new check within the coding category to detect large static collection initializers that exceed a specific element count. Currently, Checkstyle does not have a dedicated check to flag massive hard coded arrays, which can lead to significant bytecode bloat and poor separation of data and logic.

**Rationale**
In high-performance engineering, especially in AI and Data Engineering domains, developers sometimes embed lookup tables or model weights directly into Java source files. 
This practice:
- Increases the size of the compiled .class file.
- Can lead to `MethodTooLargeException` if the static initializer grows too big.
- Makes the code difficult to maintain and read.

By implementing `LargeConstantCollectionCheck`, we can enforce a threshold (e.g., `maxElements = 10`) to encourage moving such data to external resource files like .json or .csv.

**Proposed Configuration**
The check will be configurable with a maxElements property.
```
<module name="LargeConstantCollection">
  <property name="maxElements" value="10"/>
</module>
```

**Example of Violation**
```
public class Config {
    // Violation: 12 elements exceed the default max of 10
    int[] lookup = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}; 
}
```

**Technical Implementation**
The check will target `TokenTypes.ARRAY_INIT` and count the `EXPR` child tokens. If the count exceeds the threshold, it will log a violation using a message key for internationalization.

---

## #18911: asking about do they have any plan on supporting Webagent in the next quarter

---

## #18858: False positive: EmptyLineSeparator report wrong violation in the case of anonymous class

**Labels:** approved

detected at https://github.com/checkstyle/checkstyle/pull/18545#issuecomment-3822474864

I have read check documentation: https://checkstyle.org/checks/whitespace/emptylineseparator.html#EmptyLineSeparator
I have downloaded the latest checkstyle from: https://checkstyle.org/cmdline.html#Download_and_Run
I have executed the cli and showed it below, as cli describes the problem better than 1,000 words

`EmptyLineSeparatorCheck` reports wrong violation or two violation pointing to same line in the case of anonymous class.

#### Config:
```
<?xml version="1.0"?>
<!DOCTYPE module PUBLIC "-//Puppy Crawl//DTD Check Configuration 1.3//EN"
   "http://www.puppycrawl.com/dtds/configuration_1_3.dtd">

<module name="Checker">
  <module name="TreeWalker">
    <module name="EmptyLineSeparator">
      <property name="tokens"
               value="PACKAGE_DEF, IMPORT, STATIC_IMPORT, CLASS_DEF, INTERFACE_DEF, ENUM_DEF,
                    STATIC_INIT, INSTANCE_INIT, METHOD_DEF, CTOR_DEF, VARIABLE_DEF, RECORD_DEF,
                    COMPACT_CTOR_DEF"/>
      <property name="allowNoEmptyLineBetweenFields" value="true"/>
      <property name="allowMultipleEmptyLines" value="false"/>
      <property name="allowMultipleEmptyLinesInsideClassMembers" value="false"/>
    </module>
  </module>
</module>
```
Taking three input example with anonymous class for better understanding:
---
### Case 1:
Anonymous class with mutiple chained method call
#### Test.java
```
import java.util.Stack;

public class Test {

    public static void foo1() {
        Stack<Integer> stack = new Stack<>();
        stack.push(5);
 	    new EarlyTerminatingScanner() {
             @Override
             protected void visit(Object role, Object element) {
                 // violation 'There is more than 1 empty line after this line.'
             }       // line  12


 	    }
 	    .setEnabled(true)
 	    .scan("ROLE", new Object());     // line 17
    }

    static abstract class EarlyTerminatingScanner {

        private boolean enabled;

        public EarlyTerminatingScanner setEnabled(boolean value) {
            enabled = value;
            return this;
        }

        public void scan(Object role, Object element) {
            if (enabled) {
                visit(role, element);
            }
        }

        protected abstract void visit(Object role, Object element);
    }
}
```
#### cli:
```
$ java -jar checkstyle-13.1.0-all.jar -c config_check.xml Test.java
Starting audit...
[ERROR] F:\GitHub\headhtmltagname\Test.java:12:14: '}' has more than 1 empty lines after. [EmptyLineSeparator]
[ERROR] F:\GitHub\headhtmltagname\Test.java:17:13: There is more than 1 empty line after this line. [EmptyLineSeparator]
Audit done.
Checkstyle ends with 2 errors.
```

### Case 2:
Anonymous class with single chained method call

#### Test.java
```
import java.util.Stack;

public class Test {

    public static void foo1() {
        Stack<Integer> stack = new Stack<>();
        stack.push(5);
 	    new

*[truncated]*

---

## #18842: google_checks.xml incorrectly marks /** {@return the customer ID} */ as violation

**Labels:** approved

Google Java Style Guide: https://google.github.io/styleguide/javaguide.html#s7.2-summary-fragment explicitly allows using `/** {@return the customer ID} */`.

<img width="1100" height="321" alt="Image" src="https://github.com/user-attachments/assets/bd092df6-b426-45cd-b06a-815aabde75e1" />

However, this now results in `SummaryJavadoc` reporting an error `Forbidden summary fragment.`

```bash
/var/tmp $ javac Test.java 

/var/tmp $ cat Test.java 
/** A test class. */
public class Test {

  /** {@return the customer ID} */
  static int customerId() {
    return 10;
  }
}

/var/tmp $ java -Duser.language=en -Duser.country=US -jar checkstyle-13.1.0-all.jar -c google_checks.xml Test.java
Starting audit...
[WARN] /var/tmp/Test.java:4: Forbidden summary fragment. [SummaryJavadoc]
Audit done.
```

This seems to be due the regexp change in `google_checks.xml` done in https://github.com/checkstyle/checkstyle/pull/18241 to fix issue https://github.com/checkstyle/checkstyle/issues/17727 . Removing the final `|^[a-z]` from the regexp no longer triggers this violation (but may  re-introduce the issue fixed with that PR).

```bash
/var/tmp $ cat test_config.xml 
<?xml version="1.0"?>
<!DOCTYPE module PUBLIC
        "-//Checkstyle//DTD Checkstyle Configuration 1.3//EN"
        "https://checkstyle.org/dtds/configuration_1_3.dtd">
<module name="Checker">
  <module name="TreeWalker">
    <module name="SummaryJavadoc">
      <property name="id" value="patternFromGoogleChecks"/>
      <property name="forbiddenSummaryFragments"
                value="^@return the *|^This method returns |^A [{]@code [a-zA-Z0-9]+[}](https://github.com/checkstyle/checkstyle/ is a )|^[a-z]"/>
    </module>
    <module name="SummaryJavadoc">
      <property name="id" value="fixedPattern"/>
      <property name="forbiddenSummaryFragments"
                value="^@return the *|^This method returns |^A [{]@code [a-zA-Z0-9]+[}](https://github.com/checkstyle/checkstyle/ is a )"/>
    </module>
  </module>
</module>

/var/tmp $ java -Duser.language=en -Duser.country=US -jar checkstyle-13.1.0-all.jar -c test_config.xml Test.java
Starting audit...
[ERROR] /var/tmp/Test.java:4: Forbidden summary fragment. [patternFromGoogleChecks]
Audit done.
Checkstyle ends with 1 errors.

```

---

## #18812: RegexpMultilineCheck: Add option to specify which capturing group determines violation position.

**Labels:** approved

From https://github.com/checkstyle/checkstyle/issues/2978

I have read check documentation: https://checkstyle.org/checks/regexp/regexpmultiline.html
I have downloaded the latest checkstyle from: https://checkstyle.org/cmdline.html#Download_and_Run
I have executed the cli and showed it below, as cli describes the problem better than 1,000 words</p>

When using RegexpMultilineCheck for conditional pattern matching, users must include context in the regex pattern. Currently, violations are reported at the start of the entire match (group 0), which reports the context line instead of the actual violation line.

<pre><code class="language-bash">Windows@Windows MINGW64 ~/check
$ cat Example.java
class Example {
    void method1() {
        // CONTEXT
        System.out.print("Should be reported here");
    }

    void method2() {
        System.out.print("This alone is OK");
    }
}
</code></pre>
<pre><code class="language-xml">Windows@Windows MINGW64 ~/check
$ cat config.xml
&lt;?xml version="1.0"?&gt;
&lt;!DOCTYPE module PUBLIC
        "-//Checkstyle//DTD Checkstyle Configuration 1.3//EN"
        "https://checkstyle.org/dtds/configuration_1_3.dtd"&gt;
&lt;module name="Checker"&gt;
  &lt;module name="RegexpMultiline"&gt;
    &lt;property name="matchAcrossLines" value="true"/&gt;
    &lt;property name="format" value="(// CONTEXT\n\s*)(System\.out\.print\()"/&gt;
    &lt;property name="message" value="Console print after specific context"/&gt;
  &lt;/module&gt;
&lt;/module&gt;
</code></pre>
<pre><code class="language-bash">Windows@Windows MINGW64 ~/check
$ java -jar checkstyle-13.1.0-all.jar -c config.xml Example.java
Starting audit...
[ERROR] C:\Users\hario\check\Example.java:3: Console print after specific context [RegexpMultiline]
Audit done.
Checkstyle ends with 1 errors.
</code></pre>
<p><strong>Current Behavior:</strong>
Violation is reported on <strong>line 3</strong> (<code>// CONTEXT</code> comment), but the actual <code>System.out.print()</code> is on <strong>line 4</strong>.</p>
<p><strong>Expected Behavior:</strong>
With a new <code>reportGroup</code> property:</p>
<pre><code class="language-xml">&lt;module name="Checker"&gt;
  &lt;module name="RegexpMultiline"&gt;
    &lt;property name="matchAcrossLines" value="true"/&gt;
    &lt;property name="format" value="(// CONTEXT\n\s*)(System\.out\.print\()"/&gt;
    &lt;property name="reportGroup" value="2"/&gt;
    &lt;property name="message" value="Console print after specific context"/&gt;
  &lt;/module&gt;
&lt;/module&gt;
</code></pre>
<p>Expected output:</p>
<pre><code class="language-bash">Starting audit...
[ERROR] C:\Users\hario\check\Example.java:4: Console print after specific context [RegexpMultiline]
Audit done.
Checkstyle ends with 1 errors.
</code></pre>
<p>Violation correctly reported on <strong>line 4</strong> where <code>System.out.print()</code> actually is.</p>
<p><strong>Capturing group breakdown:</strong></p>

Group | Captures | Line
-- | -- | --
0 | Entire match | Line 3
1 | /

*[truncated]*

---

## #18804: Kill Checker Framework violation reports for findFirstToken

Follow-up: #18482 

In #18482, a `nullUntil` function is provided as a POC, which is a good start. However, after going through the codebase, I found that `findFirstToken` is used in many places. If we add `NullUtil.notNull(...)` everywhere to assert non-null, it will introduce a lot of redundant code that is hard to read, hard to maintain, and generally ugly.

My suggestion is to introduce utility wrappers around `findFirstToken`, so that we can eliminate Checker Framework violations in a centralized and cleaner way, instead of asserting non-null at every call site.

Below are several proposals.

---
### Background and Example
I will use findFirstToken(TokenTypes.IDENT) as an example:

After scanning the codebase, there are 100+ calls to `findFirstToken(TokenTypes.IDENT)`, which result in 87 Checker Framework errors. However, in most cases, this method cannot return null.

Currently, the only known case where findFirstToken(TokenTypes.IDENT) can return null is when dealing with a receiver parameter, as shown below

```java
public static boolean isReceiverParameter(DetailAST parameterDefAst) {
    return parameterDefAst.findFirstToken(TokenTypes.IDENT) == null;
}
```
From this, we can conclude that:

When calling `ast.findFirstToken(TokenTypes.IDENT)`, only parameterDefAst may return `null`

For other AST types, the result is effectively non-null

Therefore, my core idea is to stop calling `findFirstToken` directly, and instead route all calls through a wrapper that encodes this knowledge.

---
### Solution 1: Simple wrapper utility methods

Provide two utility methods in TokenUtil (or a similar utility class):

1. TokenUtil.findIdentChild(DetailAST ast) → @Nullable DetailAST

2. TokenUtil.requireIdentChild(DetailAST ast) → @NonNull DetailAST
    Throws an exception if the result is null

Cons:
This solution is simple, but it relies on developers knowing which method to use in which context. Misuse is still possible.


### Soluction 2: Typed AST “views” (personally preferred)


Since only parameterDefAst may return null, we can encode this behavior by introducing lightweight view classes for different AST types.

```java
// Current code
DetailAST ident = methodDef.findFirstToken(TokenTypes.IDENT); // @Nullable (from Checker's perspective)

// Solution 2
MethodDefView view = MethodDefView.of(methodDef);
DetailAST ident = view.getIdent(); // @NonNull, method definitions always have IDENT

ParameterDefView view = ParameterDefView.of(parameterDef);
DetailAST ident = view.getIdent(); // @Nullable, receiver parameter is possible

```
Advantages:
Once the AST type is known (which is true in most cases), the nullability of getIdent() becomes obvious

Checker Framework violations are resolved naturally via stronger type information

Call sites become cleaner and more expressive.

I also considered creating subclasses of DetailAST instead of using composition, since inheritance could provide even stronger type guarantees. However, that approach would requi

*[truncated]*

---

## #18759: Disabling loading of module and usage of properties by some evn variable

discussed at https://github.com/checkstyle/eclipse-cs/issues/921#issuecomment-3718934260

due to fact that plugins are releasing in different frequency and there are delay to have up to date version of plugins in IDE and build system there could be situation that maven plugin use latest CS, but IDE plugin can not be updated. But users wants to use new modules.
Placing new module or new property of module to plugin makes it works for maven users and blocks all in IDE, so users have to keep version of checkstyle in as minimal that all tools support it.

suggestion is add new property to all modules `enabled` with 'true|false' values (boolean type).

same as we have https://checkstyle.org/config.html#Id

```
<module name="DescendantToken">
  <property name="id" value="someName"/>
  <property name="enabled" value="${mycomplany.jdk25enabled}"/>
</module>
```

but this approach will not help for new properties.
So we need continue brainstorming ....


https://checkstyle.org/config.html#Example-config5
```
<module name="JavadocMethod">
  <property name="severity"
    value="${checkstyle.javadoc.severity}"
    enabled="${mycomplany.jdk25enabled}"/>
</module>
```

---

## #18718: Checkstyle should update to Doxia-Core 2.0.0 to address CVE-2025-46295

Our security check reports an issue with the transitive dependencies of Checkstyle: Via its dependency on **org.apache.maven.doxia.core 1.12.0**, Checkstyle includes apache.commons.text **in the critical version of 1.3**.

(see https://nvd.nist.gov/vuln/detail/CVE-2025-46295)

Expected: Checkstyle should update to Doxia-Core 2.0.0 to fix the issue.

---

## #18679: FinalClassCheck throws NullPointerException on compact source files

While working with JDK 25 compact source files, FinalClassCheck appears to throw a NullPointerException.

The issue seems related to assumptions about AST structure that do not hold for compact source files introduced in newer Java versions.

Suspected areas include:
- Handling of typeDeclarations stack
- Access to AST children without null checks

I am currently investigating this issue and working on a fix.

---

## #18673: Organize openrewrite staticanalysis composite recipes by groups as it is done on openrewrite website

**Labels:** approved, miscellaneous

detected at https://github.com/checkstyle/checkstyle/pull/18627#discussion_r2701237696


https://docs.openrewrite.org/recipes/staticanalysis

Composite Recipes
Recipes that include further recipes, often including the individual recipes below.

Code cleanup
Common static analysis issues
Modernize BufferedWriter creation & prevent file descriptor leaks
Replace org.apache.commons.lang3.Validate#notNull with Objects#requireNonNull
Replace org.apache.commons.lang3.Validate#notNull with Objects#requireNonNull
Simplify ternary expressions
URL Equals and Hash Code


All other recipes can be grouped to non-composite group.

---

## #18660: ArrayIndexOutOfBoundsException in EmptyLineSeparatorCheck when comment immediately follows class definition

**Labels:** approved

I have read check documentation: https://checkstyle.org
I have downloaded the latest checkstyle from: https://checkstyle.org/cmdline.html#Download_and_Run
I have executed the cli and showed it below, as cli describes the problem better than 1,000 words

```bash
/var/tmp$ cat Test.java 
public class Test {
    // This comment causes a crash because there is no empty line before it

    void display(boolean ifYes) {
       if(true){
           System.out.println("Hello world");
       }
    }
}

/var/tmp$ java -jar checkstyle-13.0.0-all.jar -c /google_checks.xml Test.java
Starting audit...
com.puppycrawl.tools.checkstyle.api.CheckstyleException: Exception was thrown while processing Test.java
	at com.puppycrawl.tools.checkstyle.Checker.processFiles(Checker.java:313)
	at com.puppycrawl.tools.checkstyle.Checker.process(Checker.java:227)
	at com.puppycrawl.tools.checkstyle.Main.runCheckstyle(Main.java:429)
	at com.puppycrawl.tools.checkstyle.Main.runCli(Main.java:347)
	at com.puppycrawl.tools.checkstyle.Main.execute(Main.java:206)
	at com.puppycrawl.tools.checkstyle.Main.main(Main.java:130)
Caused by: java.lang.ArrayIndexOutOfBoundsException: Index -1 out of bounds for length 9
	at com.puppycrawl.tools.checkstyle.api.FileText.get(FileText.java:222)
	at com.puppycrawl.tools.checkstyle.api.FileContents.getLine(FileContents.java:100)
	at com.puppycrawl.tools.checkstyle.api.AbstractCheck.getLine(AbstractCheck.java:308)
	at com.puppycrawl.tools.checkstyle.checks.whitespace.EmptyLineSeparatorCheck.isTwoPrecedingPreviousLinesFromCommentEmpty(EmptyLineSeparatorCheck.java:577)
	at com.puppycrawl.tools.checkstyle.checks.whitespace.EmptyLineSeparatorCheck.isPrePreviousLineEmpty(EmptyLineSeparatorCheck.java:553)
	at com.puppycrawl.tools.checkstyle.checks.whitespace.EmptyLineSeparatorCheck.hasNotAllowedTwoEmptyLinesBefore(EmptyLineSeparatorCheck.java:474)
	at com.puppycrawl.tools.checkstyle.checks.whitespace.EmptyLineSeparatorCheck.hasMultipleLinesBefore(EmptyLineSeparatorCheck.java:367)
	at com.puppycrawl.tools.checkstyle.checks.whitespace.EmptyLineSeparatorCheck.visitToken(EmptyLineSeparatorCheck.java:171)
	at com.puppycrawl.tools.checkstyle.TreeWalker.notifyVisit(TreeWalker.java:390)
	at com.puppycrawl.tools.checkstyle.TreeWalker.processIter(TreeWalker.java:463)
	at com.puppycrawl.tools.checkstyle.TreeWalker.walk(TreeWalker.java:328)
	at com.puppycrawl.tools.checkstyle.TreeWalker.processFiltered(TreeWalker.java:212)
	at com.puppycrawl.tools.checkstyle.api.AbstractFileSetCheck.process(AbstractFileSetCheck.java:101)
	at com.puppycrawl.tools.checkstyle.Checker.processFile(Checker.java:341)
	at com.puppycrawl.tools.checkstyle.Checker.processFiles(Checker.java:300)
	... 5 more
Checkstyle ends with 1 errors.
```
---

I expect Checkstyle to parse the file and report a validation error (e.g., about missing empty lines) or process the file cleanly. It should not throw a java.lang.ArrayIndexOutOfBoundsException and crash the application.

The crash appears to happen in E

*[truncated]*

---

## #18619: Wrong error message while using check NewlineAtEndOfFile

**Labels:** approved

I have read check documentation: https://checkstyle.sourceforge.io/checks/misc/newlineatendoffile.html#NewlineAtEndOfFile
I have downloaded the latest checkstyle from: https://github.com/checkstyle/checkstyle/releases/tag/checkstyle-13.0.0
I have executed the cli and showed it below, as cli describes the problem better than 1,000 words

```
atharv@atharv-IdeaPad-3-15IIL05:~/test$ cat -A a.txt
This file has line ending CR^MThis file as new line at end of file but with CR^M
```

File as line ending CR.

```
atharv@atharv-IdeaPad-3-15IIL05:~/test$ cat config.xml
<?xml version="1.0"?>
<!DOCTYPE module PUBLIC
  "-//Puppy Crawl//DTD Check Configuration 1.3//EN"
  "https://checkstyle.org/dtds/configuration_1_3.dtd">
<module name="Checker">
  <module name="NewlineAtEndOfFile">
    <property name="lineSeparator" value="lf"/>
  </module>
</module>

```

```
atharv@atharv-IdeaPad-3-15IIL05:~/test$ java -jar checkstyle-13.0.0-all.jar -c config.xml a.txt
Starting audit...
[ERROR] /home/atharv/test/a.txt:1: File does not end with a newline. [NewlineAtEndOfFile]
Audit done.
Checkstyle ends with 1 errors.
```

Error expected was:
`Expected line ending for file is LF(\\n), but CR(\\r) is detected.`

Similar kind of example is used https://checkstyle.sourceforge.io/checks/misc/newlineatendoffile.html#Example3-code

CR is considered valid line separator: https://checkstyle.sourceforge.io/property_types.html#LineSeparatorOption

---

## #18615: False positive: indentation of text block inside annotation array parameters

**Labels:** approved, indentation

I have read check documentation: https://checkstyle.sourceforge.io/checks/misc/indentation.html
I have downloaded the latest checkstyle from: https://checkstyle.org/cmdline.html#Download_and_Run
I have executed the cli and showed it below, as cli describes the problem better than 1,000 words

```cmd
E:\temp\CheckstyleReport>type config.xml
<?xml version="1.0"?>
<!DOCTYPE module PUBLIC
          "-//Puppy Crawl//DTD Check Configuration 1.3//EN"
          "https://checkstyle.org/dtds/configuration_1_3.dtd">
<module name="Checker">
  <module name="TreeWalker">
    <module name="Indentation" />
  </module>
</module>

E:\temp\CheckstyleReport>type Test.java
public class Test {
    @interface Anno {
        String [] value();
    }

    @Anno({
        """
        example
        """
    })
    void method() {
    }
}
E:\temp\CheckstyleReport>set RUN_LOCALE="-Duser.language=en -Duser.country=US"

E:\temp\CheckstyleReport>java %RUN_LOCALE% -jar checkstyle-13.0.0-all.jar -c config.xml Test.java
Starting audit...
[ERROR] E:\temp\CheckstyleReport\Test.java:9:9: 'annotation array initialization' child has incorrect indentation level 8, expected level should be 12. [Indentation]
Audit done.
Checkstyle ends with 1 errors.
```

**Describe what you expect in detail.**
End of text block formatting shouldn't cause violation of indentation rules.

---

## #18614: False positive: indentation inside of constructor parameters inside try block

**Labels:** approved, indentation, miscellaneous

I have read check documentation: https://checkstyle.sourceforge.io/checks/misc/indentation.html
I have downloaded the latest checkstyle from: https://checkstyle.org/cmdline.html#Download_and_Run
I have executed the cli and showed it below, as cli describes the problem better than 1,000 words


Attention: file contains TABs

```cmd
E:\temp\CheckstyleReport>type config.xml
<?xml version="1.0"?>
<!DOCTYPE module PUBLIC
          "-//Puppy Crawl//DTD Check Configuration 1.3//EN"
          "https://checkstyle.org/dtds/configuration_1_3.dtd">
<module name="Checker">
  <property name="tabWidth" value="4"/>

  <module name="TreeWalker">
    <module name="Indentation" />
  </module>
</module>

E:\temp\CheckstyleReport>type Test.java
public class Test {
        private Test client;

        private Test(String string) {
        }

        private void test() {
                try {
                        client = new Test(
                                null // unexpected violation about indentation
                        );
                } catch (Exception e) {
                }
        }
}
E:\temp\CheckstyleReport>set RUN_LOCALE="-Duser.language=en -Duser.country=US"

E:\temp\CheckstyleReport>java %RUN_LOCALE% -jar checkstyle-13.0.0-all.jar -c config.xml Test.java
Starting audit...
[ERROR] E:\temp\CheckstyleReport\Test.java:10:17: 'new' child has incorrect indentation level 16, expected level should be 20. [Indentation]
Audit done.
Checkstyle ends with 1 errors.
```

---

**Describe what you expect in detail.**
The violation shouldn't be reported: the parameter passed to the constructor is already indented correctly.

NOTE: if we remove the try/catch block the violation disappears.
NOTE2: the file is formatted by tabs

---

---

## #18590: False Negative in EmptyStatement Check

**Labels:** approved

I have read check documentation: https://checkstyle.sourceforge.io/checks/coding/emptystatement.html#EmptyStatement
I have downloaded the latest checkstyle from: https://github.com/checkstyle/checkstyle/releases/tag/checkstyle-13.0.0
I have executed the cli and showed it below, as cli describes the problem better than 1,000 words

```
atharv@atharv-IdeaPad-3-15IIL05:~/test$ cat config.xml
<?xml version="1.0"?>
<!DOCTYPE module PUBLIC
    "-//Checkstyle//DTD Checkstyle Configuration 1.3//EN"
    "https://checkstyle.org/dtds/configuration_1_3.dtd">
<module name="Checker">
  <property name="severity" value="error"/>
  <property name="fileExtensions" value="java, properties, xml"/>
  <module name="TreeWalker">
    <module name="EmptyStatement"/>
  </module>
</module>

```

```
atharv@atharv-IdeaPad-3-15IIL05:~/test$ cat Test.java
public class Test {
    ; // expected violation
    ; // expected violation
    ; // expected violation

    public void name() {
        ; // violation
        ; // violation

        for (int i = 0; i < 6; i++) {
            ; // violation
            ; // violation
        }
    }
}

```
```
atharv@atharv-IdeaPad-3-15IIL05:~/test$ java -jar checkstyle-13.0.0-all.jar -c config.xml Test.java
Starting audit...
[ERROR] /home/atharv/test/Test.java:7:9: Empty statement. [EmptyStatement]
[ERROR] /home/atharv/test/Test.java:8:9: Empty statement. [EmptyStatement]
[ERROR] /home/atharv/test/Test.java:11:13: Empty statement. [EmptyStatement]
[ERROR] /home/atharv/test/Test.java:12:13: Empty statement. [EmptyStatement]
Audit done.
Checkstyle ends with 4 errors.

```

---

## #18571: Google-style: New Check BlockCommentEndPositionCheck

**Labels:** approved, new module

From #18273

`BlockCommentEndPositionCheck` should validate position of `*/`. And have property `strategy` with the values `alone` or `along_or_singleline` and default value should be `alone_or_singleLine`.

[7.1.1 General Form](https://google.github.io/styleguide/javaguide.html#s7.1.1-javadoc-multi-line) and https://github.com/google/google-java-format/issues/1279#issuecomment-3320778635

> The preferred style is to put /** and */ on their own lines (unless the entire javadoc comment fits on a single line), and to include a leading * on each line.

### Example config with default value:
```
<?xml version="1.0"?>
<!DOCTYPE module PUBLIC
        "-//Checkstyle//DTD Checkstyle Configuration 1.3//EN"
        "https://checkstyle.org/dtds/configuration_1_3.dtd">

<module name="Checker">
    <module name="TreeWalker">
        <module name="BlockCommentEndPosition"/>
    </module>
</module>
```

### Test.java
```
/**
 * Testing misaligned leading asterisks.
 */
public class Test {

  /**  Javadoc for instance variable. */   // ok, default value is `alone_or_singleline`
  private String xyz;

  /**
   * If leading asterisk is not present then identation is not checked.
   */
  private int age;

  /**
   * Leading asterisk not present. */  // violation ''BLOCK_COMMENT_END' must be on the new line.'
  private void foo1() {}

  /**
   * Correct Indentation for leading asterisk. */ // violation ''BLOCK_COMMENT_END' must be on the new line.'
  private void foo2() {}

  /** 
   * Testing... 
   */
  public static void main(String[] args) {
    System.out.println("Hello, World!");
  }
}
```

### Example output:
```
$ java -jar testing/checkstyle-10.25.0-all.jar -c config.xml TextBlocks.java 
Starting audit...
[WARN] Test.java:15:36: 'BLOCK_COMMENT_END' must be on the new line. [BlockCommentEndPosition]
[WARN] Test.java:19:48 'BLOCK_COMMENT_END' must be on the new line. [BlockCommentEndPosition]
Audit done.
```

## Example with `alone` value:

### config:
```
<?xml version="1.0"?>
<!DOCTYPE module PUBLIC
        "-//Checkstyle//DTD Checkstyle Configuration 1.3//EN"
        "https://checkstyle.org/dtds/configuration_1_3.dtd">

<module name="Checker">
    <module name="TreeWalker">
        <module name="BlockCommentEndPosition">
            <property name="strategy" value="alone">
        </module>
    </module>
</module>
```

### Test.java
```
/**
 * Testing misaligned leading asterisks.
 */
public class Test {

  /**  Javadoc for instance variable. */   // violation ''BLOCK_COMMENT_END' must be on the new line.'
  private String xyz;

  /**
   * If leading asterisk is not present then identation is not checked.
   */
  private int age;

  /**
   * Javadoc for instance method foo1. */  // violation ''BLOCK_COMMENT_END' must be on the new line.'
  private void foo1() {}

  /**
   *  Javadoc for instance method foo2. */ // violation ''BLOCK_COMMENT_END' must be on the new line.'
  private void foo2() {}

  /** 
   * Testing... 
   */
  public static void main(Strin

*[truncated]*

---

## #18570: New Check: PreferJavadocInlineTagsCheck - prefer {@code}, {@link}, {@literal} over HTML tags

**Labels:** approved, new module

## New Check: PreferJavadocInlineTagsCheck - prefer {@code}, {@link}, {@literal} over HTML tags

I have downloaded the latest cli from: https://checkstyle.org/cmdline.html#Download_and_Run
I have executed the cli and showed it below, as cli describes the problem better than 1,000 words

**How it works Now:**

```bash
vivek@Viveks-MacBook-Air checkstyle % cat > /tmp/Test.java << 'EOF'
/**
 * Returns <code>true</code> if the value is valid.
 * See <a href="#validate()">validate</a> for details.
 * Use &lt;T&gt; for generic types.
 */
public class Test {
    /**
     * Returns <code>false</code> when empty.
     */
    public boolean validate() {
        return true;
    }
}
EOF

cat /tmp/Test.java

/**
 * Returns <code>true</code> if the value is valid.
 * See <a href="#validate()">validate</a> for details.
 * Use &lt;T&gt; for generic types.
 */
public class Test {
    /**
     * Returns <code>false</code> when empty.
     */
    public boolean validate() {
        return true;
    }
}


java -Duser.language=en -Duser.country=US -jar checkstyle-13.0.0-all.jar -c src/main/resources/sun_checks.xml /tmp/Test.java

Starting audit...
Audit done.
```

Is your feature request related to a problem? Please describe.

According to OpenJDK's updated Java Style Guidelines (v6) on [Javadoc](https://cr.openjdk.org/~alundblad/styleguide/index-v6.html#toc-javadoc):
> "Prefer inline tags (such as {@code …} and {@link …} etc) over corresponding HTML tags (<code>…</code>, <a href="…">…</a> etc)."

Currently, there is no check to enforce this preference. Developers may use HTML tags in Javadoc when Javadoc inline tags would be more appropriate.

**Describe the solution you'd like**

A new check `PreferJavadocInlineTagsCheck` that flags:
1. `<code>...</code>` → should use `{@code ...}`
2. `<a href="#...">` (internal links) → should use `{@link ...}`
3. `&lt;` and `&gt;` → should use `{@literal <}` and `{@literal >}`

**Expected Output:**
```
Starting audit...
[WARN] Test.java:2:13: Use '{@code ...}' instead of '<code>...</code>'. [PreferJavadocInlineTags]
[WARN] Test.java:3:6: Use '{@link ...}' instead of '<a href="#...">'. [PreferJavadocInlineTags]
[WARN] Test.java:4:6: Use '{@literal}' instead of '&lt;' or '&gt;'. [PreferJavadocInlineTags]
[WARN] Test.java:7:13: Use '{@code ...}' instead of '<code>...</code>'. [PreferJavadocInlineTags]
Audit done.
```

**Expected configuration:**

```xml
<module name="Checker">
  <module name="TreeWalker">
    <module name="PreferJavadocInlineTags"/>
  </module>
</module>
```
What should NOT be flagged:

- External URLs: `<a href="https://..."> `(no Javadoc equivalent)
- Block tags: `<pre>, <p>, <ul>, <li>,` etc. (no Javadoc equivalent)
- Tags inside `<pre>` blocks (code examples)

---

## #18534: Spotless Plugin Not Applied and Build Passes Despite Errors #18470 #18479

### Summary
Spotless formatting tool fails locally but CI doesn't detect the issues. Similar to the PMD problem (#18479), there's inconsistency between local and CI environments.

### Details
After recent CI configuration changes, Spotless is not properly failing the build in CI when formatting issues are found locally. This suggests either:
1. Spotless is not running in CI
2. Spotless configuration differs between local and CI
3. CI is configured to ignore Spotless failures

### Expected Behavior
- Spotless should run successfully both locally and in CI
- CI should fail when Spotless detects formatting violations
- Local and CI behavior should be consistent
- Developers should get immediate feedback about formatting issues

### Current Behavior
- Spotless fails when running locally (`./mvnw spotless:check`)
- CI pipeline continues without detecting the Spotless failures
- Inconsistent behavior between local development and CI environments

### Impact
- Code formatting inconsistencies may reach the repository
- Developers waste time debugging formatting issues that CI should catch
- Inconsistent code style across the codebase
- Reduced effectiveness of automated formatting tools

### Steps to Reproduce
1. Run locally: `./mvnw spotless:check`
2. Observe formatting violations (if any)
3. Push changes to CI
4. CI passes even though local check failed

### Configuration Check Needed
Verify:
- Spotless is included in CI pipeline
- Spotless configuration is identical in local and CI
- CI properly fails on Spotless violations
- No `-DskipSpotless` or similar flags in CI configuration

### Related Issues
- #18479 - PMD Tool Fails Locally but CI Doesn't Detect It
- Recent CI configuration changes may have affected both tools

### Notes
Similar to the PMD issue, this suggests a configuration discrepancy. Need to ensure:
1. Spotless runs in CI with same parameters as local
2. CI correctly interprets Spotless exit codes
3. No silent skipping of Spotless in CI workflow


```
Caused by: org.apache.maven.plugin.MojoExecutionException: The following files had format violations:
    target/test-classes/com/puppycrawl/tools/checkstyle/grammar/comments/InputComments1.java                                                                                                                                             
        @@ -1,3 +1,22 @@                                                                                                                                                                                                                 
        +///////////////////////////////////////////////////////////////////////////////////////////////                                                                                                                                 
        +//·checkstyle:·Checks·Java·source·code·and·other·text·files·for·adherence·to·a·set·of·rules.                                                                                                  

*[truncated]*

---

## #18462: Null-pointers in multiple checks when dealing with compact source files

In PR

- #18418

we add ANTLR support for compact source files[^1]. Normally, this would allow us to remove some `BeforeExecutionExclusionFileFilter`s from `openjdk25-excluded.files` related to issue #17810. However, 10 checks currently throw `NullPointerException`s when processing the structure of compact source files. These failures are typically caused by code that assumes a fixed AST shape, such as `ast.getParent().getParent()`.

Because of this, we cannot remove the existing `BeforeExecutionExclusionFileFilter`s until **all** related null-pointer issues are fixed. The affected checks are:

* [ ] FinalLocalVariable
* [ ] RequireThis
* [ ] MethodName
* [ ] UnusedLocalVariable
* [ ] AbbreviationAsWordInName
* [ ] MissingOverride
* [ ] DesignForExtension
* [ ] EmptyLineSeparator
* [ ] FinalClass
* [ ] JavadocStyle
* [ ] MissingOverrideOnRecordAccessor

Each of these checks must be updated to correctly handle compact source files. Only after **all** null-pointer issues are resolved can we safely remove the `BeforeExecutionExclusionFileFilter`s.

EDIT: Once null-pointers are fixed, we must also remove ignore added in https://github.com/checkstyle/contribution/pull/1009

> [!IMPORTANT]
> Before fixing a null-pointer in any of the checks listed above, you must first create a dedicated issue for that check that includes a reproducible example of the `NullPointerException`.

> [!NOTE]
> I solved all of these null-pointers before creating this issue in commit https://github.com/checkstyle/checkstyle/commit/8a3216837645e9ea87c072d98f70979caefece02. Feel free to grab the solutions and/or test files from there.

[^1]: [JEP 512: Compact Source Files and Instance Main Methods](https://openjdk.org/jeps/512)

---

## #18453: Exclude external and generated files from spell checking

**Labels:** approved

### Exclude external and generated files from spell checking

Spell checking is currently being applied to **external / generated files**, which causes **significant and unnecessary maintenance effort and cost**, without providing any real value.

This became visible after the changes introduced in:

- https://github.com/checkstyle/checkstyle/pull/18434

As a result, files that are **not authored or maintained by the Checkstyle project** (for example:
generated files, vendored files, or third-party content) are now subject to spelling validation.

### Why this is a problem

* External files are **not under project control**
* Fixing spelling issues in such files is either:
  * impossible, or
  * creates constant rework when those files are regenerated or updated
* This leads to:
  * noisy CI failures
  * wasted developer time
  * increased contribution friction
  * no actual improvement in Checkstyle source quality

In short: **high cost, zero benefit**.

### Expected behavior

Spell checking should be **limited to files that are owned and maintained by the project**, for example:

* source code
* documentation authored by the project

External, generated, or third-party files should be **explicitly excluded** from spell checking.

### Actual behavior

Spell checking is applied broadly, including external files, which causes repeated failures and manual intervention.

### Visual examples

Screenshots showing the issue in practice:

- ![example 1](https://github.com/user-attachments/assets/ae504b0e-5987-4c5d-817a-66f547cb8dfe)
- ![example 2](https://github.com/user-attachments/assets/f0790be6-1634-445f-b58a-8a09dbaa2f99)

### Request

Please exclude external files from spell checking, or provide a supported configuration mechanism to opt them out.

This would significantly reduce unnecessary maintenance effort while keeping spell checking effective where it actually matters.

ONLY:
- mvnw files
- config/rewrite.yml

---

## #18438: False positive: EmptyLineSeparator reports violation on method call

**Labels:** approved

reported at https://github.com/checkstyle/checkstyle/pull/18311#issuecomment-3691084557

I have read check documentation: https://checkstyle.org/checks/whitespace/emptylineseparator.html#EmptyLineSeparator
I have downloaded the latest checkstyle from: https://checkstyle.org/cmdline.html#Download_and_Run
I have executed the cli and showed it below, as cli describes the problem better than 1,000 words

`EmptyLineSeparator` reports violation on method call which wrong. It only occurs when there are more than one empty lines before a method call.

#### Config:
```
<?xml version="1.0"?>
<!DOCTYPE module PUBLIC "-//Puppy Crawl//DTD Check Configuration 1.3//EN"
   "http://www.puppycrawl.com/dtds/configuration_1_3.dtd">

<module name="Checker">
  <module name="TreeWalker">
    <module name="EmptyLineSeparator">
      <property name="tokens"
               value="PACKAGE_DEF, IMPORT, STATIC_IMPORT, CLASS_DEF, INTERFACE_DEF, ENUM_DEF,
                    STATIC_INIT, INSTANCE_INIT, METHOD_DEF, CTOR_DEF, VARIABLE_DEF, RECORD_DEF,
                    COMPACT_CTOR_DEF"/>
      <property name="allowNoEmptyLineBetweenFields" value="true"/>
      <property name="allowMultipleEmptyLines" value="false"/>
      <property name="allowMultipleEmptyLinesInsideClassMembers" value="false"/>
    </module>
  </module>
</module>
```

#### Test.java:
```
import org.junit.Test;                              // 1
import org.junit.Assert;                            // 2
                                                    // 3
public class Test {                                 // 4
                                                    // 5
  public void foo(int a) {}                         // 6
                                                    // 7
  @Test                                             // 8
  public void testFoo() {                           // 9
                                                    // 10
                                                    // 11
    int a = 10;                                     // 12
                                                    // 13
                                                    // 14
    Test t = new Test();                            // 15
                                                    // 16
                                                    // 17
    t.foo(10);                                      // 18
    int b = 20;                                     // 19
                                                    // 20
                                                    // 21
    Assert.assertFalse(false);                      // 22
  }                                                 // 23
}                                                   // 24
```

#### Actual Cli:
```
$ java -jar checkstyle-12.3.0-all.jar -c config_check.xml Test.java
Starting audit...
[ERROR] F:\GitHub\headhtmltagname\Test.java:9:25: There is more than 1 empty line after this line. [EmptyLineSeparator]
[ERROR] F:\GitHub\headhtmltagname\Tes

*[truncated]*

---

## #18437: EmptyLineSeparatorCheck does not report violations when more than one empty line appears with enum constants.

**Labels:** approved

I have read check documentation: https://checkstyle.org/checks/whitespace/emptylineseparator.html#EmptyLineSeparator
I have downloaded the latest checkstyle from: https://checkstyle.org/cmdline.html#Download_and_Run
I have executed the cli and showed it below, as cli describes the problem better than 1,000 words

#### Config:
```
<?xml version="1.0"?>
<!DOCTYPE module PUBLIC "-//Puppy Crawl//DTD Check Configuration 1.3//EN" 
      "http://www.puppycrawl.com/dtds/configuration_1_3.dtd">

<module name="Checker">
  <module name="TreeWalker">
    <module name="EmptyLineSeparator">
      <property name="tokens"
               value="PACKAGE_DEF, IMPORT, STATIC_IMPORT, CLASS_DEF, INTERFACE_DEF, ENUM_DEF,
                    STATIC_INIT, INSTANCE_INIT, METHOD_DEF, CTOR_DEF, VARIABLE_DEF, RECORD_DEF,
                    COMPACT_CTOR_DEF"/>
      <property name="allowNoEmptyLineBetweenFields" value="true"/>
      <property name="allowMultipleEmptyLines" value="false"/>
      <property name="allowMultipleEmptyLinesInsideClassMembers" value="false"/>
    </module>
  </module>
</module>
```

#### Test.java:
```
public class Test {                                                          // 1
                                                                             // 2
  public enum Check {                                                        // 3
                                                                             // 4
    FIRST,                                                                   // 5
    SECOND,                                                                  // 6
                                                                             // 7
    THIRD,                                                                   // 8
                                                                             // 9
                                                                             // 10
    FOURTH,                                                                  // 11
                                                                             // 11
                                                                             // 12
                                                                             // 13
    SPECIAL(100) {                                                           // 14
      @Override                                                              // 15
      public String describe() {                                             // 16
          return "Special enum constant";                                    // 17
      }                                                                      // 18
    },                                                                       // 19
                                                                             // 20
                                                                             // 21
                                                                  

*[truncated]*

---

## #18435: Fix xdocs Examples AST Consistency Test (Reduce suppressions list)

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

https://github.com/checkstyle/checkstyle/blob/a94bdd41cb3f0873bed87c619d200fe1754627f7/src/test/java/com/puppycrawl/tools/checkstyle/internal/XdocsExamplesAstConsistencyTest.java#L89-L92

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

Example can be found here: https://github.com/checkstyle/checkstyle/commit/0

*[truncated]*

---

## #18423: ImportOrder: add support for Java 25's module imports

Part of issue https://github.com/checkstyle/checkstyle/issues/18127

I have read check documentation: https://checkstyle.org/checks/imports/importorder.html
I have downloaded the latest cli from: https://checkstyle.org/cmdline.html#Download_and_Run
I have executed the cli and showed it below, as cli describes the problem better than 1,000 words

**How it works Now:**

```bash
/tmp/importorder-test $ cat config.xml
<?xml version="1.0"?>
<!DOCTYPE module PUBLIC
    "-//Checkstyle//DTD Checkstyle Configuration 1.3//EN"
    "https://checkstyle.org/dtds/configuration_1_3.dtd">

<module name="Checker">
  <module name="TreeWalker">
    <module name="ImportOrder">
      <property name="option" value="top"/>
      <property name="groups" value="java,javax"/>
      <property name="ordered" value="true"/>
      <property name="separated" value="true"/>
      <property name="sortStaticImportsAlphabetically" value="true"/>
    </module>
  </module>
</module>

/tmp/importorder-test $ cat Test.java
import module java.sql;
import module java.base;

import static java.lang.System.out;

import java.util.List;
import java.util.Map;

public class Test {
    public static void main(String[] args) {
        out.println("Hello");
    }
}

/tmp/importorder-test $ RUN_LOCALE="-Duser.language=en -Duser.country=US"
/tmp/importorder-test $ java $RUN_LOCALE -jar checkstyle-12.3-all.jar -c config.xml Test.java
Starting audit...
Audit done.
```

Note: Module imports java.sql and java.base are out of alphabetical order, but no violation is reported.

Is your feature request related to a problem? Please describe.

ImportOrder check currently handles type imports (import) and static imports (import static), but completely ignores Java 25's module imports (import module). Module imports are not checked for ordering, grouping, or separation.

Describe the solution you'd like

Add support for module imports with new properties:

| Property | Type | Description | Default |
|----------|------|-------------|---------|
| `moduleOption` | ImportOrderOption | Position of module imports (top, bottom, etc.) | `top` |
| `moduleGroups` | String[] | Groups for module imports | `{}` |
| `separatedModuleGroups` | boolean | Separate module groups with blank line | `false` |
| `sortModuleImportsAlphabetically` | boolean | Sort module imports alphabetically | `true` |

Expected CLI output after fix:

```
tmp/importorder-test $ java $RUN_LOCALE -jar checkstyle-X.XX-all.jar -c config.xml Test.java
Starting audit...
[ERROR] Test.java:2:1: Wrong order for 'java.base' import. [ImportOrder]
Audit done.
```

---

## #18420: New Check: GoogleMethodNameCheck to enforce Google Java Style Guide method naming

**Labels:** approved, new module

split from https://github.com/checkstyle/checkstyle/issues/17841 , we split creation of module and activation of it in google style config to separate issues, to simplify integration.


Create a new check GoogleMethodNameCheck to enforce method naming conventions per the [Google Java Style Guide §5.2.3](https://google.github.io/styleguide/javaguide.html#s5.2.3-method-names).

## Background (Reason for new check)

The current MethodName check with regex configuration cannot fully enforce Google Style method naming rules because:
1.  It cannot distinguish between test methods (with `@Test`) and regular methods
2. Test methods have different underscore rules than regular methods
3. The regex-based approach has limitations with complex patterns (as noted in #17708)

## Proposed Rules

### For Regular Methods (without @Test ...):
- Must be lowerCamelCase (e.g., transferMoney, parseUrl)
- Single character names are invalid (e.g., `f`)
- Underscores only allowed between **adjacent numbers** (numbering suffix)
- Examples:
  - foo123                    // ok
  -  guava33_4_5       // ok (digit_digit)
  - mName                  // violation  special prefix not allowed as per [§5.1](https://google.github.io/styleguide/javaguide.html#s5-naming)
  -  fO                          // violation starts with  lowercase+uppercase 
  -  gradle_9_5_1        // violation underscore between letter-digit not allowed
  -  foo_bar                 // violation underscore between letter-letter not allowed for regular methods
  -  guava33_4_5_   // violation trailing underscore not allowed
  - _foo                        // violation leading underscore not allowed

### For Test Methods (with @Test, @ParameterizedTest, @RepeatedTest):
- Underscores allowed to separate logical components
- Underscores are allowed between **adjacent numbers** (numbering suffix)
- Each component must be lowerCamelCase
- Each component must be 2-character minimum 
- Examples:
  -  transferMoney_deductsFromSource // ok
  - test_foo // ok
  - test3_1 // ok  underscore between adjacent numbers (numbering suffix)
  - test_1 // violation (underscore between letter-digit)
  - testing_Foo // violation (2nd component starts with uppercase)
  - test_fOo // violation starts with  lowercase+uppercase 
  - test_a // violation single character component 
  - testing_foo_  // violation trailing underscore not allowed

###  Note:
 - Methods annotated with `@Override` are skipped because their names are defined by the parent type and are not a local naming choice.

---

## #18419: CustomImportOrder: add `MODULE_IMPORT` group to ensure user-specified order is maintained

**Labels:** blocked, google style

Part of issue #18127 

I have read check documentation: https://checkstyle.org/checks/imports/customimportorder.html#CustomImportOrder
I have downloaded the latest cli from: https://checkstyle.org/cmdline.html#Download_and_Run
I have executed the cli and showed it below, as cli describes the problem better than 1,000 words

**How it works Now:**

```bash
/var/tmp $ javac Example.java
# no output, because file compiles successfully

/var/tmp $ cat config.xml
<?xml version="1.0"?>
<!DOCTYPE module PUBLIC
  "-//Puppy Crawl//DTD Check Configuration 1.3//EN"
  "https://checkstyle.org/dtds/configuration_1_3.dtd">
<module name="Checker">
    <module name="TreeWalker">
        <module name="CustomImportOrder">
            <property name="customImportOrderRules"
                value="STATIC, STANDARD_JAVA_PACKAGE, THIRD_PARTY_PACKAGE"
            />                   
        </module>
    </module>
</module>

/var/tmp $ cat Example.java
package com.puppycrawl.tools.checkstyle.checks.imports;

import com.puppycrawl.tools.checkstyle.checks.imports.*;
import static java.util.Collections.*;
import java.time.*;
import static java.io.File.separator;
import module java.base;

public class Example {
}

/var/tmp $ RUN_LOCALE="-Duser.language=en -Duser.country=US"
/var/tmp $ java $RUN_LOCALE -jar checkstyle-12.3.0-all.jar -c config.xml Example.java
Starting audit...
Audit done.
```

**Is your feature request related to a problem? Please describe.**
Yes, `CustomImportOrderCheck` currently does not support `MODULE_IMPORT` which is introduced in Java 25

**Describe the solution you'd like**
I would like to modify `CustomImportOrderCheck` to support `MODULE_IMPORT`, ensuring that the user-specified order is maintained for `MODULE_IMPORT` as well.

I imagine a configuration like:
```bash
<module name="CustomImportOrder">
    <property name="customImportOrderRules"
        value="STATIC, MODULE, STANDARD_JAVA_PACKAGE, THIRD_PARTY_PACKAGE"
    />
</module>
```

that shows violations for the following code:
```java
import module java.base;
import static java.io.File.separator;
import java.time.*;
import static java.util.Collections.*;
import com.puppycrawl.tools.checkstyle.checks.imports.*;
```
with violations like the following:
```bash
[ERROR] /home/saad/code/gsoc/checkstyle-tests/Example.java:1:1: Import statement for 'java.util.Collections.*' is in the wrong order. Should be in the 'MODULE' group, expecting group 'MODULE' on this line. [CustomImportOrder]
Audit done.
Checkstyle ends with 1 error.
```

---

## #18361: NoClassDefFound Exception during compilation on jdk25

**Labels:** approved, miscellaneous

JDK Version : 25.0.1
Maven Version : 3.9.11
Operating System : Windows 11 Home

When trying to build checkstyle:

Command : ./mvnv install

screenshot:
<img width="1461" height="651" alt="Image" src="https://github.com/user-attachments/assets/40777391-c39e-4b82-8e58-46f0ac8026c8" />

---

## #18273: Closing asterisk */ not on its own line not detected for google style

**Labels:** google style, false negative

From: [7.1.1 General Form](https://google.github.io/styleguide/javaguide.html#s7.1.1-javadoc-multi-line) and https://github.com/google/google-java-format/issues/1279#issuecomment-3320778635

7.1.1 General form
The basic formatting of Javadoc blocks is as seen in this example:

```
/**
 * Multiple lines of Javadoc text are written here,
 * wrapped normally...
 */
public int method(String p1) { ... }
```
... or in this single-line example:
`/** An especially short bit of Javadoc. */`
The basic form is always acceptable. The single-line form may be substituted when the entirety of the Javadoc block (including comment markers) can fit on a single line.

---
Part of [17778](https://github.com/checkstyle/checkstyle/issues/17778), subproblem 3

According to Google Java Style, the preferred form is to place `/**` and `*/` on their own lines unless the entire Javadoc comment fits on a single line. However, in `google_checks.xml`, the [JavadocLeadingAsteriskAlign](https://checkstyle.org/checks/javadoc/javadocleadingasteriskalign.html) check validates the alignment of the closing asterisk only when whitespace appears before the `*/`. It ignore the alignment of leading asterisk when non-whitespace characters appear before the `*/`. The following example is:
```
  /**
   * Correct Indentation for leading asterisk. */
  private void foo2() {}
```
If we can add support for validating the alignment of the closing `*/`, it would improve compliance with the Google Javadoc style.

#### Google Formatter

Test.java
```
public class Test {
  
  /**
   * void constructor.
   *
   * @param a testing... */
  public Test(int a) {}

}
```
cli:
`$ java -jar google-java-format-1.33.0-all-deps.jar Test.java > FormattedCode.java`

Formatted Code:
```
public class Test {

  /**
   * void constructor.
   *
   * @param a testing...
   */
  public Test(int a) {}
}
```
Cli:
```
$ diff -Naru Test.java FormattedCode.java
--- Test.java   2025-12-12 00:50:02.874673400 +0530
+++ FormattedCode.java  2025-12-12 00:51:12.628082900 +0530
@@ -1,9 +1,9 @@
 public class Test {
-
+
   /**
    * void constructor.
    *
-   * @param a testing... */
+   * @param a testing...
+   */
   public Test(int a) {}
-
 }
```

---

## #18271: Leading asterisk is not detected at the beginning of javadoc content for google style

From: [7.1.1 General Form](https://google.github.io/styleguide/javaguide.html#s7.1.1-javadoc-multi-line) and https://github.com/google/google-java-format/issues/1279#issuecomment-3320778635

7.1.1 General form
The basic formatting of Javadoc blocks is as seen in this example:

```
/**
 * Multiple lines of Javadoc text are written here,
 * wrapped normally...
 */
public int method(String p1) { ... }
```
... or in this single-line example:
`/** An especially short bit of Javadoc. */`
The basic form is always acceptable. The single-line form may be substituted when the entirety of the Javadoc block (including comment markers) can fit on a single line.

---
Part of https://github.com/checkstyle/checkstyle/issues/17778, subproblem 1

According to Google Java Style, Javadoc content must begin on the second line after `/**`, and leading asterisks are treated as part of the content. However, in the following example:
```
/*************************************************
 * @param str testing.....
 */
public InputCorrectJavadocLeadingAsteriskAlignment(String str) {}
```
the leading asterisks that appear immediately after `/**` are treated as Javadoc content. [JavadocContentLocation](https://checkstyle.org/checks/javadoc/javadoccontentlocation.html#JavadocContentLocation) ignores such content because the check explicitly states that content beginning with a leading asterisk is skipped. As a result, this case becomes a false negative, even though the Google Style Guide requires validation of content starting rules.

please, work on this issue after merging #18255

---

## #18251: Infrastructure: CI failure in PRs due to Eclipse Static Analysis's compiler update (R-4.38)

**Labels:** approved, miscellaneous

We did workaround at https://github.com/checkstyle/checkstyle/pull/18253/files to reproduce following issue, we need to revert such update.

The Semaphore 2.0 CI pipeline is consistently failing the Eclipse Static Analysis validation step (.ci/validation.sh eclipse-static-analysis) for a multitude of PRs. ( [Example1](https://checkstyle.semaphoreci.com/jobs/0583e10d-9f9c-439e-9921-11334a67c49f) , [Example2](https://checkstyle.semaphoreci.com/workflows/f5c4fe8d-03f2-4c71-85ff-5883afd44ad9?pipeline_id=ae552ce8-1dcb-4ce2-80da-26a186a5d1e1))

The build script compares the supported options of the downloaded eclipse compiler version against `config/org.eclipse.jdt.core.prefs`.

The latest compiler version introduces the key `org.eclipse.jdt.core.compiler.problem.memberOfDeprecatedTypeNotDeprecated`, causing the validation check to fail when this key is missing from the configuration file.

This issue is currently blocking all active Pull Requests that run this validation step.

As mentioned in logs as such:
```
 org.eclipse.jdt.core.compiler.problem.invalidJavadocTagsNotVisibleRef 00:48
 org.eclipse.jdt.core.compiler.problem.invalidJavadocTagsVisibility 00:48
 org.eclipse.jdt.core.compiler.problem.localVariableHiding 00:48
+org.eclipse.jdt.core.compiler.problem.memberOfDeprecatedTypeNotDeprecated 00:48
 org.eclipse.jdt.core.compiler.problem.methodWithConstructorName 00:48
 org.eclipse.jdt.core.compiler.problem.missingDefaultCase 00:48
 org.eclipse.jdt.core.compiler.problem.missingDeprecatedAnnotation 00:48
please update config/org.eclipse.jdt.core.prefs file
```
Solution is just to add it into config/org.eclipse.jdt.core.prefs.

---

## #18228: False-positive: Suppress indentation check when quotes start at the left margin

**Labels:** approved, indentation, google style, false positive

Follow-up of #17329
From docs: https://google.github.io/styleguide/javaguide.html#s4.2-block-indentation
> [opening quotes] may either follow the same indentation rules as other constructs, or it may have no indentation at all (so it starts at the left margin).

Currently, TextBlockGoogleStyleFormatting Check covers:

- [x] Both opening and closing quotes are on their own lines.
- [x] Opening quotes are vertically aligned with closing quotes, i.e, both must have the same indentation value
- [ ] #18227 

- [ ] Quotes can have zero indentation 

Code:
```java
/** somejavadoc. */
public class InputTextBlocksIndentation {

  public void textFunc() {

    String zeroIndentation = // False-positive below
"""
content of the block
""";                         // False-positive

    getData( OK, below
    """    
        Indentation of Text-block
    """,  // OK
        5
    );
  }

  public static void getData(String data, int length) {}
```


Cli:

```
$ java -jar checkstyle-11.1.0-all.jar -c google_checks.xml InputTextBlocksIndentation.java
Starting audit...
[WARN] InputTextBlocksIndentation.java:6:1: '"""' has incorrect indentation level 0, expected level should be 8. [Indentation]
[WARN] InputTextBlocksIndentation.java:9:1: '"""' has incorrect indentation level 0, expected level should be 8. [Indentation]
[WARN] InputTextBlocksIndentation.java:12:5: 'method call' child has incorrect indentation level 4, expected level should be 6. [Indentation]
[WARN] InputTextBlocksIndentation.java:14:5: 'method call' child has incorrect indentation level 4, expected level should be 6. [Indentation]
Audit done.
```

The first two violations are not expected, as Google-style allows for indenting opening quotes at the start of the line without any additional indentation. And because closing quotes should be aligned with opening quotes, they are also allowed to appear at the 0th indentation level.

The last two violations are expected because if the indentation level is not zero, then it has to follow the indentation rules like other blocks.


Google-Formatter output:
```java
/** somejavadoc. */
public class InputTextBlocksIndentation {

  public void textFunc() {

    String zeroIndentation =
"""
content of the block
""";

    getData(
        """
            Indentation of Text-block
        """,
        5);
  }

  public static void getData(String data, int length) {}
}
```

Difference between Original and Formatted code:

```java
$ diff -Naru InputTextBlocksIndentation.java FormattedInputTextBlocksIndentation.java
--- InputTextBlocksIndentation.java	2025-12-03 08:25:55.734581300 +0530
+++ FormattedInputTextBlocksIndentation.java	2025-12-03 08:26:53.807180600 +0530
@@ -6,14 +6,13 @@

     getData(
-    """
-        Indentation of Text-block
-    """,
-        5
-    );
+        """
+            Indentation of Text-block
+        """,
+        5);
   }

   public static void getData(String data, int length) {}
```

---

## #18227: Extend TextBlockGoogleStyleFormatting to check indentation of each line in the blocks

**Labels:** approved, google style, false negative

Follow-up of #17329

From docs:
https://google.github.io/styleguide/javaguide.html#s4.8.9-text-blocks

> Each line of text in the text block is indented at least as much as the opening and closing """.

Currently, this check covers:
- [x] Both opening and closing quotes are on their own lines. 
- [x] Opening quotes are vertically aligned with closing quotes, i.e, both must have the same indentation value
- [ ]  Quotes can have zero indentation -> #18228 
- [ ] Each String line in the text block is indented at least as much as the opening and closing quotes.

We need to [extend the check](https://github.com/checkstyle/checkstyle/pull/17329#discussion_r2573980631) to add support for checking the indentation of each line between the quotes. 

Invalid cases: 

```java
        final String simpleScript =
            """
     Less Indentation than expected
     Violation is expected here.              
            """; // VIOLATION EXPECTED ABOVE
```

```java
        final String simpleScript =
            """
     Less Indentation than expected
                and each line has a different indentation value
                        Violation is expected here.                  
            """;        // VIOLATION EXPECTED ABOVE
```

Valid cases:

```java
        final String simpleScript =
"""
            More indentation than the quotes, ok
""";
```

```java
        final String simpleScript =simpleScript3.endsWith(                           
                """                                           
                This is a simple sentence                     
                    This is a simple sentence                 
                       This is a simple sentence              
                """);                                         
```

```java
        final String simpleScript =
            """
            indentation is same as the quotes, ok
            """;
```

---
