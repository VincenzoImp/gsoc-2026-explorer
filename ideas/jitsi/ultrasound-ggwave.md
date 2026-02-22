# Ultrasound experiments with ggwave (part 2)

**Parent:** Jitsi — Project Ideas
**Source:** https://github.com/jitsi/gsoc-ideas/blob/master/2026/ultrasound-ggwave.md
**Scraped:** 2026-02-22T23:28:47.585411

---

# Ultrasound experiments with ggwave (part 2)

## Overview

Extend ultrasound-based communication capabilities in Jitsi Meet using ggwave for device pairing and proximity features.

## Description

[ggwave](https://github.com/ggerganov/ggwave) enables reliable data transmission through sound waves, including
ultrasonic frequencies that are inaudible to humans.

This technology can enable novel features such as nearby device discovery, seamless device pairing, proximity detection,
and cross-device coordination without requiring network connectivity or QR codes. This can be used for device pairing in Spot client and also useful for detecting open microphones in close proximity such that advanced ML based noise supression techniques can be applied.

## Expected outcomes

* Integration of ggwave library for ultrasonic data transmission
* Device discovery and pairing using ultrasound signals
* Proximity detection between participants
* Documentation and examples for use cases (second screen, companion apps, etc.)

## Skills / Technologies

JavaScript, TypeScript, Web Audio API, Digital Signal Processing, ggwave, WebAssembly

## Possible mentors

Saúl Ibarra Corretgé

## Expected project size

Medium (175 hours) or Large (350 hours)

## Difficulty

Medium to Hard
