# open a new issue for discussion

**Parent:** API Dash — Project Ideas
**Source:** https://github.com/foss42/apidash/issues/new/choose
**Scraped:** 2026-02-22T23:28:47.569287

---

## #1125: [BUG] Cloudflare-protected APIs are blocked due to missing default User-Agent header

### Describe the bug/problem

When sending HTTP requests without manually adding a `User-Agent` header, some services behind Cloudflare block the request. This happens because Dart's `http` package sends `dart:io` as the default User-Agent, which Cloudflare flags as a bot.

The same request works fine using `curl` (which sends `User-Agent` and `Accept` headers by default) or when manually adding headers like `User-Agent: Mozilla/5.0` and `Accept: application/json`.

The root cause is in `packages/better_networking/lib/services/http_service.dart` — the `sendHttpRequestV1()` function uses `authenticatedRequestModel.enabledHeadersMap` directly without setting a fallback `User-Agent`.

**Suggestion:** Set a default `User-Agent: APIDash/<version>` and `Accept: */*` header when the user hasn't explicitly provided one, similar to how Postman sends `PostmanRuntime/7.x`.

### Steps to Reproduce the bug/problem

1. Open API Dash
2. Create a GET request to `https://jsonplaceholder.typicode.com/posts/1` (Cloudflare-protected)
3. Send it **without** adding any headers → request gets blocked
4. Add `User-Agent: Mozilla/5.0` + `Accept: application/json` manually → request succeeds with `200 OK`
5. Try the same without headers on a non-Cloudflare API like `https://reqres.in/api/users` → works fine

**Additional observations:**
- Sending with **no headers** → blocked by Cloudflare
- Sending with **only `User-Agent`** → still blocked
- Sending with **`User-Agent` + any one other header** (e.g., `Accept`) → works ✅
- `curl` works out of the box because it sends both `User-Agent` and `Accept` by default
- This issue is **specific to Cloudflare-protected APIs** — non-Cloudflare APIs like `https://reqres.in/api` work fine without any headers

### Expected behavior

API Dash should send meaningful default headers (`User-Agent` and `Accept`) automatically so requests don't get blocked by common bot detection systems.

### Device Info
- **OS:** macOS
- **Version:** Sequoia 15.2

### Flutter Doctor

```
[✓] Flutter (Channel stable, 3.41.2, on macOS 15.2 24C101 darwin-arm64, locale en-US) [683ms]
    • Flutter version 3.41.2 on channel stable at /Users/shreyanshjain/flutter
    • Upstream repository https://github.com/flutter/flutter.git
    • Framework revision 90673a4eef (4 days ago), 2026-02-18 13:54:59 -0800
    • Engine revision 6c0baaebf7
    • Dart version 3.11.0
    • DevTools version 2.54.1
    • Feature flags: enable-web, enable-linux-desktop, enable-macos-desktop,
      enable-windows-desktop, enable-android, enable-ios, cli-animations, enable-native-assets,
      omit-legacy-version-file, enable-lldb-debugging, enable-uiscene-migration

[✗] Android toolchain - develop for Android devices [632ms]
    ✗ Unable to locate Android SDK.
      Install Android Studio from: https://developer.android.com/studio/index.html
      On first launch it will assist you in installing the Android SDK components.
      (or visit https://flutter.dev/to/macos-android-setup for detai

*[truncated]*

---

## #1116: The Video Preview Plays Audio Even When the Video is Paused

#### Describe the bug/problem

When getting a video as a response and trying to pause the video in Preview, the video pauses but the audio keeps playing in a loop.

https://github.com/user-attachments/assets/3041c93c-c5c7-451e-b4ce-c4dc3273c513.mp4

#### Steps to Reproduce the bug/problem

- Send a GET request to [https://flutter.github.io/assets-for-api-docs/assets/videos/bee.mp4](https://github.com/foss42/apidash/issues/new/url)
- Pause the video 
- 
#### Expected behavior
The video should be paused properly with the audio

#### Device Info (The device where you encountered this issue)
 - OS: MacOS
 - Version: 20.3

#### Flutter Doctor
Please run the `flutter doctor -v` command and provide the details below:

```
[✓] Flutter (Channel stable, 3.41.1, on macOS 26.3 25D125 darwin-arm64, locale
    en-IN) [345ms]
    • Flutter version 3.41.1 on channel stable at /Users/sagarnewpane/flutter
    • Upstream repository https://github.com/flutter/flutter.git
    • Framework revision 582a0e7c55 (9 days ago), 2026-02-12 17:12:32 -0800
    • Engine revision 3452d735bd
    • Dart version 3.11.0
    • DevTools version 2.54.1
    • Feature flags: enable-web, enable-linux-desktop, enable-macos-desktop,
      enable-windows-desktop, enable-android, enable-ios, cli-animations,
      enable-native-assets, omit-legacy-version-file, enable-lldb-debugging,
      enable-uiscene-migration

[✓] Android toolchain - develop for Android devices (Android SDK version 36.1.0)
    [1,608ms]
    • Android SDK at /Users/sagarnewpane/Library/Android/sdk
    • Emulator version 36.4.9.0 (build_id 14788078) (CL:N/A)
    • Platform android-36.1, build-tools 36.1.0
    • ANDROID_HOME = /Users/sagarnewpane/Library/Android/sdk
    • Java binary at: /Applications/Android
      Studio.app/Contents/jbr/Contents/Home/bin/java
      This is the JDK bundled with the latest Android Studio installation on
      this machine.
      To manually set the JDK path, use: `flutter config
      --jdk-dir="path/to/jdk"`.
    • Java version OpenJDK Runtime Environment (build 21.0.9+-14649483-b1163.86)
    • All Android licenses accepted.

[✓] Xcode - develop for iOS and macOS (Xcode 26.1.1) [785ms]
    • Xcode at /Applications/Xcode.app/Contents/Developer
    • Build 17B100
    • CocoaPods version 1.16.2

[✓] Chrome - develop for the web [4ms]
    • Chrome at /Applications/Google Chrome.app/Contents/MacOS/Google Chrome

[✓] Connected device (2 available) [5.9s]
    • macOS (desktop) • macos  • darwin-arm64   • macOS 26.3 25D125 darwin-arm64
    • Chrome (web)    • chrome • web-javascript • Google Chrome 142.0.7444.177
    ! Error: Browsing on the local area network for iPhone. Ensure the device is
      unlocked and attached with a cable or associated with the same local area
      network as this Mac.
      The device must be opted into Developer Mode to connect wirelessly. (code
      -27)

[✓] Network resources [591ms]
    • All expected network resources are available.

• No issues found!

```

---

## #1113: [Bug]: App crashes when searching/filtering with an AI-type request in the collection

#### Describe the bug/problem
If you have an AI-type request in your collection and try to use the search/filter bar, the app crashes immediately. It doesn't matter what you type — just clicking into the search bar and typing anything is enough to bring the whole app down.

#### Steps to Reproduce the bug/problem
1. Open API Dash
2. Create a new request and change its type to **AI**
3. Click on the **search/filter bar** in the collection pane
4. Type anything (e.g. `test`)
5. App throws "Null check operator used on a null value" error 

https://github.com/user-attachments/assets/6d7b3a27-22a3-4173-a943-5c31031f498b

#### Expected behavior
Typing in the search bar should never throw an error regardless of what request types are in the collection.

#### Device Info
- OS: Windows 11 Home Single Language 64-bit, 25H2
- Version: 10.0.26200.7840

#### Flutter Doctor
```
[√] Flutter (Channel stable, 3.41.2, on Microsoft Windows [Version 10.0.26200.7840], locale en-US) [368ms]
    • Flutter version 3.41.2 on channel stable at C:\flutter\flutter
    • Upstream repository https://github.com/flutter/flutter.git
    • Framework revision 90673a4eef (3 days ago), 2026-02-18 13:54:59 -0800
    • Engine revision 6c0baaebf7
    • Dart version 3.11.0
    • DevTools version 2.54.1
    • Feature flags: enable-web, enable-linux-desktop, enable-macos-desktop, enable-windows-desktop, enable-android,
      enable-ios, cli-animations, enable-native-assets, omit-legacy-version-file, enable-lldb-debugging,
      enable-uiscene-migration

[√] Windows Version (11 Home Single Language 64-bit, 25H2, 2009) [1,571ms]

[!] Android toolchain - develop for Android devices (Android SDK version 34.0.0) [941ms]
    • Android SDK at C:\Users\lenovo\AppData\Local\Android\sdk
    • Emulator version 33.1.24.0 (build_id 11237101) (CL:N/A)
    X cmdline-tools component is missing.
      Try installing or updating Android Studio.
      Alternatively, download the tools from https://developer.android.com/studio#command-line-tools-only and make sure
      to set the ANDROID_HOME environment variable.
      See https://developer.android.com/studio/command-line for more details.
    X Android license status unknown.
      Run `flutter doctor --android-licenses` to accept the SDK licenses.
      See https://flutter.dev/to/windows-android-setup for more details.

