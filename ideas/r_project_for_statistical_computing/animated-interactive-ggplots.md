# Animated interactive ggplots

**Parent:** R project for statistical computing — Project Ideas
**Source:** https://github.com/rstats-gsoc/gsoc2026/wiki/Animated-interactive-ggplots
**Scraped:** 2026-02-22T23:28:47.625964

---

-
[Notifications](https://github.com/login?return_to=%2Frstats-gsoc%2Fgsoc2026)You must be signed in to change notification settings -
[Fork 0](https://github.com/login?return_to=%2Frstats-gsoc%2Fgsoc2026)

# Animated interactive ggplots

[49 revisions](https://github.com/rstats-gsoc/gsoc2026/wiki/Animated-interactive-ggplots/_history)

[animint2](https://github.com/tdhock/animint2) is an R package for making interactive animated data
visualizations on the web, using ggplot syntax and two new keywords:

-
**showSelected=variable**means that only the subset of the data that corresponds to the selected value of**variable**will be shown. -
**clickSelects=variable**means that clicking a plot element will change the currently selected value of**variable**.

Toby Dylan Hocking initiated the project in 2013. Contributors during previous GSOC projects are Susan VanderPlas (2013), Carson Sievert (2014), Tony Tsai (2015), Kevin Ferris (2015), Faizan Khan (2016-2017), Vivek Kumar (2018), Himanshu Singh (2020), Yufan Fei (2022-2023), Jocelyn Chen (2023), Siddesh Deodhar (2024), Suhaani Agarwal (2025), Biplab Sutradhar (2025).

[The animint2 manual](https://animint-manual-en.netlify.app/ch02/) is the definitive reference on how to design data
visualizations using animint2.

Standard R graphics are based on the pen and paper model, which makes animations and interactivity difficult to accomplish. Some existing packages that provide interactivity and/or animation are

- Non-interactive animations can be accomplished with
[animation](http://yihui.name/animation/)/[gganim](https://github.com/tdhock/gganim)/[gganimate](https://github.com/thomasp85/gganimate)/[plotteus](https://www.plotteus.dev/docs/introduction)(animint2 provides interactions other than moving forward/back in time). - Some interactions with non-animated linked plots can be done with
the
[qtbase, qtpaint, and cranvas packages](https://github.com/ggobi/cranvas/wiki)(no longer maintained, animint2 provides animation and showSelected). - Linked plots in the web are possible using
[SVGAnnotation](http://www.omegahat.org/SVGAnnotation/SVGAnnotationPaper/SVGAnnotationPaper.html)(no longer maintained) or[gridSVG](http://sjp.co.nz/projects/gridsvg/)but using these to create such a visualization requires knowledge of Javascript (animint2 designers write only R/ggplot2 code). - The
[svgmaps](https://r-forge.r-project.org/scm/viewvc.php/pkg/?root=svgmaps)package defines interactivity (hrefs, tooltips) in R code using igeoms, and exports SVG plots using gridSVG, but does not support showing/hiding data subsets (animint2 does). - The
[ggvis](https://github.com/rstudio/ggvis)(dormant/archived) package defines a grammar of interactive graphics that relies on[shiny](https://github.com/rstudio/shiny)’s reactivity model for most of its interactive capabilities (animint2 does not need a shiny server). Like[vegawidget](https://github.com/vegawidget/vegawidget)/[vegalite](https://github.com/hrbrmstr/vegalite)it uses[Vega](https://github.com/trifacta/vega)but does not support the interactive clickSelects/showSelected keywords (animint2 does). -
[plotly](https://plotly-r.com/client-side-linking.html)supports client-side interactions without a shiny server, but does not support the interactive clickSelects/showSelected keywords (animint2 does). The[plotly performance page](https://web.archive.org/web/20250827141658/https://plotly-r.com/performance)does not mention chunking (animint2 supports dividing input data into smaller TSV files, so the user only has to download data that is clicked on), although that could be implemented with a shiny server (animint2 does not require any special server, so can be deployed to any static webserver like GitHub Pages). -
[loon](https://github.com/great-northern-diver/loon)provides interactive graphics using the tcltk R package, and is great for exploratory graphics, but does not support the interactive clickSelects/showSelected keywords (animint2 does). -
[RIGHT](http://cran.r-project.org/web/packages/RIGHT/)(archived),[htmlwidgets](https://www.htmlwidgets.org/), and[DC](http://dc-js.github.io/dc.js/)(JavaScript not R) implement interactive plots for some specific plot types (animint2 uses the multi-layered grammar of graphics so is not limited to pre-defined plot types). -
[altair](https://altair-viz.github.io/user_guide/large_datasets.html)is a python package which provides similar functionality as animint2, but its compiler lacks chunking (dividing input data into smaller TSV files, so the user only has to download data that is clicked on). JupyterChart widget can be used with altair for a similar effect, as long as server with Python kernel is available (animint2 does not require any special server, so can be deployed to any static webserver like GitHub Pages). -
[Nebula](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9417674&utm_source=sciencedirect_contenthosting&getft_integrator=sciencedirect_contenthosting&tag=1)[examples](https://nebula-vis.github.io/examples)is a JavaScript framework, with more complex interactive grammar than clickSelects/showSelected. -
[G2](https://www.sciencedirect.com/science/article/pii/S2468502X26000033#fn2)[examples](https://g2.antv.antgroup.com/en/examples)do not show multiple linked views, but do show interaction in one plot. -
[5 shiny apps hosted for free](https://support.posit.co/hc/en-us/articles/217592947-What-are-the-limits-of-the-shinyapps-io-Free-plan)on shinyapps.io, whereas unlimited number of animints hosted for free on GitHub Pages (max 1GB data for each).

For even more related work see [The animint JCGS paper by Sievert et al
(2018)](https://amstat.tandfonline.com/doi/abs/10.1080/10618600.2018.1513367?journalCode=ucgs20), the [Dynamic Visualizations](https://cran.r-project.org/web/views/DynamicVisualizations.html) and [Web technologies](http://cran.r-project.org/web/views/WebTechnologies.html) task views on CRAN, and
[Visualization design resources from the UBC InfoVis Group](http://www.cs.ubc.ca/group/infovis/resources.shtml).

The goal of this GSOC project is to implement new features for animint2 in order to

-
[draw holes in a polygon](https://github.com/animint/animint2/issues/252), using`geom_polygon(aes(subgroup))`

. -
[Move getCommonChunk() to C++](https://github.com/animint/animint2/issues/258)for big constant factor speedups at data viz compile time. - Previously Faizan implemented updating of axes/legends after
changing the currently displayed data subset. Currently the
computations are done in the compiler but there are some
limitations, so it would be preferable to move the computations to
the renderer. See issue,
[move scale range calculation to renderer](https://github.com/animint/animint2/issues/48). - Compute stats/positions in JavaScript, after applying showSelected. Currently stats/positions are not used, and
[there is an issue for removing them from the documentation to avoid confusion](https://github.com/animint/animint2/issues/158). Some stats like sum or mean could be interesting to implement with multiple selection variables, like how`geom_label_aligned`

adjusts label positions after showSelected variables are applied.

An ideal contributor project will also plan to write some tests and
documentation ([vignette](https://animint.github.io/animint2/articles/animint2.html), [web page](https://animint.github.io/animint2/), [blog example 1](http://kferris10.github.io/AnimintBlog/), [blog example 2](https://faye-yufan.github.io/gsoc22-animint/2023-11-04-gsoc23-summary/)).

- fixing any of the
[other issues](https://github.com/tdhock/animint2/issues).

Any other ideas for improving Animint are welcome, as long as they can fit in the 3-month coding time frame.

Animint2 already provides useRs with some unique features for interactive data visualization. At the end of GSOC, the animint2 package will be easier to maintain, and have even more features, tests, documentation, and gallery examples.

YES. If you don’t know JavaScript then I suggest you read some
tutorials, e.g. [Mozilla JavaScript basics](https://developer.mozilla.org/en-US/Learn/Getting_started_with_the_web/JavaScript_basics), [W3Schools](http://www.w3schools.com/js/), [mbostock’s D3 examples](https://observablehq.com/@mbostock).

Please get in touch with EVALUATING MENTOR [Toby Dylan Hocking](https://github.com/tdhock)
<toby.hocking@r-project.org> and
[Yufan Fei](https://github.com/Faye-yufan) <yufanfei8@gmail.com>
after completing at least one of the tests below.

Do one or several — doing more hard tests makes you more likely to be selected.

- Easy: do one of the exercises listed in one of the chapters of the
animint2 Manual, and upload your visualization to the web using
[The GitHub deployment steps](https://animint-manual-en.netlify.app/ch05/#the-animint2-github-deployment-steps). Include a link to your rendered data viz along with your R source code. Even better: use animint2 to visualize some data from your domain of expertise. Show an example of an error that you see when animint2 is loaded/attached at the same time as standard ggplot2. - Medium: translate an
[example of the animation package](https://yihui.org/animation/examples/)into an Animint. Do not do[one of the examples that has already been ported](https://github.com/tdhock/animint/wiki/Ports-of-animation-examples). Post a link to your result on the[Ports of animation examples](https://github.com/tdhock/animint/wiki/Ports-of-animation-examples)page on the Animint wiki.- look at source code of one of the animation package functions e.g. grad.desc() for a demonstration of the gradient descent algorithm. Translate the for loops and plot() calls into code that generates data.frames. In the grad.desc() example, there should be one data.frame for the contour lines, one for the arrows, and one for the values of the objective/gradient at each iteration.
- Use the data.frames to make some ggplots. In the grad.desc()
example, there should be one ggplot with a
`geom_contour`

and a`geom_path`

, and another ggplot with a`geom_line`

that shows objective or gradient value versus iteration, and a`geom_tallrect`

in the background for selecting the iteration number. - Make a list of ggplots. For the
grad.desc() example the plot list should be something like
`animint(contour=ggplot(), objective=ggplot(), time=list(variable="iteration", ms=2000))`

.

- Medium-hard: first
[read about how to create a new gallery](https://animint-manual-en.netlify.app/ch05/#gallery), then create one that organizes all of the data viz from the[Ports of animation examples](https://github.com/tdhock/animint/wiki/Ports-of-animation-examples)page. - Hard: write a
[testthat unit test](https://github.com/tdhock/animint/wiki/Testing)based on one of your Animint visualizations. Fork animint and add a renderer test (using animint2HTML) to tests/testthat/test-renderer-YOUR-TEST.R, then send us a Pull Request. Upload a screencast to Vimeo that shows you executing your test from the R command line. Make sure to`install.packages("chromote")`

- use
`tests_init()`

to start the remote-controlled web browser. - use
`animint2HTML()`

to get the HTML rendered by the animint.js code.- parse the result to verify that the data are rendered to SVG. (look at other test-renderer-* files for examples)

- show two windows,
- a remote-controlled browser window rendering the data viz,
- and the R script/terminal that executes the test code.



IMPORTANT: please avoid using AI code generation tools (Copilot, ChatGPT, etc) for this project.
[Please read contributor guidelines for this project](https://github.com/animint/animint2?tab=contributing-ov-file#avoiddeclare-ai-code-generation).
If your test results seem to be AI-generated, then you will probably not be selected as a contributor for this project.

Contributors, please post a link to your test results here.

- Your name, your solution here
- Aviral Sapra –
[worldbank-Visualisation](https://AviraL0013.github.io/worldbank-viz)–[worldbank-Github](https://github.com/AviraL0013/worldbank-viz/tree/gh-pages)|[Student Performance Visualisation](https://AviraL0013.github.io/student-performance-viz)–[Viz-Github](https://github.com/AviraL0013/student-performance-viz/tree/gh-pages)–[R file](https://github.com/AviraL0013/student-performance-code) - Aviral Sapra –
[Least Squares Method](https://aviral0013.github.io/least-squares-animint/)|[Source](https://github.com/AviraL0013/least-squares-animint/blob/main/source/least_squares_animint.R) - Aviral Sapra –
[Animation_Gallery](https://aviral0013.github.io/animation-examples-gallery/)|[Source](https://github.com/AviraL0013/animation-examples-gallery/tree/gh-pages) - Aakriti Kushwaha –
[Animint Tests – GitHub](https://github.com/aakritixyz/animint-tests) -
**Prateek Kalwar**-[Solutions](https://github.com/prateek-kalwar-95/r/blob/main/README.md) - Aryan Singh,
[Tests-Solution](https://github.com/Aryan-SINGH-GIT/animated-interactive-ggplots/blob/master/README.md)

- Aviral Sapra –
