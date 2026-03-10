# webpack — Project Ideas

**Source:** https://docs.google.com/document/d/1Mr_IPVdbupGwmGtcvLlVqFEL8wYN_rlfHUghJ2EPBVE/edit?usp=sharing
**Scraped:** 2026-03-10T16:58:40.268832

---

Webpack - Ideas List

Google Summer of Code 2026

- Webpack: Universal Targets

Difficulty: Hard

Project Size: 350 hours

Mentors: Alexander Akait, Nitin Kumar

Introduction

This project aims to enhance the versatility of Webpack's targets. Currently, there are limitations, and a web bundle doesn't seamlessly fit into Node.js or a web worker environment. The proposal is to introduce a Universal Target that incorporates runtime code suitable for web, web worker, and Node.js. While this may increase code size slightly, the benefit is the ability to create Universal Module Definition (UMD) bundles that work seamlessly across all environments. Additionally, this enhancement facilitates sharing chunks between web and web worker environments.

Related Issue(s): [#6525](https://www.google.com/url?q=https://github.com/webpack/webpack/issues/6525&sa=D&source=editors&ust=1773160634486481&usg=AOvVaw0JACXN4R9u3q0RzlXsRTHT)

Prerequisites

JavaScript, Node.js

- Webpack: New Documentation Website

Difficulty: Medium

Project Size: 350 hours

Mentors: Claudio Wunder, Aviv Keller, Sebastian Beltran

Introduction

We’re redesigning and reworking on Webpack’s website and its documentation. This project is a fundamental work for the release of Webpack 6 and ensures we have a redesigned website, redesigned docs, updated docs with improved DevEx, UX and that is AI-friendly.

Related Issue(s): [#4](https://www.google.com/url?q=https://github.com/webpack/docs.webpack.js.org/issues/4&sa=D&source=editors&ust=1773160634488093&usg=AOvVaw2smusmfoA3ZJOavx1fjxpJ)

Prerequisites

JavaScript, CSS, HTML

- Webpack: Entry points as HTML

Difficulty: Medium

Project Size: 350 hours

Mentors: Even Stensberg, Nitin Kumar, Alexander Akait

Introduction

Webpack allows entry points to be as JavaScript but we also want to support having HTML files as entry points. When webpack internally notices an .html extension, it will automatically apply the correct bundling technique similar to [html-bundler-plugin](https://www.google.com/url?q=https://github.com/webdiscus/html-bundler-webpack-plugin&sa=D&source=editors&ust=1773160634489367&usg=AOvVaw3zSnifNY9FqjjnXiT625T8).

Related Issue(s): [#536](https://www.google.com/url?q=https://github.com/webpack/webpack/issues/536&sa=D&source=editors&ust=1773160634489588&usg=AOvVaw1hgF1kqvnIQZKdn-T_pYXJ)

Prerequisites

JavaScript, CSS, HTML
