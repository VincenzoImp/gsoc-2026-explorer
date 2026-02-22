# javadoc issues on github

**Parent:** checkstyle — Project Ideas
**Source:** https://github.com/checkstyle/checkstyle/issues?labels=javadoc&page=1&state=open
**Scraped:** 2026-02-22T23:28:47.591999

---

## #18993: Metadata/Xdoc generators do not handle {@literal} and incorrectly handle {@code} with XML special characters

### Description

Javadoc inline tags {@literal} and {@code} with XML special characters (`<`, `>`) not handled correctly in metadata and xdoc generation .

There are two bugs:

1. `{@literal}` is not handled - `JavadocMetadataScraperUtil.constructSubTreeText()` and `SiteUtil.getDescriptionFromJavadocForXdoc()` have no logic for `LITERAL_INLINE_TAG` nodes. The child nodes (including syntax tokens `{`,`@literal`, `}`) are written to the output as plain text instead of being processed. This becomes a breaking issue when the content contains XML special characters like `<` or `>`, as they are not escaped.

2. **`{@code}` does not escape `<` and `>`**  - `adjustCodeInlineTagChildToHtml()` only escapes `&` -> `&amp;`, but not `<` -> `&lt;` or `>` -> `&gt;`. This means `{@code <p>}` produces `<code><p></code>` (broken XML) instead of the correct `<code>&lt;p&gt;</code>`.

### How to Reproduce

Add `{@literal <}` or `{@code <p>}` to any module's class-level Javadoc and run `mvn clean verify`. The build will fail because the generated meta XML and/or xdoc XML files contain invalid XML.

For example, changing a module's Javadoc from:

` Each paragraph but the first has &lt;p&gt; immediately`

to the preferred inline tag form:

` Each paragraph but the first has {@code <p>} immediately`

causes the meta XML generator to produce `<code><p></code>` instead of `<code>&lt;p&gt;</code>`, resulting in malformed XML because the `<p>` is not escaped and gets interpreted as an actual HTML tag.

### Actual Behavior

Currently, the generators produce broken output:

- `{@literal <}` -> `{@literal <}` (raw structural tokens leak into the output as plain text)
- `{@literal >}` -> `{@literal >}` (same issue)
- `{@code <p>}` -> `<code><p></code>` (the `<p>` is not escaped, producing invalid XML)
- `{@code &}` -> `<code>&amp;</code>` (only `&` escaping works correctly)

### Expected Behavior

After the fix, the generators should produce correct XML output:

- `{@literal <}` -> `&lt;` in both meta XML and xdoc output
- `{@literal >}` -> `&gt;` in both meta XML and xdoc output
- `{@code <p>}` -> `<code>&lt;p&gt;</code>` in both meta XML and xdoc output

---

## #18971: NoGetMessageInThrow: New check to not put caught exception message to exception that we are going to throw.

Describe the problem in detail:

Exception messages should not include ex.getMessage() when the exception is
already passed as a cause, as this leads to duplicate information in stack
traces and logs.

/var/tmp $ cat config.xml
<module name="Checker">
  <module name="TreeWalker">
    <module name="NoGetMessageInThrow"/>
  </module>
</module>

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

/var/tmp $ java -jar checkstyle-X.XX-all.jar -c config.xml Test.java
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

## #18926: Re-enable inspections that were temporarily suppressed for Qodana

**Labels:** approved

We recently migrated to Qodana for code inspections. During the migration, some inspections were temporarily suppressed to allow the transition to complete without blocking development.

These suppressions are still in place, and the underlying code violations need to be resolved and suppressions should be removed.

Inspections to Re-enable
  - [ ] ClassCanBeRecord
  - [ ] ClassEscapesItsScope
  - [ ] EmptyClass
  - [ ] EqualsWithItself
  - [ ] ExtractMethodRecommender
  -  [ ] FieldMayBeStatic
  - [ ] Java9ReflectionClassVisibility
  - [ ] MappingBeforeCount
  - [ ] RedundantSuppression
  - [ ]  SystemGetProperty
  - [ ]  UnnecessarilyQualifiedStaticUsage
  - [ ]  PropertiesAsHashtable
  - [ ] WhileCanBeDoWhile

Target 1 inspection per pr.

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

## #18494: New Check: GoogleNonConstantFieldNameCheck to enforce Google Java Style Guide member naming

**Labels:** approved

split from https://github.com/checkstyle/checkstyle/issues/17842 , we split creation of module and activation of it in google style config to separate issues, to simplify integration.


