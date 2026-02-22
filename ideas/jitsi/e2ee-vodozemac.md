# E2EE: Replace olm with vodozemac

**Parent:** Jitsi — Project Ideas
**Source:** https://github.com/jitsi/gsoc-ideas/blob/master/2026/e2ee-vodozemac.md
**Scraped:** 2026-02-22T23:28:47.584901

---

# E2EE: Replace olm with vodozemac

## Overview

Modernize Jitsi Meet's end-to-end encryption implementation by migrating from olm to vodozemac.

## Description

This project aims to migrate Jitsi Meet's E2EE implementation from olm to vodozemac while maintaining compatibility and improving overall encryption performance. While functional, olm is now in maintenance mode and has been superseded by vodozemac, a modern Rust implementation of the same cryptographic ratchets (Olm and Megolm).

## Expected outcomes

* Complete migration from olm to vodozemac in lib-jitsi-meet and jitsi-meet.
* Updated documentation and test coverage for E2EE implementation.

## Skills / Technologies

JavaScript, TypeScript, Rust, WebAssembly, Cryptography basics, End-to-End Encryption

## Possible mentors

Hristo Terezov, Saúl Ibarra Corretgé

## Expected project size

Medium (175 hours)

## Difficulty

Hard
