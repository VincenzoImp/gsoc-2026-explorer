# Gemini CLI — Project Ideas

**Source:** https://docs.google.com/document/d/1iaMZliqwUn-ACyZAbgzdXmDiQZ7l5gp8UQIIY2BnPO8/edit?usp=sharing
**Scraped:** 2026-02-22T23:28:47.631927

---

Feb 4, 2026

A partial list of ideas for Google Summer of Code 2026 participants contributing to the Gemini CLI project is provided here. Summary information for these ideas is as follows:


- Mix of difficulties: 2 Hard (350hr), 7 Medium (175hr), 1 Easy-Medium (90hr)
- Aligned with existing roadmap items: Extensions gallery (#18246), Hooks (#18253), Windows quality (#18251), Evals (#18257), Skills (#18255)
- Mentors provided are only suggestions and are subject to change

[1 - Network Traffic Proxy and Domain Filtering](https://docs.google.com)

[2 - Behavioral Evaluation Test Framework](https://docs.google.com)

[3 - Windows Developer Experience Improvements](https://docs.google.com)

[4 - Multi-IDE Integration Enhancement](https://docs.google.com)

[5 - Performance Monitoring and Optimization Dashboard](https://docs.google.com)

[6 - Interactive Progress Visualization & Task Stepping](https://docs.google.com)

[7 - Terminal-Integrated Debugging Companion](https://docs.google.com)

[8 - Native Windows Sandbox using AppContainer](https://docs.google.com)

[9 - Interactive Security Policy and Sandbox Wizard](https://docs.google.com)

[10 - Unified Sandbox Driver Architecture](https://docs.google.com)

[11 - Hands-Free Multimodal Voice Mode](https://docs.google.com)

[12 - Generative Architecture & UI Visualization](https://docs.google.com)

Difficulty: Medium | Size: 175 hours | Area: Security

Implement a network proxy layer for sandboxed command execution that routes HTTP/HTTPS and other TCP traffic through a controlled gateway. This enables domain allowlisting/denylisting, traffic logging for audit purposes, and permission prompts for new network destinations. The feature would provide defense-in-depth protection even against potential sandbox escapes

Expected Outcomes

- HTTP/HTTPS proxy implementation with domain filtering capabilities
- SOCKS5 proxy support for non-HTTP traffic (SSH, database connections)
- Configurable allowlist/denylist with wildcard pattern support
- Permission prompt UI for new/unknown domains
- Traffic logging for security auditing (opt-in)
- Integration with existing Seatbelt and Docker sandbox modes

- Required: TypeScript/Node.js, networking fundamentals (TCP/IP, HTTP, proxies)
- Preferred: Experience with proxy servers (mitmproxy, squid), TLS/SSL, network security

- Gaurav Ghosh

Difficulty: Medium | Size: 175 hours | Area: Quality/Testing

Develop a comprehensive behavioral evaluation framework for testing Gemini CLI's agent capabilities against real-world coding scenarios. This includes creating a benchmark suite of coding tasks, measuring success rates across different task categories, and providing regression detection for agent behavior changes. The framework will help maintain quality as the agent evolves and enable contributors to validate their changes.

- Evaluation framework with standardized test harness
- Benchmark suite covering 50+ coding scenarios across categories (debugging, refactoring, new features, code review)
- Automated scoring and success rate metrics
- Regression detection system integrated with CI/CD
- Dashboard or report generation for evaluation results
- Documentation for adding new evaluation scenarios
- Baseline metrics for current Gemini CLI version

- Required: TypeScript/Node.js, testing methodologies, CI/CD pipelines
- Preferred: Experience with LLM evaluation, benchmarking, statistical analysis

- Christian Gunderman

Difficulty: Medium | Size: 175 hours | Area: Platform/Quality

Improve the Gemini CLI experience for Windows developers by addressing platform-specific issues, optimizing performance, and ensuring feature parity with macOS/Linux. This includes fixing terminal rendering issues, improving PATH handling, enhancing PowerShell/CMD integration, and creating comprehensive Windows-specific documentation and tooling.

- Resolution of top 20 Windows-specific issues from the issue tracker
- Native Windows terminal rendering improvements (fixing black backgrounds, theme issues)
- PowerShell and CMD integration enhancements
- Windows-specific installation and update improvements
- Performance optimizations for Windows file system operations
- Comprehensive Windows troubleshooting documentation
- Automated Windows-specific CI testing pipeline

- Required: TypeScript/Node.js, Windows development, PowerShell
- Preferred: Windows terminal APIs, cross-platform development experience

- Tommaso Sciortino

Difficulty: Medium | Size: 175 hours | Area: IDE/Tooling

Expand Gemini CLI's IDE integration beyond VS Code to provide first-class support for additional popular editors including JetBrains IDEs (IntelliJ, PyCharm, WebStorm), Neovim, and Zed. This includes implementing editor-specific plugins/extensions, establishing a common IDE context protocol, and enabling features like synchronized file state, cursor position awareness, and real-time collaboration between the CLI and editor.

- JetBrains IDE plugin with core functionality (open file, apply diff, get context)
- Enhanced Neovim integration with bidirectional communication
- Zed editor full integration completion
- Common IDE Context Protocol specification
- Shared context synchronization across CLI and IDE
- IDE detection improvements for automatic integration
- Documentation and setup guides for each supported IDE

- Required: TypeScript/Node.js, at least one IDE plugin development experience
- Preferred: JetBrains plugin SDK, Neovim Lua, Zed extension API

- Shreya Keshive

Difficulty: Easy-Medium | Size: 90 hours | Area: Observability/DX

Build an in-CLI performance monitoring dashboard that provides developers and contributors with visibility into Gemini CLI's runtime behavior. This includes startup time analysis, memory usage tracking, tool execution profiling, and model latency metrics. The dashboard helps identify performance regressions and optimization opportunities while providing users with session statistics.

- In-CLI performance dashboard accessible via /stats or /perf command
- Startup time breakdown and optimization suggestions
- Memory usage monitoring with warnings for high consumption
- Tool execution timing and frequency statistics
- Model API latency tracking
- Session statistics (tokens used, tools called, files modified)
- Performance regression detection for CI integration
- Export capability for performance reports

- Required: TypeScript/Node.js, CLI/TUI development, performance profiling
- Preferred: React/Ink, data visualization, OpenTelemetry

- Sehoon Shon

Difficulty: Medium | Size: 175 hours | Area: UX/UI

Enhance the Ink-based terminal UI to provide deep visibility into the agent's internal reasoning and tool execution chains. Currently, complex multi-step tasks can be a "black box" for users. This project involves building an interactive visualization that shows the hierarchy of tasks, tool calls, and model decisions in real-time, allowing users to "step through" execution like a debugger.

- Real-time task tree visualization in the Ink TUI
- "Step-through" mode where users must approve individual tool calls or agent decisions
- Rich-text rendering of tool inputs/outputs with collapsible sections
- Improved error state visualization for nested agent failures
- User-configurable verbosity levels for different task categories

- Required: React (Ink), TypeScript, State Management
- Preferred: CLI UX design, experience with asynchronous UI updates, terminal rendering optimizations

- Jacob Richman

Difficulty: Hard | Size: 175 hours | Area: Integration/DX

Integrate Gemini CLI with standard debugging protocols (DAP) to provide an interactive debugging companion. The agent should be able to attach to running processes (Node.js, Python, Go, etc.), set breakpoints, inspect stack traces, and query variable states to assist in root-cause analysis of bugs directly within the terminal interface.

- Debugger toolset for the agent using Debug Adapter Protocol (DAP)
- Automated stack trace analysis and variable inspection tools
- Interactive "debug mode" where the agent can pause execution and ask for clarification
- Seamless integration with existing run_shell_command for launching debug sessions
- Automated fix suggestions based on runtime state inspection

- Required: Node.js, Debugger Internals (DAP), TypeScript
- Preferred: Experience with VS Code debugger extensions or LLM-driven debugging

- Keith Schaab

Difficulty: Hard | Size: 350 hours | Area: Security

Implement a native Windows sandboxing driver using Windows AppContainer or the Windows Sandbox API. Currently, Gemini CLI on Windows relies on Docker Desktop for isolation. A native driver would provide a lighter, faster, and dependency-free experience for Windows users, utilizing OS-level security primitives to isolate file system and network access effectively.

- Native Windows sandbox driver implementation using AppContainer
- Parity with macOS Seatbelt for file system and registry restrictions
- Network isolation using Windows Filtering Platform (WFP)
- Automated setup and validation tool for Windows security features
- Performance benchmarks showing improvement over Docker-based isolation on Windows
- Detailed security audit of the native implementation

- Required: C#, Windows APIs (AppContainer, Win32), Node-API/TypeScript
- Preferred: Security-focused Windows development, experience with Windows Sandbox

- Gaurav Ghosh

Difficulty: Easy | Size: 90 hours | Area: Security/UX

Build a guided configuration "Wizard" to help users set up and manage security policies for different projects. The wizard will simplify the creation of Seatbelt profiles and Docker mount configurations, providing a user-friendly way to define "safe zones" and network permissions for the agent, ensuring that security is accessible even to non-experts.

- Interactive gemini sandbox-setup command with a guided UI
- Visual dashboard for reviewing and auditing active sandbox permissions
- Per-project policy file management (.gemini/policy.json)
- Template-based security profiles for common project types (Web, CLI, API)
- Real-time policy validation and conflict detection

- Required: React (Ink), TypeScript, Security concepts
- Preferred: CLI design, experience with security configuration or policy-as-code

- Gal Zahavi

Difficulty: Medium | Size: 175 hours | Area: Architecture/Security

Refactor the Gemini CLI's sandboxing logic into a modular, plugin-based driver architecture. Currently, sandboxing logic is split across the CLI and Core packages with many platform-specific conditional checks. This project involves creating a clean SandboxDriver interface that abstracts away the platform-specific details, making it easy to support macOS Seatbelt, Linux Bubblewrap, Windows AppContainer, and Docker through a unified API. This architecture will serve as the foundation for all future native sandboxing implementations.

- A well-defined SandboxDriver TypeScript interface and lifecycle manager in @google/gemini-cli-core.
- Refactored macOS Seatbelt and Docker/Podman implementations using the new interface.
- A "No-Op" driver for unsandboxed environments that provides consistent logging and warnings.
- Support for dynamic driver discovery and selection based on host OS and user configuration.
- Improved error handling and diagnostic tools for sandbox initialization failures.
- Comprehensive unit and integration tests for the new driver lifecycle.

- Required: TypeScript, Software Architecture (SOLID principles), Node.js.
- Preferred: Experience with plugin systems or abstraction layers, cross-platform development, systems programming concepts.

- Taylor Mullen

Difficulty: Hard | Size: 350 hours | Area: Innovation/Multimodal

Transform Gemini CLI into a hands-free, conversational coding partner—your personal J.A.R.V.I.S. for software development. This project builds a real-time, bidirectional voice interface where developers can speak naturally to the agent and hear responses read aloud. Unlike basic speech-to-text wrappers, this leverages Gemini's native multimodal audio capabilities for a fluid, continuous conversation with minimal latency.

- Real-time voice input/output using Gemini's native audio streaming API
- Multiple activation modes: Voice Activity Detection (VAD), Push-to-Talk (hotkey), Wake Word ("Hey Gemini")
- Visual feedback: animated waveform visualizer showing listening/speaking/processing states
- Interruption support: speak to stop the agent's current response
- Voice-optimized response formatting (concise, spoken-friendly output)
- Audio feedback and text-to-speech for agent responses with configurable voices
- Noise cancellation and multi-accent robustness

- Required: TypeScript/Node.js, Audio processing (PCM, WAV, WebAudio), Real-time streaming
- Preferred: Gemini Multimodal API, Voice Activity Detection, Whisper integration, accessibility engineering

- Bryan Morgan

Difficulty: Medium | Size: 175 hours | Area: Innovation/UX

Break the "text-only" constraint of the terminal by teaching Gemini CLI to draw. This project enables the agent to generate and render visual artifacts directly in the terminal console—architecture diagrams, dependency graphs, data flow visualizations, and even live previews of generated UI components. Using Mermaid.js for diagrams and terminal image protocols (Sixel, iTerm2, Kitty) for rich graphics, developers can finally see what they're building without context-switching to a browser or IDE.

Imagine asking "explain the authentication flow" and seeing a beautifully rendered sequence diagram appear inline. Or generating a React component and instantly seeing a pixel-perfect preview in your terminal. This transforms the CLI from a text interface into a visual development environment.

- Inline rendering of architecture diagrams (Sequence, Class, ERD, Flowcharts) generated from codebase analysis
- Live preview of generated frontend components (HTML/CSS/React) rendered as terminal images
- Support for multiple terminal image protocols: Sixel, iTerm2 inline images, Kitty graphics protocol
- Intelligent ASCII/ANSI box-drawing fallback for unsupported terminals
- New tool: visualize for on-demand diagram generation
- Integration with explain command ("Explain this architecture" → renders diagram)
- Dependency graph visualization for package.json/requirements.txt
- Git history visualization (branch graphs, contributor timelines)
- Caching layer for rendered images to avoid regeneration

- Paradigm shift: No CLI coding tool renders rich graphics—this is genuinely new
- Frontend developer appeal: Instant visual feedback without leaving the terminal
- Viral demo potential: Terminal diagrams are visually striking and shareable

- Required: TypeScript/Node.js, Image processing (Sharp, node-canvas), streaming I/O
- Preferred: Terminal graphics protocols (Sixel, iTerm2), Mermaid.js/Graphviz, Puppeteer for HTML rendering

- Dmitry Lyalin
