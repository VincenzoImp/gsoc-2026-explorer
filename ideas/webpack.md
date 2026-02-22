# webpack — Project Ideas

**Source:** https://docs.google.com/document/d/1Mr_IPVdbupGwmGtcvLlVqFEL8wYN_rlfHUghJ2EPBVE/edit?usp=sharing
**Scraped:** 2026-02-22T23:28:47.632386

---

Webpack - Ideas List

Google Summer of Code 2026

- Webpack: Universal Targets

Difficulty: Hard

Project Size: 350 hours

Mentors: Alexander Akait, Nitin Kumar

Introduction

This project aims to enhance the versatility of Webpack's targets. Currently, there are limitations, and a web bundle doesn't seamlessly fit into Node.js or a web worker environment. The proposal is to introduce a Universal Target that incorporates runtime code suitable for web, web worker, and Node.js. While this may increase code size slightly, the benefit is the ability to create Universal Module Definition (UMD) bundles that work seamlessly across all environments. Additionally, this enhancement facilitates sharing chunks between web and web worker environments.

Related Issue(s): [#6525](https://www.google.com/url?q=https://github.com/webpack/webpack/issues/6525&sa=D&source=editors&ust=1771802486112501&usg=AOvVaw0Usx620749rERbl1GKMCeG)

Prerequisites

JavaScript, Node.js

- Webpack: New Documentation Website

Difficulty: Medium

Project Size: 350 hours

Mentors: Claudio Wunder, Even Stensberg, Nitin Kumar, Aviv Keller, Sebastian Beltran

Introduction

We’re redesigning and reworking on Webpack’s website and its documentation. This project is a fundamental work for the release of Webpack 6 and ensures we have a redesigned website, redesigned docs, updated docs with improved DevEx, UX and that is AI-friendly.

Related Issue(s): [#4](https://www.google.com/url?q=https://github.com/webpack/docs.webpack.js.org/issues/4&sa=D&source=editors&ust=1771802486113742&usg=AOvVaw0FMEi3WfATulLZEWjWLb4E)

Prerequisites

JavaScript, CSS, HTML

- Webpack: Entry points as HTML

Difficulty: Medium

Project Size: 350 hours

Mentors: Even Stensberg, Nitin Kumar, Alexander Akait

Introduction

Webpack allows entry points to be as JavaScript but we also want to support having HTML files as entry points. When webpack internally notices an .html extension, it will automatically apply the correct bundling technique similar to [html-bundler-plugin](https://www.google.com/url?q=https://github.com/webdiscus/html-bundler-webpack-plugin&sa=D&source=editors&ust=1771802486114754&usg=AOvVaw3BTCRSsl9WgxZa4T_bT42q).

Related Issue(s): [#536](https://www.google.com/url?q=https://github.com/webpack/webpack/issues/536&sa=D&source=editors&ust=1771802486114946&usg=AOvVaw2JFTT7bgYEov9rUCvTo8DW)

Prerequisites

JavaScript, CSS, HTML
