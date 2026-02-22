# help wanted issue list

**Parent:** MIT App Inventor — Project Ideas
**Source:** https://github.com/mit-cml/appinventor-sources/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22
**Scraped:** 2026-02-22T23:28:47.578376

---

## #3771: Player Vibrate Method Not Working in Android, Issue in iOS

**Labels:** bug, status: new

In the following example app, the Vibrate method for the Player component does not appear to work in Android. In iOS, it works, but does not appear to obey the time parameter. 

We may suggest using Vibrate in one of the Hour of Code or Beginner tutorials. 

[Example AIA. ](https://drive.google.com/file/d/1Ck8Pev0LMxbf9U_AZhUejL5dxLz-rYzn/view?usp=drive_link)

@stezelMIT

---

## #3764: DataFile not implemented in iOS

**Labels:** status: new, feature request

**Describe the desired feature**

DataFile component, which read csv files, is not implemented in iOS

**Give an example of how this feature would be used**

@bobparks is there any data science aia files that uses DataFile component that I can use for testing?

---

## #3761: Implement a AndroidMinSdk project property

**Labels:** help wanted, issue: noted for future Work, feature request, affects: ucr, android

Provide a new project property that allows for the user to specify a minSDK in the project.properties file. The value must default to ComponentConstants.APP_INVENTOR_MIN_SDK.

---

## #3759: Update to Blockly 12

**Labels:** enhancement, issue: accepted, affects: master

---

## #3736: Implement CopyToClipboard block for Sharing component

**Labels:** help wanted, issue: accepted, status: needs discussion, feature request, affects: ucr, android, ios

**Describe the desired feature**

Implement a block on the Sharing component that enables the app developer to copy content to the system clipboard. The feature needs to work on both Android and iOS. Update the version number in YaVersion accordingly as well as YoungAndroidFormUpgrader.java and versioning.js.

---

## #3735: Deployment error occurred（I have tried many methods, but I am unable to solve it）

**Labels:** bug, status: new

The system is Debian 12
The following are the error messages

root@zhufuwu:/www/wwwroot/wanjuanwang.com/duozhan/appinventor-sources/appinventor# java -version
java version "11.0.19" 2023-04-18 LTS
Java(TM) SE Runtime Environment 18.9 (build 11.0.19+9-LTS-224)
Java HotSpot(TM) 64-Bit Server VM 18.9 (build 11.0.19+9-LTS-224, mixed mode)
root@zhufuwu:/www/wwwroot/wanjuanwang.com/duozhan/appinventor-sources/appinventor# ant -version
Apache Ant(TM) version 1.10.13 compiled on January 4 2023
root@zhufuwu:/www/wwwroot/wanjuanwang.com/duozhan/appinventor-sources/appinventor# git --version
git version 2.39.5
root@zhufuwu:/www/wwwroot/wanjuanwang.com/duozhan/appinventor-sources/appinventor# gcloud version
Google Cloud SDK 551.0.0
app-engine-java 4.0.0
app-engine-python 1.9.118
beta 2026.01.02
bq 2.1.26
bundled-python3-unix 3.13.10
cloud-datastore-emulator 2.3.1
core 2026.01.02
gcloud-crc32c 1.0.0
gsutil 5.35
root@zhufuwu:/www/wwwroot/wanjuanwang.com/duozhan/appinventor-sources/appinventor# python3 --version
Python 3.11.2
root@zhufuwu:/www/wwwroot/wanjuanwang.com/duozhan/appinventor-sources/appinventor# cd ..
root@zhufuwu:/www/wwwroot/wanjuanwang.com/duozhan/appinventor-sources# ./buildtools doctor
Diagnosing your system...

[PASS] Java is installed.
[PASS] Required version of Java is installed.
[PASS] Git is installed.
[PASS] Git submodules are properly set up.
[PASS] Google Cloud SDK is installed.

Passed 5 checks and 0 failing

root@zhufuwu:/www/wwwroot/wanjuanwang.com/duozhan/appinventor-sources# cd appinventor
root@zhufuwu:/www/wwwroot/wanjuanwang.com/duozhan/appinventor-sources/appinventor# ant MakeAuthKey
Buildfile: /www/wwwroot/wanjuanwang.com/duozhan/appinventor-sources/appinventor/build.xml

MakeAuthKey:

init:

CheckAuthKey:

MakeAuthKey:

BUILD SUCCESSFUL
Total time: 0 seconds
root@zhufuwu:/www/wwwroot/wanjuanwang.com/duozhan/appinventor-sources/appinventor# ant
Final Error......
     [java]     at com.google.gwt.dev.Precompile.precompile(Precompile.java:255)
     [java]     at com.google.gwt.dev.Precompile.precompile(Precompile.java:202)
     [java]     at com.google.gwt.dev.Precompile.precompile(Precompile.java:143)
     [java]     at com.google.gwt.dev.Compiler.compile(Compiler.java:204)
     [java]     at com.google.gwt.dev.Compiler.compile(Compiler.java:155)
     [java]     at com.google.gwt.dev.Compiler.compile(Compiler.java:144)
     [java]     at com.google.gwt.dev.Compiler$1.run(Compiler.java:118)
     [java]     at com.google.gwt.dev.CompileTaskRunner.doRun(CompileTaskRunner.java:55)
     [java]     at com.google.gwt.dev.CompileTaskRunner.runWithAppropriateLogger(CompileTaskRunner.java:50)
     [java]     at com.google.gwt.dev.Compiler.main(Compiler.java:125)
     [java]    [ERROR] Errors in 'gen/com/google/appinventor/client/explorer/dialogs/NoProjectDialogBox_NoProjectDialogBoxUiBinderImpl.java'
     [java]       [ERROR] Line 168: Failed to resolve 'com.google.appinventor.client.Images' via deferred binding
     [java]    [WARN] For 

*[truncated]*

---

## #3730: Redis Database leaking connections

**Labels:** bug, issue: noted for future Work

**Describe the bug**

See #3624 

Redis is not closing connections in all situations it should be expected to. Instead of granting the extra feature the user requested, the database should close in these situations.

**Affects**

<!--
Please check off the part of the system that is affected by the bug.
-->

- [ ] Designer
- [ ] Blocks editor
- [ ] Projects Explorer
- [ ] Android Companion
- [ ] iOS Companion
- [ ] Android Compiled APK/AAB
- [ ] iOS Compiled IPA
- [ ] Buildserver
- [ ] Debugging
- [X] Other... (please describe)

---

## #3729: Download link needs more contrast

**Labels:** bug, help wanted, issue: noted for future Work, affects: master, A11y

The download button in the download APK dialog has text that is too low contrast compared to the background color. I believe this text used to be black. It should be corrected:

<img width="448" height="407" alt="Image" src="https://github.com/user-attachments/assets/ed4a748a-2d70-471a-be1b-fdb23a54548c" />

---

## #3716: in iOS ListView Elements stopped working and gives error

**Labels:** bug, issue: accepted, ios

**Describe the bug**
Previously I was able to assign a ListView.Elements a list and it would work fine.  Now it is giving a runtime error as you can try with the attached AIA file.

[ListViewTest.aia.zip](https://github.com/user-attachments/files/24509092/ListViewTest.aia.zip)

<!--
Describe the bug in sufficient detail so that we can understand the issue. You should also describe the steps to reproduce the issue (below) so that we ideally can confirm it.
-->

**Affects**

<!--
Please check off the part of the system that is affected by the bug.
-->

- [ ] Designer
- [ ] Blocks editor
- [ ] Projects Explorer
- [ ] Android Companion
- [ X] iOS Companion
- [ ] Android Compiled APK/AAB
- [ ] iOS Compiled IPA
- [ ] Buildserver
- [ ] Debugging
- [ ] Other... (please describe)

**Expected behavior**
ListView should accept a list and display the contents of the list as elements.
<!--
Please describe what you expected to happen before you encountered the bug.
-->

**Steps to reproduce**
Try the AIA given.
<!--
Please describe the steps needed to reproduce the bug. If possible, please include a minimal example project that demonstrates the issue.
-->

---

## #3710: Add the ability to internationalize apps

**Labels:** issue: accepted, feature request

**Describe the desired feature**

Provide a UI in the designer or blocks editor, it may also need to be a separate editor type, where app developers can provide string translations for more than one language. There will need to be a way to reference these internationalized strings in both the designer and blocks editor. When compiling apps, the strings will have to be placed in the appropriate locations (values-LANG for Android LANG.lproj for iOS) and make use of the system specific APIs to read and use those strings at runtime.

**Give an example of how this feature would be used**

The creation of multilingual apps.

**Why doesn't the current App Inventor system address this use case?**

It can be done, but requires the user to represent the translations as dictionaries in the blocks (or load them from a file asset), and then apply them programmatically at app start. This would streamline the development of apps intended to be used with more than one language.

**Why is this feature beneficial to App Inventor's educational mission?**

Many countries have more than one national language and students creating an app may want to offer it in all languages.

---

## #3707: ListView ios selectionColor doesn't work

**Labels:** bug, issue: accepted

Selection color doesn't show up at all in any state when an item is clicked

---

## #3689: LastOpened can bork projects after deleting a screen

**Labels:** bug, issue: accepted, affects: master

**Describe the bug**

After deleting a screen, the lastopened project property does not get properly reset and can cause App Inventor to fail if the screen named no longer exists. I suggest we both reset the lastopened property to Screen1 when this happen as well as put a guard in that if the screen doesn't exist we open Screen1 as well.

**Affects**

- [x] Designer
- [ ] Blocks editor
- [ ] Projects Explorer
- [ ] Android Companion
- [ ] iOS Companion
- [ ] Android Compiled APK/AAB
- [ ] iOS Compiled IPA
- [ ] Buildserver
- [ ] Debugging
- [ ] Other... (please describe)

**Expected behavior**

Projects should reopen after deleting a screen.

**Steps to reproduce**

Not 100% sure yet, but I expect deleting a screen and then immediately closing the window should trigger the failure mode.

---

## #3680: AR: refactor detach and reattaching of markers

**Labels:** feature request, ios, augmented reality

detachToWorldIfNeeded
reattachNodesToMarker
both walk through a marker's attachednodes but don't call the IM's detach and attach functions

eg
```
for node in marker._attachedNodes {
          guard let localOffset = node._nodeLocalTransform else {
              print("⚠️ No local transform for \(node.Name)")
              continue
          }

          node._tempWorldAnchor?.removeFromParent()
          node._tempWorldAnchor = nil
          
          node._modelEntity.setParent(markerAnchor, preservingWorldTransform: false)
          //node._modelEntity.setOrientation(worldOrientation, relativeTo: nil)
          node._modelEntity.position = localOffset.translation
          node._modelEntity.orientation = localOffset.rotation
          if node is TextNode || node is VideoNode {
            node._modelEntity.orientation = simd_quatf(angle: -90, axis: [1,0,0])
          }
          // CSB for now, we are billboarding during attachment
          if marker._billboardNodes { // this doesn't do anything
             print("   💾 Restored local orientation for \(node.Name): \(localOffset.rotation)")
             
             // ✅ THEN apply camera-facing orientation (which will preserve the restored orientation)
             if let cameraTransform = _arView.cameraTransform as Optional {
             //node.applyCameraFacingOrientation(cameraPosition: cameraTransform.translation)
             }
          }```

---

## #3665: AR: Determine marker identification and correct data storage architecture

**Labels:** feature request, augmented reality

To persist data across a broad range of users, what is the best way?

_Atomic_
Markers
nodes

or

_Nested_
Room/Lab
Markers
nodes

how do we signify that a location has virtual content?

---

## #3661: Block workspace gestures fail

**Labels:** bug, issue: accepted, affects: master

**Describe the bug**

At the DHA workshops, a few students ran into an issue where the block workspace would stop recognizing mouse up/down gestures. The only way to resume was to reload App Inventor.

**Affects**

- [ ] Designer
- [x] Blocks editor
- [ ] Projects Explorer
- [ ] Android Companion
- [ ] iOS Companion
- [ ] Android Compiled APK/AAB
- [ ] iOS Compiled IPA
- [ ] Buildserver
- [ ] Debugging
- [ ] Other... (please describe)

**Expected behavior**

General interactions with the workspace should not cause it to reach a state where the user can no longer do anything.

**Steps to reproduce**

Unclear. It did not happen to every student, and even for a given student only once during the 90 minute period. My intuition is that it probably has something to do with lexical variable flydowns, where the blocks get destroyed while having an active gesture and then the gesture cannot be cleared because another flydown has opened.

---

## #3660: Neo Connect menu does not reset correctly.

**Labels:** bug, help wanted, issue: accepted, affects: master

**Describe the bug**

When the students at DHA were testing on Chromebooks, the Connect menu items were not behaving properly after an initial session. The emulator and USB options would reappear even though they are not an option, and the enable/disable states seemed inconsistent. We should probably look at some of the menu logic and refactor/improve it.

**Affects**

- [x] Designer
- [ ] Blocks editor
- [ ] Projects Explorer
- [ ] Android Companion
- [ ] iOS Companion
- [ ] Android Compiled APK/AAB
- [ ] iOS Compiled IPA
- [ ] Buildserver
- [ ] Debugging
- [ ] Other... (please describe)

**Expected behavior**

We shouldn't show impossible menu options, and the states of the menu items should be consistent with the current state of the App Inventor companion connection.

**Steps to reproduce**

On a Chromebook establish a session with tablet using AI Companion mode. Close the tablet and trigger the WebRTC disconnect. Review the state of the Connect menu items. Also try Reset Connection.

---

## #3655: Add Timeout Handling to Bluetooth Components to Prevent Indefinite Hangs

## Summary
Add explicit **timeout handling** to App Inventor’s Bluetooth components to prevent indefinite hangs, improve reliability, and ensure graceful recovery when Bluetooth operations fail or devices become unresponsive.

---

## Problem
Bluetooth components such as **BluetoothClient.java** and **BluetoothServer.java** handle operations like connecting, reading, and writing data. However, these lack timeout mechanisms, which can cause the app to hang indefinitely in scenarios such as:

- **Unresponsive devices:** If the paired device is out of range, powered off, or faulty, operations like `connect()` or `read()` can block indefinitely.  
- **Thread blocking:** `BluetoothClient.java` uses a `ScheduledExecutorService` for polling, but without timeout checks, threads may remain stuck, causing UI freezes or excessive CPU usage.  
- **No timeout logic in base classes:** `BluetoothConnectionBase.java` manages connections but doesn't apply operation-level timeouts, risking ANRs (Application Not Responding) and battery drain.

---


## Potential Impact if Unaddressed
- App hangs or **ANRs** when a Bluetooth device fails or disconnects unexpectedly.  
- Poor user experience in real-world scenarios involving unreliable Bluetooth hardware.  
- Resource leaks due to threads or sockets left open indefinitely.

---

## Proposed Solution

### 1. Add Timeout Properties
Introduce configurable timeout parameters to Bluetooth components:
- **ConnectionTimeout** (e.g., 10–30 seconds default)  
- **ReadTimeout** (e.g., 5–10 seconds default)  
- **WriteTimeout** (e.g., 5 seconds default)

These can be exposed as component properties or constants within the class.

---

### 2. Implement Timeout Logic in Operations
- **Connections:**  
  Wrap `BluetoothSocket.connect()` in a timeout-controlled thread using `Future.get(timeout)` or equivalent.  
- **Reads:**  
  Apply timeouts on `InputStream.read()` using a thread wrapper or `ExecutorService`.  
- **Writes:**  
  Add timeout handling to ensure `OutputStream.write()` doesn’t block indefinitely.  
- **Polling:**  
  Add timeout checks in `ScheduledExecutorService` tasks to terminate long-running or stuck operations.

---

### 3. Error Handling
- Dispatch timeout errors through `dispatchErrorOccurredEvent()` with a new constant in `ErrorMessages.java`, e.g.:
  - `ERROR_BLUETOOTH_TIMEOUT`  
- Provide clear, user-friendly error messages like:  
  > “Bluetooth operation timed out. Please check your device connection.”

---

### 4. Testing
- Add or update unit tests (e.g., `BluetoothClientTest.java`, `BluetoothConnectionBaseTest.java`) to simulate slow or unresponsive devices.  
- Verify that:
  - Timeouts trigger correctly without hanging.  
  - Successful operations still function normally.

---

## Files to Modify
- `appinventor/components/src/com/google/appinventor/components/runtime/BluetoothClient.java`  
- `appinventor/components/src/com/google/appinventor/components/runtime/BluetoothServer.java`  
- `appinventor/

*[truncated]*

---

## #3653: Android: Notifier needs corresponding text + image block

**Labels:** issue: accepted, feature request, android

fill out the block from the ios branch. see [ios code](https://github.com/mit-cml/appinventor-sources/pull/3652/commits/c7419449031ed6d883abc00ee715d140f76ac2d7)

---

## #3650: APK build failed when an extension has maxSdkVersion attribute with permission element

**Labels:** bug, issue: accepted, affects: buildserver

**Describe the bug**

When we use maxSdkVersion attribute with **WRITE_EXTERNAL_STORAGE** AI2 failed to compile the APK.
```
[
    {
        "permissionConstraints": {
            "android.permission.WRITE_EXTERNAL_STORAGE": {
                "maxSdkVersion": 18
            }
        },
        "type": "com.jewel.youtube.YouTube",
        "androidMinSdk": [
            "14"
        ],
        "assets": [],
        "permissions": [
            "android.permission.INTERNET",
            "android.permission.WRITE_EXTERNAL_STORAGE"
        ],
        "activities": []
    }
]
```

**Affects**

- [ ] Designer
- [ ] Blocks editor
- [ ] Projects Explorer
- [ ] Android Companion
- [ ] iOS Companion
- [ ] Android Compiled APK/AAB
- [ ] iOS Compiled IPA
- [x] Buildserver
- [ ] Debugging
- [ ] Other... (please describe)

**Expected behavior**

I think it should be able to build the APK.

No issues for the below JSON:

```
[
    {
        "type": "com.jewel.youtube.YouTube",
        "androidMinSdk": [
            "14"
        ],
        "assets": [],
        "permissions": [
            "android.permission.INTERNET",
            "android.permission.WRITE_EXTERNAL_STORAGE"
        ],
        "activities": []
    }
]
```

---

## #3645: iOS parity for the File component

**Labels:** issue: accepted, status: in progress, technical debt, affects: master, ios

---

## #3642: Let's add iOS verbiage to AI2 Menu

**Labels:** status: needs discussion, feature request, affects: master

**Describe the desired feature**

At the top of the AI2 menu, it would be good to add a word or two to reinforce for users that it is cross-platform. 

<img width="302" height="321" alt="Image" src="https://github.com/user-attachments/assets/10b2146a-f589-4653-84b6-192543bad741" />

One way to do this would be to change the menu items in the Connect menu to "AI Companion for iOS and Android" and "Emulator for iOS and Android."

---

## #3640: Update Links to Spreadsheet Component Instructions

**Labels:** bug, help wanted, status: new, documentation, affects: master

**Describe the bug**

The [instructions](https://ai2.appinventor.mit.edu/reference/other/googlesheets-api-setup.html) for creating a Service Account to use the Google Sheets component in App Inventor are obsolete. A link to these instructions is on the Designer screen here: 

<img width="354" height="581" alt="Image" src="https://github.com/user-attachments/assets/16175326-166e-42fb-93ab-98a5159b5f2b" />

And [another link](https://ai2.appinventor.mit.edu/reference/components/storage.html#Spreadsheet
) can be found on the Spreadsheet documentation page (in the opening paragraph of the Spreadsheet documentation). 

We've heard from a few teachers directly that they couldn't follow the older instructions. 

Suggest changing both links to the current and updated App Inventor instructions [here](https://docs.google.com/document/d/10PcV0WGgtedebzxn1H1tu58BP1cSFOIVSUGPwVQ_rsQ/edit?tab=t.0).

---

## #3639: Move "Update the Companion" menu item in AI2

**Labels:** help wanted, issue: accepted, feature request, affects: master

**Describe the desired feature**

Currently, the "Update the Companion" menu item under "Connect" is confusing to workshop users. 

<img width="308" height="321" alt="Image" src="https://github.com/user-attachments/assets/e2c9c512-19b2-4904-a223-cbcda983c1c1" />

This is confusing for the majority of AI2 users, who are coming in with a mobile device and expect this menu item to help them update their device's companion. 

The menu item should say, "Update the Companion for Emulator." Alternatively, the item could go under Help and say, "Update the Companion for Emulator."

---

## #3638: Add iOS Companion Information to AI2 menu

**Labels:** help wanted, status: new, feature request

**Describe the desired feature**

Currently, the menu item "Companion Information" under Connect --   

<img width="459" height="318" alt="Image" src="https://github.com/user-attachments/assets/07df7511-eb51-4aed-9fc5-8cb10e5d8397" />

launches a pop-up that only shows a way to get to the Android companion: 

<img width="497" height="386" alt="Image" src="https://github.com/user-attachments/assets/eeae90c5-ba55-4335-9188-b81d159a71d3" />

Let's provide both iOS and Android links on this pop-up in a manner similar to how Option 1 is formatted on the landing website: 

https://appinventor.mit.edu/explore/ai2/setup

That is, let's change the pop-up to show icons for iOS and Android, then split off into two pop-ups, each with a link, QR code, or both.

---

## #3635: Customize CheckBox colors

**Labels:** help wanted, feature request, affects: ucr, android, ios

Switch has a bunch of features to customize its color scheme. CheckBox, which is similar in purpose and functionality, does not. Users would appreciate having more control over the CheckBox appearance.

---

## #3618: Implement SSE support for Web component

**Labels:** help wanted, status: needs discussion, feature request, affects: ucr, android, ios

**Describe the desired feature**

[From the forum](https://community.appinventor.mit.edu/t/streaming-from-firebase-rest-api/157013?u=ewpatton): The Web component performs standard HTTP style transactions. Server-side events is a new mechanism for data to be pushed from the server to the client and is used particularly in streaming chat completions, among other things.

**Give an example of how this feature would be used**

App developers could build apps that stream changes from HTTP servers using SSE.

**Why doesn't the current App Inventor system address this use case?**

The Web component does not understand the SSE protocol and therefore cannot consume SSE streams.

**Why is this feature beneficial to App Inventor's educational mission?**

See reference to chatbots above.

---

## #3616: Canvas behaves differently on iOS than Android

**Labels:** bug, help wanted, issue: accepted, ios

**Describe the bug**

[From the forum](https://community.appinventor.mit.edu/t/scratchcard-example-does-not-work-on-ios/156601): An app meant to shown how to create a scratch off game does not work on iOS but does work on Android.

**Affects**

<!--
Please check off the part of the system that is affected by the bug.
-->

- [ ] Designer
- [ ] Blocks editor
- [ ] Projects Explorer
- [ ] Android Companion
- [x] iOS Companion
- [ ] Android Compiled APK/AAB
- [ ] iOS Compiled IPA
- [ ] Buildserver
- [ ] Debugging
- [ ] Other... (please describe)

**Expected behavior**

Canvas operations should behave the same on iOS as they do on Android.

**Steps to reproduce**

See the post for the test app and description.

---

## #3610: Build android tools update

**Labels:** bug, issue: accepted, affects: buildserver

**Describe the bug**

While adding AAR libraries to the extension, I encountered a problem compiling the APK. The problem turned out to be a font file added to the library resources, in the res/font/font.ttf folder. The tools/libraries used by the build server are too old to handle this type of resource, so they return an error.

<!--
Describe the bug in sufficient detail so that we can understand the issue. You should also describe the steps to reproduce the issue (below) so that we ideally can confirm it.
-->

**Affects**

<!--
Please check off the part of the system that is affected by the bug.
-->

- [ ] Designer
- [ ] Blocks editor
- [ ] Projects Explorer
- [ ] Companion
- [x] Compiled apps
- [x] Buildserver
- [ ] Debugging
- [ ] Other... (please describe)

**Expected behavior**

AAR libraries shouldn't cause any problems during compilation. If we already have the ability to add AAR libraries, it should work flawlessly.

<!--
Please describe what you expected to happen before you encountered the bug.
-->

**Steps to reproduce**

Add any AAR library to the project that contains a font folder and, within it, a font file, e.g., ttf. If you don't have such a library, add the font folder with the ttf file to any AAR library. Then, when compiling the APK, you'll get an error.

<!--
Please describe the steps needed to reproduce the bug. If possible, please include a minimal example project that demonstrates the issue.
-->

---

## #3600: iOS Saved Apps feature not working properly

**Labels:** bug

**Describe the bug**

<!--
Describe the bug in sufficient detail so that we can understand the issue. You should also describe the steps to reproduce the issue (below) so that we ideally can confirm it.
-->
The iOS Companion Saved Apps has many issues.  
All my previously saved apps from before are gone this morning, not sure if these are supposed to be cleared every time there is a new release or something 
I saved a new app today and it looked saved but is not clickable and I cannot open it.  When I tested a few days ago, the saved app opened but even though the first screen (password UI) opened and worked fine the second screen came blank.
This is such an important new iOS feature that it will cause a big excitement in the Ed community for iOS based teachers all over the world and it should not be released until all the issues are fully tested and corrected.


**Affects**

<!--
Please check off the part of the system that is affected by the bug.
-->

- [ ] Designer
- [ ] Blocks editor
- [ ] Projects Explorer
- [ X] Companion
- [ ] Compiled apps
- [ ] Buildserver
- [ ] Debugging
- [ ] Other... (please describe)

**Expected behavior**

<!--
Please describe what you expected to happen before you encountered the bug.
-->
The Saved apps in iOS companion should work as intended
I am including the project I tested but there must be other that do not work which I cannot test due to the total lack of function that I encountered today
[GenAI_MyToDoList_Voice.aia.zip](https://github.com/user-attachments/files/22277561/GenAI_MyToDoList_Voice.aia.zip)


**Steps to reproduce**

<!--
Please describe the steps needed to reproduce the bug. If possible, please include a minimal example project that demonstrates the issue.
-->
Try to save the AIA in iOS companion and see the issues.

My iphone 16 is running iOS 18.6.2 and is up to date

---

## #3596: Refactor properties for screen layout boundaries to "full screen" or "safe area"

**Labels:** help wanted, feature request, android, ios

**Describe the desired feature**

As of Android 15, the display defaults to "edge-to-edge", i.e. laying an app out over all of the screen, including under top status bar, bottom navbar (if present), and cutout areas for things like cameras. The bottom edge of iOS's screen has always run behind cutouts.

Our current appearance properties offer the ability to hide the title bar and status bar -- these are hidden separately in Android but together in iOS, so the "ShowStatusBar" property does nothing iOS. We don't have a property for hiding the bottom navbar on Android, which has been optional for several versions and doesn't exist on iOS.

The paradigm for available screen area has shifted since App Inventor designed these properties. A better modern approach would be to give the app developer the option to define screen layout to 

 - "safe" area, i.e. the area that does not intersect with screen cutouts and leaves OS features like status bar alone
 - "full screen" i.e. what Android calls edge-to-edge, i.e. hiding status/title/nav bars and extending the layout under any cutouts.

Additionally, the app developer probably wants the option to extend a background image over the entire screen while keeping the actual component layout to safe areas.

The new properties should replace the old ones with a logical migration for old apps, especially Android ones.

---

## #3589: AR Capabilities: Android Geo Anchors

**Labels:** feature request, augmented reality

implemented in IOS, not yet in Android/ARCore

---

## #3584: Deleting account w/o emptying trash

**Labels:** help wanted, feature request, affects: master

**Describe the desired feature**

When using https://code2.appinventor.mit.edu/ and attempting to **Delete Account** with projects, I get: *You must first delete all your projects before you can delete your account.*

OK... probably a good idea. However, if I **Move to Trash** all projects, I *still* get that message. 

If there are no projects in the projects page, then it should be possible to delete the account (with an implicit emptying of the trash). 

**Give an example of how this feature would be used**

Why would one want to do this?

Use case: Creating tutorials that include screenshots or videos with the secret four-word phrase, it should be possible to delete those temporary accounts (more) easily.

**Why doesn't the current App Inventor system address this use case?**

Not sure...

**Why is this feature beneficial to App Inventor's educational mission?**

It makes it easier to make many anonymous tutorials with out cluttering up the https://code2.appinventor.mit.edu/ servers.

---

## #3569: Description text is not showing in the designer section for the extension's properties.

**Labels:** bug, status: new

**Describe the bug**

The description text is showing for built-in components perfectly. See below:

<img width="443" height="311" alt="Image" src="https://github.com/user-attachments/assets/2fe1830c-ce85-442a-b221-6bf756215c0f" />

But it's not showing for extension properties, it always just shows a default message!

<img width="436" height="295" alt="Image" src="https://github.com/user-attachments/assets/7a075ed0-49d6-44df-9ed5-3ee2bf65afae" />

**Affects**

- [x] Designer
- [ ] Blocks editor
- [ ] Projects Explorer
- [ ] Companion
- [ ] Compiled apps
- [ ] Buildserver
- [ ] Debugging
- [ ] Other... (please describe)

**Expected behavior**

It should show the description text from the extension properties, if available.

**Steps to reproduce**

---

## #3551: Add method/event pair to get ChatBot provider/model in app

**Labels:** status: new, feature request

**Describe the desired feature**

[From the community](https://community.appinventor.mit.edu/t/problem-using-list-picker-with-chatbot-models/153336?u=ewpatton): It might be useful to have a method to request the provider/model list in an app to help drive UI rather than people needing to hard code providers and models.

**Give an example of how this feature would be used**

A generic app where students test different models to compare and contrast their responses.

**Why doesn't the current App Inventor system address this use case?**

No block exists currently but we do have an API in the ChatBot proxy to obtain this information, which is used in the designer and blocks.

**Why is this feature beneficial to App Inventor's educational mission?**

See aforementioned example.

---

## #3548: AR Capabilities: Collision Detection with ARCore

**Labels:** status: new, feature request, android, augmented reality

arcore has a totally different way to handle collisions

---

## #3542: Some Code Does Not Fire Inside EntryClick hander in Android

**Labels:** bug, status: new

**Describe the bug**

We have two conditionals in the example provided at the bottom here. Android fires the first conditional, but ignores the second. iOS is fine. 

<!--
Describe the bug in sufficient detail so that we can understand the issue. You should also describe the steps to reproduce the issue (below) so that we ideally can confirm it.
-->

**Affects**

<!--
Please check off the part of the system that is affected by the bug.
-->

- [ ] Designer
- [x ] Blocks editor
- [ ] Projects Explorer
- [ ] Companion
- [ ] Compiled apps
- [ ] Buildserver
- [ ] Debugging
- [ ] Other... (please describe)

**Expected behavior**

All code should run inside the EntryClick handler. 

<!--
Please describe what you expected to happen before you encountered the bug.
-->

**Steps to reproduce**

Here are two example AIAs ([Example 1 ](https://drive.google.com/file/d/1-vAR5WBq8VWsjGL8BUl0I9jCqvh5LyYq/view?usp=drive_link
)and [Example 2](https://drive.google.com/file/d/1aCRVzVi21lQI4R3PioOa5RsSP2d9gyyW/view?usp=drive_link
)) for testing in Android and iOS. [Here is an image of the code in question](https://drive.google.com/drive/folders/1d0qwc8M3XmnaP0duOtbOQuV1BFwhk3kC
). 


In Android we can tell that the second conditional inside EntryClick is not firing because the numbers along the bottom do not change when anomalies are clicked on the phone screen. Contrast with the successful behavior in iOS. 

<!--
Please describe the steps needed to reproduce the bug. If possible, please include a minimal example project that demonstrates the issue.
-->

---

## #3535: Proposal: CI - Diff intermediate build artifacts on PR

At Kodular, we are improving our build and test systems to ensure platform stability. As part of that effort, we have overhauled our CI pipeline to diff the intermediate build artifacts such as AndroidRuntime.jar, simple_components.json (& others), and the companion AAB + APK. This allows us to merge with greater confidence and gives us visibility into what has actually changed at the ABI level.

Is there value in adding such a CI workflow to this repo? I have noticed that GitHub Actions are currently disabled on this repo. I have attached a bunch of screenshots to help you judge the usefulness yourself -

<img width="1124" height="526" alt="Image" src="https://github.com/user-attachments/assets/95b90019-e41a-4708-a23d-730343661f5a" />

<img width="908" height="671" alt="Image" src="https://github.com/user-attachments/assets/e4f927a5-7140-4229-9fe8-f16353f45f26" />

<img width="766" height="719" alt="Image" src="https://github.com/user-attachments/assets/4a002020-9981-430e-a97e-2db37da6e73c" />

<img width="904" height="937" alt="Image" src="https://github.com/user-attachments/assets/73ea5b53-dfac-47f6-a602-964f477b1e7a" />

<img width="1403" height="922" alt="Image" src="https://github.com/user-attachments/assets/377dc81f-45da-4c7c-b7c7-6d33f2292807" />

---

## #3533: Make an API for components/extensions to cache extra assets

**Labels:** status: new, feature request

**Describe the desired feature**

Add a mechanism for components and extensions to download supporting resources (e.g., model files) that are unable to be packaged normally due to their size.

**Give an example of how this feature would be used**

Teachable LLM and other tools.

**Why doesn't the current App Inventor system address this use case?**

It's possible we can repurpose the logic in AssetFetcher for this, but currently there is no API and each component author may end up writing their own implementation rather than using a shared framework.

**Why is this feature beneficial to App Inventor's educational mission?**

This will enable building more educational tools requiring a rich set of resources.

---

## #3532: Package up Workspace Search for v11

**Labels:** enhancement, issue: accepted, status: new, affects: master, priority: high, dependencies

This is an official plugin but there were some modification during GSoC that we do not have the sources for.

Two options:
1. reverse engineer the latest changes based on the minified file
2. try and use the official plugin

---

## #3531: Package up Lexical vars for version 11

**Labels:** enhancement, issue: accepted, affects: master, priority: high, dependencies

The lexical vars plugin has not been fully tested but seems to work with v11 of Blockly (see [readme](https://github.com/mit-cml/blockly-plugins/tree/main/block-lexical-variables)).

First thing would be to package it up and test it, then actually do a release in the repo.

@mark-friedman anything we should be looking at when testing?

NOTE: this is not pulled in through Karma for tests, it is actually in [lib/blockly-plugins](https://github.com/mit-cml/appinventor-sources/blob/master/appinventor/lib/blockly-plugins/block-lexical-variables-core-3.0.1.min.js) and likely pulled in through ant for the war file.

Actually the other plugins are actually loaded from [index.jsp](https://github.com/mit-cml/appinventor-sources/blob/master/appinventor/appengine/war/index.jsp) but lexvars are pulled in from [blocklyeditor/build.xml](https://github.com/mit-cml/appinventor-sources/blob/master/appinventor/blocklyeditor/build.xml#L134)

---

## #3530: Package up MultiSelect and Scroll Options Search plugins for v11

**Labels:** enhancement, issue: accepted, status: new, technical debt, affects: master, priority: high, dependencies

Currently running a v11 Blockly compressed files crashes with DragTarget issues that might be brought in by either or both the MultiSelect plugin and the Scroll Options plugin.

Package up the right versions to run with v11.2.2 and see if the Drag related issues go away.

The location of the files is in the [karma config file](https://github.com/mit-cml/appinventor-sources/blob/master/appinventor/karma.conf.js).

---

## #3529: V11 Migration Plugins

**Labels:** enhancement, issue: accepted, status: new, priority: high, Is Still Draft

**Describe the desired feature** [WIP]: adding more content soon

Upgrading to Blockly v11 also means updated plugins.

This is a list of plugins used:

- Lexical vars
- MultiSelect
- Workspace search
- Scroll Options (ScrollMetricsManager)
- Block Dynamic connections


Is Backpack a plugin? not yet, because the plugin does not support async operations.
Eventually Typeblocks should be a plugin.

This is a list of plugins that need some work:

- [x] MultiSearch (already at v11 but needs to be packaged for it
- [x] Lexical vars (upgrade to v11 - mostly testing and see what fails)

Current progress: MultiSelect and Workspace Search have been disabled because issues with dragging targets. It might just be a case of downloading the v11 versions.

---

## #3498: Make TextBox border visible for iOS (either by default or new property)

**Labels:** status: new, feature request

**Describe the desired feature**

The TextBox is a very prominent component in beginner App Inventor tutorials. On iOS devices (which are more common than Android in U.S. classrooms), TextBoxes don't have a visual indicator in the Companion unless the "BackgroundColor" is changed or a "Hint" is added in Properties, which can be confusing since it's not visually obvious that the text of the Hint is a fillable TextBox. There is also no option to show where the TextBox's border is without changing the BackgroundColor. This can create confusion, especially when following beginner tutorials on iOS.

**Give an example of how this feature would be used**

In the attached image, we have a tutorial app with 6 TextBoxes: 5 below "Name Your Favorite Music" to allow users to list songs, and 1 next to "Name" for users to enter their name. If we change the BackgroundColor of the TextBoxes to one color, they will visually blend into a single TextBox unless spacers are added in between them. Adding Hints can also just look like normal text without it being obvious that they are for TextBoxes.

![Image](https://github.com/user-attachments/assets/b5772586-c02d-49f3-8670-fd6e3c20e3e6)

**Why doesn't the current App Inventor system address this use case?**

The current workarounds (setting BackgroundColors or adding Hints) have limitations. They either alter the design unnecessarily or require extra explanation in tutorials. These add unnecessary complexity, especially for beginners.

**Why is this feature beneficial to App Inventor's educational mission?**

Because TextBoxes are widely used in beginner projects and iOS is the dominant platform in many educational settings, improving the default visibility of TextBoxes on iOS would make App Inventor more intuitive and accessible.

---

## #3487: AR Capabilities: Lighting nodes

**Labels:** status: new, feature request, android, augmented reality

currently the lighting is added into the Filament scene in ARFilamentRenderer as well as in ARView3D. Do we want to provide different ways to add lighting? Ideally, yes. There are stubs for LightNodes in the android codebase, `AmbientLight`, `PointLIght`, `SpotLight`

---

## #3474: macOS zoom seems to befuddle blocks editor

**Labels:** bug, status: new

**Describe the bug**

Sometimes when I triple-click to zoom in/out for demos, this locks the block editor until I reload the page.

**Affects**

<!--
Please check off the part of the system that is affected by the bug.
-->

- [ ] Designer
- [x] Blocks editor
- [ ] Projects Explorer
- [ ] Companion
- [ ] Compiled apps
- [ ] Buildserver
- [ ] Debugging
- [ ] Other... (please describe)

**Expected behavior**

Zooming in/out should not cause the blocks editor to become unresponsive.

**Steps to reproduce**

It doesn't seem to happen always, but if one triple-taps to turn on accessibility zooming and then zoom out, the blocks editor gets into a weird state where it no longer responds to mouse events.

1. Open a project in App Inventor on macOS on a MacBook Pro
2. Tap the touchpad with three fingers twice to activate accessibility zoom
3. Tap twice again to turn off the zoom
4. At this point, the workspace may no longer be responsive.

Investigating further...

---

## #3473: Support for compiling apps in Linux aarm64 architecture

**Labels:** status: new, feature request

**Describe the desired feature**

As of now, App Inventor can only build apps on amd64 / x86_64 architectures (and Mac aarch64). This is mainly limited due to dependencies on pre-compiled binaries for building apps, more specifically the ones in the following folders: [linux](https://github.com/mit-cml/appinventor-sources/tree/master/appinventor/lib/android/tools/linux), [mac](https://github.com/mit-cml/appinventor-sources/tree/master/appinventor/lib/android/tools/mac), [windows](https://github.com/mit-cml/appinventor-sources/tree/master/appinventor/lib/android/tools/windows).

Ideally, App Inventor should support compiling apps in Linux arm64 / aarch64 architectures, as that would help to increase the number of compatible servers.

**Give an example of how this feature would be used**

For buildservers when compiling apps.

**Why doesn't the current App Inventor system address this use case?**

Limitation on existing binaries.

**Why is this feature beneficial to App Inventor's educational mission?**

This is more of a feature which would enhance development, not a new feature "for app developers".

---

## #3465: Enhance procedure parameter refactoring in blocks editor

**Labels:** status: new, feature request

**Describe the desired feature**

<!--
Describe the feature that you'd like to see implemented for App Inventor. More detail is useful as it allows us to better understand the complexity of the task.
-->
The refactoring capabilities of the App Inventor build environment are a powerful feature. I have two requests for their enhancement concerning modification of procedure parameters.

_Request A_

Currently when a parameter is removed from a procedure already in use in a project, the blocks editor modifies each call site by reassigning the arguments that remain and appear in the argument list following the one removed in a manner that requires that the call sites be manually edited/corrected. For example,  suppose procedure p1 has parameters x, y, z, a, b, and c.

![Image](https://github.com/user-attachments/assets/20e80437-64ef-4f70-8c24-37e986c78021)

If parameter z is removed, a, b, and c are miss-assigned and the last argument is left unassigned.

![Image](https://github.com/user-attachments/assets/e01747a7-dec8-44ce-98a5-0438df6aecba)

This requires that each call site be manually corrected, which can be tedious and error prone.

I suggest that better behavior would be that when argument z is removed from the parameter list that the call site should be modified only by removal of parameter z while leaving its assigned argument unassigned and leaving the other arguments and assignments unchanged.

![Image](https://github.com/user-attachments/assets/8dfc72b3-a966-469e-b0b0-a11b06b53b28)

_Request B_

In a similar fashion when parameters are re-ordered in the procedure definition, at present the arguments at the call site remain in the same order. so that a mismatch is created for all parameters whose position in the parameter order is changed. For example in the case of the unmodified p1 above, if c is moved from the end of the parameter list  to the beginning, all arguments are miss-assigned.:

![Image](https://github.com/user-attachments/assets/0f1bd7fa-4c59-4efe-9330-f5658050247f)

I suggest that, as in _Request A_, the parameter=>argument pairs at the call sites be preserved after the change of parameter order:

![Image](https://github.com/user-attachments/assets/cc125059-5bec-430c-8eda-f66745454950)

**Give an example of how this feature would be used**

<!--
How would a teacher or student use this feature?
-->
This this feature would be used implicitly for the user by the blocks editor, eliminating tedious and error prone editing of call sites.

**Why doesn't the current App Inventor system address this use case?**

<!--
Explain why the use case cannot be completed using the features of the current system.
-->
Not only is this not done presently, but it may very well surprise users after the fact (after having already made these parameter changes) that the call sites have been somewhat "un-coded". And that the call sites must be inspected and recoded, which would be facilitated by reference to an earlier state which was not saved and cann

*[truncated]*

---

## #3458: Add median (and other statistical functions?) to the math component

**Labels:** help wanted, status: new, feature request

The math component (https://ai2.appinventor.mit.edu/reference/blocks/math.html) has many useful functions — including `mean` and `mode`. Calculating the `median` of a list of values is a bit of a mouthful of code and could be easily implemented as another of the dropdown statistics functions.

<!--
Describe the feature that you'd like to see implemented for App Inventor. More detail is useful as it allows us to better understand the complexity of the task.
-->

### `median`

A `median` procedure *not* implemented as another of the dropdown statistics operations must:

- sort the list of values;
- find the middle value (if the length of the list is odd); or
- average the middle two values (if the length of the list is even).

<!--
How would a teacher or student use this feature?
-->

Teachers and students will use this feature, for example, when calculating `ConvertMessagesToTDS` (total dissolved solids from a list of sensor voltage samples) in a water-quality activity, which involves calculating the median of a list of sampled sensor voltage values. 

<!--
Explain why the use case cannot be completed using the features of the current system.
-->

`median` *can* be completed using the features of the current system, but the implementation is unwieldy.

<!--
Because MIT App Inventor is aimed at educational use, we prioritize development of features with an educational benefit. Help us understand how your feature request relates to our mission.
-->

### Discussion

A further request is to evaluate *other* statistical formulas that may be of use in data-science or physical-computing calculations. For example, those listed here: https://stattrek.com/statistics/formulas. 

There is a tradeoff between usefulness and ease of explanation when teaching statistics or MIT App Inventor. The more operations there are, the more explanations are necessarily. That said, it is best to provide all useful operations and complete [documentation](https://ai2.appinventor.mit.edu/reference/blocks/math.html). For example:
- Is the `arithmetic mean (average)` operation the *population* mean or the *sample* mean?
- The `mode` operation returns a *list* of modes, in case there are more than one 'most common' value.

Also, should factorial, permutation, combination operations be included? Financial operations (TVM, NPV, IRR, amortization, depreciation, yield)? Others (if so, what)?

---

## #3442: Pop-Up Instructions for Spreadsheet ID need to be revised

**Labels:** bug, status: new

Users have been getting confused by the instructions say that users need to pull out the spreadsheet ID from the URL. This is no longer true. Users can paste the entire spreadsheet URL in the field. 

![Image](https://github.com/user-attachments/assets/84f8d7b5-c13f-415a-acac-3811effe3dd0)

Can we rewrite to say: "The SpreadsheetID is part of the web address of the Google Sheets spreadsheet you want to use. The web address (URL) starts https://docs.google.com/spreadsheets . . . .  Go to the spreadsheet in your browser and paste its web address here."

---

## #3434: Update YAIL generator to use Blockly v11 `forBlock` dictionary

**Labels:** issue: noted for future Work, technical debt, affects: master, priority: high

The generators in Blockly v11 have been refactored. This will prevent our current YAIL generator from working. The generator will have to be updated to follow the new approach required by Blockly core.

---
