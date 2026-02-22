# Add complex layouts to sway

**Parent:** CCExtractor Development — Project Ideas
**Source:** https://ccextractor.org/public/gsoc/2026/sway_complex
**Scraped:** 2026-02-22T23:28:47.612458

---

# Add complex layouts to sway

**Mentor:**
Probably: Soumya Ranjan Patnaik

**Time estimation**
350 hours

### Project Brief

First step is to make these two statements true:

Outputs always render the tiled views in their own sway_container and never anyone else's Floating views are rendered with respect to the output layout, and can show on multiple outputs Then, we should start to introduce two new kinds of configuration to each output config:

Layout configuration Mirroring configuration A layout configuration stores how much of the output's space is allocated to its sway_container:

output HDMI-A-1 layout 100x100@10,10

Bonus: could subdivide the output into multiple layouts

output HDMI-A-1 res 1920x1080 layout 960x1080@0,0 layout 960x1080@960,0 subdivides a 1080p output into two halves, which each get their own workspace (useful for ultrawides, for example)

If no layout is specified, the default layout is used - WxH@0,0

No layout at all can also be specified via layout none, in which case no workspace is allocated.

Separately, you can specify a mirroring configuration via mirror [source output] [at X,Y], which will draw tiling windows from the source output onto the configured output at the target position. You can specify this several times.

Some example configurations:

Normal configuration

output HDMI-A-1 res 1920x1080 output DP-1 res 1920x1080 pos 1920,0 basic-side-by-side

Basic mirroring

output HDMI-A-1 res 1920x1080 output DP-1 layout none mirror HDMI-A-1 basic-mirroring

Disjoint resolution mirroring

output DP-1 res 1280x720 output HDMI-A-1 res 1920x1080 layout none mirror DP-1 disjoint-res-mirroring

Disjoint resolution mirroring with floating views

Note: this is the same config as the last example

output DP-1 res 1280x720 output HDMI-A-1 res 1920x1080 layout none mirror DP-1 disjoint-res-mirroring-float

Disjoint resolution mirroring with multiple layouts

output DP-1 res 1280x720 output HDMI-A-1 res 1920x1080 mirror DP-1 disjoint-res-mirroring-multi

Disjoint resolution mirroring with multiple layouts and double mirroring

output DP-1 res 1280x720 mirror HDMI-A-1 output HDMI-A-1 res 1920x1080 mirror DP-1 disjoint-res-mirroring-multi-double

Partial mirroring plus partial layout

output HDMI-A-1 res 1920x1080 output DP-1 res 1920x1080 mirror HDMI-A-1 at -1800,0 layout 1800x1080@120,0 mirroring-overlap

Unanswered questions:

z-ordering config

### Additional discussion

### Qualification tasks

Come up with a plan and prove that you can execute on it by doing its initial steps.