Create a new check GoogleNonConstantFieldNameCheck to enforce non-constant field naming conventions per the [Google Java Style Guide §5.2.5](https://google.github.io/styleguide/javaguide.html#s5.2.5-non-constant-field-names).

## Background (Reason for new check)

The current MemberName check with regex configuration cannot fully enforce Google Style non-constant field naming rules because it cannot:

1. Correctly enforce Google-specific underscore placement rules
2. Support multipart numeric version suffixes (for example guava33_4_5)
3. Reject special-prefix (Hungarian-style) names such as mValue

## Proposed Rules (Non-constant fields only)

- Field names must follow lowerCamelCase
- Single-character field names are not allowed
- Special prefix names (for example mValue, sCount, kSize) are not allowed, per [Google Java Style Guide §5.1](https://google.github.io/styleguide/javaguide.html#s5-naming)
- Underscores are allowed only between adjacent digits (multipart version or numbering suffix)
- Leading, trailing or double underscores are not allowed

## Scope

This check applies only to non-constant fields:

- Instance fields

## Explicitly out of scope

- Constant fields (static final)
- Local variables
- static fields that are not static final

## Examples

### Valid:

```
userName
timeoutMs
foo123
guava33_4_5
kotlinVersion1_9_24
```
### Invalid:

```
f                                    // violation, single character
mValue                         // violation,special prefix not allowed
sCount                         // violation, special prefix not allowed 
foo_bar                        // violation, underscore between letters
gradle_9_5_1               // violation, underscore between letter-digit
kotlin_version1_9_24  // violation, underscore between letters
guava_33_4_5             // violation, underscore between letter-digit
guava33__4_5             // violation, consecutive underscores
guava33_4_5_             // violation, trailing underscore
_foo                               // violation, leading underscore
```

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

## #18200: Maven try to download artifact that supposed to be taken from local m2 local repostory

**Labels:** approved, CI

example https://dev.azure.com/romanivanovjr/romanivanovjr/_build/results?buildId=33925&view=logs&jobId=c902ebb4-c9f8-5f09-4e17-ff78fbbc842e&j=c902ebb4-c9f8-5f09-4e17-ff78fbbc842e&t=9ca98c81-ff64-58f0-9d03-a23ac1c4a111

but this becomes annoying problems across multiple CIs.
For some reason maven cache is not working or does not have some artifacts and maven tries to download them and fails on network operation.

Expected: maven should not download anything and use local cache. Only in PRs where we add new dependency, we expect download from web by maven.  

```
cmd: ./.ci/validation.sh test
openjdk 21.0.9 2025-10-21 LTS
OpenJDK Runtime Environment Temurin-21.0.9+10 (build 21.0.9+10-LTS)
OpenJDK 64-Bit Server VM Temurin-21.0.9+10 (build 21.0.9+10-LTS, mixed mode, sharing)
    at org.eclipse.aether.internal.impl.DefaultArtifactResolver.resolveArtifacts (DefaultArtifactResolver.java:261)
    at org.eclipse.aether.internal.impl.DefaultRepositorySystem.resolveDependencies (DefaultRepositorySystem.java:353)
    at org.apache.maven.project.DefaultProjectDependenciesResolver.resolve (DefaultProjectDependenciesResolver.java:182)
    at org.apache.maven.lifecycle.internal.LifecycleDependencyResolver.getDependencies (LifecycleDependencyResolver.java:224)
    at org.apache.maven.lifecycle.internal.LifecycleDependencyResolver.resolveProjectDependencies (LifecycleDependencyResolver.java:136)
    at org.apache.maven.lifecycle.internal.MojoExecutor.ensureDependenciesAreResolved (MojoExecutor.java:355)
    at org.apache.maven.lifecycle.internal.MojoExecutor.doExecute (MojoExecutor.java:313)
    at org.apache.maven.lifecycle.internal.MojoExecutor.execute (MojoExecutor.java:212)
    at org.apache.maven.lifecycle.internal.MojoExecutor.execute (MojoExecutor.java:174)
    at org.apache.maven.lifecycle.internal.MojoExecutor.access$000 (MojoExecutor.java:75)
    at org.apache.maven.lifecycle.internal.MojoExecutor$1.run (MojoExecutor.java:162)
    at org.apache.maven.plugin.DefaultMojosExecutionStrategy.execute (DefaultMojosExecutionStrategy.java:39)
    at org.apache.maven.lifecycle.internal.MojoExecutor.execute (MojoExecutor.java:159)
    at org.apache.maven.lifecycle.internal.LifecycleModuleBuilder.buildProject (LifecycleModuleBuilder.java:105)
    at org.apache.maven.lifecycle.internal.LifecycleModuleBuilder.buildProject (LifecycleModuleBuilder.java:73)
    at org.apache.maven.lifecycle.internal.builder.singlethreaded.SingleThreadedBuilder.build (SingleThreadedBuilder.java:53)
    at org.apache.maven.lifecycle.internal.LifecycleStarter.execute (LifecycleStarter.java:118)
    at org.apache.maven.DefaultMaven.doExecute (DefaultMaven.java:261)
    at org.apache.maven.DefaultMaven.doExecute (DefaultMaven.java:173)
    at org.apache.maven.DefaultMaven.execute (DefaultMaven.java:101)
    at org.apache.maven.cli.MavenCli.execute (MavenCli.java:906)
    at org.apache.maven.cli.MavenCli.doMain (MavenCli.java:283)
    at org.apache.maven.cli.MavenCli.main (MavenCli.java:206)
 

*[truncated]*

---

## #18197: Indentation check fails to check line-wrapped expressions as part of a return statement

**Labels:** approved, indentation

I have read check documentation: https://checkstyle.org/checks/misc/indentation.html
I have downloaded the latest checkstyle from: https://checkstyle.org/cmdline.html#Download_and_Run
I have executed the cli and showed it below, as cli describes the problem better than 1,000 words

```bash
/var/tmp $ javac IndentationIssueDemo.java

/var/tmp $ cat checkstyle.xml
<?xml version="1.0"?>
<!DOCTYPE module PUBLIC
        "-//Checkstyle//DTD Checkstyle Configuration 1.3//EN"
        "https://checkstyle.org/dtds/configuration_1_3.dtd">

<module name="Checker">
    <property name="charset" value="UTF-8"/>
    <property name="severity" value="error"/>
    <property name="fileExtensions" value="java, properties, xml"/>

    <module name="TreeWalker">
        <module name="Indentation">
            <property name="basicOffset" value="4"/>
            <property name="braceAdjustment" value="0"/>
            <property name="caseIndent" value="4"/>
            <property name="throwsIndent" value="8"/>
            <property name="lineWrappingIndentation" value="8"/>
            <property name="arrayInitIndent" value="4"/>
            <property name="forceStrictCondition" value="true"/>
        </module>
    </module>
</module>


/var/tmp $ cat IndentationIssueDemo.java
package com.example;

import java.util.stream.IntStream;

public class IndentationIssueDemo {

    public static int workingIndentationCheck() {
        var intermediate = 1
                + 1
    + 1 // Violation (indent should be 16)
                        + 1 // Violation (indent should be 16)
                    + 1; // Violation (indent should be 16)
        return intermediate;
    }

    public static int failingIndentationCheck() {
        return 1
                + 1
    + 1 // incorrect violation ("'method def' child has incorrect indentation level 4, expected level should be 16")
                        + 1 // missing violation (indent should be 16)
                    + 1; // missing violation (indent should be 16)
    }

    public static int workingIndentationCheckWithMethodChain() {
        var intermediate = IntStream.range(0, 10)
                        .filter(i -> i % 2 == 0) // Violation (indent should be 16)
            .map(i -> i * 2) // Violation (indent should be 16)
                .sum();
        return intermediate;
    }

    public static int failingIndentationCheckWithMethodChain() {
        return IntStream.range(0, 10)
                        .filter(i -> i % 2 == 0) // missing violation (indent should be 16)
            .map(i -> i * 2) // missing violation (indent should be 16)
                .sum();
    }
}

/var/tmp $ RUN_LOCALE="-Duser.language=en -Duser.country=US"
/var/tmp $ java $RUN_LOCALE -jar checkstyle-12.1.2-all.jar -c checkstyle.xml IndentationIssueDemo.java
Starting audit...
[ERROR] /var/tmp/IndentationIssueDemo.java:10:5: '+' has incorrect indentation level 4, expected level should be 16. [Indentation]
[ERROR] /var/tmp/IndentationIssueDemo.java:1

*[truncated]*

---

## #18146: Clean up grammar for discontinued preview feature (pattern matching for switch)

**Labels:** approved, antlr, breaking compatibility

Follow-up from issue
- https://github.com/checkstyle/checkstyle/issues/18104

---

[JEP 406](https://openjdk.org/jeps/406) introduced a new preview feature in Java 17 called `Pattern Matching for switch`. Checkstyle added support for this in Issue #10848 and PR #11100. Since then, however, the feature got refined multiple times in:

- [JEP 420: Pattern Matching for switch (Second Preview)](https://openjdk.org/jeps/420)
- [JEP 427: Pattern Matching for switch (Third Preview)](https://openjdk.org/jeps/427)
- [JEP 433: Pattern Matching for switch (Fourth Preview)](https://openjdk.org/jeps/427)

In those refinements, some syntax was dropped and it is no longer compilable with Java 21. Checkstyle still supports this outdated grammar.

The goal of this issue is to remove ANTLR grammar for `Pattern Matching for switch`. The grammar was added in PR
- #11100

---

## #18127: Update imports checks to support module imports

**Labels:** approved

In

- Issue #17919 
- and PR #18079

we added support for Java 25's `import module` syntax. What is next is to follow the [New Language Feature Check Integration Process](https://github.com/checkstyle/checkstyle/blob/master/docs/NEW_LANGUAGE_FEATURE_INTEGRATION_PROCESS.md) and update [imports checks](https://checkstyle.org/checks/imports/index.html).

Checks that need an update are:
- [ ] [`CustomImportOrder`](https://checkstyle.org/checks/imports/customimportorder.html#CustomImportOrder)
    - The check currently supports 5 groups of imports (`STATIC`, `SAME_PACKAGE`...). We could add a 6th group called `MODULE`.
- [x] [`UnusedImports`](https://checkstyle.org/checks/imports/unusedimports.html#UnusedImports)
    - We could update the documentation and mention that we cannot check module imports and that it's a limitation. Checkstyle is not a compiler, so there is no way for us to know which classes/packages are imported from that module. 
    - Resolved in
        - PR https://github.com/checkstyle/checkstyle/pull/18216
- [x] [`IllegalImport`](https://checkstyle.org/checks/imports/illegalimport.html#IllegalImport)
    - The check has 2 properties called `illegalClasses` and `illegalPkgs`. We could add an additional property called `illegalModules`.
    - Resolved in
        - Issue https://github.com/checkstyle/checkstyle/issues/18207
        - PR https://github.com/checkstyle/checkstyle/pull/18220
- [ ] [`ImportControl`](https://checkstyle.org/checks/imports/importcontrol.html#ImportControl)
    - Similar to `IllegalImport`, this check could allow & disallow modules. It currently only does that for classes and packages.
- [ ] [`ImportOrder`](https://checkstyle.org/checks/imports/importorder.html#ImportOrder)
    - The check currently deals (sorting, grouping, separating, etc..) with type and static imports. We could enhance it to also deal with module imports.
- [x] [`RedundantImport`](https://checkstyle.org/checks/imports/redundantimport.html#RedundantImport)
    - The check is only aware of normal imports (`IMPORT`) and static imports (`STATIC_IMPORT`). We could add the new `MODULE_IMPORT` token to be recognized too.
    - Resolved in
        - Issue https://github.com/checkstyle/checkstyle/issues/18171
        - PR https://github.com/checkstyle/checkstyle/pull/18195

> [!IMPORTANT]  
> Each check should be updated in separate PR, and separate issue that clearly claims malfunction by CLI.

Checks that _do not need_ an update are:
- [`AvoidStarImport`](https://checkstyle.org/checks/imports/avoidstarimport.html#AvoidStarImport)
    - Reason is that `import module` does not support star import `.*`
- [`AvoidStaticImport`](https://checkstyle.org/checks/imports/avoidstaticimport.html#AvoidStaticImport)
    - Reason is that `import module` has nothing to do with `import static`

---

## #18065: Forbit Emoj in code

**Labels:** approved, new module

AI generates unicode emoj in code comments
[example](https://github.com/checkstyle/checkstyle/pull/18008/files#diff-e8685d13c843aea432b0c89f0ef7f09fddfd9f00bf2c332e7e7d1a47e776354dR60): 

> // ✅ Enhancement 1: Basic validation

this also raised by other users to address this at https://github.com/checkstyle/checkstyle/discussions/17983#discussioncomment-14888080

Potential soluton: 
```
    <module name="RegexpSingleline">
        <property name="format" value="\u2705" />
        <property name="message" value="Unicode emoj symbols should not be used." />
    </module>
```

use https://www.mauvecloud.net/charsets/CharCodeFinder.html in mode "Hexadecimal Character Codes" to get code.

To make it easier to search and collaborate to extend to all other Unicode pictures, we can put this as example https://checkstyle.org/checks/regexp/regexpsingleline.html#Examples so it will part of git files and user can contribute to make list to cover most

Website sources are part of main repository https://github.com/checkstyle/checkstyle/blob/master/src/site/xdoc/checks/regexp/regexpsingleline.xml.template

We need to put in https://github.com/checkstyle/checkstyle/blob/master/config/checkstyle-checks.xml config  that violates majority of unicode emoj symbols, try to find in web or AI list of them.

---

## #18064: New check: ArrayBracketWhitespace

**Labels:** approved, new module

**Related**:
- https://github.com/checkstyle/checkstyle/issues/17728
- https://github.com/checkstyle/checkstyle/pull/18048

---

**Proposal:**
  New whitespace check `ArrayBracketWhitespace`, _inspired by [GenericWhitespace](https://checkstyle.org/checks/whitespace/genericwhitespace.html#GenericWhitespace)_

**Rationale:**  
The idea started from  
- #17728 

where the user wants to be able to enforce whitespace between type and variable:  
```java
int[]numbers;    // violation, no whitespace after ]
```

We tried adding [`RBRACK`](https://github.com/checkstyle/checkstyle/issues/17728#issuecomment-3476328399) and [`TYPE`](https://github.com/checkstyle/checkstyle/pull/18048) to WhitespaceAfter's tokens, but there are many cases to cover. Therefore, it's better to create a new check.  
  
**Description**  
Checks that the whitespace around square-bracket tokens `[` and `]` follows the typical Java convention for array declarations, array creation, and array indexing.   
  
Left square bracket `[`:  
- must not be preceded by whitespace when preceded by a `TYPE` or `IDENT` in array declarations or array access
  ```java
  int[] arr         // ok
  int []arr         // violation
  arr[i]            // ok
  arr [i]           // violation
  new int[10]       // ok
  char letters[]    // ok
  ```
- must not be followed by whitespace
  ```java
  arr[i]      // ok
  arr[ i]     //violation
  ```
  
Right square bracket `]`:  
- must not be preceded by whitespace
  ```java
  arr[i]     // ok
  arr[i ]    // violation
  ```
- must be followed by whitespaces in all cases, except when followed by:
	- another bracket:
        ```java
        int[][] matrix     // ok
        int[] [] matrix    // violation
        ```
	- a dot for member access:
        ```java
        arr[i].length     // ok
        arr[i] .length    // violation
        ```
	- a comma or semicolon `arr[i],` | `arr[i];`:
        ```java
        arr[i],     // ok
        arr[i] ,    // violation
        arr[i];     // ok
        arr[i] ;    // violation
        ```
	- postfix operators `arr[i]++` | `arr[i]--`
        ```java
        arr[i]++     // ok
        arr[i] ++    // violation
        arr[i] += 1 // ok
        arr[i]+= 1  // violation
        ```
	- a right parenthesis or another closing construct `(arr[i])` | `[arr[i]]`
        ```java
        method(arr[i])     // ok
        method(arr[i] )    // violation
        x[arr[i]]          // ok
        x[arr[i] ]         // violation
        ```

**Parameters:**
None

---

## #18031: Resolve Pitest Suppressions - java-ast-visitor

**Labels:** approved, miscellaneous, good fifth issue

As a part of this issue, we have to kill the mutation listed below and remove the suppression from [pitest xxxx suppression.xml](https://github.com/checkstyle/checkstyle/blob/master/config/pitest-suppressions/)

To understanding how to kill the mutation 
Visit [Wiki page](https://github.com/checkstyle/checkstyle/wiki/How-to-Generate-and-Analyze-Pitest-Reports), [Pitest-docs](https://pitest.org/) and expected actions and workflow at https://github.com/checkstyle/checkstyle/issues/12341.

Target is to remove all `<mutation` from [Pitest-java-ast-visitor](https://github.com/checkstyle/checkstyle/blob/master/config/pitest-suppressions/pitest-java-ast-visitor-suppressions.xml)

Attention!!!!
No pure unit testing, all should be covered by execution of whole Check or Filter. In other words xxxxCheckTest should be extended with usage of verifyxxxx methods. If that is not possible, please share reasoning and we can allow pure unit test with bit comment above method to cover mutation.

---

## #17933: Resolving spotbugs violations

**Labels:** approved, miscellaneous, blocked

Blocked by https://github.com/spotbugs/spotbugs/issues/1338

As [#1338](https://github.com/spotbugs/spotbugs/issues/1338) was closed expected spotbugs violations where none.
But found:
```
[ERROR] Medium: Redundant nullcheck of stream, which is known to be non-null in
 com.puppycrawl.tools.checkstyle.Main.loadProperties(File) [com.puppycrawl.tools.checkstyle.Main,
 com.puppycrawl.tools.checkstyle.Main] Redundant null check at Main.java:[line 451]
Another occurrence at Main.java:[line 453] RCN_REDUNDANT_NULLCHECK_OF_NONNULL_VALUE

[ERROR] Medium: Redundant nullcheck of inStream, which is known to be non-null in com.puppycrawl.tools.checkstyle.PropertyCacheFile.load() [com.puppycrawl.tools.checkstyle.PropertyCacheFile, com.puppycrawl.tools.checkstyle.PropertyCacheFile] Redundant null check at PropertyCacheFile.java:[line 124]Another occurrence at PropertyCacheFile.java:[line 131] RCN_REDUNDANT_NULLCHECK_OF_NONNULL_VALUE
[ERROR] Medium: Redundant nullcheck of out, which is known to be non-null in com.puppycrawl.tools.checkstyle.PropertyCacheFile.persist() [com.puppycrawl.tools.checkstyle.PropertyCacheFile, com.puppycrawl.tools.checkstyle.PropertyCacheFile] Redundant null check at PropertyCacheFile.java:[line 151]Another occurrence at PropertyCacheFile.java:[line 153] RCN_REDUNDANT_NULLCHECK_OF_NONNULL_VALUE
[ERROR] Medium: Redundant nullcheck of inStream, which is known to be non-null in com.puppycrawl.tools.checkstyle.ant.CheckstyleAntTask.createOverridingProperties() [com.puppycrawl.tools.checkstyle.ant.CheckstyleAntTask, com.puppycrawl.tools.checkstyle.ant.CheckstyleAntTask] Redundant null check at CheckstyleAntTask.java:[line 425]Another occurrence at CheckstyleAntTask.java:[line 427] RCN_REDUNDANT_NULLCHECK_OF_NONNULL_VALUE
[ERROR] Medium: Redundant nullcheck of inputStream, which is known to be non-null in com.puppycrawl.tools.checkstyle.checks.OrderedPropertiesCheck.processFiltered(File, FileText) [com.puppycrawl.tools.checkstyle.checks.OrderedPropertiesCheck, com.puppycrawl.tools.checkstyle.checks.OrderedPropertiesCheck] Redundant null check at OrderedPropertiesCheck.java:[line 108]Another occurrence at OrderedPropertiesCheck.java:[line 110] RCN_REDUNDANT_NULLCHECK_OF_NONNULL_VALUE
[ERROR] Medium: Redundant nullcheck of inStream, which is known to be non-null in com.puppycrawl.tools.checkstyle.checks.TranslationCheck.getTranslationKeys(File) [com.puppycrawl.tools.checkstyle.checks.TranslationCheck, com.puppycrawl.tools.checkstyle.checks.TranslationCheck] Redundant null check at TranslationCheck.java:[line 507]Another occurrence at TranslationCheck.java:[line 511] RCN_REDUNDANT_NULLCHECK_OF_NONNULL_VALUE
[ERROR] Medium: Redundant nullcheck of inputStream, which is known to be non-null in com.puppycrawl.tools.checkstyle.checks.UniquePropertiesCheck.processFiltered(File, FileText) [com.puppycrawl.tools.checkstyle.checks.UniquePropertiesCheck, com.puppycrawl.tools.checkstyle.checks.UniquePropertiesCheck] Redundant null check at UniquePropertiesC

*[truncated]*

---

## #17882: Update `JavadocCommentsTokenTypes.java` to new format of AST print

**Labels:** approved, miscellaneous, good first issue

Continuation of https://github.com/checkstyle/checkstyle/issues/14631

We need to update the Javadoc of each token in [`JavadocCommentsTokenTypes.java`](https://github.com/checkstyle/checkstyle/blob/master/src/main/java/com/puppycrawl/tools/checkstyle/api/JavadocCommentsTokenTypes.java) to include an example of the **new AST print format** generated by the latest Checkstyle snapshot.

Each update should document how the token appears in the Javadoc AST, providing both an example input and its corresponding tree structure.

---

### **Example Task: `PARAM_BLOCK_TAG`**

#### **Steps to fix**

1. **Build the snapshot version of Checkstyle**

   Generate the latest snapshot JAR by following the steps in
   [How to generate all binaries and `-all.jar` too](https://github.com/checkstyle/checkstyle/wiki/How-to-run-certain-phases-and-validations#how-to-generate-all-binaries-and--alljar--too).

2. **Generate the AST for the example**

   Example input (`src/Test.java`):

   ```java
   * @param value The parameter of method.
   ```

   Command to generate the Javadoc AST:

   **Windows (PowerShell):**

   ```powershell
   java -jar checkstyle-12.0.0-SNAPSHOT-all.jar -j src/Test.java | ForEach-Object { $_ -replace '\[[0-9]+:[0-9]+\]', '' }
   ```

   **Linux/macOS:**

   ```bash
   java -jar checkstyle-12.0.0-SNAPSHOT-all.jar -j src/Test.java | sed "s/\[[0-9]\+:[0-9]\+\]//g"
   ```

   **Output:**

   ```
   JAVADOC_CONTENT -> JAVADOC_CONTENT 
   |--LEADING_ASTERISK -> * 
   |--TEXT ->   
   `--JAVADOC_BLOCK_TAG -> JAVADOC_BLOCK_TAG 
       `--PARAM_BLOCK_TAG -> PARAM_BLOCK_TAG 
           |--AT_SIGN -> @ 
           |--TAG_NAME -> param 
           |--TEXT ->   
           |--PARAMETER_NAME -> value 
           `--DESCRIPTION -> DESCRIPTION 
               `--TEXT ->  The parameter of method
   ```

3. **Update Javadoc for `PARAM_BLOCK_TAG`**

   Example update:

   ```java
   /**
    * {@code @param} Javadoc block tag.
    *
    * <p>Such Javadoc tag can have two children:</p>
    * <ol>
    *   <li>{@link #PARAMETER_NAME}</li>
    *   <li>{@link #DESCRIPTION}</li>
    * </ol>
    *
    * <p><b>Example:</b></p>
    * <pre>{@code * @param value The parameter of method.}</pre>
    *
    * <b>Tree:</b>
    * <pre>{@code
    * JAVADOC_CONTENT -> JAVADOC_CONTENT 
    * |--LEADING_ASTERISK -> * 
    * |--TEXT ->   
    * `--JAVADOC_BLOCK_TAG -> JAVADOC_BLOCK_TAG 
    *     `--PARAM_BLOCK_TAG -> PARAM_BLOCK_TAG 
    *         |--AT_SIGN -> @ 
    *         |--TAG_NAME -> param 
    *         |--TEXT ->   
    *         |--PARAMETER_NAME -> value 
    *         `--DESCRIPTION -> DESCRIPTION 
    *             `--TEXT ->  The parameter of method
    * }</pre>
    *
    * @see #JAVADOC_BLOCK_TAG
    */
   public static final int PARAM_BLOCK_TAG = JavadocCommentsLexer.PARAM_BLOCK_TAG;
   ```

---

### **Notes**

* Each token’s update should be submitted in **its own pull request**.
* Include the **full CLI output** (AST print) for the example in the **PR description

*[truncated]*

---

## #17878: False-Negative: NoTrailingWhitespace misses spaces after * in multi-line comments (Google Style)

**Labels:** approved, google style, false negative

I have read check documentation: https://checkstyle.org/checks/whitespace/index.html
I have downloaded the latest checkstyle from: https://checkstyle.org/cmdline.html#Download_and_Run
I have executed the cli and showed it below, as cli describes the problem better than 1,000 words

From: https://google.github.io/styleguide/javaguide.html#s2.3.1-whitespace-characters

> Aside from the line terminator sequence, the ASCII horizontal space character (0x20) is the only whitespace character that appears anywhere in a source file.

Code:
```
/*
 * Copyright 2025
 */

/**
 * Test.
 */
public class Test {

  /**
   * Line one.
   *    // <--- This line has a single space or tab after the asterisk (should violate)
   * Line three.
   */
  public void exampleMethod() {
  }
}

```

Cli:
```
$ java -jar checkstyle-11.1.0-all.jar -c google_checks.xml Test.java
Starting audit...
Audit done.
```
Formatter:
```
java -jar google-java-format-1.28.0-all-deps.jar Test.java
/*
 * Copyright 2025
 */

/** Test. */
public class Test {

  /**
   * Line one. // <--- This line has a single space or tab after the asterisk (should violate) Line
   * three.
   */
  public void exampleMethod() {}
}
```
I've found a false negative related to the enforcement of the Google Java Style Guide, Section 2.3.1 (Whitespace), which prohibits trailing whitespace. The current configuration appears to miss trailing spaces on lines that contain only the asterisk (*) within a Javadoc block.

The issue is that the NoTrailingWhitespaceCheck does not report a violation when one or more space characters exist between the final asterisk and the newline character.

I am ready to submit a Pull Request for this if the team agrees it is a valid missed check. Thank you.

---

## #17842: False-negative: Member names with underscores

**Labels:** approved, new module, google style

From: https://google.github.io/styleguide/javaguide.html#s5.3-camel-case
> In very rare circumstances (for example, multipart version numbers), you may need to use underscores to separate adjacent numbers, since numbers do not have upper and lower case variants.

Google style is not exact. On one hand it says `_` can be used in test methods to combine sentences and on another hand in general CamelCase explanation, `_` is allowed for numbering suffix in all names(except package and generic names).

Valid uses of underscore :
```
1. guava33_4_5
2. guavaVersion33_4_5 
3. guavaversion33_4_5 (same as 1.)
```

Invalid uses of underscore:
```
1. guava_33_4_5_ (underscore at the end)
2. guava_33_4_5   (underscore between digit and letter)
3. guava_version33_4_5 (underscore between lowercase character sequences)
```

Some false-negatives in member names left to address from #17708  

```java
$ cat NamesWithUnderscores.java
/** some javadoc. */
public class NamesWithUnderscores {
  int gradle9_5_1 = 0;

  int gradle9_5_1_ = 0; // ok

  int gradle_9_5_1 = 0; // Expected violation, _ between digit and letter

  int jdk_9_0_392 = 0; // Expected violation, _ between digit and letter

  int testing_01231 = 0; // Expected violation, _ between digit and letter
}
```

```
$ java -jar checkstyle-11.1.0-all.jar -c google_checks.xml NamesWithUnderscores.java 
Starting audit...
[WARN] /mnt/5D92528E6B945467/test/testing/NamesWithUnderscores.java:5:7: Member name 'gradle9_5_1_' must match pattern '^(?![a-z]$)(?![a-z][A-Z])[a-z][a-zA-Z0-9]*(?:_[0-9]+)*$'. [MemberName]
Audit done.
```

we probably need a better approach than Regex as current regex has already grown very complex.

https://github.com/checkstyle/checkstyle/blob/5d52248c85b0fc37ddd786ddb5354e332f8a54b8/src/main/resources/google_checks.xml#L254-L256

if special check is needed, it should first determine the type of name - regular or name with numbering and then it should validate the name against the appropriate regex format, which will differ for each type of naming

---

## #17841: False-negative: Method names with underscores

**Labels:** approved, new module, google style

From: https://google.github.io/styleguide/javaguide.html#s5.3-camel-case
> In very rare circumstances (for example, multipart version numbers), you may need to use underscores to separate adjacent numbers, since numbers do not have upper and lower case variants.

Google style is not exact. On one hand it says `_` can be used in test methods to combine sentences and on another hand in general CamelCase explanation, `_` is allowed for numbering suffix in all names(except package and generic names).

Valid uses of underscore :
```
1. guava33_4_5
2. guavaVersion33_4_5 
3. guavaversion33_4_5 (same as 1.)
```

Invalid uses of underscore:
```
1. guava_33_4_5_ (underscore at the end)
2. guava_33_4_5   (underscore between digit and letter)
3. guava_version33_4_5 (underscore between lowercase character sequences)
```

**Note**: Underscores are not allowed in normal method names. Name has to have the numbering format part at the end. Following are all invalid

```
guava_version
guava_Version
Set_guavaVersion3345
```

Some false-negatives left to address from #17708  

```java
$ cat NamesWithUnderscores.java
/** some javadoc. */
public class NamesWithUnderscores {
  void gradle9_5_1_() {} // Expected violation, _ at the end

  void gradle_9_5_1() {} // Expected violation, _ between digit and letter

  void jdk_9_0_392() {} // Expected violation, _ between digit and letter

  void testing_01231(String str) {} // Expected violation, _ between digit and letter
}
```

```
$ java -jar checkstyle-11.1.0-all.jar -c google_checks.xml NamesWithUnderscores.java 
Starting audit...
[WARN] /mnt/5D92528E6B945467/test/testing/NamesWithUnderscores.java:4:8: Method name 'gradle9_5_1_' must match pattern '^(?![a-z]$)(?![a-z][A-Z])[a-z][a-z0-9]*(?:[A-Z][a-z0-9]*)*(?:_[0-9]+)*$'. [MethodName]
Audit done.
```

We probably need a better approach than Regex. Current regex has already grown very complex.
 
https://github.com/checkstyle/checkstyle/blob/5d52248c85b0fc37ddd786ddb5354e332f8a54b8/src/main/resources/google_checks.xml#L436-L438

if special check is needed, it should first determine the type of name - regular or name with numbering and then it should validate the name against the appropriate regex format, which will differ for each type of naming

Keep in mind: unless it's a non-regular name i.e name that has number formating suffix at the end or method with `@Test` annotation,  underscores are not allowed.

---

## #17839: False-negative: Method and Member names with underscores

**Labels:** new module, google style, false negative

From: https://google.github.io/styleguide/javaguide.html#s5.3-camel-case
> In very rare circumstances (for example, multipart version numbers), you may need to use underscores to separate adjacent numbers, since numbers do not have upper and lower case variants.

Google style is not exact. On one hand it says `_` can be used in test methods to combine sentences and on another hand in general CamelCase explanation, `_` is allowed for numbering suffix in all names(except package and generic names).

Valid uses of underscore :
```
1. guava33_4_5
2. guavaVersion33_4_5 
3. guavaversion33_4_5 (same as 1.)
```

Invalid uses of underscore:
```
1. guava_33_4_5_ (underscore at the end)
2. guava_33_4_5   (underscore between digit and letter)
3. guava_version33_4_5 (underscore between lowercase character sequences)
```

**Note**: Underscores are not allowed in normal method names. Name has to have the numbering format part at the end. Following are all invalid

```
guava_version
guava_Version
Set_guavaVersion3345
```

Some false-negatives left to address from #17708  

```java
/** some javadoc. */
public class NamesWithUnderscores {
 
  void gradle_9_5_1() {} // Expected violation, _ between digit and letter

  void jdk_9_0_392() {} // Expected violation, _ between digit and letter

  void testing_01231(String str) {} // Expected violation, _ between digit and letter

  int jdk_8_90; // Expected violation, _ between digit and letter

  int guava_33_4_7; // Expected violation, _ between digit and letter
}
```

```
$ java -jar checkstyle-11.0.0-all.jar -c google_checks.xml NamesWithUnderscores.java 
Starting audit...
Audit done.
```

we probably need a better approach than Regex. Regex has already grown very complex.
 
https://github.com/checkstyle/checkstyle/blob/5d52248c85b0fc37ddd786ddb5354e332f8a54b8/src/main/resources/google_checks.xml#L436-L438

https://github.com/checkstyle/checkstyle/blob/5d52248c85b0fc37ddd786ddb5354e332f8a54b8/src/main/resources/google_checks.xml#L254-L256

if special check is needed, it should first determine the type of name - regular or name with numbering and then it should validate the name against the appropriate regex format, which will differ for each type of naming

Keep in mind: unless it's a non-regular name i.e name that has number formating suffix at the end or method with `@Test` annotation,  underscores are not allowed.

---

## #17832: New check: JavadocBlockStyle

**Labels:** google style

From:  [7.1.1 General Form](https://google.github.io/styleguide/javaguide.html#s7.1.1-javadoc-multi-line) and https://github.com/google/google-java-format/issues/1279#issuecomment-3320778635


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
The basic form is always acceptable. The single-line form may be substituted when the entirety of the Javadoc block (including comment markers) can fit on a single line




<hr>
JavadocBlockStyleCheck ensures: 

1. Leading asterisk is always present.
2. Preferred style is to put /** and */ on their own lines (unless the entire javadoc comment fits on a single line)

Expected config:
```xml
<?xml version="1.0"?>
<!DOCTYPE module PUBLIC
        "-//Checkstyle//DTD Checkstyle Configuration 1.3//EN"
        "https://checkstyle.org/dtds/configuration_1_3.dtd">

<module name="Checker">
    <module name="TreeWalker">
        <module name="JavadocBlockStyle"/>
    </module>
</module>
```

Some other examples showing how the `JavadocBlockStyle` should work:

1. Missing leading asterisk

```java
public class JavadocAsteriskFormat {

    /**
     * Leading Asterisk is missing in next line.
        it should not be allowed   // violation
     */
    void testMethod() {}

    /*
     * Some Method.
     * 
       @param num some-number.
       @param path some-path.   // violation
     */
    void testMethod2(int num, String path) {}

    /**
     * Some method.
     *
      @return randomString.   // violation
     */
    String testMethod3() {
        return "method";
    }
}
```

Expected Output:
```
$ java -jar checkstyle-11.0.0-all.jar -c config.xml JavadocAsteriskFormat.java 
Starting audit...
[WARN] /mnt/5D92528E6B945467/test/testing/JavadocAsteriskFormat.java:5: Leading asterisk is missing. [JavadocBlockStyle]
[WARN] /mnt/5D92528E6B945467/test/testing/JavadocAsteriskFormat.java:12: Leading asterisk is missing. [JavadocBlockStyle]
[WARN] /mnt/5D92528E6B945467/test/testing/JavadocAsteriskFormat.java:13: Leading asterisk is missing. [JavadocBlockStyle]
[WARN] /mnt/5D92528E6B945467/test/testing/JavadocAsteriskFormat.java:20: Leading asterisk is missing. [JavadocBlockStyle]
Audit done.
```

2. `/**` and `*/` not on their own lines

```java
public class JavadocAsteriskFormat {

    /**
     * Javadoc closing asterisk not on it's own line. */  // violation
    private void testMethod1() {}

    /** Javadoc opening asterisk not on it's own line. so this    // violation
     * is a invalid code.
     */
    private void testMethod2() {}

    /**
     * Returns a random number.
     * 
     * @return random number */   // violation
    private int testMethod3() {
        return 1;
    }
}
```

Expected output:
```
$ java -jar checkstyle-11.0.0-all.jar -c config.xml JavadocAsteriskFo

*[truncated]*

---

## #17810: JDK 25, JEP 512: Compact Source Files and Instance Main Methods not supported

**Labels:** approved, antlr

I have read check documentation: https://checkstyle.org/checks/xxxxxx/nameofaffectedcheck.html
I have downloaded the latest cli from: https://checkstyle.org/cmdline.html#Download_and_Run
I have executed the cli and showed it below, as cli describes the problem better than 1,000 words

**How it works Now:**

```bash
% java -version
java version "25" 2025-09-16 LTS
Java(TM) SE Runtime Environment (build 25+37-LTS-3491)
Java HotSpot(TM) 64-Bit Server VM (build 25+37-LTS-3491, mixed mode, sharing)
% cat Hello.java
void main() {
    System.out.println("Hello World!");
}
% java Hello.java
Hello World!
% java -jar checkstyle-11.0.1-all.jar -c /google_checks.xml Hello.java
Starting audit...
com.puppycrawl.tools.checkstyle.api.CheckstyleException: Exception was thrown while processing Hello.java
        at com.puppycrawl.tools.checkstyle.Checker.processFiles(Checker.java:313)
        at com.puppycrawl.tools.checkstyle.Checker.process(Checker.java:227)
        at com.puppycrawl.tools.checkstyle.Main.runCheckstyle(Main.java:429)
        at com.puppycrawl.tools.checkstyle.Main.runCli(Main.java:347)
        at com.puppycrawl.tools.checkstyle.Main.execute(Main.java:206)
        at com.puppycrawl.tools.checkstyle.Main.main(Main.java:130)
Caused by: com.puppycrawl.tools.checkstyle.api.CheckstyleException: IllegalStateException occurred while parsing file /home/markus/Dokument/git/lehre/progra-ws25/uebungsblaetter/aufgaben/ballistic/task/Hello.java.
        at com.puppycrawl.tools.checkstyle.JavaParser.parse(JavaParser.java:104)
        at com.puppycrawl.tools.checkstyle.TreeWalker.processFiltered(TreeWalker.java:192)
        at com.puppycrawl.tools.checkstyle.api.AbstractFileSetCheck.process(AbstractFileSetCheck.java:101)
        at com.puppycrawl.tools.checkstyle.Checker.processFile(Checker.java:341)
        at com.puppycrawl.tools.checkstyle.Checker.processFiles(Checker.java:300)
        ... 5 more
Caused by: java.lang.IllegalStateException: 1:0: no viable alternative at input 'void'
        at com.puppycrawl.tools.checkstyle.JavaParser$CheckstyleErrorListener.syntaxError(JavaParser.java:254)
        at org.antlr.v4.runtime.ProxyErrorListener.syntaxError(ProxyErrorListener.java:41)
        at org.antlr.v4.runtime.Parser.notifyErrorListeners(Parser.java:544)
        at org.antlr.v4.runtime.DefaultErrorStrategy.reportNoViableAlternative(DefaultErrorStrategy.java:310)
        at org.antlr.v4.runtime.DefaultErrorStrategy.reportError(DefaultErrorStrategy.java:136)
        at com.puppycrawl.tools.checkstyle.grammar.java.JavaLanguageParser.compilationUnit(JavaLanguageParser.java:432)
        at com.puppycrawl.tools.checkstyle.JavaParser.parse(JavaParser.java:98)
        ... 9 more
Caused by: org.antlr.v4.runtime.NoViableAltException
        at org.antlr.v4.runtime.atn.ParserATNSimulator.noViableAlt(ParserATNSimulator.java:2014)
        at org.antlr.v4.runtime.atn.ParserATNSimulator.execATN(ParserATNSimulator.java:445)
        at org.antlr.v4.runtime.atn.ParserATNSimu

*[truncated]*

---
