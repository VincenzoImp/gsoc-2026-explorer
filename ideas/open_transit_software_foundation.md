# Open Transit Software Foundation — Project Ideas

**Source:** https://opentransitsoftwarefoundation.org/2026/01/google-summer-of-code-2026-project-ideas/
**Scraped:** 2026-02-22T23:28:47.625704

---

# Google Summer of Code 2026 Project Ideas

**Caution:** Please do not consider this list to be definitive: we have lots of ideas for projects we want to see pursued as part of GSoC 2026, but will certainly not receive as many slots as we want. The order of the list is also not indicative of priority.

## iOS App/Apple Platforms

### Modernize the iOS App UI

*Difficulty: Advanced // Size: 350 hours*

The OneBusAway iOS app has served hundreds of thousands of transit riders well, but its interface is showing its age. We’ve begun initial investigations into modernizing the app’s UI by eliminating the tab bar and adopting a design language closer to Apple Maps—with a focus on a sheet-based interface that feels native to modern iOS.

You will be responsible for pushing this project through to completion. This includes:

- Working with our design team to finalize the new UI direction
- Refactoring the app’s navigation architecture to remove the tab bar in favor of a Maps-style sheet-based interface
- Implementing the new UI in SwiftUI while maintaining compatibility with existing features
- Ensuring the new design maintains or improves accessibility for VoiceOver users
- Writing comprehensive UI tests for the new navigation patterns

**Expected outcomes:**

- A fully modernized iOS app UI that matches contemporary Apple design patterns
- Improved user experience with intuitive sheet-based navigation
- Complete feature parity with the existing app

## Golang/Backend Projects

### Maglev: Next Generation REST API Server

*Difficulty: Advanced // Size: 350 hours // Slots: 2*

[Maglev](https://github.com/onebusaway/maglev) is our next generation REST API server, written in Go. It’s designed to be a modern, high-performance replacement for portions of the existing Java-based OBA API server. The project is moving along well, but needs sustained work to become production-ready for transit agencies.

We’re looking for two developers to help us get Maglev across the finish line. You’ll work closely with our core team to:

- Implement missing API endpoints to achieve parity with the existing OBA API server
- Build comprehensive test coverage for all endpoints
- Optimize performance for high-traffic deployments
- Write documentation for transit agency deployment
- Implement caching strategies and database optimizations

**Expected outcomes:**

- A production-ready REST API server that can serve as a drop-in replacement for transit agency deployments
- Comprehensive documentation and deployment guides
- Performance benchmarks demonstrating improvements over the legacy server

### Vehicle Tracker: Realtime Vehicle Positioning for Developing Countries

*Difficulty: Advanced // Size: 350 hours*

The OneBusAway server relies upon specialized software and hardware to generate the vehicle position feeds that power its realtime data. This works well for transit agencies in developed countries with existing AVL (Automatic Vehicle Location) systems, but creates a significant barrier for transit systems in developing countries that are building out fixed route transit.

To unlock the potential of OneBusAway for these regions, we need to create a new, lightweight solution for tracking vehicle locations in realtime. This project involves building both a server component and a companion Android app.

You will be responsible for:

- Building a server application (in Go) that receives vehicle location data and generates GTFS-RT Vehicle Positions protobuf feeds
- Creating a companion Android app that drivers can use to reliably report their vehicle’s location
- Implementing secure authentication between the Android app and server
- Designing the system to work reliably in areas with intermittent network connectivity
- Building administrative tools for transit operators to manage vehicles and drivers

**Expected outcomes:**

- A production-ready server that generates GTFS-RT Vehicle Positions feeds
- A reliable Android app for vehicle location tracking
- Documentation for transit agencies to deploy and operate the system
- Support for offline operation and data sync when connectivity is restored

## Your Idea Here!

We don’t have a monopoly on great ideas. Let us know what you think would be a great addition to the OBA platform!
