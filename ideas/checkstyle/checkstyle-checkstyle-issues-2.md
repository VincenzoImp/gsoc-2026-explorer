# issues

**Parent:** checkstyle — Project Ideas
**Source:** https://github.com/checkstyle/checkstyle/issues?q=is%3Aissue%20state%3Aopen%20label%3Awebsite
**Scraped:** 2026-02-22T23:28:47.591855

---

## #15457: Fix false website failure on absolute links for javadocs to our own website

**Labels:** approved, website

Master failure:
https://github.com/checkstyle/checkstyle/actions/runs/10268868835/job/28412946322#step:4:2435
> `<a class="externalLink" href="https://checkstyle.org/styleguides/google-java-style-20220203/javaguide.html#s4.8.6.1-block-comment-style">https://checkstyle.org/styleguides/google-java-style-20220203/javaguide.html#s4.8.6.1-block-comment-style</a>: 404 Not Found`

Link to file with failure: https://github.com/checkstyle/checkstyle/blob/93d7140c4f38583f281f56df55603057cc85e8a2/src/main/java/com/puppycrawl/tools/checkstyle/checks/indentation/CommentsIndentationCheck.java#L38

Failure only occurs in master and not in PRs.

Issue is we don't know if the link is really valid or not until after we do a release and update our website since its an absolute link.

Javadocs need to be absolute link since we would want to use it on our locals, and on website javadoc is in some weird directory. If the link is in our xdoc, we should be using relative links as it is moved to versioning directory eventually, and absolute links in versioning break versioning directory.

Javadoc link is at: https://checkstyle.org/apidocs/com/puppycrawl/tools/checkstyle/checks/indentation/CommentsIndentationCheck.html

We need to find some way to ignore our website in javadoc, and only validate it once we have released new version of website in release process. It would be better if we found someway to validate this before release, otherwise GH will always be behind validation. We will be fixing errors in X.Y release in X.(Y+1) snaspshot.

Additional reasoning for this issue at https://github.com/checkstyle/checkstyle/pull/15459#issuecomment-2278094799

---

## #14542: All contribution and development documentation should live in GitHub

**Labels:** approved, miscellaneous, website

Right now, we have development and contribution documentation both on our website and GitHub. I think it makes sense to consolidate these to GitHub and allow our website to be only for Checkstyle usage. To be clear, i am proposing that we move the entire "[Developers](https://checkstyle.org/eclipse.html#:~:text=Sun%27s%20Style-,Developers,-Extending%20Checkstyle)" section to GitHub.

This has several advantages:
1. Code blocks are rendered more clearly in markdown
2. Markdown supports different types of syntax highlighting
3. Code blocks are easily copy-pasted

I really can't think of any disadvantages for this. Personally, I find markdown much easier to read and much prefer markdown for developer documentation due to it's simple formatting.

If we move forward with this issue, we should also remove the IDE setup stuff from the wiki since it will now live in GitHub (we should probably just do this anyway now).

---

## #13986: links to "subset of tokens" properties need rethinking

**Labels:** website

define more clear policy on what is true source metadata content from javadocs.
not finished discussion:
https://github.com/checkstyle/checkstyle/pull/13925#discussion_r1368922550

in same PR we made special hack in xdoc macros to handle it, but we need to comeback to it and rethink

---

## #13722: Decide on how to process validation-type

**Labels:** approved, website

In https://github.com/checkstyle/checkstyle/pull/13670 we reuse functionality from site generation in the metadata module in an effort to start removing Javadocs.

One property that is mentioned in Javadocs but we do not have a way to extract is `validation-type`
https://github.com/checkstyle/checkstyle/blob/c2e65aa2e9f6854f3902c8c018301ba97e8a1706/src/main/resources/com/puppycrawl/tools/checkstyle/meta/checks/DescendantTokenCheck.xml#L19-L22

https://github.com/checkstyle/checkstyle/blob/c2e65aa2e9f6854f3902c8c018301ba97e8a1706/src/main/java/com/puppycrawl/tools/checkstyle/checks/DescendantTokenCheck.java#L46-L49

How should we proceed with the extraction of this property?

---
One idea is to mention it as a Javadoc param above the setter and get it from there:
```java
    /**
     * Setter to specify set of tokens with limited occurrences as descendants.
     *
     * @param limitedTokensParam tokens to ignore.
     * @validationType tokenTypesSet
     * @since 3.2
     */
    public void setLimitedTokens(String... limitedTokensParam) {
        ....
    }
```

