# open a new issue for discussion

**Parent:** API Dash — Project Ideas
**Source:** https://github.com/foss42/apidash/issues/new/choose
**Scraped:** 2026-03-10T16:58:40.286575

---

## #1319: feat: show response latency in history sidebar cards

#### Tell us about the task you want to perform and are unable to do so because the feature is not available
When reviewing past API requests in the History tab, I can see the timestamp and status code for each run in the sidebar list, but I cannot quickly compare how long each request took without clicking into each one individually and checking the response pane header. This makes it slow to spot performance regressions or outliers across multiple runs of the same endpoint.


#### Describe the solution/feature you'd like us to add
Show response latency inline on each history sidebar card, alongside the existing timestamp and status code.

Each card in the history run list would display:

<img width="1088" height="449" alt="Image" src="https://github.com/user-attachments/assets/bf88ed3a-a374-4a99-9b30-ae531fe0bb96" />

#### Implementation details:

Add a ```Duration? latency``` field to ```HistoryMetaModel``` so it is stored in the lightweight metadata index (same pattern as ```responseStatus```)
Populate it from the already-measured duration value at request completion time in ```CollectionStateNotifier```
Render it in ```HistoryRequestCard``` between the timestamp and status chip using the existing ```humanizeDuration() ```utility
Gracefully hidden for older history entries that predate this field (null check)
This avoids loading full ```HistoryRequestModel``` records from Hive just to show latency, the meta layer is already designed for exactly this kind of lightweight display data.

---

## #1315: Implement "Add Custom Model" functionality in AI Model Selector

#### Tell us about the task you want to perform and are unable to do so because the feature is not available

In the AI Model Selector dialog, there is no way to add a custom AI model to a provider's model list. The "Add" button next to "Models" is commented out, and the [addNewModel](file:///d:/Projects/apidash/lib/screens/common_widgets/ai/dialog_add_ai_model.dart#6-45) function in [dialog_add_ai_model.dart](file:///d:/Projects/apidash/lib/screens/common_widgets/ai/dialog_add_ai_model.dart) contains a TODO - it collects a model ID and display name via a dialog but discards the result without adding the model.

#### Describe the solution/feature you'd like us to add

