# issues

**Parent:** checkstyle — Project Ideas
**Source:** https://github.com/checkstyle/checkstyle/issues?q=is%3Aissue%20state%3Aopen%20label%3Aantlr
**Scraped:** 2026-02-22T23:28:47.591567

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

## #17052: Add support for flexible constructor bodies (JEP 513) targeted for JDK25

**Labels:** approved, antlr

👍 I have read check documentation: https://checkstyle.org/checks/xxxxxx/nameofaffectedcheck.html
👍 I have downloaded the latest checkstyle from: https://checkstyle.org/cmdline.html#Download_and_Run
👍 I have executed the cli and showed it below, as cli describes the problem better than 1,000 words

[Flexible constructor bodies (JEP 513)](https://openjdk.org/jeps/513) is targeted for JDK 25. That means it is leaving preview and will become standard Java with the release of JDK 25 this fall.

Therefore, checkstyle will need to support the new syntax. It doesn't yet:

```bash
$ javac -version
javac 25-internal
$ javac MyClass.java
# my config is google_checks.xml but it doesn't matter
$ cat MyClass.java
public class MyClass {
    public MyClass() {
        System.out.println("hello");
        super();
    }
}
$ RUN_LOCALE="-Duser.language=en -Duser.country=US"
$ java $RUN_LOCALE -jar checkstyle-10.23.1-all.jar -c google_checks.xml MyClass.java 
Starting audit...
com.puppycrawl.tools.checkstyle.api.CheckstyleException: Exception was thrown while processing MyClass.java
	at com.puppycrawl.tools.checkstyle.Checker.processFiles(Checker.java:312)
	at com.puppycrawl.tools.checkstyle.Checker.process(Checker.java:226)
	at com.puppycrawl.tools.checkstyle.Main.runCheckstyle(Main.java:424)
	at com.puppycrawl.tools.checkstyle.Main.runCli(Main.java:347)
	at com.puppycrawl.tools.checkstyle.Main.execute(Main.java:206)
	at com.puppycrawl.tools.checkstyle.Main.main(Main.java:130)
Caused by: com.puppycrawl.tools.checkstyle.api.CheckstyleException: IllegalStateException occurred while parsing file /Users/archie/Downloads/checkstyle-bug/MyClass.java.
	at com.puppycrawl.tools.checkstyle.JavaParser.parse(JavaParser.java:104)
	at com.puppycrawl.tools.checkstyle.TreeWalker.processFiltered(TreeWalker.java:195)
	at com.puppycrawl.tools.checkstyle.api.AbstractFileSetCheck.process(AbstractFileSetCheck.java:101)
	at com.puppycrawl.tools.checkstyle.Checker.processFile(Checker.java:340)
	at com.puppycrawl.tools.checkstyle.Checker.processFiles(Checker.java:299)
	... 5 more
Caused by: java.lang.IllegalStateException: 3:26: mismatched input '(' expecting ';'
	at com.puppycrawl.tools.checkstyle.JavaParser$CheckstyleErrorListener.syntaxError(JavaParser.java:254)
	at org.antlr.v4.runtime.ProxyErrorListener.syntaxError(ProxyErrorListener.java:41)
	at org.antlr.v4.runtime.Parser.notifyErrorListeners(Parser.java:544)
	at org.antlr.v4.runtime.DefaultErrorStrategy.reportInputMismatch(DefaultErrorStrategy.java:327)
	at org.antlr.v4.runtime.DefaultErrorStrategy.reportError(DefaultErrorStrategy.java:139)
	at com.puppycrawl.tools.checkstyle.CheckstyleParserErrorStrategy.recoverInline(CheckstyleParserErrorStrategy.java:38)
	at org.antlr.v4.runtime.Parser.match(Parser.java:208)
	at com.puppycrawl.tools.checkstyle.grammar.java.JavaLanguageParser.statement(JavaLanguageParser.java:7046)
	at com.puppycrawl.tools.checkstyle.grammar.java.JavaLanguageParser.blockStatement(JavaLanguageParser.java:6207)
	a

*[truncated]*

---

## #10699: COMMENT_CONTENT comes after BLOCK_COMMENT_END

**Labels:** antlr

Identified at https://github.com/rnveach/checkstyle/commits/token_order_check when checking which tokens appear out of order compared to the source,

````
$ cat TestClass.java
package com.puppycrawl.tools.checkstyle.api.abstractcheck;

public class InputAvoidNoArgumentSuperConstructorCall extends java.util.ArrayList {
    public InputAvoidNoArgumentSuperConstructorCall(int a, long b) {
        super(/**/); // violation
    }
}
````

Produces the following piece of Tree that is in question from the command `java -jar checkstyle-8.45.1-all.jar -T TestClass.java`:
````
    |  `--SLIST -> { [4:67]
    |      |--SUPER_CTOR_CALL -> super [5:8]
    |      |  |--LPAREN -> ( [5:13]
    |      |  |--ELIST -> ELIST [5:18]
    |      |  |--BLOCK_COMMENT_BEGIN -> /* [5:14]
    |      |  |  |--COMMENT_CONTENT ->  [5:16]
    |      |  |  `--BLOCK_COMMENT_END -> */ [5:15]
    |      |  |--RPAREN -> ) [5:18]
    |      |  `--SEMI -> ; [5:19]
````

The issue is that `COMMENT_CONTENT` says it comes after `BLOCK_COMMENT_END` which seems unnatural.

I would expect both tokens to have the same line/column since there is no contents, so it should act like a length of 0.

---

## #10626: SEMI Token: Non-standard locations in tree for DetailAST items

**Labels:** antlr

Taken from https://github.com/checkstyle/checkstyle/issues/950 ,

When traversing the DetailAST tree to build a custom checker, I notice some of the same types are found in different areas, either as a child or as a sibling. One example is "return" has ";" as a child while an expression has ";" as a sibling.
It is making traversing the tree and finding items a little bit more tricky than it is needed. It would be much easier if they were to be found in the same location.

````
$ cat TestClass.java
public class TestClass {
    void method() {
        int a = 0, b = 0;

        // line 6 below
        if (a == 1) return;
        // line 9 below
        if (a == 2)
            b = 3;
    }
}
````

Create the following tree:
````
    |      |--LITERAL_IF -> if [6:8]
    |      |  |--LPAREN -> ( [6:11]
    |      |  |--EXPR -> EXPR [6:14]
    |      |  |  `--EQUAL -> == [6:14]
    |      |  |      |--IDENT -> a [6:12]
    |      |  |      `--NUM_INT -> 1 [6:17]
    |      |  |--RPAREN -> ) [6:18]
    |      |  `--LITERAL_RETURN -> return [6:20]
    |      |      `--SEMI -> ; [6:26] // <-- child of "return"

    |      |--LITERAL_IF -> if [8:8]
    |      |  |--LPAREN -> ( [8:11]
    |      |  |--EXPR -> EXPR [8:14]
    |      |  |  `--EQUAL -> == [8:14]
    |      |  |      |--IDENT -> a [8:12]
    |      |  |      `--NUM_INT -> 2 [8:17]
    |      |  |--RPAREN -> ) [8:18]
    |      |  |--EXPR -> EXPR [9:14]
    |      |  |  `--ASSIGN -> = [9:14]
    |      |  |      |--IDENT -> b [9:12]
    |      |  |      `--NUM_INT -> 3 [9:16]
    |      |  `--SEMI -> ; [9:17] // <-- sibling of "EXPR"
````

---

## #8656: Checkstyle fails to parse unicode escapes as comment delimiters

**Labels:** approved, antlr

Identified at https://github.com/checkstyle/checkstyle/pull/8634#discussion_r468594904
Check documentation: https://checkstyle.sourceforge.io/config_naming.html#ClassTypeParameterName

```
➜  IdeaProjects /usr/lib/jvm/java-14-openjdk/bin/javac --enable-preview --source 14 jdk14/test/langtools/tools/javac/unicode/UnicodeCommentDelimiter.java
➜  IdeaProjects cat single-module-config.xml 
<?xml version="1.0"?>
<!DOCTYPE module PUBLIC
        "-//Checkstyle//DTD Checkstyle Configuration 1.3//EN"
        "https://checkstyle.org/dtds/configuration_1_3.dtd">
<module name="Checker">
  <module name="TreeWalker">
    <!-- Here we use simple module to prove that we can parse files -->
    <module name="ClassTypeParameterName"/>
  </module>
</module>
➜  IdeaProjects cat jdk14/test/langtools/tools/javac/unicode/UnicodeCommentDelimiter.java
/*
 * Copyright (c) 2002, Oracle and/or its affiliates. All rights reserved.
 * DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS FILE HEADER.
 *
 * This code is free software; you can redistribute it and/or modify it
 * under the terms of the GNU General Public License version 2 only, as
 * published by the Free Software Foundation.
 *
 * This code is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
 * FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
 * version 2 for more details (a copy is included in the LICENSE file that
 * accompanied this code).
 *
 * You should have received a copy of the GNU General Public License version
 * 2 along with this work; if not, write to the Free Software Foundation,
 * Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA.
 *
 * Please contact Oracle, 500 Oracle Parkway, Redwood Shores, CA 94065 USA
 * or visit www.oracle.com if you need additional information or have any
 * questions.
 */

/*
 * @test
 * @summary unicode escapes delimiting and inside of comments
 *
 * @compile UnicodeCommentDelimiter.java
 */

class UnicodeCommentDelimiter {
    public static void main(String[] args) {
        // no error on the following line because although \u005c
        // represents a backslash, that cannot be considered to begin
        // a unicode escape sequence.
        // \u005c000a xyzzy plugh;

        // no error on the following line because there are an even
        // number of backslashes before the u, meaning it is not a
        // unicode escape sequence.
        // \\u000a xyzzy plugh;

        // However, unicode escaped characters can delimit comments.
        \u002f\u002f xyzzy plugh;

        // \u000a class plugh{}
        plugh xyzzy;
    }
}
➜  IdeaProjects java -jar /home/nick/IdeaProjects/checkstyle/target/checkstyle-8.36-SNAPSHOT-all.jar -c single-module-config.xml jdk14/test/langtools/tools/javac/unicode/UnicodeCommentDelimiter.java
Starting audit...
com.puppycrawl.tools.checkstyle.api.Checkstyl

*[truncated]*

---

## #8655: Checkstyle fails to parse unicode escape line terminators

**Labels:** approved, antlr

Identified at https://github.com/checkstyle/checkstyle/pull/8634#discussion_r468594904
Check documentation: https://checkstyle.sourceforge.io/config_naming.html#ClassTypeParameterName

```
➜  IdeaProjects /usr/lib/jvm/java-14-openjdk/bin/javac --enable-preview --source 14 jdk14/test/langtools/tools/javac/unicode/UnicodeAtEOL.java
➜  IdeaProjects cat single-module-config.xml 
<?xml version="1.0"?>
<!DOCTYPE module PUBLIC
        "-//Checkstyle//DTD Checkstyle Configuration 1.3//EN"
        "https://checkstyle.org/dtds/configuration_1_3.dtd">
<module name="Checker">
  <module name="TreeWalker">
    <!-- Here we use simple module to prove that we can parse files -->
    <module name="ClassTypeParameterName"/>
  </module>
</module>
➜  IdeaProjects cat jdk14/test/langtools/tools/javac/unicode/UnicodeAtEOL.java
/*
 * Copyright (c) 1997, 1998, Oracle and/or its affiliates. All rights reserved.
 * DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS FILE HEADER.
 *
 * This code is free software; you can redistribute it and/or modify it
 * under the terms of the GNU General Public License version 2 only, as
 * published by the Free Software Foundation.
 *
 * This code is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
 * FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
 * version 2 for more details (a copy is included in the LICENSE file that
 * accompanied this code).
 *
 * You should have received a copy of the GNU General Public License version
 * 2 along with this work; if not, write to the Free Software Foundation,
 * Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA.
 *
 * Please contact Oracle, 500 Oracle Parkway, Redwood Shores, CA 94065 USA
 * or visit www.oracle.com if you need additional information or have any
 * questions.
 */

/* @test
   @bug 4086919
   @summary Correct handling of unicode escapes for line termination
   @compile UnicodeAtEOL.java
*/
public class UnicodeAtEOL {
   public static void main(String[] args) {
       // \u000D
       // should end the line; bug doesn't see it as escape
       int a; \u000D

       // \u000A
       // should end the line; bug doesn't see it as escape
       int b; \u000A

   }
}
➜  IdeaProjects java -jar /home/nick/IdeaProjects/checkstyle/target/checkstyle-8.36-SNAPSHOT-all.jar -c single-module-config.xml jdk14/test/langtools/tools/javac/unicode/UnicodeAtEOL.java
Starting audit...
com.puppycrawl.tools.checkstyle.api.CheckstyleException: Exception was thrown while processing jdk14/test/langtools/tools/javac/unicode/UnicodeAtEOL.java
        at com.puppycrawl.tools.checkstyle.Checker.processFiles(Checker.java:311)
        at com.puppycrawl.tools.checkstyle.Checker.process(Checker.java:221)
        at com.puppycrawl.tools.checkstyle.Main.runCheckstyle(Main.java:408)
        at com.puppycrawl.tools.checkstyle.Main.runCli(Main.ja

*[truncated]*

---

## #8654: Checkstyle fails on escapes in identifiers

**Labels:** approved, antlr

Identified at https://github.com/checkstyle/checkstyle/pull/8634#discussion_r468594904
Check documentation: https://checkstyle.sourceforge.io/config_naming.html#ClassTypeParameterName

```
➜  IdeaProjects /usr/lib/jvm/java-14-openjdk/bin/javac --enable-preview --source 14 jdk14/test/langtools/tools/javac/unicode/SupplementaryJavaID1.java
➜  IdeaProjects cat single-module-config.xml 
<?xml version="1.0"?>
<!DOCTYPE module PUBLIC
        "-//Checkstyle//DTD Checkstyle Configuration 1.3//EN"
        "https://checkstyle.org/dtds/configuration_1_3.dtd">
<module name="Checker">
  <module name="TreeWalker">
    <!-- Here we use simple module to prove that we can parse files -->
    <module name="ClassTypeParameterName"/>
  </module>
</module>
➜  IdeaProjects cat jdk14/test/langtools/tools/javac/unicode/SupplementaryJavaID1.java
/*
 * Copyright (c) 2003, Oracle and/or its affiliates. All rights reserved.
 * DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS FILE HEADER.
 *
 * This code is free software; you can redistribute it and/or modify it
 * under the terms of the GNU General Public License version 2 only, as
 * published by the Free Software Foundation.
 *
 * This code is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
 * FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
 * version 2 for more details (a copy is included in the LICENSE file that
 * accompanied this code).
 *
 * You should have received a copy of the GNU General Public License version
 * 2 along with this work; if not, write to the Free Software Foundation,
 * Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA.
 *
 * Please contact Oracle, 500 Oracle Parkway, Redwood Shores, CA 94065 USA
 * or visit www.oracle.com if you need additional information or have any
 * questions.
 */

/*
 * @test
 * @bug 4914724
 * @summary Check that valid supplementary characters can be used as Java identifiers.
 * @author Naoto Sato
 *
 * @compile SupplementaryJavaID1.java
 * @run main SupplementaryJavaID1
 */

public class SupplementaryJavaID1 {
    public static void main(String[] s) {
        // U+10400 (\ud801\udc00): DESERET CAPITAL LETTER LONG I (can be start or part)
        // U+1D17B (\ud834\udd7b): MUSICAL SYMBOL COMBINING ACCENT (can only be part)
        // U+1D100 (\ud834\udd00): MUSICAL SYMBOL SINGLE BARLINE (can be none of start nor part)
        int \ud801\udc00abc = 1;
        int \ud802\udc00abc = 2;
        int \ud801\udc01abc = 3;
        int def\ud801\udc00 = 4;
        int \ud801\udc00\ud834\udd7b = 5;

        if (\ud801\udc00abc != 1 ||
            \ud802\udc00abc != 2 ||
            \ud801\udc01abc != 3 ||
            def\ud801\udc00 != 4 ||
            \ud801\udc00\ud834\udd7b != 5) {
                throw new RuntimeException("test failed");
        }
    }
}
➜  IdeaProjects java -jar /home/nick/I

*[truncated]*

---

## #8650: Checkstyle fails to parse unusual parameter names

**Labels:** approved, antlr

Identified at https://github.com/checkstyle/checkstyle/pull/8634#discussion_r468594904
Check documentation: https://checkstyle.sourceforge.io/config_naming.html#ClassTypeParameterName

```
➜  IdeaProjects /usr/lib/jvm/java-14-openjdk/bin/javac --enable-preview --source 14 jdk14/test/langtools/tools/javac/MethodParameters/UncommonParamNames.java
➜  IdeaProjects cat single-module-config.xml 
<?xml version="1.0"?>
<!DOCTYPE module PUBLIC
        "-//Checkstyle//DTD Checkstyle Configuration 1.3//EN"
        "https://checkstyle.org/dtds/configuration_1_3.dtd">
<module name="Checker">
  <module name="TreeWalker">
    <!-- Here we use simple module to prove that we can parse files -->
    <module name="ClassTypeParameterName"/>
  </module>
</module>
➜  IdeaProjects cat jdk14/test/langtools/tools/javac/MethodParameters/UncommonParamNames.java
/*
 * Copyright (c) 2013, 2016, Oracle and/or its affiliates. All rights reserved.
 * DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS FILE HEADER.
 *
 * This code is free software; you can redistribute it and/or modify it
 * under the terms of the GNU General Public License version 2 only, as
 * published by the Free Software Foundation.
 *
 * This code is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
 * FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
 * version 2 for more details (a copy is included in the LICENSE file that
 * accompanied this code).
 *
 * You should have received a copy of the GNU General Public License version
 * 2 along with this work; if not, write to the Free Software Foundation,
 * Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA.
 *
 * Please contact Oracle, 500 Oracle Parkway, Redwood Shores, CA 94065 USA
 * or visit www.oracle.com if you need additional information or have any
 * questions.
 */

/*
 * @test
 * @bug 8006582
 * @summary javac should generate method parameters correctly.
 * @modules jdk.jdeps/com.sun.tools.classfile
 * @build MethodParametersTester ClassFileVisitor ReflectionVisitor
 * @compile -parameters UncommonParamNames.java
 * @run main MethodParametersTester UncommonParamNames UncommonParamNames.out
 */

/** Test uncommon parameter names */
class UncommonParamNames {
    public UncommonParamNames(int _x) { }
    public UncommonParamNames(short $1) { }
    public UncommonParamNames(long \u0061) { }
    public UncommonParamNames(char zero\^@zero\^@) { }
    public UncommonParamNames(String zero\^@zero\^@seven\^G) { }
    public UncommonParamNames(Object zero\^@zero\^@eight\^H) { }
    public UncommonParamNames(Object aLoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooongName,
                              Object baLoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooongName,
                              Object cbaLoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooon

*[truncated]*

---

## #8240: Java Grammar: module-info.java support

**Labels:** discussion ongoing, antlr

Original issue https://github.com/checkstyle/checkstyle/issues/3059

We should extend our grammar to support module-info.java

- there are may be comments and Javadoc. We should validate them.
- there may be annotations. We have checks for annotations.
- we may add checks specifically for modules. For example, `ModuleName` check.

---

## #6376: Improper TYPE_UPPER_BOUNDS antlr tree

**Labels:** antlr

Taken from https://github.com/checkstyle/checkstyle/pull/6355#discussion_r246981352 ,

https://github.com/checkstyle/checkstyle/blob/4bd317469eb55e6f28449f53ff9ba1fd1def3077/src/test/resources/com/puppycrawl/tools/checkstyle/grammar/InputRegressionJavaClass2Ast.txt#L386-L395

it seems to me `c3` and `<T>` should all be under 1 node and not combined with the `TYPE_EXTENSION_AND`.
I would expect something similar to `TYPECAST`:
````
TYPE_UPPER_BOUNDS -> extends [43:11]
   |-- TYPE
   |   |-- IDENT -> c3
....
   |-- TYPE_EXTENSION_AND
   |-- TYPE
   |   |-- IDENT -> i1
````

---

## #6233: Trailing comments in ast tree

**Labels:** approved, antlr

In AST tree produced by checkstyle trailing comments appends to token, which is next to comment related token.

For example for file:
```
~/$ cat MyClass.java 
public class InputEmptyLineSeparatorWithComments {

    public void testTrailingComment() { } // no violation

    // Should have violation
    public void testPlainComment() { }

}
```
checkstyle with following parameters
```
~/checkstyle$ mvn exec:java \
   -Dexec.mainClass="com.puppycrawl.tools.checkstyle.Main" \
   -Dexec.args="-J '/home/user/MyClass.java'"
```
produce following tree:
```
CLASS_DEF -> CLASS_DEF [1:0]
|--MODIFIERS -> MODIFIERS [1:0]
|   `--LITERAL_PUBLIC -> public [1:0]
|--LITERAL_CLASS -> class [1:7]
|--IDENT -> InputEmptyLineSeparatorWithComments [1:13]
`--OBJBLOCK -> OBJBLOCK [1:49]
    |--LCURLY -> { [1:49]
    |--METHOD_DEF -> METHOD_DEF [3:4]
    |   |--MODIFIERS -> MODIFIERS [3:4]
    |   |   `--LITERAL_PUBLIC -> public [3:4]
    |   |--TYPE -> TYPE [3:11]
    |   |   `--LITERAL_VOID -> void [3:11]
    |   |--IDENT -> testTrailingComment [3:16]
    |   |--LPAREN -> ( [3:35]
    |   |--PARAMETERS -> PARAMETERS [3:36]
    |   |--RPAREN -> ) [3:36]
    |   `--SLIST -> { [3:38]
    |       `--RCURLY -> } [3:40]
    |--METHOD_DEF -> METHOD_DEF [6:4]
    |   |--MODIFIERS -> MODIFIERS [6:4]
    |   |   |--SINGLE_LINE_COMMENT -> // [3:42]
    |   |   |   `--COMMENT_CONTENT ->  no violation\n [3:44]
    |   |   |--SINGLE_LINE_COMMENT -> // [5:4]
    |   |   |   `--COMMENT_CONTENT ->  Should have violation\n [5:6]
    |   |   `--LITERAL_PUBLIC -> public [6:4]
    |   |--TYPE -> TYPE [6:11]
    |   |   `--LITERAL_VOID -> void [6:11]
    |   |--IDENT -> testPlainComment [6:16]
    |   |--LPAREN -> ( [6:32]
    |   |--PARAMETERS -> PARAMETERS [6:33]
    |   |--RPAREN -> ) [6:33]
    |   `--SLIST -> { [6:35]
    |       `--RCURLY -> } [6:37]
    `--RCURLY -> } [8:0]

```
Comment "no violation" on third line is trailing and related to testTrailingComment method. But in produced AST tree it appears as one of comments for testPlainComment.

---

## #3893: grammar: depreate METHOD_REF and user DOUBLE_COLON

**Labels:** approved, antlr

from https://github.com/checkstyle/checkstyle/pull/3884#issuecomment-283476031

>DOUBLE_COLON was named after :: (obviously) and was created as token for lexical part of grammar. I don't remember reason why we have both DOUBLE_COLON and METHOD_REF now, but most probably I was needed it on start in parts of grammar which have already been removed (or even was removed in process of grammar update) and token was simply forgotten. Now I don't see any reason why we need it.
I would suggest to try to remove it from syntax part and keep token in lexical part to keep compatibility. If grammar works fine we will be able to mark token as deprecated and remove.

on next major update of grammar we should resolve this. to keep DOUBLE_COLON as token type. Keep METHOD_REF (we can not remove tokens from grammar to keep compatibility) but make it deprecated in javadoc.

---

## #3151: Java Grammar: multiple variable declaration tree doesn't look natural

**Labels:** approved, antlr

```
$ cat TestClass.java
public class TestClass {
    int var6 = 5; int var7 = 6, //indent:4 exp:4
        var8 = 5; //indent:8 exp:8
}


$ java -jar checkstyle-6.18-all.jar -T TestClass.java
CLASS_DEF -> CLASS_DEF [1:0]
|--MODIFIERS -> MODIFIERS [1:0]
|  `--LITERAL_PUBLIC -> public [1:0]
|--LITERAL_CLASS -> class [1:7]
|--IDENT -> TestClass [1:13]
`--OBJBLOCK -> OBJBLOCK [1:23]
    |--LCURLY -> { [1:23]
    |--VARIABLE_DEF -> VARIABLE_DEF [2:4]
    |  |--MODIFIERS -> MODIFIERS [2:4]
    |  |--TYPE -> TYPE [2:4]
    |  |  `--LITERAL_INT -> int [2:4]
    |  |--IDENT -> var6 [2:8]
    |  |--ASSIGN -> = [2:13]
    |  |  `--EXPR -> EXPR [2:15]
    |  |      `--NUM_INT -> 5 [2:15]
    |  `--SEMI -> ; [2:16]
    |--VARIABLE_DEF -> VARIABLE_DEF [2:18] // variable 7
    |  |--MODIFIERS -> MODIFIERS [2:18]
    |  |--TYPE -> TYPE [2:18]
    |  |  `--LITERAL_INT -> int [2:18]
    |  |--IDENT -> var7 [2:22]
    |  |--ASSIGN -> = [2:27]
    |  |  `--EXPR -> EXPR [2:29]
    |  |      `--NUM_INT -> 6 [2:29]
    |  `--SEMI -> ; [3:16] // semi-colon
    |--COMMA -> , [2:30] // comma
    |--VARIABLE_DEF -> VARIABLE_DEF [2:18] // variable 8
    |  |--MODIFIERS -> MODIFIERS [2:18]
    |  |--TYPE -> TYPE [2:18]
    |  |  `--LITERAL_INT -> int [2:18]
    |  |--SINGLE_LINE_COMMENT -> // [2:32]
    |  |  `--COMMENT_CONTENT -> indent:4 exp:4\n [2:34]
    |  |--IDENT -> var8 [3:8]
    |  `--ASSIGN -> = [3:13]
    |      `--EXPR -> EXPR [3:15]
    |          `--NUM_INT -> 5 [3:15]
    |--SINGLE_LINE_COMMENT -> // [3:18]
    |  `--COMMENT_CONTENT -> indent:8 exp:8\n [3:20]
    `--RCURLY -> } [4:0]
```

I was expecting variables 7 and 8 to either have the same parent, or have some continuity with the line order and where the semi-colon would be. As it is now, it looks like `var7` has the semi-colon and `var8` ends with nothing which does not accurately reflect the code. This also causes the line numbers to look out of order, as `var7` ends with line 3, a comma at line 2, and then `var8` starts at line 2.

[JLS 8 - 8.3](https://docs.oracle.com/javase/specs/jls/se8/html/jls-8.html#jls-8.3) says it should be defined in a `VariableDeclaratorList`.
##

---

## #2766: Expression list token (ELIST) reports invalid line number when used as method param

**Labels:** approved, antlr

Example file:

``` java
public class Main {
    public class ExpressionList {
        public void test() {
            throw new IllegalStateException("Wrapped"
                + " message " + ex.getMessage(), null
            );
        }
    }
}
```

`ELIST` and its left sibling (`LPAREN`) are on the same line, but `ELIST` will have line number +1.

Unit test I am using to reproduce the problem:

``` java
    @Test
    public void expressionListTokeHasValidLineNumber() throws Exception {
        final String path = "/ExpressionList.java";
        final FileContents contents =
            new FileContents(
                new FileText(
                    new File(this.getClass().getResource(path).getFile()),
                    StandardCharsets.UTF_8.name()
                )
            );
        final DetailAST ast = TreeWalker.parse(contents);
        final DetailAST token = findToken(ast, TokenTypes.ELIST).get();
        MatcherAssert.assertThat(
            token.getLineNo(),
            Matchers.equalTo(
                token.getPreviousSibling().getLineNo()
            )
        );
    }

    private static Optional<DetailAST> findToken(final DetailAST ast,
        final int type) {
        DetailAST child = ast.getFirstChild();
        while (child != null) {
            final DetailAST token = child.findFirstToken(type);
            if (token != null) {
                return Optional.of(token);
            }
            final Optional<DetailAST> deep = findToken(child, type);
            if (deep.isPresent()) {
                return deep;
            }
            child = child.getNextSibling();
        }
        return Optional.absent();
    }
```

Checkstyle version `6.12.1`.
##

---

## #950: Non-standard locations in tree for DetailAST items

**Labels:** approved, antlr

When traversing the DetailAST tree to build a custom checker, I notice some of the same types are found in different areas, either as a child or as a sibling. One example is "return" has ";" as a child while an expression has ";" as a sibling.
It is making traversing the tree and finding items a little bit more tricky than it is needed. It would be much easier if they were to be found in the same location. 

I am using checkstyle 6.5 and extending the "Check" class and getting the DetailAST from the "visitToken" method.
Here is an example I am seeing. Code:

```
// line 9
    if (a == 1) return;
// line 15
    if (a == 2)
        b = 3;
```

produces the following DetailAST tree:

```
Type "if" (83) Line 9
    Type "(" (76) Line 9
    Type "EXPR" (28) Line 9
        Type "==" (116) Line 9
            Type "a" (58) Line 9
            Type "1" (137) Line 9
    Type ")" (77) Line 9
    Type "return" (88) Line 9
        Type ";" (45) Line 9 // <-- child of "return"

Type "if" (83) Line 15
    Type "(" (76) Line 15
    Type "EXPR" (28) Line 15
        Type "==" (116) Line 15
            Type "a" (58) Line 15
            Type "2" (137) Line 15
    Type ")" (77) Line 15
    Type "EXPR" (28) Line 16
        Type "=" (80) Line 16
            Type "b" (58) Line 16
            Type "3" (137) Line 16
    Type ";" (45) Line 16 // <-- sibling of "EXPR"
```

Another example is where {}s are children and ()s for if statements are siblings.
##

---

## #851: Comments location in AST

**Labels:** antlr, in-review

I've faced some weirdness during comments analyzing in AST, e.g.:

```
switch(...) {
      case x:
          doSmth();
          // this comment has Y's CASE_GROUP as its parent
      case y:
          doSmth();
}
```

It provides problems during analyzing surrounding statements
##

---