same problems is blocking macros usage at MultipleStringLiterals https://github.com/checkstyle/checkstyle/pull/13721

---

## #13490: Refactor ViolationMessagesMacro::constructMessageKeyUrl to use UrlEncoder

**Labels:** approved, website

From https://github.com/checkstyle/checkstyle/pull/13423#discussion_r1272910995

Method `constructMessageKeyUrl` in `ViolationMessagesMacro` does not encode the URL
```java
    private static String constructMessageKeyUrl(Class<?> clss, String messageKey) {
        return "https://github.com/search?q="
                + "path%3Asrc%2Fmain%2Fresources%2F"
                + clss.getPackage().getName().replace(".", "%2F")
                + "%20path%3A**%2Fmessages*.properties+repo%3Acheckstyle%2F"
                + "checkstyle+%22" + messageKey + "%22";
}
```

`UrlEncoder.encode` can be used in this case (https://www.baeldung.com/java-url-encoding-decoding). However, this is not possible without creating a ton of suppressions.

A `space` can be transformed to `+` or `%20`. From https://www.w3schools.com/tags/ref_urlencode.ASP:
>  URLs cannot contain spaces. URL encoding normally replaces a space with a plus (+) sign or with %20.

`UrlEncoder.encode` replaces spaces to `+` but the following test expects both `%20` and `+`
https://github.com/checkstyle/checkstyle/blob/0c2ab5338db569b4699d5d20121d1bd508394eb9/src/test/java/com/puppycrawl/tools/checkstyle/internal/XdocsPagesTest.java#L1427-L1433

After all check templates use the violation messages macro, we can switch to `UrlEncoder` and edit the test to expect `+`

---

## #13206: Improvements to site workflow

**Labels:** website

In a similar fashion to https://github.com/checkstyle/checkstyle/issues/12991, the workflow can be improved. Lots of logic is in the workflow and can be extracted to a separate script. Both workflows(`site` and  `diff-report`) share an almost identical  last job step(`send_message`). Another issue is that sometimes runners are taken and we have to wait more than 30 minutes inbetween jobs. Placing the whole script under one job will be better - start action -> run script, upload to aws, comment -> free runner for whatever needs it next.

---
Here are things split into chunks with no specific order:
- Move workflow to use only one job instead of 3
- Move each step that contains bash instructions into a `site.sh` script. Simiar to what the description of #12991 describes
    > We should move steps out to a single script file, where we can invoke the script with a single argument command to handle steps, like we do with validation.sh.
- Create a separate script for the identical `send_message` part that `diff-report` and `site`share

---

## #13194: Rethink purpose of package section in Check module documentation 

**Labels:** approved, website

Detected at https://github.com/checkstyle/checkstyle/pull/13103#issuecomment-1585817452

https://checkstyle.org/checks/naming/abbreviationaswordinname.html#Package

Todo:
- find in history why we have it.
- define a reason why it should be in New web page structure

---

## #13162: Trigger linkcheck by Github comment

**Labels:** approved, miscellaneous, website

From https://github.com/checkstyle/checkstyle/pull/13103#issuecomment-1576878233
> I think we need to think one more time to make GitHub action triggered by comment to run link check plugin validation. It will help a lot us during summer.

---

## #13159: Decide on a naming convention in the `xdocs` folder

**Labels:** website

From https://github.com/checkstyle/checkstyle/pull/13103#discussion_r1215725714

Names of files in `xdocs` are mixed - `writingchecks.xml`, `property_types.xml`, `writingfilters.xml`, `beginning_development.xml`, etc...

For the checks pages, we went with `_`. I assume this would be the case for the rest?

---

## #11572: linkcheck report full of error on damaged links to javadoc

**Labels:** approved, miscellaneous, website

https://checkstyle.org/linkcheck.html

Example of damaged link:
> error | writingjavadocchecks.html 
  | error apidocs/com/puppycrawl/tools/checkstyle/checks/javadoc/AbstractJavadocCheck.html#getAcceptableJavadocTokens--: doesn't exist.

at page https://checkstyle.org/writingjavadocchecks.html#Customize_token_types_in_Javadoc_Checks
expected link https://checkstyle.org/apidocs/com/puppycrawl/tools/checkstyle/checks/javadoc/AbstractJavadocCheck.html#getAcceptableJavadocTokens()

we need to fix all problems.


hit, generation of site:
`mvn site -Pno-valdations`

---
