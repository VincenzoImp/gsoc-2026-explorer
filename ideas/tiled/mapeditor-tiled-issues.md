# open issues

**Parent:** Tiled — Project Ideas
**Source:** https://github.com/mapeditor/tiled/issues
**Scraped:** 2026-03-10T16:58:40.245036

---

## #4396: Export as Image gives no error when image save fails

### Describe the bug

When using File → Export as Image, if the image file cannot be saved (due to file permissions, an invalid path, or an unsupported file extension), the dialog closes without showing any error. The user gets no indication that the export failed. This is inconsistent with map and tileset export paths, which do show error dialogs on failure.

The root cause is in `exportasimagedialog.cpp` — the return value of `QImage::save()` is not checked.

### Steps to reproduce

1. Open any map in Tiled
2. Go to File → Export as Image...
3. Choose a read-only directory as the save location (or use an unsupported file extension like .xyz)
4. Click Save
5. The dialog closes silently — no image file is created and no error is shown

### Expected behavior

An error dialog should appear informing the user that the image could not be saved, similar to how other export operations (map export, tileset export) report errors when writing fails.

### OS version

Windows 10

### Tiled version

Latest

---

## #4362: Tiled installer for Windows 10+ (64-bit) (21 MB): starts with error :"sticker-knight is not a valid short file name."

**Labels:** windows

### Describe the bug

<img width="496" height="387" alt="Image" src="https://github.com/user-attachments/assets/c6dfb606-317a-4520-81b5-5ecefaa6e4b6" />

Tiled installer for Windows 10+ (64-bit) (21 MB): starts with error message :"sticker-knight is not a valid short file name." 

### Steps to reproduce

1. https://thorbjorn.itch.io/tiled?download
2. Windows 10+ (64-bit) (21 MB) download
3. Install 

### Expected behavior

A would be nice not to have this error message ;-) 

### OS version

Windows 11 24H2 Build : 26100.7840

### Tiled version

1.11.2

---

## #4361: Terrain Tool Expansion - World Compatibility

### Is your feature request related to a problem? Please describe.

Right now, the terrain tool only works for a single TMX file at a time. It would be cool if when drawing near the borders of a map within a world that it automatically detects the edges of adjacent maps and applies the terrain tool's painting where appropriate. 

If a map is also the only in the world, the terrain stamp should detect the opposite edge so that one can easily make looping maps.

### Describe the solution you'd like.

Summary: Instead of clipping at the edge of the map when painting tiles with the Terrain Stamp. It should instead detect the appropriate edge for a TMX file that is adjacent to the one that you are drawing on. I will provide visual cues later.

### Describe alternatives you've considered.

_No response_

---

## #4357: Only some parts of Tiled properly respond to changing windows with a different Display Scale setting

### Describe the bug

This might be related to #2835 (or maybe is the same thing? It seems a bit different from an outside view, but unsure if that's actually the case).

When moving Tiled between a primary monitor with 150% display scale and a secondary monitor with 100% display scale, the fonts and padding seem to resize appropriately, but the UI size/padding/etc. doesn't reflect the changes.

Example image of:
* Maximized notepad window on the primary monitor in the background, as a baseline size reference
* A smaller notepad window also on the primary monitor, for size/behavior reference of another program's behavior
* Tiled on the primary monitor