[√] Chrome - develop for the web [105ms]
    • Chrome at C:\Program Files\Google\Chrome\Application\chrome.exe

[√] Visual Studio - develop Windows apps (Visual Studio Community 2022 17.13.5) [104ms]
    • Visual Studio at C:\Program Files\Microsoft Visual Studio\2022\Community
    • Visual Studio Community 2022 version 17.13.35919.96
    • Windows 10 SDK version 10.0.22621.0

[√] Connected device (3 available) [197ms]
    • Windows (desktop) • windows • windows-x64    • Microsoft Windows [Version 10.0.26200.7840]
    • Chrome (web)      • chrome  • web-javascript • Google Chrome 144.0.7559.134
    • Edge (web)        • edge    • web-java

*[truncated]*

---

## #1112: Postman import silently drops request body for urlencoded body mode

## Bug

When importing a Postman collection, requests that use `application/x-www-form-urlencoded` body mode have their entire request body **silently dropped**. No error or warning is shown. The imported request appears to succeed but contains no body content.

This affects one of the most common HTTP body types — login forms, OAuth token requests, search forms, and any traditional HTML form submission.

## Root Cause

The `Body` model in `packages/postman/lib/models/postman_collection.dart` (line 142–147) does not include a `urlencoded` field:

```dart
const factory Body({
    String? mode,
    String? raw,
    Options? options,
    List<Formdatum>? formdata,
    // Missing: List<UrlencodedParam>? urlencoded
}) = _Body;
```

The importer in `packages/apidash_core/lib/import_export/postman_io.dart` (lines 52–84) only handles two body modes:

- `mode == 'raw'` (line 53)
- `mode == 'formdata'` (line 62)

When `mode == 'urlencoded'`, neither condition matches. The body falls through as `null` with the default content type (JSON), silently discarding all form data.

## Steps to Reproduce

1. Create a Postman collection with a POST request using `x-www-form-urlencoded` body:

```json
{
  "info": {
    "name": "Test Collection",
    "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
  },
  "item": [
    {
      "name": "Login",
      "request": {
        "method": "POST",
        "header": [],
        "body": {
          "mode": "urlencoded",
          "urlencoded": [
            { "key": "username", "value": "admin", "type": "text" },
            { "key": "password", "value": "secret123", "type": "text" }
          ]
        },
        "url": { "raw": "https://api.example.com/login" }
      }
    }
  ]
}
```

2. Export this from Postman as JSON (or save the above as a `.json` file)
3. In API Dash, import the file via the Postman import option
4. Open the imported "Login" request

**Expected:** Request body contains `username=admin&password=secret123` with content type `application/x-www-form-urlencoded`

**Actual:** Request body is empty. Content type is set to `application/json` (the default). No error or warning is displayed.

## Impact

- **Silent data loss** — Users have no indication that body content was dropped
- **Very common body type** — urlencoded is used for login forms, OAuth2 token endpoints, search APIs, and any traditional form-based API
- **Breaks onboarding** — Users importing from Postman discover their requests don't work, with no clue why
- **API Dash already supports urlencoded** — The app can handle this body type natively (documented in user guide), it's only the Postman importer that drops it

## Additional: `graphql` body mode also affected

Postman's `graphql` body mode is similarly unhandled:

```json
{
  "body": {
    "mode": "graphql",
    "graphql": {
      "query": "{ users { id name } }",
      "variables": "{}"
    }
  }
}
```

This is also silently dropped during import.

## Suggested F

*[truncated]*

---

## #1109: Add default HTTP headers to avoid 403 errors from Cloudflare-protected APIs ({JSON} Placeholder)

#### Describe the bug/problem

