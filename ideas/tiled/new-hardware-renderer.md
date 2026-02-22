# New Hardware Renderer

**Parent:** Tiled — Project Ideas
**Source:** https://github.com/mapeditor/tiled/wiki/New-Hardware-Renderer
**Scraped:** 2026-02-22T23:28:47.582889

---

Modernize the rendering engine to use the [Qt Scene Graph](https://doc.qt.io/qt-6/qtquick-visualcanvas-scenegraph.html) instead of [`QPainter`](https://doc.qt.io/qt-6/qpainter.html).

**Expected outcome:** Tiled performs better and is more flexible thanks to a new renderer based on a modern graphics API.\
**Required skills:** Qt, C++ (preferred: Qt Quick, experience with modern graphics APIs)\
**Possible mentors:** bjorn, Ablu, Leonidax\
**Expected size:** 350 hours\
**Difficulty:** Medium

### Limitations of the Current Renderer

Tiled still mainly uses software rasterization, rendering the map through the [`QPainter`](https://doc.qt.io/qt-6/qpainter.html) API in combination with a [`QGraphicsScene`](https://doc.qt.io/qt-6/qgraphicsscene.html). This has generally worked quite well due to scrolling optimizations (moving existing pixels) and making sure to only update affected regions when changes are made.

The software rendering starts to show problems whenever the full map view needs to be repainted, especially when rendering scaled or tinted graphics. Full repaints happen when tile animations or parallax are enabled, or when the scale changes.

Another problem with software rendering, is that there is no support for custom meshes and shaders. A hardware renderer would enable more flexible but fast graphical primitives.

### New Renderer Based on Qt Quick

Qt ships with a new powerful visualization module, Qt Quick. It has many features in common with the currently used `QGraphicsScene`. Its rendering is based on the [Qt Scene Graph](https://doc.qt.io/qt-6/qtquick-visualcanvas-scenegraph.html), which is much closer to the hardware than `QPainter`, while still abstracting over various modern graphics APIs like OpenGL, Vulkan, Metal, or Direct 3D.

This project is about writing a full replacement for the `MapView`, `MapScene` and the various `QGraphicsItem` derived classes, based on Qt Quick. This would replace the `MapView` widget with a `QQuickWidget` that instantiates the necessary Qt Quick items for rendering and interacting with the map. To limit the scope of this project, all the remaining UI would stay in place and appropriate abstractions should enable reusing most of the existing tool implementations.

### Existing Work

Some work has been done towards using Qt Quick for displaying the map as part of the "Tiled Quick" product living at `src/tiledquick`. So far this can only do basic rendering of tile layers and notably does not implement any editing operations. As first step, this code could be adjusted such that it can be embedded in Tiled to render a loaded map.

### Meshes and Shaders

This project is considered completed when the existing features are supported by the new renderer. However, when there is still time left it would be interesting to explore additional features that are made possible by the new renderer.

One idea is to implement a custom "textured polygon" object, based on polygon-shaped tiles. This would allow rendering arbitrary shapes from a tileset, which could be defined as polygons and triangularized.

Another idea is to add support for custom shaders, or to write a few built-in shaders, to achieve various effects like shadows, blur, lights or use bump / normal maps.
