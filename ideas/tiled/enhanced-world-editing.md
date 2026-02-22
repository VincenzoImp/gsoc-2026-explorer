# Enhanced World Editing

**Parent:** Tiled — Project Ideas
**Source:** https://github.com/mapeditor/tiled/wiki/Enhanced-World-Editing
**Scraped:** 2026-02-22T23:28:47.582963

---

Tiled 1.2 added displaying multiple maps within the same view by [setting up a World](https://doc.mapeditor.org/en/stable/manual/worlds/). Since Tiled 1.4, a basic "World Tool" was added, which enabled [basic editing of the world](https://doc.mapeditor.org/en/stable/manual/worlds/#editing-worlds). This project is about making several improvements to the world editing functionality.

**Expected outcome:** Worlds are a natural and convenient part of creating game content with Tiled.\
**Required skills:** C++ (preferred: Qt)\
**Possible mentors:** bjorn, dogboydog\
**Expected size:** 350 hours (or 175 hours, by selecting a sub-set of listed improvements)\
**Difficulty:** Medium

### Adding a World Grid

Currently when moving around a map in a world, it only snaps to tile positions. Since maps are generally quite large, it would be nice to introduce a "world grid", the visibility of which can be toggled and to which maps can be snapped.

### Resizing of Maps

Maps can currently only be resized through the Resize dialog, triggered by _Map > Resize Map_. Even though this dialog provides a convenient preview of the resize operation, it would be much nicer if a map could be resized directly in the world editing mode, using intuitive drag handles. When resizing, the content of the map is expected to stay in the same place, regardless of which side is resized.

Of course, when resizing a map its size should optionally snap to the world grid.

### Creating and Deleting Maps

It should be possible to create a new map directly from the world editing mode, by dragging the area that it should occupy. It should automatically share its general setup (orientation, tile size, etc.) with an existing map in the world, so that we don't need to pop up the "New Map" dialog. We can also avoid the need to pop up a "Save As" dialog, either based on a default file name pattern or by allowing the map to stay unsaved at first.

Similarly, it should probably be possible to delete maps from the world, removing their files as well. Currently one can only add or remove existing maps, without affecting their files.

### A Default World

If no world is set up, this currently disables the "World Tool" entirely. Instead, such a map should behave as if it was part of a default world, making sure the world editing mode is available and can be used to resize the map, for example. It can also provide a quick way to save the world, when the user would like to add additional maps to the world.

### Shared Map View

Currently, switching between different maps in the same world is implemented by opening the other map and synchronizing the position and scale of the view. The experience would be a lot better if only the "active" map in the current view would change, since this could be much faster and in addition it would avoid opening a new tab for every selected map.
