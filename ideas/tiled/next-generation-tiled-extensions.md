# Read more...

**Parent:** Tiled — Project Ideas
**Source:** https://github.com/mapeditor/tiled/wiki/Next-generation-Tiled-extensions
**Scraped:** 2026-02-22T23:28:47.583117

---

Tiled can be extended by using JavaScript, using either plain .js files or JavaScript modules (.mjs). However, Qt provides [QML](https://doc.qt.io/qt-6/qmlapplications.html), a powerful declarative language. It would be great if we could use it to declare custom actions, file formats, tools, etc. Additionally, we could ship the necessary QML modules to enable extensions to implement custom UI.

**Expected outcome:** Tiled extensions can be written in a convenient declarative language and can define custom UI.\
**Required skills:** Qt, C++ (preferred: JavaScript, Qt Quick)\
**Possible mentors:** bjorn, dogboydog\
**Expected size:** 175 hours when excluding UI work, or 350 hours for the full project\
**Difficulty:** Medium

### General Idea

Compare for example the imperative implementation of a custom tool:

```js
var action = tiled.registerAction("CustomAction", function(action) {
    tiled.log(action.text + " was " + (action.checked ? "checked" : "unchecked"))
})

action.text = "My Custom Action"
action.checkable = true
action.shortcut = "Ctrl+K"

```

With a potential declarative version:

```qml
import Tiled

Action {
    name: "CustomAction"
    text: "My Custom Action"
    shortcut: "Ctrl+K"
    checkable: true
    onTriggered: {
        tiled.log(text + " was " + (checked ? "checked" : "unchecked"))
    }
}
```

One of the main advantages of using a declarative approach, is that it enables the use of bindings to hugely simplify setting dynamic property values. For example, an action that is only enabled when a map is selected could declare:

```qml
    enabled: tiled.activeAsset && tiled.activeAsset.isTileMap
```

Current extension types that should be provided as QML types: `Action`, `Tool`, `MapFormat`, `TilesetFormat` (or a more generic `FileFormat` that declares its supported asset types) and `Menu` (or some way of adding custom actions to a certain menu).

### Potential Additional Types

It would be a nice idea to introduce an `Extension` or `Plugin` type, that could enable dynamically enabling/disabling a certain extension in the UI, and would automatically register/unregister any additions within. For example (based on [AutomapHelper.js](https://github.com/eishiya/tiled-scripts/blob/main/AutomapHelper.js)):

```qml
import Tiled

Extension {
    name: "AutoMap Helper"

    Action {
        id: addUIDsToLayerNames
        ...
    }

    Action {
        id: removeUIDsFromLayerNames
        ...
    }

    Menu {
        extend: "Edit"
        actions: [
            { action: addUIDsToLayerNames, before: "Preferences" },
            { action: removeUIDsFromLayerNames },
            { separator: true },
        ]
    }
}
```

### Existing QML Modules

Care should be taken to integrate nicely with existing QML modules available in Qt. The main module to consider here is the [Qt Quick Controls](https://doc.qt.io/qt-6/qtquickcontrols-index.html) module. It would be great if we could enable Tiled extensions to use this module in general, to enable writing custom UI, as well as to integrate with its `Action` and `Menu` components.

One of the challenges here is to adjust the various Tiled packages to ship the necessary Qt Quick modules.