![Image](https://github.com/user-attachments/assets/56276ff5-e58b-4242-ae18-ec780d507f7e)

Followup example:
* Maximized notepad window still on primary monitor
* Smaller notepad window moved to secondary monitor
* Tiled moved to secondary monitor

![Image](https://github.com/user-attachments/assets/d11c89de-536f-4f6d-8c54-ce252f800544)

You'll notice that Notepad feels the same size (relatively speaking) in isolation, but the window size is actually much smaller compared to when it was on the primary monitor.

Meanwhile with Tiled, the fonts are smaller, but almost everything else is basically the same size. This makes the window itself feel much larger despite technically being the same size, and also makes it seem like most UI elements have an unusually large amount of inner padding.

---

I'm not sure if this is actually Tiled or Qt. I tested with the Windows 64bit Qt6 build, but an interesting thing to note is that the Windows 32bit Qt5 build has a similar problem with slight differences: the outer window size *was* correctly adjusted, and some other things seem closer to what I would expecte too. However, some parts appear to be worse since they didn't account for the window size changing, like the sidebars.

Primary monitor example (conditions matching the first example from before):
![Image](https://github.com/user-attachments/assets/de7b9fe7-8bf2-44df-8263-c9c0b5fc592e)

Secondary monitor example (conditions matching the second example from before):
![Image](https://github.com/user-attachments/assets/b3f4be43-b009-4fb8-8f91-a5fcd9d61925)

### Steps to reproduce

Move Tiled from one monitor to the other.

At least on my computer, you can see the adjustments take place when it gets a little over halfway across the monitor boundary.

### Expected behavior

Every aspect of Tiled to feel appropriately rescaled on the new monitor, not just some parts.

### OS version

Windows 11, 64-bit

### Tiled version

CI build from 2/20/2026 (second from last commit in #4308, commit e794b0a, from action run 22233411625)

---

## #4324: Masking Layer

### Is your feature request related to a problem? Please describe.

I'm creating overworld maps with a lot of different biomes and various terrain mixing patterns, too many in fact (over 10'000 variations).

In game I'm using full tiles and many layers for the terrain, with masks to mix them all together. I'd love to be able to have this in Tiled!

### Describe the solution you'd like.

A mask layer would apply to all layers under it. The layers below would be rendered and then alpha multiplied with the mask's alpha (or using grayscale, whatever is easiest), which will allow one to mask layers!

I assume they would be placed in groups where they'd only apply to the layers in their group.

### Describe alternatives you've considered.

As far as I know there are no alternatives, if there is one (that doesn't involve generating thousands of tilesets) please let me know!

---

## #4306: [Project Folder View] Collapse All/"Only expand to current"

### Is your feature request related to a problem? Please describe.

In the case that the project has a lot of nested folders, the folder view becomes hard to navigate, especially when folder names are ambiguous. User has to manually collapse each folder.

### Describe the solution you'd like.

At the most basic level, a "Collapse All" button can be added on the top of Project folder view near the title to collapse all expanded folders.

With an additional LOE there can be a toggleable setting to "Only expand to current", i.e., collapse all folders other than the one containing the currently active file in the editor.

### Describe alternatives you've considered.

if `"expandedProjectPaths"` in the tiled project session were exposed to the Tiled API, it could be scripted externally.

---

## #4298: Add optional labels to maps in worlds

### Is your feature request related to a problem? Please describe.

When I'm creating levels for a game, it is usually done linearly. Sometimes though, I might find that a level I am creating works better earlier than it's intended. e.g. level 3 works better as level 2 and level should 2 should actually be level 3.

I then reorder them in the world file so I can visually see this but this isn't clear anywhere else.


### Describe the solution you'd like.

This reordering works however I can't visually tell anymore than level 3 is now level 2 and it's something I have to remember myself.

If there was kind of optional label above each, it would reduce the cognitive load.
Something like this:

<img width="1416" height="436" alt="Image" src="https://github.com/user-attachments/assets/7a5e309a-9db8-41b7-b69b-6177b79abe70" />

My suggestion is to add  `name` field to the map. This would be consistent with how objects currently display their names while in the map

### Describe alternatives you've considered.

Renaming the files is the obvious solution but I find this a bit clunky, it takes me out of the editing experience. It's also not very source-control friendly.

---

## #4291: BIG-BUG!!!!!!!! firstgid corruption when editing multiple maps sharing tilesets

### Describe the bug


Our designer encountered firstgid corruption when working with two maps that share some common tilesets.

**Actual Behavior:**
After saving Season_1_miniMap, the firstgid values for shared tilesets are overwritten and become inconsistent with their original values.

**File Evidence:**

*Normal Season_1_miniMap (before corruption):*
```xml
<tileset firstgid="264" source="../tilesets/s1/easy_water/s1_easy_water.tsx"/>
<tileset firstgid="288" source="../meta_tilesets/collision_check/collision_check.tsx"/>
<tileset firstgid="290" source="../tilesets/s1/one_tree/s1_2x2sk.tsx"/>
<tileset firstgid="294" source="../tilesets/s1/xzddb/s1_xzddb.tsx"/>
<tileset firstgid="298" source="../tilesets/s1/xzddb/s1_xzddb_c.tsx"/>
<tileset firstgid="314" source="../tilesets/s1/map_anim_objs/map_anim_objs_tileset.tsx"/>
```

*Normal Season_1:*
```xml
<tileset firstgid="270" source="../tilesets/s1/easy_water/s1_easy_water.tsx"/>
<tileset firstgid="408" source="../tilesets/s1/xzddb/s1_xzddb.tsx"/>
<tileset firstgid="412" source="../tilesets/s1/xzddb/s1_xzddb_c.tsx"/>
<tileset firstgid="428" source="../tilesets/s1/one_tree/s1_2x2sk.tsx"/>
<tileset firstgid="432" source="../tilesets/s1/db_2/s1_db.tsx"/>
```

*Corrupted Season_1_miniMap (after saving):*
```xml
 <tileset firstgid="264" source="../tilesets/s1/easy_water/s1_easy_water.tsx"/>
 <tileset firstgid="402" source="../meta_tilesets/collision_check/collision_check.tsx"/>
 <tileset firstgid="404" source="../tilesets/s1/one_tree/s1_2x2sk.tsx"/>
 <tileset firstgid="408" source="../tilesets/s1/xzddb/s1_xzddb.tsx"/>
 <tileset firstgid="412" source="../tilesets/s1/xzddb/s1_xzddb_c.tsx"/>
 <tileset firstgid="428" source="../tilesets/s1/map_anim_objs/map_anim_objs_tileset.tsx"/>
```

**Suspected Cause:**
We suspect that Tiled might be treating tileset objects as globally shared instances, and the firstgid assignment logic might be using a global context instead of being map-specific.

### Steps to reproduce

1. Open and edit `Season_1.tmx`
2. Then open and edit `Season_1_miniMap.tmx`  
3. Save `Season_1_miniMap.tmx`
4. The firstgid values for shared tilesets become corrupted

### Expected behavior

Each map should maintain its own firstgid assignments for tilesets, even when they reference the same source tileset files.

### OS version

Windows 10

### Tiled version

1.11.2

---

## #4290: Change Clipboard Mime-Type to Support Text

### What is the current behavior?

Tiled checks for `text/tmx` as the mime-type of your clipboard before enabling the `Paste` function (as defined in [src/tiled/clipboardmanager.cpp](https://github.com/mapeditor/tiled/blob/a43264f4b5dc6f8b7832189644696df12fa500c3/src/tiled/clipboardmanager.cpp#L50)). However, the content copied from and pasted into Tiled (as held in the clipboard) is simply Tiled XML in plain text.

### Why is this a problem?

Using the mime-type `text/tmx` means it is only possible to copy and paste within Tiled itself. External programs (specifically web browsers) are not typically able to set their clipboard to uncommon mime-types (like `text/tmx`) thus eliminating any copy/paste interoperability between web browsers and Tiled which would otherwise be possible. 

For example, I would like to create a web application that will generate Tiled XML objects with Custom Properties that I can paste into Tiled (without having to manually configure them in Tiled), but no modern web browser will allow the clipboard mime-type to be set to `text/tmx` thus the web app would be pointless (as you would have to download the generated TMX, open it in Tiled, copy the objects, then paste them in the destination TMX).

### What is your proposed solution?

Change the mime-type on Line 50 in `clipboardmanager.cpp` to `text/plain` so programs like browsers are able to general valid Tiled XML that can be pasted directly into Tiled. Please see [Pull Request 4289](https://github.com/mapeditor/tiled/pull/4289).

In my testing, simply changing the mime-type to `text/plain` allows Tiled XML to be directly pasted into open TMX maps without any obvious side effects (attempting to paste invalid XML or gibberish text fails and does not affect the Tiled map in any way).

---

## #4260: Qbs: installing header files should not include moc output

Judging by the files included in the Fedora `tiled-devel` package, the option to install header files is causing the `moc_*.cpp` files in libtiled to be installed as well:

```
bjorn@thor:tiled$ dnf repoquery -l tiled-devel
Updating and loading repositories:
Repositories loaded.
/usr/include/tiled
/usr/include/tiled/compression.h
/usr/include/tiled/containerhelpers.h
/usr/include/tiled/fileformat.h
/usr/include/tiled/filesystemwatcher.h
/usr/include/tiled/gidmapper.h
/usr/include/tiled/grid.h
/usr/include/tiled/grouplayer.h
/usr/include/tiled/hex.h
/usr/include/tiled/hexagonalrenderer.h
/usr/include/tiled/imagecache.h
/usr/include/tiled/imagelayer.h
/usr/include/tiled/imagereference.h
/usr/include/tiled/isometricrenderer.h
/usr/include/tiled/layer.h
/usr/include/tiled/logginginterface.h
/usr/include/tiled/map.h
/usr/include/tiled/mapformat.h
/usr/include/tiled/mapobject.h
/usr/include/tiled/mapreader.h
/usr/include/tiled/maprenderer.h
/usr/include/tiled/maptovariantconverter.h
/usr/include/tiled/mapwriter.h
/usr/include/tiled/minimaprenderer.h
/usr/include/tiled/moc_fileformat.cpp
/usr/include/tiled/moc_filesystemwatcher.cpp
/usr/include/tiled/moc_logginginterface.cpp
/usr/include/tiled/moc_mapformat.cpp
/usr/include/tiled/moc_objecttemplateformat.cpp
/usr/include/tiled/moc_plugin.cpp
/usr/include/tiled/moc_pluginmanager.cpp
/usr/include/tiled/moc_properties.cpp
/usr/include/tiled/moc_templatemanager.cpp
/usr/include/tiled/moc_tileanimationdriver.cpp
/usr/include/tiled/moc_tilelayer.cpp
/usr/include/tiled/moc_tilesetformat.cpp
/usr/include/tiled/moc_tilesetmanager.cpp
/usr/include/tiled/moc_tmxmapformat.cpp
/usr/include/tiled/moc_world.cpp
/usr/include/tiled/object.h
/usr/include/tiled/objectgroup.h
/usr/include/tiled/objecttemplate.h
/usr/include/tiled/objecttemplateformat.h
/usr/include/tiled/objecttypes.h
/usr/include/tiled/orthogonalrenderer.h
/usr/include/tiled/plugin.h
/usr/include/tiled/pluginmanager.h
/usr/include/tiled/properties.h
/usr/include/tiled/propertytype.h
/usr/include/tiled/savefile.h
/usr/include/tiled/staggeredrenderer.h
/usr/include/tiled/templatemanager.h
/usr/include/tiled/tile.h
/usr/include/tiled/tileanimationdriver.h
/usr/include/tiled/tiled.h
/usr/include/tiled/tiled_global.h
/usr/include/tiled/tilelayer.h
/usr/include/tiled/tileset.h
/usr/include/tiled/tilesetformat.h
/usr/include/tiled/tilesetmanager.h
/usr/include/tiled/tmxmapformat.h
/usr/include/tiled/varianttomapconverter.h
/usr/include/tiled/wangset.h
/usr/include/tiled/world.h
```

### Steps to reproduce

Install the `tiled-devel` package on Fedora.

### Expected behavior

The `moc_*.cpp` files are not expected to be present.

### OS version

Linux Fedora

### Tiled version

1.11.2

---

## #4252: Panning with 2-finger scroll triggers an "initial boost" that overshoots

### Describe the bug

This is not about "cursor sensitivity", this only happens when trying to pan. After the app detects that the user is "panning", the exaggerated acceleration is reverted to normal while the user is panning

### Steps to reproduce

1. Open a map or tileset
2. Use a touchpad with 2-finger scroll gesture enabled (this should be reproducible with a traditional mouse wheel)
3. Scroll vertically or horizontally (hold, from now on)
4. Notice a long delay before any panning happens
5. Then the view overshoots far from intended
6. Further panning is "stable"
7. Stop holding

This is not a lag issue either, because I can see the UI is fluid and CPU usage isn't high

### Expected behavior

Panning should have the same sensitivity all the time. No "boost"

### OS version

Debian Testing

### Tiled version

1.11.0

---

## #4237: Option to show the camera bounds of the in-game view

### Is your feature request related to a problem? Please describe.

I'm making a little GBA game with tons of parallax. So I use the parallax feature of the Tiled editor to represent that. But I've noticed that the parallax appears far more extreme in the editor, because my view is likely zoomed out significantly, which scales the parallax scrolling.

So I thought it'd be nice to be able to see exactly what's going to appear in-game while editing, in the form of a little box in the center of the screen that has the same size as the in-game view.

This will likely benefit level designs that don't use parallax, as well, since level designers can more clearly see what's on-screen at any given moment.

### Describe the solution you'd like.

I suggest adding an option in, say, the map properties to specify the size of the in-game view (such as 240×160 pixels in my case). In addition, there should be a toggle in the "view" menu that simply draws a rectangle of that size in the middle of the viewport.

### Describe alternatives you've considered.

I've also come up with a simple workaround that I'm currently using, in which I have an object layer with a parallax factor of 0 (so it's fixed to the viewport) with a rectangle object in the center. This works pretty well, and the only real downsides are that it's a bit hacky and will require that I inform the engine that this isn't an actual object.

I'm honestly fine with it, so this proposal is really more about making something more standardized and less hacky than filling some gap in the editor's feature set.

EDIT: This hack also has the downside that the inside of the rectangle object is slightly tinted. It's not a lot, but it is slightly noticable.

<img width="1108" height="730" alt="Image" src="https://github.com/user-attachments/assets/5a3a39fd-ee50-445a-ba1d-b4e0fe6a29e2" />

---

## #4229: Isometric Map built from 2D tileset

### Is your feature request related to a problem? Please describe.

It would be useful if the editor would support building isometric maps from 2D tilesets by doing isometric projection on the fly. 

Benefits:
- Editor can now be use in 2D and 3D isometric engines
- 2D tileset arrangement greatly improves texture space utilization by tightly packing tiles (there is no wasted space like in isometric tiles)

### Describe the solution you'd like.

The category for tile projection could be specified on a tileset level:
- Ground
- Wall

Tile level ?
- Draw offset should be specified on the tile level to avoid duplicating tile.

Bonus features:
- Specify tile texture filtering: nearest, linear
- Allow to specify any wall Y rotation to increase the degree of freedom and expression

<img width="902" height="439" alt="Image" src="https://github.com/user-attachments/assets/3ac2591f-7169-480e-b4e3-3f4803f1dd29" />

### Describe alternatives you've considered.

_No response_

---

## #4217: Updating map position in world via javascript extension cannot be undone.

### Describe the bug

Updating a map's location in a world via an extension doesn't update the undo stack, so it cannot be undone.

### Steps to reproduce

Load a world file with at least one map.
Call world.setMapPos or setMapRect from an extension to move any map in the world.
try to undo the change, the map won't move back to it's previous location.

### Expected behavior

Hitting undo should return the map to it's previous position.

### OS version

Windows 11

### Tiled version

1.11.2

---

## #4216: Properties editor becomes hard to read because of color contrast on Breeze Dark

### Describe the bug

Part of the new properties editor is illegible in the Breeze Dark colorscheme:

<img width="307" height="686" alt="Image" src="https://github.com/user-attachments/assets/33b30621-8a08-46bb-ac18-f83be75a40ac" />

It could be that the wrong color roles for the color scheme are being used.

### Steps to reproduce

Set the system colorscheme to Breeze Dark and the Tiled theme to Native

### Expected behavior

Be legible

### OS version

openSUSE Tumbleweed Linux

### Tiled version

2025.06.13

---

## #4201: Bugs / Inconsistencies with Fullscreen, Keybindings, Status Bar, Vertical Sorting.

Hi everyone, 

I got lots of bugs and inconsistencies in Tiled noticed.

**Specifications:**
 - OS: Win11 Pro
 - Tiled Version: Version 1.11.2

### **1. Bug with Fullscreen mode:**
- In Fullscreen mode (via TAB), no rotation is possible of Objects or flipping, or other transformations - when using keybindings.

### **2. Bug with vertical position:**
- Click on Object in Map and then you can use PageUp and PageDown perfectly as intended. Also Home / End works for shifting Object vertically in its list.
- Click on the same Objects, but via Widget "Objects", then only PageUp / PageDown work the same way (or sometimes not?). But Home / End don't work, here the cursor jumps to first and last entry. Or vice versa, I couldn't reproduce it every time - seems to be also about selecting Objects or where the mouse cursor is?

### **3. Missing feature in Tile Collision Editor:**
- Tile Collision Editor: I can't use "DEL" as a keyboard shortcut to delete a polygon when having a polygon selected. But this shortcut works elsewhere, e.g. on Tiles. Should be more consistent.
- EDIT: This bug only appears when trying to delete Polygons within Objects which are part of an Image Collection. For normal Tileset Tiles, I have no problems. This is also independent of any custom properties being present, I just tested it.

### **4. Inconsistencies with Tools / Hotkeys:**

**4a. Rectangular Select Tool:** 
- Here I miss the SHIFT effect I have with the Shape Fill Tool (helping 1:1 square sized form)
- I miss the same when forming selection in the "Tilesets" widget, here I also want to use SHIFT to select a square selection. I would also like to have a status bar inside the Tilesets view then. I don't mean the fullscreen Tilesets, I mean when selecting Tiles for placing it in the Map.

**4b. Stamp Brush:**
- When I hold down right mouse button to span a rectangle for picking Tiles, I would expect in the Status bar the size info. 
![Image](https://github.com/user-attachments/assets/63b59b2c-4099-42b7-b407-dd5be72482d0)

**4c. Terrain Brush:** 
- Here I miss the Status bar info about the size / length I'm holding down before confirming.

**4d. Eraser:** 
- When holding down SHIFT, I would expect the same behavior as I have with using the Stamp Brush. With the Stamp Brush, I can hold down SHIFT after clicking the first time and it suggests a line I can confirm to paint. Additionally, I would like to also have the Status bar info here about size / length.

**Overall, all tools should work the same way regarding holding down SHIFT / CTRL and also give the same status bar info about rectangle / line size / length.** 

Cheers,
Abo

---

## #4193: Crash occurs with multiple iterations of instantiating TileMap objects via tiled.registerMapFormat.

**Describe the bug**
The initial load of the World file works as expected.
Upon unload and any subsequent reload, Tiled crashes.
If you uninstall and reinstall Tiled, the World file will load without issue.
If you rename the World file to a filename not previously seen by Tiled, the World file will load without issue.

**To Reproduce**
Steps to reproduce the behavior:
1. Load world using an API registered map format.
2. Unload the world.
3. Reload the world.
4. Tiled crashes

**Expected behavior**
The world will load just as it did upon its initial load.

**Specifications:**
 - OS: Windows 11
 - Tiled Version: Reproduced on 1.11.0 and 1.11.2

---

## #4189: tiled crash when trying to select an object in warn/error callback from issues view

**Describe the bug**
When registering a callback for tiled.warn or tiled.error and clicking on it in the issue tab tiled crashes when setting selected or trying to change selectedObjects

```ts
tiled.warn("test", function () {
	if (obj) {
		// First select the object
                obj.map.selectedObjects = [];
		obj.map.selectedObjects.push(obj);
		// obj.layer.selected = true;
		// obj.selected = true;

		// Then center the view on it
		tiled.mapEditor.currentMapView.centerOn(obj.x + obj.width / 2, obj.y + obj.height / 2);
	}
});
```

**To Reproduce**
Steps to reproduce the behavior:
1. Go to the issues tab
2. Double Click on 'the warning or error
3. tiled crashes to desktop with no error

**Expected behavior**
That the object would be selected in the tiled editor

**Specifications:**
 - OS: Windows 11
 - Tiled Version: 1.11.2

---

## #4185: Bad performance when painting over existing tiles

**Describe the bug**
At least on big maps (1024x1024 tiles), painting over existing tiles with the stamp brush results in very poor performance (read: unusable).

**To Reproduce**
- Create a 1024x1024 maps, 100x100px tiles
- Use 2 tilesets of 100 separate tiles each. Each tileset has its own image ("Collection of images")
- Select all the 100 tiles of tileset 1. Fill the entire map with the bucket fill tool in random mode so that you have different tiles every where.
- Select one tile of tileset 2. Select the stamp brush tool. On the same layer, attempt to paint over existing tiles by clicking and dragging the mouse.
- Notice that performance is so bad it's unusable. Everything hangs for seconds on each mouse drag. The longer the drag, the longer the hang.

Performance is good when you clear a small patch before painting (with the rectangle select tool and hitting delete). So it seems to be a problem with drawing over existing tiles (drawing over empty tiles is fine).

Performance is also good if you paint on a new layer.

**Expected behavior**
Painting should not provoke hangs.

**Specifications:**
 - OS: Arch Linux
 - Tiled Version: v1.11.2

I tried to see what was going on by running perf record while painting one tile every second. Please find the perf report attached. I'm not sure how helpful it is.

[perf4.txt](https://github.com/user-attachments/files/19506344/perf4.txt)

---

## #4183: Layer tint color doesn't affect shapes

**Labels:** documentation

**Describe the bug**
The tint color property in layers doesn't seem to affect objects, the Color property does tint shapes, but this property is not documented neither in the JSON format or the API.

**To Reproduce**
Steps to reproduce the behavior:
1. Set the value for Tint color in a layer with shapes.
![Image](https://github.com/user-attachments/assets/a38c1d4e-73d8-4356-9688-73809e853f63)
2. The shapes are not tinted.
3. Set the value for Color in a layer with shapes.
![Image](https://github.com/user-attachments/assets/60d309e6-bb64-4b89-bec5-0615a19c9a4a)
4. The shapes are tinted.
5. The Map JSON now has a property `color`

**Expected behavior**
Tint the shapes when setting the layer property TintColor.

**Specifications:**
 - OS: Linux
 - Tiled Version: 1.11.2

---

## #4177: Activating the Erase Terrain button fails to switch to Terrain Brush

**Describe the bug**
erase terrain does not switch the tool to the terrain tool

**To Reproduce**
Steps to reproduce the behavior:
1. select stamp tool
2. click on erase terrain
3. the tool is not changed to the terrain tool

**Expected behavior**
clicking erase terrain should switch the current tool to the terrain tool

**Specifications:**
 - OS: arch linux
 - Tiled Version: Tiled 1.11.2

---

## #4169: Allow custom properties to be assigned a unique color to show inside of tileview/mapview/tileset preview windows

**Is your feature request related to a problem? Please describe.**
I love how flexible Tiled is with custom properties. It allows me to keep all my map related configs in one editor. My biggest gripe with tiled is it's impossible to visually see what tiles have custom properties and which dont.

**Describe the solution you'd like**
It'd be amazing if we could assign a color value to each property type (optional maybe?) and use that color to outline the tile on the mapview/tileview/tileset preview window. Also, show the color when the tile is selected next to the custom property itself.

**Describe alternatives you've considered**
Can't think of any other than using a different map editor. For example, I have an "interactable" property which allows me to configure if the tile is interactable in game or not. Currently, it's impossible to quickly see all the interactable tiles in your tileset. 

It doesn't need to be a color either, just some sort of visual representation to see. I picked color since it would be easy to have several colors representing several properties by using a dashed outline with different colors.

---

## #4159: Report similar class/type for tileset

**Is your feature request related to a problem? Please describe.**
Want suggest a option to Report similar class/type for tileset

**Describe the solution you'd like**
Pop'up maybe as "Exist similar class/type for tilest" and log about.

**Describe alternatives you've considered**
Resolve problem when importing .tmx and .tsx ? Eg. ask what to do if exist?

Not sure about good practice around this type case.
Some times this same type name have other id.
Also is possible to have this same name for tilesets when importing or something what is not good solution.

---

## #4156: Tiled/extensions/SelectLayerTiles.js:33: TypeError: Cannot call method 'disconnect' of undefined

**Describe the bug**
`..AppData/Local/Tiled/extensions/SelectLayerTiles.js:33: TypeError: Cannot call method 'disconnect' of undefined`

**To Reproduce**
After created new project in new installation Tiled Version: 1.11.1

**Expected behavior**
No errors

**Media**
 

**Specifications:**
 - OS: W11
 - Tiled Version: 1.11.1

---

## #4155: Map with numbers - preview

**Is your feature request related to a problem? Please describe.**
Due map is starting from 0,0 and user operating on some logic as shift square, enemy etc, is good to see map cordinations without operate mouse and cursor - right now user must check on down belt the coordination.

**Describe the solution you'd like**
Looking something like "virtual" sprites with numbers under or above images as transparent (option to set alpha), all in grid.
Due possible long map, the numbers can be to big, by this require a number size.

**Describe alternatives you've considered**
Something like "axes" can be helpful around map as numbers above with cross line to spy coordination of tile.
More cognitive can be grid line difference, eg. units 5, 10 as solid, other type line style or color (for configuration) - if have big map is hard to recognize cords and especially in debug process.

---

## #4153: Option to clip map contents to map bounds

## Problem

When using Image Layers (with repeat X/Y, or with oversized images), or when using oversized tiles, the contents of a map can be much larger than its bounds, causing it to get in the way of other maps in its World. Even when editing such a map without other maps visible, this overspill can misrepresent the map, since in most cases, engines will only show in-bounds content.

## Proposal
A View option to crop the map contents to the map bounds. This should affect at least Image and Tile layers, where it should be relatively straight-forward.

### Objects
For Object Layers, the situation is trickier - Objects don't usually get in the way as much, and it's often desirable to see when an Object is out of bounds even when other layers are clipped and indeed, clipping the other layers may be desirable to help see such Objects better. But, games that use Objects decoratively may also want to clip them to the map bounds. Perhaps there should be a separate View option for Objects, with three options: Show All, Clip to Map Bounds, Hide Out of Bounds. The difference between the latter two would be in how Objects that straddle the map boundary are displayed - clipped, or shown in full. If clipping Objects to map bounds is too complicated, then an option to hide Objects that are completely out of bounds would be fine.

### Other concerns
- The rectangular bounds can be used for non-orthographic maps.
- Parallax should be calculated before the crop, so that parallax cannot cause the map's visuals to extend beyond its bounds.
- Infinite maps don't have defined bounds, but clipping is still useful for those. Infinite maps should be clipped to the bounds Tiled displays for them, i.e. some multiple of the 16x16 chunks Tiled uses internally.
- These options should *not* be tied to Worlds, as clipping map contents can be useful even in stand-alone maps.
- Maps with foreground parallax layers have larger bounds than their "actual" bounds, and users may want to clip to a smaller rectangle than the map bounds. Even if per-layer sizing is added, the map size would probably be the largest of those layers rather than an arbitrary size (which would be convenient for Tiled map loaders, since it would give them a maximum tile layer size right away), then per-layer sizing won't solve the problem of foreground parallax making the clipping region too large. Clipping to the layer bounds also wouldn't help. To accomodate maps with foreground parallax, it would help to have a clipping rect property on the map which, if not set, is the same as the map's current bounding area. The reason it should be a rect rather than a size is to accommodate infinite maps, but it would be useful for some finite maps with "margin" areas too.

---

## #4150: Tiling Disabled After Closing Donation

The ability to tile stuff is disabled after closing the donation box, even if I click maybe later or don't remind me.

This is the kind of nonsense closed source software does. If I wanted features disabled, I'd go pay for software I can't afford.

---

## #4130: Make "file not found" behavior more source control friendly

**Is your feature request related to a problem? Please describe.**
Every time an open file is deleted or moved, Tiled pops up a dialog that requires user interaction to resolve, like this:
![image](https://github.com/user-attachments/assets/a4f63d20-a238-4a2e-a989-c69c01ad2106)

This gets very frustrating very quickly when you have a lot of maps open and you're working with source control. I use git, and I'm often moving between branches or commits, stashing and un-stashing changes, etc., and there's a constant cacophony of error dialog sounds from Tiled and an ever increasing stack of dialogs like the one above I have to press "OK" on before I can resume work after I'm done.

**Describe the solution you'd like**
I love the way Visual Studio Code deals with this situation. The open file gets a red color and a strikethrough on the open file tab, but otherwise nothing happens:
![image](https://github.com/user-attachments/assets/72c16651-e34a-4db7-86ed-8a67aa317238)
and if you bring the file back, it reloads it and goes back to showing it as a normal, open tab:
![image](https://github.com/user-attachments/assets/e9f111d2-c2f9-4dd1-b859-de19622e9b35)

If you happen to be editing the file and it is removed and restored *with different changes* since you started editing it, you will be notified of this only when attempting to save your new changes:
![image](https://github.com/user-attachments/assets/f87e0148-37ff-4481-953f-e7cbab4efb88)
and again, it's an important detail that this only shows up when the file being saved is *different* on disk than when the edit started. So even if you made a bunch of edits to the file behind the scenes, it'll still save just fine if the contents of it is back to what VSCode expects by the time you save, or if you deleted it.

**Describe alternatives you've considered**
Something that does work is closing all the maps before doing file operations as the editor only complains about rug pulls on open files. But it's easy to forget and a less friendly option when making on-going changes to multiple files that you like keeping open.

---

## #4128: request: isometric tilemaps with height and specific tools

**Is your feature request related to a problem? Please describe.**
We can't create tilemaps where each tile can have a height

**Describe the solution you'd like**
I would like to request support for isometric tilemaps with support for height of the tiles.
Example is the map in openrct2

https://openrct2.io/

---

## #4126: Enabling the use of QML for Tiled extensions

**Labels:** Winter Of Code 4.0

As of Tiled 1.11, extensions can be written in plain JavaScript files or as JavaScript modules. However, Tiled actually uses a [`QQmlEngine`](https://doc.qt.io/qt-6/qqmlengine.html) internally, which is able to load [QML files](https://doc.qt.io/qt-6/qmlapplications.html) as well.

See [Next generation Tiled extensions](https://github.com/mapeditor/tiled/wiki/Next-generation-Tiled-extensions) for more information about this idea.

When the necessary libraries and plugins are available, [`Qt.createComponent`](https://doc.qt.io/qt-6/qtqml-javascript-dynamicobjectcreation.html) can already be used to instantiate QML types. A nicer integration should be possible when Tiled recognizes QML files and creates [`QQmlComponent`](https://doc.qt.io/qt-6/qqmlcomponent.html#QQmlComponent-1) instances with those files and creates objects from them.

---

## #4118: Add a flag so custom classes and custom enums are only usable as class members

**Feature request description**
As far as I know, it is currently not possible to select which custom enums we see when adding a new property.
We always see all available enums, while some of them could only be used through custom classes (and not directly added as properties).
It would be nice to be able to select which enum to show or to hide.

**Describe the solution you'd like**
When creating a new custom enum, add the possibility to hide it when adding new properties, ie. to not use it as a property value.

It could be done the same as for custom classes, by adding a `Property value` tickbox:
![image](https://github.com/user-attachments/assets/f38bd3e5-ac20-49c1-8649-98e2d154b7b3)

For JSON export, we could use the same `useAs` array but only take into account the `property` value.

---

## #4117: Custom Property Extension: String Validation

**Feature**

We have started using Tiled as our all-in-one map builder for a game in my custom engine. The long-story-short is that we have decided to attach dialog to characters on the map per character occurrence, and need a way to validate the text for the writer.

**Proposed Solution**

Because this is potentially a niche use-case, I think the broader solution is the ability to add an extension that creates a custom-named string property type, which can be validated by the extension. Even just turning the box outline red and showing some text when invalid is enough for this specific use-case.

**Alternatives Considered**

I made an external tool that does exactly this basic functionality, but getting the writer to cross-reference an associated dialog ID in Tiled to the tool is proving difficult. If they could find the character on a map and edit a property of a custom type "Dialog" to get immediate feedback, that would make Tiled a perfect solution for our use-case.

**Notes**

I'd be willing to contribute towards this if I can get some feedback on whether this could be approved, and would be useful to others.

---

## #4116: "Contiguous" option for Bucket Fill and Magic Wand tools

**Labels:** missing feature

### Request
It would be nice to have a "contiguous" toggle for the Bucket Fill and Magic Wand, allowing them to affect tiles in non-contiguous region. Currently, non-contiguous fills require first selecting all those tiles and then using Shift+Bucket Fill to fill those areas, but with a "contiguous" toggle, this behaviour could be achieved without any selections, without additional tools.

This toggle should, if possible, be a checkbox with the label "Contiguous" next to it, rather than an icon like the other tool options, as there does not appear to be any iconography associated with this concept. Every program I've ever seen describes this option only as text.

### Justification
Non-contiguous bucket filling is useful for replacing tiles within a layer. For example, one may want it for making similar sets of Automapping rules, for replacing shallow water with deep water, filling flat areas with a pattern/random tiles, and so on. It would be nice to not need extra tools and a modifier key to do this :] If we get Terrain Mode on the bucket fill, non-contiguous bucket filling will get even more useful, allowing quick, terrain-aware replacement of one terrain with another, and selections would likely get in the way of that feature more than plain tile Bucket Fill.

Tiled already has the Select Same Tile tool for non-contiguous selections, but I feel that if Bucket FIll has a contiguous toggle, then so should Magic Wand for consistency. This would make Select Same Tile obsolete.
The benefits of this is that it'll remove a tool from the toolbar and bring the tooling more in line with other software like Aseprite (but further away from GIMP, after which these tools were modelled). The drawback is that if a user needs to frequently alternate between the two selection modes and other tools, it may require extra clicks, since they'll need to first click the Magic Wand Tool, and then check/change the Contiguous option. In my experience in other software, this has not been a problem.
I'll miss the Select Same Tile icon though, it's probably my favourite in Tiled :]

### Comparison to other programs
GIMP works just like Tiled: Separate contiguous and non-contiguous selection tools. Bucket Fill is only Contiguous, but with a non-contiguous selection, you can shift+Bucket Fill to fill it (provided you have the "fill selection" option chosen for the Shift behaviour).
Krita has separate contiguous and non-contiguous selection tools, but a contiguous toggle on its Fill tool. An odd inconsistency.
Aseprite and Photoshop have contiguous toggles on both their Magic Wand and Paint Bucket tools, like what I'm requesting here.

Bjorn noted on Discord,
> at the time that [the two selection tools and bucket fill] was implemented I don't think we had the toolbar with tool options available.

Tiled's current tool set-up, with a toolbar that can also have tool-specific options displayed, is most like that of Aseprite and Photoshop, which is perhaps why 

*[truncated]*

---

## #4112: request: right mouse button to scroll map

**Is your feature request related to a problem? Please describe.**
There is no mouse action to scroll the map in a fast way

**Describe the solution you'd like**
I wouls like to request: right mouse button to scroll map (button pressed)

---

## #4111: question: compiling using visual studio

**Labels:** documentation

Hi

Can you explain where to download Qbs and how to install it in order to compile with visual studio?

![afbeelding](https://github.com/user-attachments/assets/ba3ea9ad-8dd5-4c2e-84da-c1d4618b462e)

Is it possible to update it so we can use visual studio 2022? Visual studio 2017 is incredibly not up to date anymore...

---

## #4106: Use TileMapLayer for Godot exports as opposed to deprecated TileMap

**Describe the bug**
Tiled exports to Godot using the `TileMap` node which has been deprecated (https://docs.godotengine.org/en/stable/tutorials/migrating/upgrading_to_godot_4.3.html#id4). 

I think the change on the plugin is small-ish, it currently produces this:

```
[node name="01" type="Node2D"]

[node name="TileMap" type="TileMap" parent="."]
tile_set = ExtResource("TileSet_0")
format = 2
layer_0/name = "Ground"
layer_0/tile_data =  PackedInt32Array(...)
```

We want:
```
[node name="01" type="Node2D"]

[node name="Ground" type="TileMapLayer" parent="."]
tile_set = ExtResource("TileSet_0")
use_parent_material = true
tile_map_data = PackedByteArray(...)"
```

So the primary complexity is implementing the change from the int32 array into the data format in the byte array.

I'm not sure if the specs are documented anywhere, but the Godot code is easy enough to follow as a spec (https://github.com/godotengine/godot/blob/9aed9eca40127bcf21ecd71d25fe8809f345d9e3/scene/2d/tile_map_layer.cpp#L2844) and the marshaling functions are defined here https://github.com/godotengine/godot/blob/9aed9eca40127bcf21ecd71d25fe8809f345d9e3/core/io/marshalls.h.

**To Reproduce**
Steps to reproduce the behavior:
1. Export a map to Godot
2. Open map in Godot
3. See deprecation warning for the use of a `TileMap` node

**Expected behavior**
The export should not produce a deprecation warning.

**Specifications:**
 - OS: macOS
 - Tiled Version: 1.11.0

Not exactly sure if this is a bug or a feature request, please feel free to re-label.

---

## #4097: Allow pattern matching on automap input and output.

**Is your feature request related to a problem? Please describe.**
When working with Tiled, I design dungeons from a top-down perspective and have multiple levels / elevations by organizing the project into groups:
![bild](https://github.com/user-attachments/assets/fe2679bd-4d1e-4e28-a005-3768fbba2e4d)
Today I must edit the layer names of the input and corresponding output layer removing the trailing index number before I start automapping the dungeon layout. And then when I want to work on an other elevation, I need to re-add the indices and start the process over.

**Describe the solution you'd like**
If the automapping could be done with pattern matching like `input_in%d` and `output_out%d` so that edits to a layer called `in2` only outputs to `out2` would be really neat.

**Describe alternatives you've considered**
I've tried reading through the documentation and the issue backlog and haven't found any workaround besides the procedure I describe.
I noticed issue #428 is sort of similar, but I think, it is somewhat orthogonal.

---

## #4096: Create JSON Schema for Tiled json format

**Is your feature request related to a problem? Please describe.**
- Get up-to-date C parser for tiled json files. Not sure which C parsers are up-to-date, whether they read all or some part of the file etc.

**Describe the solution you'd like**
- Create (and maintain) official JSON Schema and then use [quicktype](https://app.quicktype.io/?utm_source=awesome-jsonschema) to generate C code.
- Note that code can be generated for over 20 languages

**Describe alternatives you've considered**
- Three C libraries linked to in docs.

**Additional notes**
- Such approach is provided by ldtk [here](https://ldtk.io/docs/game-dev/loading/#2-the-quicktype-way) which I tested and works well
- Dedicated library might have more ergonomic API. The generated parser, for example, uses list to iterate over multiple elements (`list_get_head(ldtk->levels)`) instead of regular array access
- JSON Schema can contain description for various data which is later added to the code in form of comments.
- JSON Schema could be used to generate documentation, example: [here](https://github.com/adobe/jsonschema2md), and [here](https://github.com/coveooss/json-schema-for-humans)
- JSON Schema could be converted to XSD schema (if needed): [here](https://www.convertsimple.com/convert-json-schema-to-xsd/)
- There are tools to generate JSON Schema from json file, which could serve as a starting point: [here](https://www.jsonschema.net/)

Documentation of the json format has to exist in some form: html, markdown or JSON schema. Moving to adopting JSON schema might thus potentially be only one off cost.

---

## #4095: Scripting: `tiled.open()` and `Asset.save()` in scripts executed via CLI

When running scripts via command line interface, there is no good way to open and save Tiled assets. Such scripts are responsible for opening any Assets mentioned in their arguments, or may choose which Assets they'd like to open (e.g. all the Assets in a Project), but the only method available to open Assets seems to be via MapFormat/TilesetFormat. The only other option is to run a scripted exporter via `--export-map/tileset`, where Tiled will handle loading the (single) initial asset for you.

In addition, it's a common task to modify some asset via a script and to then save it, but once again, the only option to save an Asset in a script run via CLI is MapFormat/TilesetFormap, one can't simply `map.save()` like one can in the GUI.

Allowing more of the GUI-only methods to be usable in CLI mode would make it much easier to write scripts that can work both via CLI and via GUI. Aside from making the aforementioned methods available, it would also be convenient if there was some way to have Tiled load the Asset(s) listed in parameters instead of just passing the paths along to the script, and allowing scripts to use `tiled.activeAsset` and/or `tiled.openAssets` to get at those loaded Assets; this would allow many scripts written for the GUI to work via CLI without any changes, since those properties are the main way scripts choose the Assets to work on.

As a counterpart to `tiled.open()`, `tiled.close()` should also be made available, so that memory use can be kept in check for scripts that process many Assets.

This is not a critical feature since all the functionality is technically available via MapFormat/TilesetFormat. Making these GUI-only features available via CLI will just make scripting more straightforward rather than more capable. However, though it seems minor, I think this difference in approach to opening and saving files is significant enough that it discourages people from writing scripts that can work both in the GUI and via CLI. I think we'd see more widely useful scripts if the differences between the two modes were restricted to truly GUI-specific functionality like Automapping.

---

## #4089: request: add nes exporters

**Is your feature request related to a problem? Please describe.**
I found 2 nes exporters (see last post)

https://forums.nesdev.org/viewtopic.php?t=20108

**Describe the solution you'd like**
I would like to request adding them to Tiled. They are copyleft.

---

## #4081: User-defined zoom levels

For different tile sizes and art styles, as well as different screen resolutions, different zoom levels are more appropriate. Someone working with large tiles may want to have smaller zoom levels available as well as more steps in the low %s, and may not want the ability to zoom in beyond 200% or so, while someone working with pixel art may never want 150% blurring their art and may often want 500 or 600% (currently only possible in Tiled by typing those values in), while yet another user may want some zoom steps that correspond to the specific camera zooms in their game. Currently, Tiled has the same set of zoom steps for everyone, so useful zoom levels might not be easily available to users, while scrolling their mouse wheel to zoom takes through through a bunch of extra steps they never want.

I think a flexible way to address these differences in needs would be to allow users to specify the zoom steps Tiled will use while zooming.
Here's a screenshot from ImageGlass, showing their zoom settings. They have a drop-down for the interpolation method and, more relevant to this issue, a text box where users can enter a list of zoom steps (in percent) that the program will step through. They use semicolons as the separator, presumably to avoid ambiguity with the comma potentially used as a decimal separator. It's not beautiful, but it works well.
![image](https://github.com/user-attachments/assets/e682bf4b-4842-4da8-9d78-6814d7052473)
The initial value of this list could correspond to Tiled's current zoom steps, `1; 3; 6; 12; 25; 33; 50; 75; 100; 150; 200; 300; 400; 550; 800; 1100; 1600; 2300; 3200; 4500; 6400; 9000;12800; 18000; 25600` (does anyone actually use the upper third of this list? It feels like it must've been taken from a vector program). For my own needs (pixel art, mostly), I'd probably replace it with `6.25; 12.5; 25; 50; 100; 200; 300; 400; 500; 600; 700; 800`, while someone working with 256px tiles might instead go for `0.78125; 1.5625; 3.125; 6.25; 12.5; 25; 50; 100; 200; 300` (1/128x, 1/64x... 1/2x, 1x, 2x, 3x)
This box should display a warning if its contents cannot be parsed into a valid list of zoom steps. If Tiled allows saving such an invalid list, then it should use the default steps while the user-provided list is invalid.

In Tiled, the smallest allowed zoom level is 1% and the zoom drop-downs only allow entering integer values. For smaller and more flexible zooms to be possible, Tiled would need to allow non-integer percentages, e.g. 0.2%, 33.3333%. Such values should be allowed in the text box where the steps are defined, as well as in the drop-downs. I imagine Qt would handle the decimal point (`.` or `,`) based on the current locale, but if not, both should be considered valid.

Typing in zoom values in the zoom dropdown should continue to allow values that aren't listed in the steps. So if someone has a max zoom step of 200%, they should still be able to zoom to 1600% by typing it in. By allowing decimal val

*[truncated]*

---

## #4078: Add option for viewing all object names in world

**Is your feature request related to a problem? Please describe.**

Tiled doesn't have option for viewing all object names when you building map using world, only current selected map objects are displayed.

example map:
![image](https://github.com/user-attachments/assets/27595093-ec29-48ac-929b-836598748b48)

**Describe the solution you'd like**
Add new option for rendering object names when `world` are loaded:
1. only selected (default)
2. nearest to selected
3. all

**Describe alternatives you've considered**
Build your map in single file.

---

## #4064: Search function through tsx files

**Is your feature request related to a problem? Please describe.**
I'm strugling to find my files when I have large amounts

**Describe the solution you'd like**
A search box on the project window, can be hidden until user presses Ctrl-F

**Describe alternatives you've considered**
there are no alternatives that I can think of.

---

## #4063: Tiled not unloading files stored in RAM

**Describe the bug**
While loading a large sum of image files, I noticed memory usage had hit 90%+ and so closed the file i was currently working on. Memory usage did not change.

**To Reproduce**
Steps to reproduce the behavior:
1. Load large amount of files
2. Open Task Manager, or similar system viewer
3. Close Tab with large amount of files
4. Observe memory usage not changing

**Expected behavior**
Expected memory usage to decrease when closing tab and deloading the images.

**Media**
N/A

**Specifications:**
 - OS: Windows 11
 - Tiled Version: 1.11.0

---

## #4060: Tiled Crashes when switching from importing Collection of Images Tileset type to Based on Image type

**Describe the bug**
Tiled Crashes when switching from importing "Collection of Images" Tileset type to "Based on Image" type.

**To Reproduce**
Steps to reproduce the behavior:
1. Click on New Tileset
2. Set type to "Collection of Images".
3. Set type back to "Based on Image".
4. Crash.

**Expected behavior**
I expect it should not crash and I should be able to import a single image tileset.

**Specifications:**
 - OS: Ubuntu 22.4
 - Tiled Version: 1.11.0

---

## #4049: registerWorldFormat for worlds with embedded tilemaps

I'm attempting to write a map import/export handler for a platform game that has rooms of arbitrary size that can be moved around.  In Tiled this translates to a world with multiple tilemaps.  Reading the Tiled documentation it doesn't look like worlds can have the tilemaps embedded.

The problem is that this game stores this data in one file per "world", and I can't see a way to write a `registerWorldFormat` that would then generate the world and all of its tilemaps in a single data structure (and be able to save that entire structure back to a single file).

It would be great if tilemaps could be embedded in the world data, and if you could then register a file handler instead of being restricted to .world JSON files.

Although I could just load the entire world into one great big tilemap, it loses the ability to define room sizes.

---

## #4047: Could not find the Qt platform plugin "wayland"

**Describe the bug**
Cannot run AppImage

**To Reproduce**
run ./Tiled-1.11.0_Linux_Qt-5_x86_64.AppImage or ./Tiled-1.11.0_Linux_Qt-6_x86_64.AppImage

**Expected behavior**
qt.core.plugin.factoryloader: checking directory path "/tmp/.mount_Tiled-4TIzQy/usr/plugins/platforms" ...
qt.core.plugin.factoryloader: looking at "/tmp/.mount_Tiled-4TIzQy/usr/plugins/platforms/libqxcb.so"
qt.core.plugin.loader: Found metadata in lib /tmp/.mount_Tiled-4TIzQy/usr/plugins/platforms/libqxcb.so, metadata=
{
    "IID": "org.qt-project.Qt.QPA.QPlatformIntegrationFactoryInterface.5.3",
    "MetaData": {
        "Keys": [
            "xcb"
        ]
    },
    "archlevel": 1,
    "className": "QXcbIntegrationPlugin",
    "debug": false,
    "version": 395008
}


qt.core.plugin.factoryloader: Got keys from plugin meta data QList("xcb")
qt.core.plugin.factoryloader: checking directory path "/tmp/.mount_Tiled-4TIzQy/usr/bin/platforms" ...
qt.qpa.plugin: Could not find the Qt platform plugin "wayland" in ""
This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.

Available platform plugins are: xcb.

[1]    4587 IOT instruction (core dumped)  ./Tiled-1.11.0_Linux_Qt-6_x86_64.AppImage

**Specifications:**
 - OS: Arch Linux x86_64
 - WM: Hyprland (Wayland)
 - Tiled Version: Tiled-1.11.0_Linux_Qt-5_x86_64.AppImage or Tiled-1.11.0_Linux_Qt-6_x86_64.AppImage

---

## #4041: JSON export changed behaviour in 1.11.0 

In 1.11.0 when exporting to JSON all properties are included in the export. Previously only those with a modified value would be included. Not sure if this is intended or by mistake. In my case it creates issues as objects have values now that normally would be undefined and get their default values for specific cases. 

An easy example would be that I  use the layer tint to set the tint of all objects in that layer, unless an object have a value in the gfx class with a color property. This no longer works as all objects in a layer will have a #ffffff value etc.

![json_diff](https://github.com/user-attachments/assets/2919d3d2-0813-4595-a86d-9f1bbb56ffbc)
JSON diff for export in 1.11.0 compared to old behaviour.

**Expected behavior**
If intended, a feature request instead to have option in export settings for old behaviour.

**Specifications:**
 - OS: Linux (KDE Neon)
 - Tiled Version: 1.11.0

---

## #4040: Import tileset as .tsx - not only create tileset as now

**Is your feature request related to a problem? Please describe.**
Right now user have create tileset and then save as .tsx. 
Looks that this is basic problem is in case is no option to import .tsx but create new and save/override exit this same if user want use this same tile set.

**Describe the solution you'd like**
Import like Export.

**Describe alternatives you've considered**
Right now trying copy path to .tsx in to .tmx but sometimes save doing case from GUI like tileset parameters saved in .tmx
Thats why bad workflow around class/type: https://github.com/mapeditor/tiled/issues/4018#issuecomment-2303018079
Confirmed here: https://github.com/mapeditor/tiled/issues/4018#issuecomment-2275449399

---

## #4035: Allow collapsing/expanding of custom properties en-masse

When there are a lot of custom properties, it becomes cumbersome to look through the properties and find the results you want.
This is exaggerated by the default behaviour in Tiled which automatically expands all properties when you click on the object.

Here's an example

![image](https://github.com/user-attachments/assets/d26d2742-2c6e-4594-9bf9-a43ec0f0f1d4)

Would be much easier to read if we could "collapse/expand all".
It then becomes

![image](https://github.com/user-attachments/assets/42e43b97-ce81-4724-b984-ae8e245d9920)

Ideally it would remember these settings so you don't have to re-click collapse/expand

---