When making requests to APIs protected by Cloudflare (e.g., https://jsonplaceholder.typicode.com), I encountered 403 Forbidden error. This happens because the HTTP client sends requests without standard browser-like headers, which Cloudflare's bot protection interprets as suspicious traffic.

Note: While this can be handled easily by adding the header within the request manually, adding default values will prevent the extra step for developers. They should still be able to override the default values. 

403 Response 
```
<!DOCTYPE html>
<!--[if lt IE 7]> <html class="no-js ie6 oldie" lang="en-US"> <![endif]-->
<!--[if IE 7]>    <html class="no-js ie7 oldie" lang="en-US"> <![endif]-->
<!--[if IE 8]>    <html class="no-js ie8 oldie" lang="en-US"> <![endif]-->
<!--[if gt IE 8]><!--> <html class="no-js" lang="en-US"> <!--<![endif]-->
<head>
<title>Attention Required! | Cloudflare</title>
<meta charset="UTF-8" />
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<meta http-equiv="X-UA-Compatible" content="IE=Edge" />
<meta name="robots" content="noindex, nofollow" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<link rel="stylesheet" id="cf_styles-css" href="/cdn-cgi/styles/cf.errors.css" />
<!--[if lt IE 9]><link rel="stylesheet" id='cf_styles-ie-css' href="/cdn-cgi/styles/cf.errors.ie.css" /><![endif]-->
<style>body{margin:0;padding:0}</style>


<!--[if gte IE 10]><!-->
<script>
  if (!navigator.cookieEnabled) {
    window.addEventListener('DOMContentLoaded', function () {
      var cookieEl = document.getElementById('cookie-alert');
      cookieEl.style.display = 'block';
    })
  }
</script>
<!--<![endif]-->

</head>
<body>
  <div id="cf-wrapper">
    <div class="cf-alert cf-alert-error cf-cookie-error" id="cookie-alert" data-translate="enable_cookies">Please enable cookies.</div>
    <div id="cf-error-details" class="cf-error-details-wrapper">
      <div class="cf-wrapper cf-header cf-error-overview">
        <h1 data-translate="block_headline">Sorry, you have been blocked</h1>
        <h2 class="cf-subheadline"><span data-translate="unable_to_access">You are unable to access</span> typicode.com</h2>
      </div><!-- /.header -->

      <div class="cf-section cf-highlight">
        <div class="cf-wrapper">
          <div class="cf-screenshot-container cf-screenshot-full">
            
              <span class="cf-no-screenshot error"></span>
            
          </div>
        </div>
      </div><!-- /.captcha-container -->

      <div class="cf-section cf-wrapper">
        <div class="cf-columns two">
          <div class="cf-column">
            <h2 data-translate="blocked_why_headline">Why have I been blocked?</h2>

            <p data-translate="blocked_why_detail">This website is using a security service to protect itself from online attacks. The action you just performed triggered the security solution. There are several actions that could trigger this block incl

*[truncated]*

---

## #1107: FEATURE: Add paste-from-text support to import dialog

## Description

The import dialog currently only supports importing API requests via 
file drag-and-drop. However, the most common developer workflow is 
copy-pasting — e.g., copying a cURL command from a browser's Network tab 
or from a colleague's message.

There is an existing TODO in the codebase requesting this feature:

**[File](https://github.com/foss42/apidash/blob/main/lib/importer/import_dialog.dart):  ** [lib/importer/import_dialog.dart](cci:7://file:///b:/apidash/lib/importer/import_dialog.dart:0:0-0:0)  (line 13)  has mentioned: 

  <mark>// TODO: The dialog must have a feature to paste contents in a text field
  // Also, a mechanism can be added where on importing a file it shows the
  // contents in the text field and then the user presses ok to add it to collection

Added by @ashitaprasad in commit 4d426dcf.</mark>

So  currently the import dialog is like this:
<img width="1785" height="984" alt="Image" src="https://github.com/user-attachments/assets/c26e4787-67b7-4d19-ba0b-78d52bd2a1cd" />

## Proposed Solution
Add a multiline `TextField` below the existing drag-and-drop area in the 
import dialog, separated by an "OR paste content below" divider. The text 
field shows format-specific hints (e.g., "Paste cURL command here..." 
when cURL is selected). An "Import" button submits the pasted text to 
the existing `Importer.getHttpRequestModelList()` parser.
**Key design decisions:**
- Reuses the existing [Importer](cci:2://file:///b:/apidash/lib/importer/importer.dart:3:0-18:1) class — no new parsing logic needed
- Hint text updates dynamically based on the selected import format
- Both file and text import paths remain available simultaneously
- Cancel/Import buttons for explicit user control

looks like:

<img width="314" height="381" alt="Image" src="https://github.com/user-attachments/assets/34a55647-d821-4516-86cd-a3ef7e50a9cc" />





This is a small, high-impact UI change that improves the developer experience for every user. Implementing it and making PR as it is already mentioned by @ashitaprasad in commit 4d426dcf. Happy to implement !!!
@animator @ashitaprasad

---

## #1106: [Bug]: Deleting the last request leaves the editor blank

#### Describe the bug/problem
When you have multiple requests and delete the last one in the list, the editor just goes blank — even though there are still other requests sitting right there. It feels like the app forgot they exist. You have to manually click on another request to get back to work, which is a bit jarring.

#### Steps to Reproduce the bug/problem
1. Open API Dash
2. Create 2 requests by clicking `+` twice
3. Select the **second (last) request** in the list
4. Right click on it → Delete
5. The editor goes completely blank even though the first request is still there

https://github.com/user-attachments/assets/4f10bb6e-d77d-4135-a06a-20c064a4ac7d

#### Expected behavior
After deleting the last request, the app should automatically select the one above it — so you can keep working without any interruption. That's how most tools handle this kind of thing.

#### Device Info
- OS: Windows 11 Home Single Language 64-bit, 25H2
- Version: 10.0.26200.7840

#### Flutter Doctor
```
[√] Flutter (Channel stable, 3.41.2, on Microsoft Windows [Version 10.0.26200.7840], locale en-US) [368ms]
    • Flutter version 3.41.2 on channel stable at C:\flutter\flutter
    • Upstream repository https://github.com/flutter/flutter.git
    • Framework revision 90673a4eef (3 days ago), 2026-02-18 13:54:59 -0800
    • Engine revision 6c0baaebf7
    • Dart version 3.11.0
    • DevTools version 2.54.1
    • Feature flags: enable-web, enable-linux-desktop, enable-macos-desktop, enable-windows-desktop, enable-android,
      enable-ios, cli-animations, enable-native-assets, omit-legacy-version-file, enable-lldb-debugging,
      enable-uiscene-migration

[√] Windows Version (11 Home Single Language 64-bit, 25H2, 2009) [1,571ms]

[!] Android toolchain - develop for Android devices (Android SDK version 34.0.0) [941ms]
    • Android SDK at C:\Users\lenovo\AppData\Local\Android\sdk
    • Emulator version 33.1.24.0 (build_id 11237101) (CL:N/A)
    X cmdline-tools component is missing.
      Try installing or updating Android Studio.
      Alternatively, download the tools from https://developer.android.com/studio#command-line-tools-only and make sure
      to set the ANDROID_HOME environment variable.
      See https://developer.android.com/studio/command-line for more details.
    X Android license status unknown.
      Run `flutter doctor --android-licenses` to accept the SDK licenses.
      See https://flutter.dev/to/windows-android-setup for more details.

[√] Chrome - develop for the web [105ms]
    • Chrome at C:\Program Files\Google\Chrome\Application\chrome.exe

[√] Visual Studio - develop Windows apps (Visual Studio Community 2022 17.13.5) [104ms]
    • Visual Studio at C:\Program Files\Microsoft Visual Studio\2022\Community
    • Visual Studio Community 2022 version 17.13.35919.96
    • Windows 10 SDK version 10.0.22621.0

[√] Connected device (3 available) [197ms]
    • Windows (desktop) • windows • windows-x64    • Microsoft Windows [Version 10.0.26200.7840]
  

*[truncated]*

---

## #1105: [Feature]: Show Response Body Size in Response Header

#### Tell us about the task you want to perform and are unable to do so because the feature is not available

When testing APIs, I need to quickly understand the size of the response body to evaluate API performance, debug slow responses, and verify that pagination or filtering is working correctly. Currently, the response pane only shows status code and response time — there is no way to see the response body size without manually inspecting it.

#### Describe the solution/feature you'd like us to add

Add a response body size indicator (e.g., `2.3 KB`) in the response pane header bar, displayed alongside the existing status code and response time.

- The `bytes` field is already available in `HttpResponseModel` — just needs `bytes.length` to be calculated and formatted
- Changes required in `response_pane_header.dart` only
- Format: bytes < 1KB shown in B, above 1KB shown in KB, above 1MB shown in MB

**Example:**
```
200 OK    124ms    2.3 KB
```
#### Any other feedback you would like to provide
This is a small, high-impact UI change that improves the developer experience for every user. Happy to implement this if the feature is accepted! 
@animator @ashitaprasad

---

## #1103: Add double-click reset to 50:50 for pane divider

#### Tell us about the task you want to perform and are unable to do so because the feature is not available
When resizing panes using the divider, it’s easy to end up with uneven widths. Currently there isn’t a quick way to restore the default balanced layout without manually dragging the divider back to the center.

#### Describe the solution/feature you'd like us to add
Add a double-click action on the divider that resets the pane widths to a 50:50 split. This would provide a quick way to restore the default layout without affecting existing drag-to-resize behaviour.

#### Any other feedback you would like to provide regarding the site
I’m planning to open a PR implementing this for discussion and would be happy to adjust the approach based on feedback.

---

## #1101: Feature: Improve DashBot Reasoning Trace for better observability

### Description
Currently, DashBot API Error Debugging outputs a summary natively without an explicit Chain-of-Thought layer. To improve the observability and logical flow of the agent, we should inject a  requirement into the prompt.

### Motivation
It instantly improves agent logic observability by allowing developers to see the why before the final summary in the debug tab.

---

## #1099: Feature: Upgrade DashBot Test Generation to Agentic Self-Healing Test Suites (Idea 4 PoC)

### Description
This issue proposes upgrading the standard DashBot test generation prompt into an intelligent **Agentic Test Suite Generator**. It enforces LLM outputs to include self-healing conditionals (e.g., dynamically adjusting payloads on 400 errors or mocking token refresh on 401s), stateful execution chains, and advanced security edge cases. This serves as a functional Proof of Concept for GSoC 2026 Idea #4.

### Motivation
Providing an agentic baseline for DashBot's test generation aligns with Idea #4 and adds more robust testing capabilities out-of-the-box.

---

## #1092: Build fails on latest Flutter due to Freezed 2.x and dart_style 3.x dependency conflict

#### Describe the bug/problem
Installation from source code fails on 'melos pub-get' due to dependency conflict

<img width="1116" height="628" alt="Image" src="https://github.com/user-attachments/assets/52bb24a2-e77d-4b29-8e04-0f14054541a8" />

#### Steps to Reproduce the bug/problem
Follow the Local installation guide from the offical md.
[https://github.com/foss42/apidash/blob/main/doc/dev_guide/setup_run.md](https://github.com/foss42/apidash/issues/new/url)

#### Expected behavior
Installation to be successful without any errors

#### Device Info (The device where you encountered this issue)
 - OS: MacOS
 - Version: 26.4

#### Flutter Doctor
Please run the `flutter doctor -v` command and provide the details below:

```
[✓] Flutter (Channel stable, 3.41.1, on macOS 26.3 25D125 darwin-arm64, locale
    en-IN) [217ms]
    • Flutter version 3.41.1 on channel stable at /Users/sagarnewpane/flutter
    • Upstream repository https://github.com/flutter/flutter.git
    • Framework revision 582a0e7c55 (9 days ago), 2026-02-12 17:12:32 -0800
    • Engine revision 3452d735bd
    • Dart version 3.11.0
    • DevTools version 2.54.1
    • Feature flags: enable-web, enable-linux-desktop, enable-macos-desktop,
      enable-windows-desktop, enable-android, enable-ios, cli-animations,
      enable-native-assets, omit-legacy-version-file, enable-lldb-debugging,
      enable-uiscene-migration

[✓] Android toolchain - develop for Android devices (Android SDK version 36.1.0)
    [1,485ms]
    • Android SDK at /Users/sagarnewpane/Library/Android/sdk
    • Emulator version 36.4.9.0 (build_id 14788078) (CL:N/A)
    • Platform android-36.1, build-tools 36.1.0
    • ANDROID_HOME = /Users/sagarnewpane/Library/Android/sdk
    • Java binary at: /Applications/Android
      Studio.app/Contents/jbr/Contents/Home/bin/java
      This is the JDK bundled with the latest Android Studio installation on
      this machine.
      To manually set the JDK path, use: `flutter config
      --jdk-dir="path/to/jdk"`.
    • Java version OpenJDK Runtime Environment (build 21.0.9+-14649483-b1163.86)
    • All Android licenses accepted.

[✓] Xcode - develop for iOS and macOS (Xcode 26.1.1) [590ms]
    • Xcode at /Applications/Xcode.app/Contents/Developer
    • Build 17B100
    • CocoaPods version 1.16.2

[✓] Chrome - develop for the web [4ms]
    • Chrome at /Applications/Google Chrome.app/Contents/MacOS/Google Chrome

[✓] Connected device (2 available) [5.7s]
    • macOS (desktop) • macos  • darwin-arm64   • macOS 26.3 25D125 darwin-arm64
    • Chrome (web)    • chrome • web-javascript • Google Chrome 142.0.7444.177
    ! Error: Browsing on the local area network for iPhone. Ensure the device is
      unlocked and attached with a cable or associated with the same local area
      network as this Mac.
      The device must be opted into Developer Mode to connect wirelessly. (code
      -27)

[✓] Network resources [1,487ms]
    • All expected network resources are available.

• No issues found!
```

---

## #1090: Request/Response pane widths reset when toggling View Code

#### Describe the bug/problem
When resizing the Request and Response panes using the draggable divider, the layout resets to its default 50/50 split after clicking the </> View Code button. This causes the user’s manually adjusted pane widths to be lost and disrupts workflow.

#### Steps to Reproduce the bug/problem

1. Launch the app and open any API request
2. Drag the divider between the Request and Response panes
3. Click the </> View Code button in the Request pane
4. Observe the divider snapping back to the default center position

![Image](https://github.com/user-attachments/assets/984039fb-52a8-4595-89b4-1ddbb2f8170c)

#### Expected behavior

- Pane widths should remain unchanged when toggling the View Code pane.
- User-adjusted layout should persist across UI rebuilds.

**Root cause**

- EqualSplitView (in splitview_equal.dart) is currently implemented as a StatelessWidget. When the View Code toggle updates codePaneVisibleStateProvider, the parent widget rebuilds and recreates the internal MultiSplitViewController, resetting pane sizes.
- Converting EqualSplitView to a StatefulWidget and initializing the controller in initState() preserves pane sizes across rebuilds. I have implemented this fix locally and will open a PR shortly for review.

#### Device Info (The device where you encountered this issue)
 - OS: Windows
 - Version: Windows 11 25H2

#### Flutter Doctor
Please run the `flutter doctor -v` command and provide the details below:

```
[√] Flutter (Channel stable, 3.38.7, on Microsoft Windows [Version 10.0.26200.7840], locale en-US) [583ms]
    • Flutter version 3.38.7 on channel stable at C:\Users\Avinav\fvm\versions\3.38.7
    • Upstream repository https://github.com/flutter/flutter.git
    • Framework revision 3b62efc2a3 (6 weeks ago), 2026-01-13 13:47:42 -0800
    • Engine revision 78fc3012e4
    • Dart version 3.10.7
    • DevTools version 2.51.1
    • Feature flags: enable-web, enable-linux-desktop, enable-macos-desktop, enable-windows-desktop,
      enable-android, enable-ios, cli-animations, enable-native-assets, omit-legacy-version-file,
      enable-lldb-debugging

[√] Windows Version (Windows 11 or higher, 25H2, 2009) [1,280ms]

[X] Android toolchain - develop for Android devices [197ms]
    X Unable to locate Android SDK.
      Install Android Studio from: https://developer.android.com/studio/index.html
      On first launch it will assist you in installing the Android SDK components.
      (or visit https://flutter.dev/to/windows-android-setup for detailed instructions).
      If the Android SDK has been installed to a custom location, please use
      `flutter config --android-sdk` to update to that location.


[√] Chrome - develop for the web [150ms]
    • Chrome at C:\Program Files\Google\Chrome\Application\chrome.exe

[√] Visual Studio - develop Windows apps (Visual Studio Community 2026 18.3.1) [148ms]
    • Visual Studio at C:\Program Files\Microsoft Visual Studio\18\Community
    • Visual Studio Community 2026

*[truncated]*

---

## #1084: Build failure on Windows with Flutter SDK 3.38+ due to csv package conflicts

#### Describe the bug/problem
The project fails to build on Windows when using newer Flutter SDK versions (3.38+). The primary issue is a version conflict between core dependencies (freezed, test, matcher) and a specific compilation error in lib/widgets/previewer_csv.dart due to a breaking change in how constant expressions are handled in Dart.

#### Steps to Reproduce the bug/problem

Clone the repository on a Windows machine.

Ensure you are using Flutter SDK 3.38.7 or newer.

Run flutter pub get.

Run flutter run -d windows.

The build fails with the following error:

<img width="1629" height="249" alt="Image" src="https://github.com/user-attachments/assets/196b9d7c-2376-4644-9435-3acbab0647ba" />

#### Expected behavior

The project should compile successfully on Windows without any manual dependency overrides or code changes in previewer_csv.dart, even on newer Flutter SDK versions.

<img width="1919" height="1079" alt="Image" src="https://github.com/user-attachments/assets/14d5cf4d-9546-4837-ab4e-dcd3edf53d8b" />

#### Device Info (The device where you encountered this issue)
OS: Windows
Version: Windows 11

#### Flutter Doctor
[√] Flutter (Channel stable, 3.41.1, on Microsoft Windows [Version 10.0.26200.7840], locale en-US)
    • Flutter version 3.41.1 on channel stable at C:\src\flutter
    • Dart version 3.11.0
    • DevTools version 2.54.1

[√] Windows Version (11 Home Single Language 64-bit, 25H2, 2009)

[X] Android toolchain - develop for Android devices
    X Unable to locate Android SDK.

[√] Chrome - develop for the web
    • Chrome at C:\Program Files\Google\Chrome\Application\chrome.exe

[√] Visual Studio - develop Windows apps (Visual Studio Build Tools 2019 16.11.49)
    • Visual Studio at C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools
    • Windows 10 SDK version 10.0.19041.0

[√] Connected device (3 available)
    • Windows (desktop) • windows • windows-x64
    • Chrome (web)      • chrome  • web-javascript
    • Edge (web)        • edge    • web-javascript

[√] Network resources
    • All expected network resources are available.

---

## #1075: Azure OpenAI model selection triggers error/crashing when endpoint URL is left empty

#### Describe the bug/problem
When selecting Azure OpenAI AI model in the application and leaving the URL endpoint field empty, the app throws an uncaught empty URI error. This error is not handled gracefully and results in the application crashing inside VS Code.

The crash occurs upon saving the configuration and sending the first request, without any user-facing validation message or fallback behavior. Ideally, the application should either prevent saving or sending a request when the endpoint is empty or display a clear validation error instead of terminating unexpectedly.

#### Steps to Reproduce the bug/problem
Video Added to recreate the issue

https://github.com/user-attachments/assets/1f6927e3-2e83-49b3-b319-444f7cedc3af

#### Expected behavior
The application should validate the configuration before saving or sending a request. If the endpoint URL is empty, it should either throw a clear, user-facing error or display a warning indicating that the **endpoint cannot be empty**, rather than crashing the application.

#### Device Info (The device where you encountered this issue)
 - OS: Windows
 - Version: Windows 11 25H2

#### Flutter Doctor
Please run the `flutter doctor -v` command and provide the details below:

```
PS C:\Users\rishi\apidash> flutter doctor -v
[√] Flutter (Channel stable, 3.38.9, on Microsoft Windows [Version
    10.0.26200.7840], locale en-IN) [612ms]
    • Flutter version 3.38.9 on channel stable at C:\Users\rishi\Flutter\flutter
    • Upstream repository https://github.com/flutter/flutter.git
    • Framework revision 67323de285 (3 weeks ago), 2026-01-28 13:43:12 -0800
    • Engine revision 587c18f873
    • Dart version 3.10.8
    • DevTools version 2.51.1
    • Feature flags: enable-web, enable-linux-desktop, enable-macos-desktop,    
      enable-windows-desktop, enable-android, enable-ios, cli-animations,       
      enable-native-assets, omit-legacy-version-file, enable-lldb-debugging     

[√] Windows Version (11 Home Single Language 64-bit, 25H2, 2009) [1,622ms]

[√] Android toolchain - develop for Android devices (Android SDK version 35.0.0)
    [6.1s]
    • Android SDK at C:\Users\rishi\AppData\Local\Android\sdk
    • Emulator version 35.2.10.0 (build_id 12414864) (CL:N/A)
    • Platform android-36, build-tools 35.0.0
    • Java binary at: C:\Users\rishi\java\17.0.13+11\bin\java
      This JDK is specified in your Flutter configuration.
      To change the current JDK, run: `flutter config --jdk-dir="path/to/jdk"`. 
    • Java version OpenJDK Runtime Environment Temurin-17.0.13+11 (build        
      17.0.13+11)
    • All Android licenses accepted.

[√] Chrome - develop for the web [334ms]
    • Chrome at C:\Program Files\Google\Chrome\Application\chrome.exe

[√] Visual Studio - develop Windows apps (Visual Studio Build Tools 2022
    17.14.7) [333ms]
    • Visual Studio at C:\Program Files (x86)\Microsoft Visual
      Studio\2022\BuildTools
    • Visual Studio Build Tools 2022 version 17.14.36221.1
    • Wi

*[truncated]*

---

## #1059: Windows SmartScreen blocks app causing HandshakeException on first run

#### Describe the bug/problem
After fresh installation on Windows, the app is blocked by Windows Defender SmartScreen 
due to "Unknown publisher". Even after bypassing the warning and running the app, 
all HTTP requests fail with `HandshakeException: Connection terminated during handshake`.

#### Steps to Reproduce the bug/problem
1. Download and install API Dash on Windows (fresh install)
2. Windows SmartScreen shows warning: "Unknown publisher"
3. Click "Run anyway" to bypass the warning
4. Create a simple GET request to `https://jsonplaceholder.typicode.com/todos/1`
5. Click "Send"
6. Error appears: `HandshakeException: Connection terminated during handshake`

#### Expected behavior
The request should complete successfully and return the JSON response.

#### Device Info
 - OS: Windows 
 - Version: Windows 11 Pro
 - API Dash Version: 0.3.0

#### Screenshots

<img width="1823" height="870" alt="Image" src="https://github.com/user-attachments/assets/88d7d9e1-c7d7-4a89-b2e9-5a3704f3de4c" />

<img width="1909" height="980" alt="Image" src="https://github.com/user-attachments/assets/310f6819-f82b-4c15-bdf9-24d849caccd5" />

#### Additional Context
- The same URL works perfectly in web browsers (Chrome/Edge)
- Downloaded pre-built Windows executable from official website
- **Tried running as Administrator - issue persists**
- Issue occurs immediately on fresh installation
- No workarounds found yet
- Issue appears to be related to Windows restricting network access for unsigned applications

#### Flutter Doctor
```
[√] Flutter (Channel stable, 3.35.3, on Microsoft Windows [Version 10.0.26200.7623], locale en-US)
    • Flutter version 3.35.3 on channel stable at C:\src\flutter
    • Upstream repository https://github.com/flutter/flutter.git
    • Framework revision a402d9a437 (5 months ago), 2025-09-03 14:54:31 -0700
    • Engine revision ddf47dd3ff
    • Dart version 3.9.2
    • DevTools version 2.48.0

[√] Windows Version (11 Pro 64-bit, 25H2, 2009)

[!] Android toolchain - develop for Android devices (Android SDK version 36.1.0)
    • Android SDK at E:\android\Sdk
    • Platform android-36, build-tools 36.1.0
    • Java version OpenJDK Runtime Environment (build 21.0.8+-14196175-b1038.72)
    ! Some Android licenses not accepted.

[√] Chrome - develop for the web
    • Chrome at C:\Program Files\Google\Chrome\Application\chrome.exe

[X] Visual Studio - develop Windows apps
    X Visual Studio not installed

[√] Android Studio (version 2025.2.3)
    • Android Studio at E:\android_dev
    • Java version OpenJDK Runtime Environment (build 21.0.8+-14196175-b1038.72)

[√] VS Code (version unknown)
    • VS Code at C:\Users\[username]\AppData\Local\Programs\Microsoft VS Code
    • Flutter extension version 3.128.0
    X Unable to determine VS Code version.

[√] Connected device (3 available)
    • Windows (desktop) • windows • windows-x64    • Microsoft Windows [Version 10.0.26200.7623]
    • Chrome (web)      • chrome  • web-javascript • Google Chrome 1

*[truncated]*

---

## #1032: Add URL request history with autocomplete in request editor

#### Tell us about the task you want to perform and are unable to do so because the feature is not available

While working with APIs, the same request URLs are often reused multiple times during development and testing. Currently, API Dash requires retyping or manually copying previously used URLs each time, which can slow down workflows and become repetitive, especially when switching between multiple endpoints.

#### Describe the solution/feature you'd like us to add

Add URL request memory with autocomplete in the request editor.  
When a user starts typing in the URL field, API Dash should suggest URLs from previously successful requests. This would help reduce repetitive typing, speed up request creation, and improve the overall developer experience.

The feature can initially be scoped to URL autocomplete only, with the possibility to extend later to other request fields if needed.

#### Any other feedback you would like to provide regarding the site

This would be a useful developer-experience improvement and aligns well with common patterns in API testing tools.

---

## #1027: Timeout Support for API Requests

### Tell us about the task you want to perform and are unable to do so because the feature is not available

When testing APIs that return responses after a delay (for example:  
`https://httpstat.us/200?sleep=15000`), API Dash fails with a low-level `ClientException` without providing any control over how long the request should wait or a clear indication that the failure was due to a timeout.

Currently:

- There is no way to configure a request timeout duration.
- Slow but valid APIs may be interpreted as failed requests.
- The error message shown is technical and not clearly associated with a timeout.
- There is no option to cancel an in-progress request.

This makes it difficult to reliably test APIs that legitimately require more time to respond.

---

###  Describe the solution/feature you'd like us to add

Introduce request timeout handling with the following behavior:

- A global default timeout value configurable in settings.
- An optional per-request override when required.
- A clear timeout message such as:  
  > "Request timed out after X seconds."
- Optional ability to cancel an ongoing request.

The default timeout can remain at a sensible value so that existing workflows are not affected unless users choose to modify it.

---

### Any other feedback you would like to provide regarding the site

API Dash already provides a clean and intuitive API testing experience. Adding proper timeout handling would significantly improve reliability and clarity when working with slow or unpredictable APIs.

I would appreciate hearing the maintainers’ thoughts on whether this aligns with the project roadmap before exploring implementation.

---

## #995: Web support for API Dash

#### Tell us about the task you want to perform and are unable to do so because the feature is not available
Currently, API Dash cannot be accessed or explored from the web. This makes it harder for new users to quickly try the tool, understand the workflow, or build sample requests without installing the desktop or mobile app upfront.
Additionally, API testing from a browser is constrained by CORS, which prevents certain requests from being executed reliably in a pure web environment.

#### Describe the solution/feature you'd like us to add
Findings:

1. Proxy-based web support:

A managed proxy or a user-hosted proxy can enable full request execution from the web, offering functionality closer to desktop parity. This approach provides maximum capability but introduces additional considerations around infrastructure, configuration, and maintenance.

2. Web-to-desktop handoff approach

The web client focuses on request creation and organization. When a request cannot be executed due to CORS: 
- The failure is detected in the web client
- Users are offered a fallback to the desktop app via deeplinks or firstly download the app.

#### Any other feedback you would like to provide regarding the site
Looking for guidance on the preferred direction.

---

## #969: RenderFlex overflow while selecting model provider on mobile screens

#### Describe the bug/problem
A `RenderFlex overflow` error occurs in the AI Model Selector Dialog on mobile-width screens. The specific error "RenderFlex overflowed by 80 pixels on the right" is caused by the content within the [AIModelSelectorDialog](cci:2://file:///c:/Users/aman0/OneDrive/Desktop/apidash_contri/apidash/lib/screens/common_widgets/ai/ai_model_selector_dialog.dart:7:0-14:1) (specifically the "Select Model Provider" row) being too wide for the screen.

#### Steps to Reproduce the bug/problem
1. Run the app on a mobile device or resize the window to a mobile width (< 600px).
2. Open the AI pane (select an AI request).
3. Click on the "Select Model" button to open the [AIModelSelectorDialog](cci:2://file:///c:/Users/aman0/OneDrive/Desktop/apidash_contri/apidash/lib/screens/common_widgets/ai/ai_model_selector_dialog.dart:7:0-14:1).
4. Observe the `RenderFlex overflow` error indicated by the yellow/black stripes on the right side of the dialog content.

#### Expected behavior
The content within the [AIModelSelectorDialog](cci:2://file:///c:/Users/aman0/OneDrive/Desktop/apidash_contri/apidash/lib/screens/common_widgets/ai/ai_model_selector_dialog.dart:7:0-14:1), particularly the dropdown, should wrap or stack vertically on smaller screens to fit within the viewport without overflowing.

#### Device Info (The device where you encountered this issue)
 - **OS**: Windows (tested with window resizing to simulate mobile)
 - **Version**: Windows 11
 
#### Attached image
<img src="https://github.com/user-attachments/assets/6639bdd4-8c72-4905-ba22-4981e57cbb6c" width="300">

#### Attached video

https://github.com/user-attachments/assets/4334b46a-65c9-4d8e-9510-cbf6cf133eeb

---

## #964: Shared Community Collections

#### Tell us about the task you want to perform and are unable to do so because the feature is not available

Currently, the API dashboard does not support collaboration on a single API collection. When multiple developers or community members want to work together, each person must create their own collection or manually sync changes.so because of this there are few issue's

- Duplicate collections
- Outdated or inconsistent requests
- No clear ownership or review process

#### Describe the solution/feature you'd like us to add
the solution is to Introduce Shared Community Collections, allowing multiple users to collaborate on the same API collection without duplication .A community (or organization/team) should be able to own a collection and manage contributors within it

**workflow**:-

1. A community or organization creates a shared API collection
2. Members are invited to the collection with specific roles
3. Contributors can work on the same collection simultaneously
4. Maintainers review and approve changes
5. Approved updates are merged into the main collection

**roles/permissions**:-

- Owner / Admin:-Manage members & permissions, Approve or reject changes
- Editor:-Create, update, and delete requests
-Reviewer:-Comment on requests

#### Any other feedback you would like to provide regarding the site
rest everything is good

---

## #962: Code Generation for AI API Calls

#### Tell us about the task you want to perform and are unable to do so because the feature is not available
Code Generation for AI API calls not implemented yet.

#### Describe the solution/feature you'd like us to add
As discussed in community, the code generation for AI based calls should be done through DashBot code generation flow.

---

## #955: Added formatting option to AI answer tab

#### Tell us about the task you want to perform and are unable to do so because the feature is not available
When using AI request mode, the AI responds in markdown format (.md). However, in the Answer tab of the response page, the markdown content is displayed as raw unformatted text, making it difficult to read headers, bold text, lists, code blocks, and other markdown elements.

#### Describe the solution/feature you'd like us to add
Add a "**Format Markdown**" checkbox toggle in the Answer tab that allows users to:

1. Enable formatting: Render the AI response with proper markdown formatting (headers, bold, italics, lists, code blocks, etc.)
2. Disable formatting: Display the raw unformatted markdown text (current behavior)


#### Any other feedback you would like to provide regarding the site
This feature would significantly improve the user experience when working with AI-powered API requests, as AI responses typically contain structured markdown content that benefits from proper rendering.

**without formatting**

<img width="1119" height="1320" alt="Image" src="https://github.com/user-attachments/assets/b8ebaa84-bcad-48f2-bbbd-3af0c881e6ee" />

**with formatting**

<img width="1121" height="1299" alt="Image" src="https://github.com/user-attachments/assets/17a33e4b-8f36-40e9-a997-f56aa68eec71" />

**with code block**

<img width="1112" height="1231" alt="Image" src="https://github.com/user-attachments/assets/143d6aee-ceb4-4e06-8923-67f45416e363" />

---

## #953: Auto-parse curl command when pasted into URL field

#### Tell us about the task you want to perform and are unable to do so because the feature is not available

When working with APIs, I often have curl commands available (from backend teams, docs, or logs). While API Dash has curl parsing through the import dialog, pasting directly into the URL field treats it as plain text. It would be faster if pasting a curl command into the URL field automatically detected and parsed it, populating all request fields instantly,similar to Postman's behaviour.

This makes importing existing curl commands time-consuming and error-prone compared to tools like Postman.

#### Describe the solution/feature you'd like us to add

Add automatic curl command parsing when a user pastes a curl command into the URL field.

When a curl command is detected on paste:
- Parse the curl using the existing CurlIO parser
- Automatically populate request method, URL, headers, query parameters, body, and form data
- Replace the URL text field content with only the parsed URL (not the full curl command)
- Show a user-friendly error message if the curl command is invalid

This behavior should be limited to REST API requests and should not trigger during normal typing.

#### Any other feedback you would like to provide regarding the site

This feature would significantly improve developer experience and bring API Dash closer to the
workflow users expect from modern API clients like Postman, especially for quickly importing
existing requests.

---

## #944: Add swipe gesture navigation for request editor tabs

**Labels:** priority: low

#### Tell us about the task you want to perform and are unable to do so because the feature is not available

Currently, when working in the request editor tabs (Params, Auth, Headers, Body, Scripts), users can only navigate between tabs by clicking on the tab labels at the top. This requires moving the cursor/mouse to the tab bar, which is a bit irritating to me, especially when working on mobile devices. 

I've worked on this already and implemented this

#### Describe the solution/feature you'd like us to add

Add horizontal swipe gesture(2 fingers on laptop) support to switch between tabs in the request pane. The behavior should be:

- **Swipe Right** : Navigate to the **next** tab
  - Example: From "Auth" tab, swipe right → goes to "Headers" tab
  
- **Swipe Left** : Navigate to the **previous** tab

The implementation should:
- Only detect intentional swipes via 2 fingers (using distance/velocity thresholds to avoid accidental tab switches)
- Respect tab boundaries (no navigation beyond first or last tab)
- Not interfere with vertical scrolling within tab content 
- Provide smooth animation when switching tabs

#### Any other feedback you would like to provide regarding the site
We'll have to work on the UI/UX, i'll simultaneously be exploring the entire codebase and checkout for more technical changes.

---

## #942: Empty text of Select model button when no model is chosen.

#### Describe the bug/problem
When selecting AI model, if user choses the model from the options of Ollama, OpenAI, Anthropic, Gemini, Azure OpenAI but not the exact model, the Select button displays empty text.

#### Expected behavior
It should continue to show Select Model text.

#### Device Info (The device where you encountered this issue)
 - OS: Windows
 - Version: Windows 11 22H2

<img width="1500" height="606" alt="Image" src="https://github.com/user-attachments/assets/807b074e-55a9-4136-8ae1-d9e751d0c331" />

---

## #938: macOS traffic light icons overlap the sidebar border in the Dashboard view

**Labels:** triage required

#### Describe the bug/problem
macOS traffic light icons (close, minimize, maximize) overlap with the sidebar navigation icons in the Dashboard view. The traffic lights appear on top of the "Requests" icon and label, making the sidebar content partially obscured.

#### Steps to Reproduce the bug/problem

1. Launch API Dash on macOS
2. Observe the top-left corner of the application window
3. Notice that the traffic light icons (red, yellow, green) overlap with the sidebar navigation icons
<img width="1582" height="1034" alt="Image" src="https://github.com/user-attachments/assets/8a1f28d7-fb70-49e8-9e4a-e4ca1fb990c6" />

### Expected behavior
The right border of the sidebar should be positioned to the right of the macOS traffic light icons, with sufficient spacing to avoid any visual overlap.

#### Device Info (The device where you encountered this issue)
 - OS: macOS
 - Version: Tahoe 26.1
 - Browser: N/A (Desktop app)

#### Flutter Doctor

```
[✓] Flutter (Channel stable, 3.35.1, on macOS 26.1 25B78 darwin-arm64, locale en-US)
    [1,029ms]
    • Flutter version 3.35.1 on channel stable at
      /Users/abhinavkumarchoudhary/flutter
    • Upstream repository https://github.com/flutter/flutter.git
    • Framework revision 20f8274939 (4 months ago), 2025-08-14 10:53:09 -0700
    • Engine revision 1e9a811bf8
    • Dart version 3.9.0
    • DevTools version 2.48.0
    • Feature flags: enable-web, enable-linux-desktop, enable-macos-desktop,
      enable-windows-desktop, enable-android, enable-ios, cli-animations,
      enable-lldb-debugging

[✓] Android toolchain - develop for Android devices (Android SDK version 36.0.0)
    [2.5s]
    • Android SDK at /Users/abhinavkumarchoudhary/Library/Android/sdk
    • Emulator version 36.1.9.0 (build_id 13823996) (CL:N/A)
    • Platform android-36, build-tools 36.0.0
    • Java binary at: /Applications/Android
      Studio.app/Contents/jbr/Contents/Home/bin/java
      This is the JDK bundled with the latest Android Studio installation on this
      machine.
      To manually set the JDK path, use: `flutter config --jdk-dir="path/to/jdk"`.
    • Java version OpenJDK Runtime Environment (build 21.0.6+-13391695-b895.109)
    • All Android licenses accepted.

[✓] Xcode - develop for iOS and macOS (Xcode 26.1.1) [1,642ms]
    • Xcode at /Applications/Xcode.app/Contents/Developer
    • Build 17B100
    • CocoaPods version 1.16.2

[✓] Chrome - develop for the web [6ms]
    • CHROME_EXECUTABLE = /Applications/Brave Browser.app/Contents/MacOS/Brave
      Browser

[✓] Android Studio (version 2025.1) [6ms]
    • Android Studio at /Applications/Android Studio.app/Contents
    • Flutter plugin can be installed from:
      🔨 https://plugins.jetbrains.com/plugin/9212-flutter
    • Dart plugin can be installed from:
      🔨 https://plugins.jetbrains.com/plugin/6351-dart
    • Java version OpenJDK Runtime Environment (build 21.0.6+-13391695-b895.109)

[✓] VS Code (version 1.107.0) [5ms]
    • VS Code at /Applications/Visual Studio C

*[truncated]*

---

## #881: Ability to inherit auth credentials

#### Tell us about the task you want to perform and are unable to do so because the feature is not available
Currently, we have ability to add auth credentials but it only applies to per request.

#### Describe the solution/feature you'd like us to add
We need to have some way to inherit auth credentials, either on the basis of environment or creating generic credentials which can be then used in multiple requests.

#### Any other feedback you would like to provide regarding the site
This feature is similar to other api testing clients like postman and insomnia

---

## #879: Importing postman collection doesn't respect folder structure

#### Describe the bug/problem
When trying to import postman v2.1 collection into apidash, the individual requests are imported without the folder hierarchy present in the import file. Thus, causing issues with properly organizing the api request definitions.

#### Steps to Reproduce the bug/problem
- Export a postman v2.1 collection with multiple api requests neatly grouped with folder hierarchy.
- Import the collection into apidash, you wouls notice, the requests get imported successfully without retaining the original folder hierarchy.

#### Expected behavior
- Folders should also get created when importing the collection.

#### Device Info (The device where you encountered this issue)
 - OS: Android, MacOS; but should be reproducible on all platforms.
 - Version: v0.5.0 built locally from main branch
 - Browser: NA

#### Flutter Doctor
Please run the `flutter doctor -v` command and provide the details below:

```
❯ flutter doctor -v                
[✓] Flutter (Channel stable, 3.35.2, on macOS 15.6.1 24G90 darwin-arm64, locale en-US) [579ms]
    • Flutter version 3.35.2 on channel stable at /opt/homebrew/Caskroom/flutter/3.29.1/flutter
    • Upstream repository https://github.com/flutter/flutter.git
    • Framework revision 05db968908 (3 days ago), 2025-08-25 10:21:35 -0700
    • Engine revision a8bfdfc394
    • Dart version 3.9.0
    • DevTools version 2.48.0
    • Feature flags: enable-web, enable-linux-desktop, enable-macos-desktop, enable-windows-desktop, enable-android, enable-ios,
      cli-animations, enable-lldb-debugging

[✓] Android toolchain - develop for Android devices (Android SDK version 36.0.0) [1,339ms]
    • Android SDK at /opt/homebrew/Cellar/android-sdk
    • Emulator version 35.6.11.0 (build_id 13610412) (CL:N/A)
    • Platform android-36, build-tools 36.0.0
    • ANDROID_HOME = /opt/homebrew/Cellar/android-sdk/
    • ANDROID_SDK_ROOT = /opt/homebrew/Cellar/android-sdk/
    • Java binary at: /Library/Java/JavaVirtualMachines/temurin-17.jdk/Contents/Home/bin/java
      This JDK is specified in your Flutter configuration.
      To change the current JDK, run: `flutter config --jdk-dir="path/to/jdk"`.
    • Java version OpenJDK Runtime Environment Temurin-17.0.16+8 (build 17.0.16+8)
    • All Android licenses accepted.

[✓] Xcode - develop for iOS and macOS (Xcode 16.4) [1,095ms]
    • Xcode at /Applications/Xcode.app/Contents/Developer
    • Build 16F6
    • CocoaPods version 1.16.2

[✓] Chrome - develop for the web [8ms]
    • CHROME_EXECUTABLE = /Applications/Chromium.app/Contents/MacOS/Chromium

[✓] Android Studio (version 2025.1) [7ms]
    • Android Studio at /Applications/Android Studio.app/Contents
    • Flutter plugin can be installed from:
      🔨 https://plugins.jetbrains.com/plugin/9212-flutter
    • Dart plugin can be installed from:
      🔨 https://plugins.jetbrains.com/plugin/6351-dart
    • Java version OpenJDK Runtime Environment (build 21.0.6+-13391695-b895.109)

[✓] Connected device (3 available) [6.4s]
    

*[truncated]*

---

## #873: SSE - Raw response doesn't show all entries

**Labels:** APP: BUG

#### Describe the bug/problem
SSE - Raw Response doesn't show all the entries

#### Steps to Reproduce the bug/problem
https://github.com/user-attachments/assets/12c6662e-baa7-44ab-beb5-4c2d98b6309b

#### Device Info (The device where you encountered this issue)
 - OS: Windows
 - Version: Windows 11 22H2

---

## #848: Switching to a different screen does not stop the background tasks from the previous screen

**Labels:** APP: BUG

#### Describe the bug/problem
In the History Screen if the requests that contain the video preview response are in the `play` state (initial state is 'play' and is being looped). Switching over to a different screen, keeps that request in the `play` state. The video is played in the background. 

#### Steps to Reproduce the bug/problem
* Make a request that has a video preview response.
eg: make a GET request by pasting this in the https://flutter.github.io/assets-for-api-docs/assets/videos/bee.mp4 url
* Restart flutter app
* Switch to the history tab
* Select the request which has the video preview response
* Make sure it is currently on the playing state
* Switch to any other tab.
* If the video has sound you are able to identify the video is playing in background. You can also check the logs in console that also shows the video rendering logs being run

#### Expected behavior
When switching to a different tab in the navigation rail, `not active` screen should not have any background running tasks

#### Device Info (The device where you encountered this issue)
 - OS: [e.g. Windows, MacOS] Windows
 - Version: [e.g. Catalina 10.15.7, Monterey 12.3.1, Windows 11 22H2] Windows 11 22H2
 - Browser (only if you encountered the issue while running the web app): [e.g. chrome, safari]

---

## #826: Textfields should become multiline when tapped on or when the user is editing

#### Tell us about the task you want to perform and are unable to do so because the feature is not available

URL params or header values can be quite long some times (like bearer token values).
Instead of horizontally scrolling through the field (to verify due to the fear of missing out something) , life will become much easier if the value wraps across multiple lines and one can easily view the full text and edit it.

Example below:

<img width="819" alt="Image" src="https://github.com/user-attachments/assets/4193d692-ffd0-46a1-89d5-66af8100df22" />

---

## #825: [Mobile] Difficulty in Navigating URL Field for longer URLs

#### Tell us about the task you want to perform and are unable to do so because the feature is not available

In mobile, when the user wants to edit a long url. Navigating, selecting, scrolling the cursor is quite painful.
UX improvement is required in this regards. 

The floor is open to ideas below👇

---

## #824: [Mobile] Making copying values (like tokens) from JSON previewer easy for end users

#### Tell us about the task you want to perform and are unable to do so because the feature is not available

Related Desktop issue #638 

There should be a one click solution to easily copy values (like token values) to clipboard from JSON previewer for mobile users.
Currently, for desktop users there is a copy button which appears on hover, but no such provision is available for mobile/tablet.

---

## #823: Mobile Usability improvements

Meta issue to track issues required to be solved to improve mobile user experience.

---

## #773: Support various importers and exporters

**Labels:** enhancement

Meta-issue to track support for various importers and exporters

---

## #772: Supporting various API Types

**Labels:** enhancement

Meta-issue to track support for various API Types

---

## #771: Enhance API Dash Request Body

**Labels:** enhancement

A meta-issue to track various enhancements required for Request body of REST API Type

---

## #646: Errors Encountered During Flutter Tests

**Labels:** DEV: BUG

#### Describe the bug/problem
When running `flutter test`, the following errors are encountered:

1. **Pending Timer Error**
   - **Exception:**
     ```
     ═╡ EXCEPTION CAUGHT BY FLUTTER TEST FRAMEWORK ╞═════
     The following assertion was thrown running a test:
     A Timer is still pending even after the widget tree was disposed.
     'package:flutter_test/src/binding.dart':
     Failed assertion: line 1606 pos 12: '!timersPending'
     ```
   - **Possible Cause:**  
     A timer remains active after the widget tree has been disposed.

2. **Late Initialization Error**
   - **Exception:**
     ```
     ═╡ EXCEPTION CAUGHT BY WIDGETS LIBRARY ╞═
     The following LateError was thrown while finalizing the widget tree:
     LateInitializationError: Field '_videoController@28198544' has not been initialized.
     ```
   - **Possible Cause:**  
     The `_videoController` field is not properly initialized before usage, leading to this error during widget disposal.

#### Steps to Reproduce the bug/problem
1. Open the project in a preferred IDE (e.g., VS Code, Android Studio).
2. Run the command:
flutter test

#### Expected behavior
The tests should pass successfully without encountering Pending Timer or LateInitializationError issues.

#### Device Info (The device where you encountered this issue)
 - OS: Ubuntu 24.04.1 LTS

#### Additional Notes
- I discussed this with a experienced flutter dev and he concluded that the latetimer error is related to the video_player package (version 2.9.3) Not the project Codebase
- The late initialization error might indicate that _videoController should be initialized earlier in the widget -lifecycle

---

## #638: Make copying just the values from JSON rendered view possible

#### Tell us about the task you want to perform and are unable to do so because the feature is not available
I do a little login to my api, like this:

![Image](https://github.com/user-attachments/assets/bc0bc089-4b7b-49d1-9191-1f9a0672851e)

and get a token. This token i want on my clipboard obviously. Now I can't select the text to copy it, so i have to use the little copy button, which would be fine if it didnt also copy the json structure around it. When i press the little copy button i get this:

```
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJwaWQiOiJiOTFmNWZhYS05NWYzLTQ1ZDUtYmM1ZC1kMjcxNjg3NGQ0NmUiLCJleHAiOjE3NDE3ODMwNzAsImNsYWltcyI6bnVsbH0.Okfmc52W6vZzl74-Y5hxLPVefhFatdkzs3pHgEcUc1tG1RTKc2v7quV2nwoEAy-1AVme-Run3698MuX_9yc7QQ"
}
```

#### Describe the solution/feature you'd like us to add

Either make the text selectable in the rendered json view, or make the copy button give me the value of the key in the json, not a new json object with just that key.

#### Any other feedback you would like to provide regarding the site

I like the app, keep it up

---

## #627: Fix video player crash

**Labels:** priority: high, triage required

#### Describe the bug/problem

Launch API Dash

Paste the following URL in GET Request:
https://flutter.github.io/assets-for-api-docs/assets/videos/bee.mp4

Hit `Send`

Once the response is received, the App crashes due to some error in VideoPreviewer - https://github.com/foss42/apidash/blob/main/lib/widgets/video_previewer.dart

This issue requires analysis of the root cause of the crash & potential fix.

Setup - Apple M1 (Sonoma 14.6.1)

```
% flutter doctor -v
[✓] Flutter (Channel stable, 3.29.0, on macOS 14.6.1 23G93 darwin-arm64, locale en-IN) [271ms]
    • Flutter version 3.29.0 on channel stable at /Users/ap/Documents/flutter
    • Upstream repository https://github.com/flutter/flutter.git
    • Framework revision 35c388afb5 (3 weeks ago), 2025-02-10 12:48:41 -0800
    • Engine revision f73bfc4522
    • Dart version 3.7.0
    • DevTools version 2.42.2

[✓] Android toolchain - develop for Android devices (Android SDK version 35.0.0) [1,143ms]
    • Android SDK at /Users/ap/Library/Android/sdk
    • Platform android-35, build-tools 35.0.0
    • Java binary at: /Applications/Android Studio.app/Contents/jbr/Contents/Home/bin/java
      This is the JDK bundled with the latest Android Studio installation on this machine.
      To manually set the JDK path, use: `flutter config --jdk-dir="path/to/jdk"`.
    • Java version OpenJDK Runtime Environment (build 17.0.11+0-17.0.11b1207.24-11852314)
    • All Android licenses accepted.

[✓] Xcode - develop for iOS and macOS (Xcode 15.4) [603ms]
    • Xcode at /Applications/Xcode.app/Contents/Developer
    • Build 15F31d
    • CocoaPods version 1.16.2

[✓] Chrome - develop for the web [28ms]
    • Chrome at /Applications/Google Chrome.app/Contents/MacOS/Google Chrome

[✓] Android Studio (version 2024.1) [28ms]
    • Android Studio at /Applications/Android Studio.app/Contents
    • Flutter plugin can be installed from:
      🔨 https://plugins.jetbrains.com/plugin/9212-flutter
    • Dart plugin can be installed from:
      🔨 https://plugins.jetbrains.com/plugin/6351-dart
    • Java version OpenJDK Runtime Environment (build 17.0.11+0-17.0.11b1207.24-11852314)

[✓] IntelliJ IDEA Community Edition (version 2023.1.2) [27ms]
    • IntelliJ at /Applications/IntelliJ IDEA CE.app
    • Flutter plugin can be installed from:
      🔨 https://plugins.jetbrains.com/plugin/9212-flutter
    • Dart plugin can be installed from:
      🔨 https://plugins.jetbrains.com/plugin/6351-dart

[✓] VS Code (version 1.97.2) [9ms]
    • VS Code at /Applications/Visual Studio Code.app/Contents
    • Flutter extension version 3.104.0

[✓] Connected device (3 available) [6.9s]
    • macOS (desktop)                 • macos                 • darwin-arm64   • macOS 14.6.1 23G93 darwin-arm64
    • Mac Designed for iPad (desktop) • mac-designed-for-ipad • darwin         • macOS 14.6.1 23G93 darwin-arm64
    • Chrome (web)                    • chrome                • web-javascript • Google Chrome 133.0.6943.142
or associated
      with the sam

*[truncated]*

---

## #619: API Explorer

#### Tell us about the task you want to perform and are unable to do so because the feature is not available

This project is designed to enhance the API Dash user experience by integrating a curated library of popular and publicly available APIs. This feature allows users to discover, browse, search, and directly import API endpoints into their workspace for seamless testing and exploration. Developers can access pre-configured API request templates, complete with authentication details, sample payloads, and expected responses. This eliminates the need to manually set up API requests, reducing onboarding time and improving efficiency. APIs spanning various domains—such as AI, finance, weather, and social media—are organized into categories, making it easy for users to find relevant services. You are required to develop the entire process backend in the form of an automation pipeline which parses OpenAPI/HTML files, auto-tag it to relevant category, enrich the data, create templates. You can also add features such as user ratings, reviews, and community contributions (via GitHub) to ensure accurate and up-to-date resources.

---

## #601: Adding color support for environments

#### Tell us about the task you want to perform and are unable to do so because the feature is not available

When a new environment is created it can be assigned a color.
This color can be used to highlight the environment name in the dropdown when the user is switching the environment.

For example, user can assign the color RED for prod env & GREEN for dev env.

---

## #600: Reading environment variables directly from OS environment

#### Tell us about the task you want to perform and are unable to do so because the feature is not available

It would be great if API Dash has the ability to read environment variables from the operating system. This way it can access security credentials (like a password) and other system level variables.

---

## #592: Env. Variable Support for JSON request body

#### Tell us about the task you want to perform and are unable to do so because the feature is not available

Currently, env variable support available for:
- URL
- URL Params
- Headers

Instead of updating the body every time, it would be great if the support can be extended for JSON request body as well.

---

## #591: Env. Variable Support for Text request body

#### Tell us about the task you want to perform and are unable to do so because the feature is not available

Currently, env variable support available for:
- URL
- URL Params
- Headers

Instead of updating the body every time, it would be great if the support can be extended for **text** request body as well.

---

## #590: Add environment variable support in request body

#### Tell us about the task you want to perform and are unable to do so because the feature is not available

Currently, env variable support available for:
- URL
- URL Params
- Headers

Instead of updating the body every time, it would be great if the support can be extended for request body as well.

**This is a meta issue. Adding sub-issues to track the progress for all content types.**

---

## #583: Add validation for JSON request body

#### Tell us about the task you want to perform and are unable to do so because the feature is not available

Currently, validation is missing for JSON request body.

What is JSON validation?

<img width="996" alt="Image" src="https://github.com/user-attachments/assets/9eb33945-3ed3-4e93-9494-f0f09e0d6753" />

From UX point of view, 
- a single line status card below the JSON Text field would be a good idea which will turn red if the JSON is invalid and user can tap/hover on the card to view more details of the error. 
- A more preferred approach is to notify user via the Status bar as mentioned in https://github.com/foss42/apidash/issues/587

Also, the check should be triggered keeping proper debounce time which allows users to finish typing a word or phrase without triggering unnecessary checks.

There is a JSON editor in the repo which has not yet been integrated for request body:
https://github.com/foss42/apidash/blob/main/lib/widgets/editor_json.dart

---

## #576: GraphQL Variables

#### Tell us about the task you want to perform and are unable to do so because the feature is not available
Finding it hard to use the graphql feauture since the query needs to be edited again and again for minor changes in values.

#### Describe the solution/feature you'd like us to add
Introduce a section for graphql variables .  

#### Any other feedback you would like to provide regarding the site

---

## #556: Virus total and windows flagged the Windows .exe file to be malicious!

#### Describe the bug/problem
I recently tried to install the APIDASH application for windows but I have this habit of checking the file for malware on Virus Total, and suprisingly it flagged the .exe file to be malicious. I understand there might be false positives but then too I am afraid and one more thing is we should get to the root why it flagged the .exe in first place!

#### Steps to Reproduce the bug/problem

![Image](https://github.com/user-attachments/assets/1010ed86-2ce2-42bb-bbbd-bdb2cfef06fb)

![Image](https://github.com/user-attachments/assets/e0ab4867-04e0-404f-bf38-e197ea2cd9b5)

#### Expected behavior
A 0 (zero) community score on Virus Total

#### Device Info (The device where you encountered this issue)
 - OS: Windows
 - Version: Windows 11 home

#### Flutter Doctor
NA

---