- The [addNewModel](file:///d:/Projects/apidash/lib/screens/common_widgets/ai/dialog_add_ai_model.dart#6-45) function should return a [Model](file:///d:/Projects/apidash/packages/genai/lib/models/available_models.dart#60-69) object constructed from the user's input (model ID and display name).
- Input validation: reject empty model IDs; default display name to the model ID if left blank.
- The add button in [ai_model_selector_dialog.dart](file:///d:/Projects/apidash/lib/screens/common_widgets/ai/ai_model_selector_dialog.dart) should be enabled and wired up to append the new model to the currently selected provider's model list, with the UI refreshing immediately.

#### Any other feedback you would like to provide regarding the site

N/A

---

## #1313: [Feature]: Auto-detect API type (REST / GraphQL / AI) from URL

#### Tell us about the task you want to perform and are unable to do so because the feature is not available
When working with different API types in API Dash, I have to manually switch between REST, GraphQL, and AI modes using the API type dropdown every time I paste or type a new URL. This gets repetitive - especially when switching between endpoints frequently. For example, pasting `https://api.openai.com/v1/chat/completions` should obviously be an AI request, and `https://api.example.com/graphql` is clearly GraphQL, but I still have to select the type manually each time.

#### Describe the solution/feature you'd like us to add
Auto-detect the API type from the URL as the user types or pastes it into the URL field, and automatically switch the request mode accordingly. Detection should be based on multiple signals:

GraphQL: URL path contains `/graphql`
AI: URL path matches known AI endpoint patterns (e.g. `/v1/chat/completions`, `/api/generate`), or the host belongs to a known AI provider (OpenAI, Anthropic, Gemini, Groq, etc.), or it's a localhost URL on a common AI server port (11434 for Ollama, 1234 for LM Studio, etc.)
REST: Everything else
Additionally:

The detection should resolve environment variables `({{BASE_URL}}/graphql)` before matching
A settings toggle should allow users to enable/disable this behavior (disabled by default)
The user should always be able to manually override the detected type
Future protocol support: The detection logic is designed to be extensible. When API Dash adds support for additional protocols, the same auto-detection approach can be expanded to cover:

WebSocket: detect `ws://` / `wss://` URL schemes
gRPC: detect common gRPC patterns (e.g. port 50051, `grpc://` scheme, or `.proto`-related paths)
MQTT: detect `mqtt://` / `mqtts://` schemes or known MQTT broker ports (1883, 8883)

#### Any other feedback you would like to provide regarding the site
This would significantly improve the workflow for developers who frequently test across different API types in the same session. It's a small quality-of-life improvement that reduces friction without being intrusive, since the toggle lets users opt out. The extensible design also means it naturally grows as API Dash adds support for more protocols.

---

## #1296: Bug: Dashbot Ollama model Integration: "400 Invalid Request" & Configuration Wiped on Selection

# [Bug Report] Dashbot Ollama Integration: "400 Invalid Request" & Configuration Wiped on Selection

#### Bug/Problem
When using Dashbot and attempting to select or configure an Ollama model (e.g., `qwen 2.5 `), I am encountering a `400 Invalid Request: model is required` API error. 

Additionally, anytime I try to open the selector and pick an Ollama model, my existing custom configurations—specifically the **Custom URL** and **API Key**—are actively wiped out and reset within the UI. This prevents any successful interaction with custom local models since their endpoint parameters disappear before execution.

**Component:** Dashbot / AI Model Selector Dialog (`lib/screens/common_widgets/ai/ai_model_selector_dialog.dart`)

**Suspected Root Cause:**
The core issue appears to stem from how the `AIModelSelectorDialog` handles state changes when a user selects a new AI provider or model from the dropdown.

When the `onChanged` event fires, the logic instantiates a completely **new** `AIRequestModel` object from scratch:

```dart
AIRequestModel newModel = AIRequestModel(
  aiModelProvider: value.provider,
  model: aiModel.name,
);
```

Because it creates a brand new instance, it only evaluates the `aiModelProvider` and the new `model` name. It appears to completely ignore the existing state of the dialog. Consequently, user-defined properties like the `url` and `apiKey` are abandoned and implicitly set to `null` on the new object. 

When this truncated model is eventually passed back down to Dashbot to execute via the `ollama_dart` client, the lack of a proper endpoint URL triggers the `400` errors from the server.

**Console Logs:**
```text
[ChatBubble] Actions count: 0 | msg: hey
[ChatBubble] Actions count: 0 | msg: No response received from the AI.
[ChatBubble] Actions count: 0 | msg: hey
[ChatBubble] Actions count: 0 | msg: No response received from the AI.
LLM_EXCEPTION: 400
{"error":{"message":"model is required","type":"api_error","param":null,"code":null}}
```

**Local Ollama Server Logs:**
```text
[GIN] 2026/03/07 - 08:31:30 | 200 |    2.8718ms | 127.0.0.1 | GET  "/api/ps"
[GIN] 2026/03/07 - 08:32:05 | 400 |   44.3568ms | 127.0.0.1 | POST "/v1/chat/completions"
```

#### Steps to Reproduce the bug/problem
1. Open the **Dashbot** window in API Dash.
2. Click on the **AI Model Selector Button** to open the `AIModelSelectorDialog`.
3. Input a custom URL (e.g., `http://localhost:11434/api/generate`) and a custom API key.
4. Select an Ollama model from the dropdown list.
5. *Observe:* The previously entered URL and API Key fields are instantly cleared.
6. Submit a prompt to Dashbot.
7. *Result:* Dashbot returns a `400: model is required` or similar error because the backend request model appears to have lost its configuration data during the UI state change in step 4.

#### Expected behavior
Selecting an AI Model from the dropdown should preserve the existing inputs in the dialog. The configuration should merge the new `aiModelProvider` and `model

*[truncated]*

---

## #1292: Documentation: Add comprehensive scripting assertions guide with test coverage

## Summary
Add exhaustive documentation guide for API Dash scripting assertions with practical examples and corresponding test suite.

## What was requested
@animator asked to update the user guide to document scripting assertion patterns with working examples and add test files to validate them work correctly.

## Completed work
- ✅ Updated `doc/user_guide/scripting_user_guide.md` with 7 comprehensive examples covering:
  - Status code checks (equals, notEquals, greaterThan, lessThan)
  - Header verification (exists, equals, contains)
  - Performance checks (single response, history tracking)
  - Required field validation
  - Data type checking
  
- ✅ Added `test/providers/scripting_assertions_test.dart` with test coverage for all examples

- ✅ Fixed misleading "Save for tracking" comment in Example 3

## References
Related to #1239 - Feature proposal: MVP assertion checks for API responses

---

## #1283: Typo in Request Body: "answer" displayed as "anwe\nr" (shifted r)

The request body field **`answer`** is incorrectly rendered as **`anwe`**, where the character **`r`** appears below the word instead of being placed correctly at the end. This causes the parameter name to appear malformed in the request body.

---

#### Steps to Reproduce the bug/problem

1. Open the **request body** section where parameters are defined.
2. Locate the field intended to be **`answer`**.
3. Observe that the text appears as **`anwe`**, with the **`r`** positioned below the word instead of inline.

---

#### Expected behavior

The parameter name should appear correctly as **`answer`**, with all characters displayed inline in the correct order.

---

#### Device Info (The device where you encountered this issue)

* **OS:** Windows
* **Version:** Windows 11 (25H2)

---

<img width="1919" height="1079" alt="Image" src="https://github.com/user-attachments/assets/ca31a009-e368-46ee-a8e1-f88688c634d8" />

#### Flutter Doctor

```
Doctor summary (to see all details, run flutter doctor -v):

[√] Flutter (Channel stable, 3.41.4, on Microsoft Windows [Version 10.0.26200.7840], locale en-US)
[√] Windows Version (Windows 11 or higher, 25H2, 2009)

[!] Android toolchain - develop for Android devices (Android SDK version 36.1.0)
    X cmdline-tools component is missing.
      Try installing or updating Android Studio.
      Alternatively, download the tools from:
      https://developer.android.com/studio#command-line-tools-only
      and make sure to set the ANDROID_HOME environment variable.
      See https://developer.android.com/studio/command-line for more details.

    X Android license status unknown.
      Run `flutter doctor --android-licenses` to accept the SDK licenses.
      See https://flutter.dev/to/windows-android-setup for more details.

[√] Chrome - develop for the web
[√] Visual Studio - develop Windows apps (Visual Studio Community 2026 18.0.2)
[√] Connected device (3 available)
[√] Network resources

! Doctor found issues in 1 category.
```

---

## #1276: [Bug] Application crashes when searching in collection pane if AI requests are present

#### Describe the bug/problem
The application crashes when using the filter/search bar in the collection pane if there is an **AI Request** in the collection list. 

This happens because the search logic explicitly calls `item.httpRequestModel!.url`, which throws a "Null check operator used on a null value" error because AI requests have a `null` `httpRequestModel`.

#### Steps to Reproduce the bug/problem
1. Open API Dash.
2. Create a new request and change the **API Type** to **AI Request**.
3. Focus on the **Filter bar** at the top of the collection pane (sidebar).
4. Type any character (e.g., "a").
5. The application crashes immediately.

#### Expected behavior
The search should work without crashing. AI requests should be filtered by their **Name**, while HTTP requests should continue to be filtered by both **Name** and **URL**.

#### Device Info
 - **OS**: Windows 11
 - **Version**: 10.0.26200 Build 26200

#### Flutter Doctor
```text
[!] Flutter (Channel [user-branch], 3.38.7, on Microsoft Windows [Version 10.0.26200.7922], locale en-IN) [359ms]
    ! Flutter version 3.38.7 on channel [user-branch] at D:\dsa\flutter
      Currently on an unknown channel. Run `flutter channel` to switch to an official channel.
      If that doesn't fix the issue, reinstall Flutter by following instructions at https://flutter.dev/setup.
    ! Upstream repository unknown source is not a standard remote.
      Set environment variable "FLUTTER_GIT_URL" to unknown source to dismiss this error.
    • Framework revision 3b62efc2a3 (7 weeks ago), 2026-01-13 13:47:42 -0800
    • Engine revision 78fc3012e4
    • Dart version 3.10.7
    • DevTools version 2.51.1
    • Feature flags: enable-web, enable-linux-desktop, enable-macos-desktop, enable-windows-desktop, enable-android,
      enable-ios, cli-animations, enable-native-assets, omit-legacy-version-file, enable-lldb-debugging
    • If those were intentional, you can disregard the above warnings; however it is recommended to use "git" directly
      to perform update checks and upgrades.

[√] Windows Version (11 Home Single Language 64-bit, 25H2, 2009) [1,019ms]

[√] Android toolchain - develop for Android devices (Android SDK version 36.1.0) [1,987ms]
    • Emulator version 36.2.12.0 (build_id 14214601) (CL:N/A)
    • Platform android-36, build-tools 36.1.0
    • Java binary at: D:\jbr\bin\java
      This is the JDK bundled with the latest Android Studio installation on this machine.
      To manually set the JDK path, use: `flutter config --jdk-dir="path/to/jdk"`.
    • Java version OpenJDK Runtime Environment (build 21.0.8+-14196175-b1038.72)
    • All Android licenses accepted.

[√] Chrome - develop for the web [86ms]
    • Chrome at C:\Program Files\Google\Chrome\Application\chrome.exe

[√] Visual Studio - develop Windows apps (Visual Studio Community 2026 18.3.1) [85ms]
    • Visual Studio at D:\visual studio
    • Visual Studio Community 2026 version 18.3.11512.155
    • Windows 10 SDK version 10.0.26100.0

[

*[truncated]*

---

## #1269: Revamp Model Selector dialog

Meta list to track issues with model selector dialog.
Currently, it needs a complete revamp.

---

## #1264: App crashes with unhandled exception when Infinity value is entered in AI config numeric fields

#### Describe the bug/problem
When a user enters `1e309` (or any value that evaluates to Infinity) 
in a numeric configuration field (e.g., max_tokens / maxOutputTokens) 
for an AI request, the app crashes silently with an unhandled exception. 
No error is shown to the user.

#### Steps to Reproduce the bug/problem
1. Create a new request and set API type to AI
2. Open Model Selector, choose any provider (e.g., Gemini), save
3. Go to the Configurations tab
4. In the max_tokens / maxOutputTokens numeric field, type: 1e309
5. Click Send

Confirmed on multiple providers:
- Gemini: crashes with "Converting object to an encodable object failed: Infinity"
- Anthropic: same crash with anthropic.dart in stack trace
- Azure OpenAI

#### Expected behavior
The app should validate the input and show a clear error message such as 
"Please enter a valid number" — and should not allow Infinity or NaN 
values to be saved or sent.

#### Actual Behavior
The app crashes silently. No feedback is shown to the user.
The following unhandled exception appears in the console:

FormatException: Converting object to an encodable object failed: Infinity
  at GeminiModel.createRequest (genai/interface/model_providers/gemini.dart:46)
  at AIRequestModel.httpRequestModel (genai/models/ai_request_model.dart:29)

#### Stack Trace
[ERROR:flutter/runtime/dart_vm_initializer.cc(40)] Unhandled Exception:
Converting object to an encodable object failed: Infinity
#0      _JsonStringifier.writeObject (dart:convert/json.dart:824:7)
#1      _JsonPrettyPrintMixin.writeMap (dart:convert/json.dart:971:7)
#2      _JsonStringifier.writeJsonValue (dart:convert/json.dart:863:21)
#3      _JsonStringifier.writeObject (dart:convert/json.dart:815:9)
#4      _JsonPrettyPrintMixin.writeMap (dart:convert/json.dart:971:7)
#5      _JsonStringifier.writeJsonValue (dart:convert/json.dart:863:21)
#6      _JsonStringifier.writeObject (dart:convert/json.dart:815:9)
#7      _JsonStringStringifier.printOn (dart:convert/json.dart:1024:17)
#8      _JsonStringStringifier.stringify (dart:convert/json.dart:1005:5)
#9      JsonEncoder.convert (dart:convert/json.dart:353:30)
#10     GeminiModel.createRequest
(package:genai/interface/model_providers/gemini.dart:46:26)
#11     AIRequestModel.httpRequestModel
(package:genai/models/ai_request_model.dart:29:45)
#12     CollectionStateNotifier.sendRequest
(package:apidash/providers/collection_providers.dart:366:49)

#### Device Info (The device where you encountered this issue)
 - OS: Windows 11
- App type: Desktop
- Flutter: 3.41.3

#### Flutter Doctor
Please run the `flutter doctor -v` command and provide the details below:

```
[√] Flutter (Channel stable, 3.41.3, on Microsoft Windows [Version 10.0.26100.7623], locale en-US) [416ms]
    • Flutter version 3.41.3 on channel stable at C:\Users\User\flutter\flutter
    • Upstream repository https://github.com/flutter/flutter.git
    • Framework revision 48c32af034 (5 days ago), 2026-02-27 17:09:06 -0500
    • Engine revisio

*[truncated]*

---

## #1262: Add unit tests for genai agentic engine blueprint and model providers

## Description

The `packages/genai/` package currently lacks test coverage for its core agentic engine blueprint and model provider implementations. While basic utility tests exist (PR #882), the following critical areas remain untested:

### Agentic Engine Blueprint (`lib/agentic_engine/blueprint.dart`)
- `AIAgent` abstract class contract (name, system prompt, validator, output formatter)
- `SystemPromptTemplating` extension (`:variable:` placeholder substitution)
- `AgentInputs` model (query and variables handling)

### Model Providers (`lib/interface/model_providers/`)
- `OpenAIModel` — request creation, bearer auth, streaming, output formatting
- `AnthropicModel` — request creation, API key auth, anthropic-version header, output formatting
- `AzureOpenAIModel` — request creation, api-key header, empty URL validation, output formatting
- `OllamaModel` — inherited OpenAI format, config subset (temperature + top_p only)

Adding tests for these ensures reliability of the AI integration layer and provides a safety net for future MCP-related features that will build on this infrastructure.

---

## #1255: File upload crashes on macOS/iOS due to missing uniformTypeIdentifiers in XTypeGroup in DashBot

#### Describe the bug/problem
When attempting to upload a file using DashBot's ``Import OpenAPI``→ Upload file feature on macOS (Flutter desktop) or iOS, the application crashes with an exception from file_selector_ios.

This occurs because the ``XTypeGroup`` used in the file picker does not include ``uniformTypeIdentifiers``, which are required by file_selector_ios.

#### Steps to Reproduce the bug/problem
- Run ApiDash on macOS/IOS.
- Open DashBot.
- Click Import OpenAPI.
- Choose Upload file.
- Select a file.

The application throws an exception and the file picker fails.

https://github.com/user-attachments/assets/fedc7ba1-4b7e-4530-a0a0-67811495adc6

#### Expected behavior
The file picker should open normally and allow selecting files for upload without crashing.


### Suggested Fix
Add uniformTypeIdentifiers to the XTypeGroup, for example:
``` dart
uniformTypeIdentifiers: const [
  'public.json',
  'public.yaml',
  'public.data',
]
```

#### Device Info (The device where you encountered this issue)
 - OS: [e.g. Windows, MacOS]
 - Version: [e.g. Catalina 10.15.7, Monterey 12.3.1, Windows 11 22H2]
 - Browser (only if you encountered the issue while running the web app): [e.g. chrome, safari]

#### Flutter Doctor
Please run the `flutter doctor -v` command and provide the details below:

```
prajwal@prajwals-MacBook-Air-2 apidash % flutter doctor -v
[!] Flutter (Channel [user-branch], 3.38.7, on macOS 26.2 25C56 darwin-arm64, locale en-US) [490ms]
    ! Flutter version 3.38.7 on channel [user-branch] at /Users/prajwal/flutter_sdk
      Currently on an unknown channel. Run `flutter channel` to switch to an official channel.
      If that doesn't fix the issue, reinstall Flutter by following instructions at https://flutter.dev/setup.
    ! Upstream repository unknown source is not a standard remote.
      Set environment variable "FLUTTER_GIT_URL" to unknown source to dismiss this error.
    • Framework revision 3b62efc2a3 (7 weeks ago), 2026-01-13 13:47:42 -0800
    • Engine revision 78fc3012e4
    • Dart version 3.10.7
    • DevTools version 2.51.1
    • Feature flags: enable-web, enable-linux-desktop, enable-macos-desktop, enable-windows-desktop, enable-android, enable-ios,
      cli-animations, enable-native-assets, omit-legacy-version-file, enable-lldb-debugging
    • If those were intentional, you can disregard the above warnings; however it is recommended to use "git" directly to perform update
      checks and upgrades.

[✓] Xcode - develop for iOS and macOS (Xcode 26.2) [1,174ms]
    • Xcode at /Applications/Xcode.app/Contents/Developer
    • Build 17C52
    • CocoaPods version 1.16.2

[✓] Chrome - develop for the web [7ms]
    • Chrome at /Applications/Google Chrome.app/Contents/MacOS/Google Chrome

[✓] Connected device (3 available) [7.6s]
    • iPhone 16e (mobile) • DA298410-4AFF-464E-AC38-319B380B3B76 • ios            • com.apple.CoreSimulator.SimRuntime.iOS-26-2
      (simulator)
    • macOS (desktop)     • macos                    

*[truncated]*

---

## #1252: OpenAPI import does not populate form fields from schema for multipart/form-data and x-www-form-urlencoded

#### Describe the bug/problem
When importing an openApi specification that has a request body with multipart/form-data or  application/x-www-form-urlencoded with schema containing type:object ,the generated payload sets: 
``form=true``
``Content-Type`` header
but the fields defined under schema.properties are not populated in the formData[].

#### Steps to Reproduce the bug/problem
- Use an OpenAPI 3 specification that defines a requestBody with multipart/form-data or application/x-www-form-urlencoded.
- Ensure the schema defines type: object with properties, for example:
```
       requestBody:
          required: true
          content:
              multipart/form-data:
                 schema:
                     type: object
                     properties:
                          username:
                                type: string
                          avatar:
                                type: string
                                format: binary
```
- Import the OpenAPI specification into ApiDash through DashBot

#### Observed behavior
- form is set to true
- Content-Type header is correctly set
- formData is empty

Added a unit test to validate schema property extraction. The assertion fails because formData remains empty.
<img width="752" height="106" alt="Image" src="https://github.com/user-attachments/assets/a190b003-0c93-427b-a5b9-7d273acb6a52" />

#### Expected behavior
- Each property under schema.properties should be added as a form field.
- Fields with format: binary should be treated as file inputs.
- Other fields should default to text inputs.
```
[
  { "name": "username", "value": "", "type": "text" },
  { "name": "avatar", "value": "", "type": "file" }
]
```

**If this aligns with the intended behavior, I’d be happy to work on a fix and submit a PR.**



#### Flutter Doctor
```
prajwal@prajwals-MacBook-Air-2 apidash % flutter doctor -v
[!] Flutter (Channel [user-branch], 3.38.7, on macOS 26.2 25C56 darwin-arm64, locale en-US) [490ms]
    ! Flutter version 3.38.7 on channel [user-branch] at /Users/prajwal/flutter_sdk
      Currently on an unknown channel. Run `flutter channel` to switch to an official channel.
      If that doesn't fix the issue, reinstall Flutter by following instructions at https://flutter.dev/setup.
    ! Upstream repository unknown source is not a standard remote.
      Set environment variable "FLUTTER_GIT_URL" to unknown source to dismiss this error.
    • Framework revision 3b62efc2a3 (7 weeks ago), 2026-01-13 13:47:42 -0800
    • Engine revision 78fc3012e4
    • Dart version 3.10.7
    • DevTools version 2.51.1
    • Feature flags: enable-web, enable-linux-desktop, enable-macos-desktop, enable-windows-desktop, enable-android, enable-ios,
      cli-animations, enable-native-assets, omit-legacy-version-file, enable-lldb-debugging
    • If those were intentional, you can disregard the above warnings; however it is recommended to use "git" directly to perform update
      checks and upgrades.


*[truncated]*

---

## #1244: Auto-focus URL field when creating a new request

#### Tell us about the task you want to perform and are unable to do so because the feature is not available

When creating a new request using the `+` button, the URL input field is not automatically focused. This requires an additional mouse click before typing the URL.

For users who frequently create new requests, this slightly interrupts the workflow and makes the interaction less keyboard-friendly.

### Screen recording demonstrating current behavior:

[https://github.com/user-attachments/assets/ae2d749c-a966-494e-ad3e-e0ec882166fc](https://github.com/user-attachments/assets/ae2d749c-a966-494e-ad3e-e0ec882166fc)

#### Describe the solution/feature you'd like us to add

After a new request is created:

* The URL input field should automatically receive focus.
* The cursor should be placed inside the URL field so the user can immediately start typing.
* This should only trigger when a new request is added (not when switching between existing requests).

This would improve usability and make request creation faster and more intuitive.

#### Any other feedback you would like to provide regarding the site

This small improvement would make the request creation flow smoother and more aligned with common developer tools, where the primary input field is focused automatically after creating a new item.

---

## #1232: UX improvement : Add JSON Parser and auto format in request body

### Problem
The JSON editor in the API Dash request body currently lacks native parsing and formatting capabilities, requiring manual formatting and increasing the likelihood of syntax errors.

https://github.com/user-attachments/assets/25fdb5ac-4f36-439b-bcb1-1e37af905f2c

### Proposed Solution
* Enable native JSON parsing, syntax validation, and formatting within the request body editor to mirror the VS Code experience.

https://github.com/user-attachments/assets/fc7ae35b-64c5-4dc8-ae58-046a04b6e680

### Benefits
* The user can validates whether the JSON format is correct or not in the text editor
*  It solves the problem of depending on external text editors


### Implementation Ideas
* Integrate a web-compatible JSON parser or Language Server (like in VS-CODE)
* Implement core QoL (Quality of Life) features: auto-closing brackets, smart indentation, and syntax highlighting.

#### I have researched about tools to do it: 
   * [Monaco Editor](https://microsoft.github.io/monaco-editor/)
  * [CodeMirror](https://codemirror.net/)

---

## #1221: Add tests for agentic services

Hi! I'm exploring the codebase for GSoC 2026 (interested in the GSOC Idea – Agentic API Testing) and noticed that the `lib/services/agentic_services/` folder currently has no test coverage.

### Current State
The `lib/services/agentic_services/` directory currently has **zero test coverage**:

- `agent_caller.dart` — no tests
- `lib/services/agentic_services/agents/` — no tests for individual agent classes

### Proposed Solution
Add unit tests for these services, starting with:

- **`APIDashAgentCaller`** — test exception handling when no default AI model is set
- **Individual agent classes** — test `validator` and `outputFormatter` methods

### Why This Matters
-  Ensures agentic features are reliable and regression-proof
-  Provides a foundation for future agentic testing features
-  Follows the testing guidelines outlined in `CONTRIBUTING.md`

### Related Issues / Ideas
- Related to GSoC 2026 Idea #4 — Agentic API Testing
- Related to #96, #100

### Contribution
I've already written a basic test for `agent_caller.dart` and would like to 
contribute it as a starting point.
### Checklist
- [ ] Tests for `APIDashAgentCaller` (exception handling, no default model set)
- [ ] Tests for individual agent `validator` methods
- [ ] Tests for individual agent `outputFormatter` methods
- [ ] Ensure all tests follow ex

---

## #1202: [Feature]: Enable Streaming Responses in Dashbot

## 🚀 Feature Request: Enable Streaming Responses in Dashbot

### Description

Dashbot currently has all the groundwork for streaming AI responses in place, but streaming is never actually used — it is hardcoded to `false`. This means users always wait for the entire AI response to be generated before seeing any output, resulting in a noticeably sluggish experience.

---

### Current Behavior

In `chat_viewmodel.dart:211`, the AI request is always built with `stream: false`:

```dart
final enriched = ai!.copyWith(
  systemPrompt: systemPrompt,
  userPrompt: userPrompt,
  stream: false, // <-- always disabled
);
```

Additionally, `ChatRemoteRepository` only exposes a `sendChat()` method — there is no `streamChat()` counterpart to handle streamed responses.

---

### What Already Exists

The infrastructure for streaming is largely already in place:
- `streamGenAIRequest()` is fully implemented in `ai_request_utils.dart:31` with SSE (Server-Sent Events) parsing.
- The `ChatState` model already has a `currentStreamingResponse` field, indicating streaming was designed for from the start.

This means the heavy lifting is already done — streaming just needs to be wired up.

---

### ⚠️ Key Risk: JSON Parsing During Streaming

Dashbot expects structured JSON responses (`{"explanation": "...", "actions": [...]}`). During streaming, chunks arrive incomplete and can't be parsed mid-stream — naively enabling `stream: true` will cause `FormatException` errors.

**Suggested approaches:**
- **Buffer + parse at end** *(safest)* — accumulate all chunks, parse only once the stream closes. Still improves UX over the current blank wait.
- **Partial extraction** — stream the `explanation` field in real time (it appears first), defer `actions` parsing until stream ends.


---

### Proposed Solution

1. **Add `streamChat()` to `ChatRemoteRepository`** — implement a method that calls `streamGenAIRequest()` and yields chunks as they arrive.
2. **Update `chat_viewmodel.dart`** — set `stream: true` when making a request and listen to the stream, progressively updating `currentStreamingResponse` in `ChatState`.
3. **Update the Dashbot UI** — render `currentStreamingResponse` so tokens appear in real time as they stream in.

---

### Expected Behavior

Users see AI responses being typed out token-by-token in real time, dramatically improving perceived responsiveness — consistent with the experience users expect from modern AI chat interfaces.

---

## #1183: missing validation for empty API key and Endpoint URL in AI Model Selector Dialog

## Problem
The **AI Model Selector dialog** does not check if required fields are filled before saving.

When the user clicks **Save**, it allows saving an AI model even if:
- The **API Key** is empty (for providers other than Ollama)
- The **Endpoint URL** is empty

This results in invalid configurations being saved without any warning.

## Steps to reproduce
1. Open the **AI Model Selector** dialog.
2. Select any AI provider (for example, OpenAI or Gemini).
3. Leave the **API Key / Credential** field empty.
4. Leave the **Endpoint** field empty.
5. Click **Save**.
6. The dialog closes and saves the invalid configuration.

## Expected behavior
When **Save** is clicked:
- If the provider is **not Ollama** and the API key is empty, show a warning (for example: **"API Key is required"**).
- If the **Endpoint URL** is empty, show a warning (for example: **"Endpoint URL is required"**).

The dialog should not close until all required fields are valid.

## Device information
- **OS:** Windows  
- **Version:** Windows 11  
- **App type:** Desktop app

## Flutter Doctor
Run the following command and paste the output:

```bash
[√] Flutter (Channel master, 3.42.0-1.0.pre-290, on Microsoft Windows [Version 10.0.26200.7922], locale en-IN) [3.1s]
    • Flutter version 3.42.0-1.0.pre-290 on channel master at D:\dsa\flutter
    • Upstream repository https://github.com/flutter/flutter.git
    • Framework revision b7ac273fa0 (3 hours ago), 2026-02-26 09:02:27 -0500
    • Engine revision b7ac273fa0
    • Dart version 3.12.0 (build 3.12.0-178.0.dev)
    • DevTools version 2.55.0
    • Feature flags: enable-web, enable-linux-desktop, enable-macos-desktop, enable-windows-desktop, enable-android,
      enable-ios, cli-animations, enable-native-assets, omit-legacy-version-file, enable-lldb-debugging,
      enable-uiscene-migration, enable-riscv64

[√] Windows Version (11 Home Single Language 64-bit, 25H2, 2009) [2.1s]

[√] Android toolchain - develop for Android devices (Android SDK version 36.1.0) [2.3s]
    • Android SDK at C:\Users\prata\AppData\Local\Android\sdk
    • Emulator version 36.2.12.0 (build_id 14214601) (CL:N/A)
    • Platform android-36, build-tools 36.1.0
    • Java binary at: D:\Games\jbr\bin\java
      This is the JDK bundled with the latest Android Studio installation on this machine.
      To manually set the JDK path, use: `flutter config --jdk-dir="path/to/jdk"`.
    • Java version OpenJDK Runtime Environment (build 21.0.8+-14196175-b1038.72)
    • All Android licenses accepted.

[√] Chrome - develop for the web [91ms]
    • Chrome at C:\Program Files\Google\Chrome\Application\chrome.exe

[√] Visual Studio - develop Windows apps (Visual Studio Community 2026 18.3.1) [90ms]
    • Visual Studio at D:\visual studio
    • Visual Studio Community 2026 version 18.3.11512.155
    • Windows 10 SDK version 10.0.26100.0

[√] Connected device (3 available) [394ms]
    • Windows (desktop) • windows • windows-x64    • Microsoft Windows [Version 10.0.26200.79

*[truncated]*

---

## #1182: Disappearing API keys

## API Key Disappears After Selecting AI Provider

### Describe the bug/problem
When an API key is entered and saved, everything works normally. 

However, If an API key is previously inserted and the window is closed, reopening the app and selecting an AI provider causes the API key field to become empty. The key still remains there but the ui misbehaves and displays a blank input box. 

<img width="1512" height="979" alt="Image" src="https://github.com/user-attachments/assets/b6a056df-0dfc-4187-a3fc-70ae7d81f4cd" />
---

### Steps to Reproduce the bug/problem

1. Open Dashbot.
2. Navigate to AI provider/ API key settings.
3. Select an AI provider
4. Enter a valid API key.
5. Click save. 
6. Go back to the AI config tab on Dashbot.
7. Select the AI provider Chosen in Step 3

**Observed Behavior:**  
The previously entered API key disappears (the field becomes empty).

---

### Expected behavior
The API key should persist after being entered and remain populated when:
- The app is reopened.
- An AI provider is selected.
- Switching between providers (if applicable).

The API key should not be cleared out in the UI if previously set

---

### Device Info (The device where you encountered this issue)

- **OS:** macOS  
- **Version:** macOS Tahoe 26.2
- **Browser:** N/A (Desktop app)

---

### Flutter Doctor
[✓] Flutter (Channel stable, 3.41.2, on macOS 26.2 25C56 darwin-arm64, locale en-US) [2.6s]
    • Flutter version 3.41.2 on channel stable at /opt/homebrew/share/flutter
    • Upstream repository https://github.com/flutter/flutter.git
    • Framework revision 90673a4eef (8 days ago), 2026-02-18 13:54:59 -0800
    • Engine revision 6c0baaebf7
    • Dart version 3.11.0
    • DevTools version 2.54.1
    • Feature flags: enable-web, enable-linux-desktop, enable-macos-desktop, enable-windows-desktop, enable-android, enable-ios, cli-animations, enable-native-assets,
      omit-legacy-version-file, enable-lldb-debugging, enable-uiscene-migration

[✗] Android toolchain - develop for Android devices [203ms]
    ✗ Unable to locate Android SDK.
      Install Android Studio from: https://developer.android.com/studio/index.html
      On first launch it will assist you in installing the Android SDK components.
      (or visit https://flutter.dev/to/macos-android-setup for detailed instructions).
      If the Android SDK has been installed to a custom location, please use
      `flutter config --android-sdk` to update to that location.


[✓] Xcode - develop for iOS and macOS (Xcode 26.2) [1,287ms]
    • Xcode at /Applications/Xcode.app/Contents/Developer
    • Build 17C52
    • CocoaPods version 1.16.2

[✓] Chrome - develop for the web [4ms]
    • Chrome at /Applications/Google Chrome.app/Contents/MacOS/Google Chrome

[✓] Connected device (2 available) [9.4s]
    • macOS (desktop) • macos  • darwin-arm64   • macOS 26.2 25C56 darwin-arm64
    • Chrome (web)    • chrome • web-javascript • Google Chrome 145.0.7632.117

[✓] Network resources [988ms]
    • All expe

*[truncated]*

---

## #1180: [Feat] AI-powered smart request suggestions based on URL pattern

Problem :
When a user enters a new API URL in API Dash, they have to manually figure out the correct HTTP method, required headers, body format, and query parameters. This is especially tedious for unfamiliar APIs where the user has to look up documentation externally.

Proposed Feature : 
Add a **"Smart Suggest"** capability to Dashbot that analyzes the entered URL and auto-suggests:

**How It Would Work** ? 
1. User enters a URL in the request editor
2. User clicks a ✨ (sparkle) icon next to the URL field — or triggers "Suggest Request" from Dashbot's task buttons
3. Dashbot sends the URL + any existing request context to the configured AI model with a purpose-built prompt
4. The AI returns structured actions (update_method, add_header, update_body, etc.)
5. The existing AutoFixService pipeline applies the suggestions to the current request — **no new action handling code needed**

**How it would be helpful ?**
1. A new developer testing an API for the first time doesn't know what headers, params, or body format to use. Instead of switching to docs, they enter the URL and hit ✨ — the AI fills in everything they need to get a working request in seconds.
2. Right now, users often hit "Send" with wrong settings, get a 400/415/405 error, then debug manually. Smart suggestions get it right on the first try — correct method, correct Content-Type, correct body shape.
3. New API Dash users see immediate AI-powered value the moment they type a URL. It makes the tool feel intelligent and differentiates it from Postman/Insomnia where you configure everything manually.
4. It's optional — just a button click. Doesn't change the existing workflow. Power users ignore it, _**beginners rely on it.**_

---

## #1175: Support for Custom OpenAI-Compatible LLM Providers (Groq, OpenRouter, Mistral, etc.)

#### Tell us about the task you want to perform and are unable to do so because the feature is not available  
Currently, APIDash only supports specific built-in AI providers, including OpenAI, Anthropic, Gemini, Azure OpenAI, and Ollama, for its GenAI features. I want to use other alternative LLM providers that offer OpenAI-compatible API endpoints, such as OpenRouter, Groq, Mistral, Together AI, and LlamaAPI. Since there is no option to specify a custom endpoint and model identifier, I cannot connect APIDash's AI features to these powerful, often cost-effective or faster alternative models.

#### Describe the solution/feature you'd like us to add  
I would like a **"Custom (OpenAI Compatible)"** option added to the AI Model Selector Dialog. 

When this provider is selected, the dialog should allow the user to provide:  
1. **API Key / Credential:** The API key for the custom provider.  
2. **Endpoint:** The full OpenAI-compatible chat completions URL, for example, `https://api.groq.com/openai/v1/chat/completions` `https://openrouter.ai/api/v1/chat/completions` , `https://api.mistral.ai/v1/chat/completions`.  
3. **Model Name:** A text field to type out the identifier of the specific model to be used, for example, `llama-3.3-70b-versatile`.  

This would use the existing [OpenAIModel]implementation structure under the hood to serialize the request correctly using Bearer authentication and the standard OpenAI JSON schema, but it would point to the custom URL provided by the user.

#### Any other feedback you would like to provide regarding the site  
This feature would greatly increase the accessibility of AI integrations in APIDash by allowing access to hundreds of open-source and alternative hosted models without needing to change the code for every new provider on the market.

---

## #1174: [Feat] Add support for Groq like cloud based model providers

#### Tell us about the task you want to perform and are unable to do so because the feature is not available
Many students hesitate to purchase API credit to run cloud based models (like from `OpenAI, Anthropic`) nor they have proper local system infrastructure and GPU to run heavy LLM models locally using Ollama. Groq provides free API key (with limits ofcourse) which can be used for LM inference.

#### Describe the solution/feature you'd like us to add
Add Groq as a LM provider in the application with some popular models like `llama-3.3-70b-versatile , gemma2-9b-it, deepseek-r1-distill-llama-70b` etc but not limited to these, user can also select other option where they can call models other than listed ones.

#### Any other feedback you would like to provide regarding the site
No

---

## #1170: test: Add unit tests for import/export IO parsers (postman, curl, har, insomnia)

Added comprehensive unit tests for the four import/export IO parsers in **apidash_core** that had no prior test coverage.

Created `postman_io_test.dart` (21 tests)
Created `har_io_test.dart` (22 tests)
Created `insomnia_io_test.dart` (19 tests)
Extended `curl_test.dart` with 8 new edge case tests (7 → 15 total)

Each parser is tested for:

1. Basic HTTP methods (GET, POST, PUT, PATCH, DELETE)
2. Query parameters and headers (including disabled/enabled states)
3. Request bodies: raw JSON, form-data (text + file), x-www-form-urlencoded
4. Nested folder structures (Postman) / multiple entries (HAR)
5. Environment model conversion (Insomnia)
6. parseFormData utility (HAR)
7. Error handling: invalid JSON, empty strings, null/unknown methods
8. URL parameter stripping
9. Full API Dash collection round-trip parsing

**How to verify:**
`cd packages/apidash_core`
`flutter test test/parsers/ --reporter expanded`

**Result**: 77/77 tests passing.

---

## #1164: Fix: escape regex special characters in environment variable keys

#### Describe the bug/problem
There was a logic bug in [lib/utils/envvar_utils.dart](cci:7://file:///d:/top/gsoc/New%20folder/test/apidash/lib/utils/envvar_utils.dart:0:0-0:0) where environment variable keys were being used to build a `RegExp` without being escaped. This caused two main issues:

1. **Substitution Failure:** If a variable name contains regex-special characters like `.` or [()](https://github.com/foss42/apidash/issues/new/ the substitution fails. For example, a key named `auth(v2)` would prevent the value from being replaced because the regex engine interprets the parentheses as a capturing group instead of literal text.
2. **Security/Accuracy Risk:** A key like `api.url` was treated as a regex pattern where `.` matches any character. This could lead to accidental matching of incorrect strings like `api-url` or `api_url`.
3. **Stability:** Certain characters in a key name could potentially trigger a `FormatException` during regex construction, leading to unexpected app behavior.

#### Steps to Reproduce the bug/problem
1. Go to the **Variables** tab and create a new environment variable.
2. Set the key to a name with parentheses, e.g., `auth(v2)`, and give it a value.
3. Use this variable in a Request header or URL, e.g., `Bearer {{auth(v2)}}`.
4. Click **Send**.
5. Observe the response: The variable is not replaced and is sent as the literal string `{{auth(v2)}}`.

#### Expected behavior
Environment variable keys should always be treated as literal strings. By wrapping the key in `RegExp.escape()`, we ensure that characters like dots or parentheses are matched exactly as the user typed them.

#### Device Info
 - OS: Windows 11

#### Flutter Doctor
Please run the `flutter doctor -v` command and paste your output below:
## Screenshots
<img width="2558" height="1510" alt="Image" src="https://github.com/user-attachments/assets/d4a7975b-bf24-4d98-af13-54909717cce8" />
<img width="2558" height="1517" alt="Image" src="https://github.com/user-attachments/assets/9a425dcc-9059-40ce-8d17-2e5d42262533" />

---

## #1161: Bug: Cursor jumping in ai fields

#### Describe the bug/problem
Typing in the System Prompt or User Prompt fields in the AI request pane causes the cursor to jump to the end when editing in the middle of the text.

#### Steps to Reproduce the bug/problem
1.open an AI request
2.Type some text in the System Prompt or User Prompt field
3.Place the cursor in the middle of the text
4.Type and see the cursor jumps forward

#### Expected behavior
The cursor should stay at the position where the user is typing.

#### Device Info (The device where you encountered this issue)
 - OS: MacOS
 - Version: 15.6.1

---

## #1138: [Bug] "invalid text selection" crash in EnvironmentTriggerField when changing request type while text is highlighted

#### Describe the bug/problem

While testing the application, I encountered a crash related to the URL/Environment text field. It occurs during a specific edge case, but it completely breaks the UI state when triggered.

I have investigated the codebase to isolate the root cause and attached a screen recording below demonstrating the exact crash.

#### Steps to Reproduce the bug/problem
- Enter a relatively long string into the main URL/address bar.

- Use the cursor to highlight a portion of the text (specifically towards the end of the string).

- With the text still highlighted, change the overall request type (e.g., switch from HTTP to AI or GraphQL).

- The application throws an invalid text selection exception and crashes to a red screen.

Video --- 
https://github.com/user-attachments/assets/e08ee8da-c5b6-42cb-9c4b-25a1849be520

Image ---
<img width="1216" height="538" alt="Image" src="https://github.com/user-attachments/assets/b9445a21-a18b-436d-95a9-e10e8c19c7ce" />

#### Expected behavior
Changing the request type should update the UI state smoothly. If the new state causes the URL/Environment text to update or clear, the text field should either safely maintain the selection bounds or gracefully collapse the cursor, rather than throwing an out-of-bounds error.

#### Actual behavior
A RangeError (invalid text selection) exception is thrown because the TextEditingController attempts to apply a text selection that exceeds the length of the newly updated string.

#### Root Cause Analysis:
I tracked this down to the EnvironmentTriggerFieldState. Inside the didUpdateWidget method, there is logic meant to restore the cursor or selection when the parent widget passes down a new initialValue.

Currently, the check is implemented as follows:
```
if (currentSelection.baseOffset <= controller.text.length) {
  controller.selection = currentSelection;
}
```
This implementation only verifies if the start (baseOffset) of the selection is within the bounds of the new string length. It does not check if the end of the selection (extentOffset) is valid. When the widget rebuilds with a shorter string which happens during the layout swap from HTTP to AI/GraphQL, Flutter tries to stretch the highlight to an index that no longer exists in memory. Additionally, if a user highlights right-to-left, the baseOffset and extentOffset values are inverted, which bypasses this condition entirely.

Proposed Solution:
To fix this, we need to ensure the entire selection range is valid before applying it. Updating the condition to use the .end property (which accurately handles both left-to-right and right-to-left selection bounds) prevents the crash:
```
if (currentSelection.isValid && currentSelection.end <= controller.text.length) {
  controller.selection = currentSelection;
}
```

#### Next Steps:
Since I have the project set up locally and have already tested this fix, I would be glad to open a Pull Request to resolve this.

#### Device Info (The device where you enc

*[truncated]*

---

## #1135: feat : Multi-select requests with bulk delete

**Labels:** priority: low

#### Tell us about the task you want to perform and are unable to do so because the feature is not available

Currently, requests in the sidebar can only be selected and deleted one at a time. When managing a large collection, this becomes tedious. This feature would allow users to:

1. **Enter a multi-select mode** (e.g., long-press a request card, or toggle via a button/shortcut)
2. Select multiple requests via checkboxes on each sidebar card
3. Perform bulk actions — starting with bulk delete, with room for future actions like bulk duplicate or bulk export

Current Behavior : 

1. Single request selection via _selectedIdStateProvider_ (_StateProvider<String?>_)
2. Delete one request at a time via the 3-dot _ItemCardMenu_ on _SidebarRequestCard_
3. No multi-select, checkbox, or bulk action UI exists


#### Any other feedback you would like to provide regarding the site

---

## #1132: Env Variable Text Field Loses Focus After First Character Typing

#### Describe the bug/problem
After the recent fix for the cURL import variable refresh issue (#1080), When entering text into an env variable field, the field loses focus immediately after typing the first character.

#### Steps to Reproduce the bug/problem
1. Navigate to the Variables tab.
2. Click inside an env variable field.
3. Type a single character.

Observe that the field loses focus immediately.

https://github.com/user-attachments/assets/ba6bf083-941c-440b-9442-393430217615

#### Expected behavior
The env variable text field should retain focus while typing, allowing continuous input without interruption.

#### Device Info (The device where you encountered this issue)
 - OS: Windows
 - Version: Windows 11

#### Flutter Doctor
Please run the `flutter doctor -v` command and provide the details below:

<img width="1556" height="661" alt="Image" src="https://github.com/user-attachments/assets/3468f62f-718c-4d4a-8d98-0e5eaff3b97f" />

---

## #1131: Visible Delay when closing the App on Windows

#### Describe the bug/problem
When I run the Release build of the app (generated via `flutter build windows` and located in `apidash\build\windows\x64\runner\Release`), closing the app with the ❌ shows a noticeable lag or glitch.
This behavior feels unexpected in the Release build—especially since the Debug build doesn’t have this issue.

#### Expected behavior
The released build of the app should close immediately without any lag.

#### Device Info (The device where you encountered this issue)
 - OS: Windows 11 Home Single Language


#### Flutter Doctor
Please run the `flutter doctor -v` command and provide the details below:

```
E:\GSOC\apidash(project-exploring)
λ flutter doctor -v
[√] Flutter (Channel stable, 3.41.2, on Microsoft Windows [Version
    10.0.26200.7840], locale en-US) [341ms]
    • Flutter version 3.41.2 on channel stable at C:\flutter
    • Upstream repository https://github.com/flutter/flutter.git
    • Framework revision 90673a4eef (5 days ago), 2026-02-18 13:54:59
      -0800
    • Engine revision 6c0baaebf7
    • Dart version 3.11.0
    • DevTools version 2.54.1
    • Feature flags: enable-web, enable-linux-desktop,
      enable-macos-desktop, enable-windows-desktop, enable-android,
      enable-ios, cli-animations, enable-native-assets,
      omit-legacy-version-file, enable-lldb-debugging,
      enable-uiscene-migration

[√] Windows Version (11 Home Single Language 64-bit, 25H2, 2009) [981ms]

[√] Android toolchain - develop for Android devices (Android SDK version
    37.0.0-rc1) [5.8s]
    • Android SDK at C:\Users\17swa\AppData\Local\Android\sdk
    • Emulator version 36.4.9.0 (build_id 14788078) (CL:N/A)
    • Platform android-36, build-tools 37.0.0-rc1
    • Java binary at: C:\Program Files\Java\jdk-18.0.2\bin\java
      This JDK is specified in your Flutter configuration.
      To change the current JDK, run: `flutter config
      --jdk-dir="path/to/jdk"`.
    • Java version Java(TM) SE Runtime Environment (build 18.0.2+9-61)    
    • All Android licenses accepted.

[√] Chrome - develop for the web [85ms]
    • Chrome at C:\Program Files\Google\Chrome\Application\chrome.exe     

[√] Visual Studio - develop Windows apps (Visual Studio Community 2022
    17.9.6) [84ms]
    • Visual Studio at C:\Program Files\Microsoft Visual
      Studio\2022\Community
    • Visual Studio Community 2022 version 17.9.34728.123
    • Windows 10 SDK version 10.0.22621.0

[√] Connected device (4 available) [267ms]
    • RMX3710 (mobile)  • SGEQTOHU996P8POB • android-arm64  • Android 14  
      (API 34)
    • Windows (desktop) • windows          • windows-x64    • Microsoft   
      Windows [Version 10.0.26200.7840]
    • Chrome (web)      • chrome           • web-javascript • Google      
      Chrome 145.0.7632.76
    • Edge (web)        • edge             • web-javascript • Microsoft   
      Edge 145.0.3800.70

[√] Network resources [1,500ms]
    • All expected network resources are available.

• No issues found!
```

---

## #1129: [Feature] : Auto-generate meaningful names for imported requests (cURL & HAR)

#### Tell us about the task you want to perform and are unable to do so because the feature is not available

When importing requests via cURL, every imported request shows up as "untitled" in the sidebar because the cURL format has no concept of a request name. The import code passes null as the name, which gets stored as an empty string, and the sidebar falls back to displaying "untitled".

For HAR imports, the name is set to the full raw URL (e.g., https://jsonplaceholder.typicode.com/posts/1), which is hard to scan when you have many requests.

This makes the sidebar unusable after importing multiple requests — users see a wall of identical "untitled" entries or long unreadable URLs with no way to tell them apart without clicking each one.

Postman and Insomnia imports don't have this problem because those formats include user-defined request names.

Steps to Reproduce
      1. Open API Dash
      2.Click Import → select cURL format
      3.Drop a file with multiple cURL commands
      4.All imported requests appear as "untitled" in the sidebar

<img width="239" height="337" alt="Image" src="https://github.com/user-attachments/assets/084f0f24-5ac2-4978-a57e-210bdff0ca9c" />

#### Describe the solution/feature you'd like us to add

Expected Behavior
Imported requests should have auto-generated, human-readable names derived from the available information. 
A combination of HTTP method + URL path (without the host) would be short, unique, and scannable.

Solution : Well we can add a utility function that derives a short name from the HTTP method and url , then use it as the fallback name during import.

#### Any other feedback you would like to provide regarding the site

Why This Matters
      1. Users importing a batch of cURL commands can't distinguish between requests without clicking each one
      2. It slows down the workflow — the whole point of importing is to get set up quickly   
      3. Other tools (Postman, Insomnia app) auto-name imported requests from the URL when no name is provided

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

  if (!navigator.cookieEnabled) {
    window.addEventListener('DOMContentLoaded', function () {
      var cookieEl = document.getElementById('cookie-alert');
      cookieEl.style.display = 'block';
    })
  }

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
