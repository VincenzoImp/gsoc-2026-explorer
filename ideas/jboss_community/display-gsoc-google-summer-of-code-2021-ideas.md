# here

**Parent:** JBoss Community — Project Ideas
**Source:** https://spaces.redhat.com/display/GSOC/Google+Summer+of+Code+2021+Ideas?preview=/81428506/84871584/Sample%20GSoC%20proposal%20document.pdf
**Scraped:** 2026-02-22T23:28:47.565289

---

General Information

The JBoss Community is planning to participate in Google Summer of Code in 2021.

All students & developers are welcome to participate in the [https://summerofcode.withgoogle.com/](https://summerofcode.withgoogle.com/) program with the JBoss Community (once JBoss Community is accepted by Google)!

We are welcoming [Code for Cause ](https://codeforcause.org)under the umbrella of JBoss Community for GSoC 2021.

You can take look at the [org page](https://summerofcode.withgoogle.com/organizations/4681338905427968/) of the Summer of Code website for proceeding with the application process.

If you are a student looking forward to participating in the GSoC 2021 with the JBoss Community, feel free to browse the growing idea list below. Please don't hesitate to contact the mentor(s) indicated in the proposal for any related clarification and to discuss proposals. Students can submit the proposals in 2021.

You can also look at [GSoC-16 Ideas](https://developer.jboss.org/docs/DOC-54771), [2017 Ideas](https://developer.jboss.org/docs/DOC-55884), [2018 Ideas](https://developer.jboss.org/docs/DOC-56085), [2019 Ideas](https://developer.jboss.org/docs/DOC-56368), and [2020 Ideas](https://docs.jboss.org/display/GSOC/Google+Summer+of+Code+2020+ideas) for suggestions from last years.

**STUDENTS:** You may find a Sample GSoC proposal document [here](https://spaces.redhat.com/download/attachments/467058571/Sample%20GSoC%20proposal%20document.pdf?version=1&modificationDate=1615434853000&api=v2) which was for [this](https://docs.jboss.org/display/GSOC/Google+Summer+of+Code+2020+ideas#GoogleSummerofCode2020ideas-Knative-AlternativeKnativeBrokerImplementationbasedonApacheKafka) idea.

A note to mentors

MENTORS: Red Hat employees can change this page directly to add ideas. Please be extra careful to not get other mentor's edits discarded.

Red Hatters should have linked their [jboss.org](http://jboss.org) account with Red Hat and can be checked on [https://sso.jboss.org/login](https://sso.jboss.org/login)

Non-Red Hatters can add a comment to the page and admins will make sure the idea is added to the page.

__Table of Contents__

__Administrators and Mentors__

We will list the potential mentors in this place. For now, if you have any questions, please contact the GSoC administrators:

George Zaronikas ([gzaronikas](https://developer.jboss.org/people/gzaronikas)) Ali Ok ([@aliok_tr](https://twitter.com/aliok_tr)) and Anuj Garg ([@KeenWarrior](https://twitter.com/KeenWarrior)).

This year's GSoC is different.

Previously GSoC was 12 weeks with 30 hours/week commitment by students but this year it is 10 weeks with 18 hours/week commitment. So, it is %50 reduced.

Please consider this in your idea proposals.

__Communication channels__

Gitter : [JBossOutreach/GSoC - Gitter](https://gitter.im/JBossOutreach/GSoC)

Please take note - These channels are about generic doubts. For project-specific doubts you will need to contact project mentors and channels specified in the project description.

__Notes for students__

**Points to consider while choosing any project**

1. You meet at least 50 percent of the requirements. The remaining skills can be honed on the go, so don't worry if you lack some.

2. You can relate to the project idea and you have used something related to the project as a user.

3. You are willing more toward learning the skills and less toward boasting about the skills you have already.

**Suggested steps after choosing a favorite project**

1. Start to use product/tool/API as a user or hello world client application.

2. Setup the development environment for the project and start to use your own build.

3. Look for newcomer bugs and try to get your head around them.

4. Let us know if you feel stuck at any stage.

__Idea template (for mentors)__

### Project title


**Summary of idea:**

-Idea

-Feature A

-Feature B

Knowledge prerequisite: Languages/Technologies goes here

Github repo:

Skill level: Beginner/Intermediate/Advanced

Contact(s) / potential mentors(s): Mentor(s) name and contact details

Associated JBoss community project(s):

__Idea Proposals__

__Thread support in Drogue IoT__

**Summary of idea:**

The Drogue IoT project aims to support different types of connectivity to Drogue IoT Cloud. Although we have drivers and examples for WiFi, LoRa and Bluetooth LE at present, we would like to

expand support to protocols like Thread. There are several building blocks in Thread that is missing from the Rust ecosystem:

- 6LoWPAN - One building block for data transport is the 6LoWPAN protocol that maps IPv6 on top of link layers like Bluetooth LE or 802.15.4 (used in Thread)
- DHCPv6 - A DHCPv6 client is needed in order to configure a Thread device with an IPv6 address
- DNSv6 - A DNSv6 client is needed for a Thread device to map hostnames to IPv6 addresses

Each of these building blocks are probably a project on its own, so its probably best to focus on one.

Knowledge prerequisite:

- Embedded programming
- Basic understanding of network programming
- Reading protocol specifications
- Rust (optionally)

Github organization: [https://github.com/drogue-iot](https://github.com/drogue-iot)

Skill level: Intermediate

Project Chat: [https://matrix.to/#/#drogue-iot:matrix.org](https://matrix.to/#/#drogue-iot:matrix.org)

Contact(s) / potential mentors(s): Ulf Lilleengen (lulf@[redhat.com](http://redhat.com))

Associated JBoss community project(s): Drogue IoT

__CoAP protocol support for constrained devices in Rust__


**Summary of idea:**

The Drogue IoT project aims to support different types of connectitiby to Drogue IoT Cloud with examples for embedded devices written in Rust. One such protocol is the Constrained Application Protocol (CoAP).

The goal of this project is to provide a CoAP protocol library that compiles and runs on constrained embedded devices (no_std). It is not expected that the entire protocol spec is supported, having a working CoAP client sending

requests to a cloud server would be a great achievement. Reusing existing open source crates and adopting them to support constrained devices is fine, so the first phase of the project would be to identify potential libraries that could be reused and/or adopted.

Knowledge prerequisite:

- Embedded programming
- Basic understanding of network programming
- Reading protocol specs
- Rust (optionally)

Github organization: [https://github.com/drogue-iot](https://github.com/drogue-iot)

Skill level: Intermediate

Project Chat: [https://matrix.to/#/#drogue-iot:matrix.org](https://matrix.to/#/#drogue-iot:matrix.org)

Contact(s) / potential mentors(s): Ulf Lilleengen (lulf@[redhat.com](http://redhat.com))

Associated JBoss community project(s): Drogue IoT

__MQTT client support for constrained devices in Rust__


**Summary of idea:**

The Drogue IoT project aims to support different types of connectitiby to Drogue IoT Cloud with examples for embedded devices written in Rust. One such protocol is the MQTT (Message Queuing Telemetry Transport).

The goal of this project is to provide a MQTT client library that compiles and runs on constrained embedded devices (no_std). It is not expected that the entire protocol spec is supported, having a working MQTT client sending

unacked MQTT messages to a MQTT server would be a great achievement. Reusing existing open source crates and adopting them to support constrained devices is fine, so the first phase of the project would be to identify potential libraries that could be reused and/or adopted.

Knowledge prerequisite:

- Embedded programming
- Basic understanding of network programming
- Reading protocol specs
- Rust (optionally)

Github organization: [https://github.com/drogue-iot](https://github.com/drogue-iot)

Skill level: Intermediate

Project Chat: [https://matrix.to/#/#drogue-iot:matrix.org](https://matrix.to/#/#drogue-iot:matrix.org)

Contact(s) / potential mentors(s): Ulf Lilleengen (lulf@[redhat.com](http://redhat.com))

Associated JBoss community project(s): Drogue IoT

### New Drogue IoT protocol endpoint


**Summary of idea:**

On feature of Drogue IoT Cloud is to normalize the transport protocol from IoT specific protocols to Cloud Events. We currently have endpoints for MQTT and HTTP. However, there are much more protocols out there that could be added, like CoAP for example.

Choosing a protocol you would like to implement must be done as part of the project proposal, and not as part of the project. There is no need to implement whatever protocol you choose from scratch. The focus should be on the integration of the protocol to the cloud deployment, not on implementing the protocol itself.

The current protocol endpoints are written in Rust. However, implementing your protocol endpoint in Rust is not a requirement. Still, it would be a chance for you to learn about an awesome programming language, if you are up for that challenge.

Knowledge prerequisite:

- Kubernetes
- Knative
- Rust (optionally)

Github repo: [https://github.com/drogue-iot/drogue-cloud](https://github.com/drogue-iot/drogue-cloud)

Skill level: Intermediate

Project Chat: [https://matrix.to/#/#drogue-iot:matrix.org](https://matrix.to/#/#drogue-iot:matrix.org)

Contact(s) / potential mentors(s): Jens Reimann ([jreimann@redhat.com](mailto:jreimann@redhat.com))

Associated JBoss community project(s): Drogue IoT

### Implement "Hey Rodney" Drogue IoT demo using Tensorflow (Lite)


**Summary of idea:**

In Drogue IoT we have an example/demo/PoC, which implements a voice assistant based on our Drogue IoT cloud deployment. There is wake-word/keyword/trigger-word detection, which initiates the audio recording. Once the snippet is recorded it will be processed by a speech-to-text backend and is further processed.

For the wake-word detection we are currently using Pocketsphinx. However, the detection rate is pretty bad. Also it doesn't run on embedded devices.

The outcome of the project should be to use Tensforflow (Lite) to create a model for wake word detection. Additionally a program (script) which continuously listens to audio input (microphone). Once the trigger is detected, it records for up to X seconds, or until it detects silence. A single command is sufficient ("hey rodney"), no full speech-to-text model is required. It is perfectly fine to re-use existing data sets and scripts, as long as they are open source, and we can build this ourselves.

This should be able to run on a Raspberry Pi like device, with the prospect of being able to run on embedded devices (microcontroller) using Tensorflow Lite. Bonus points for actually porting that to a micro-controller, but that is not required.

Knowledge prerequisite:

- AI/ML - Tensorflow
- Python (probably)
- Linux
- Embedded programming (optionally)

Github repo: [https://github.com/drogue-iot/drogue-cloud,](https://github.com/drogue-iot/drogue-cloud) [https://github.com/drogue-iot/hey-rodney](https://github.com/drogue-iot/hey-rodney)

Skill level: Advanced

Project Chat: [https://matrix.to/#/#drogue-iot:matrix.org](https://matrix.to/#/#drogue-iot:matrix.org)

Contact(s) / potential mentors(s): Jens Reimann ([jreimann@redhat.com](mailto:jreimann@redhat.com))

Associated JBoss community project(s): Drogue IoT

__EAT - Testing Infinite Software Project Versions__

**Summary of idea:**

The innovative part of EAT is creating the test once and testing with any version of the tested software. It may be firstly applied for the JBoss Servers, but, in general, a similar structure, can be used for creating tests about any software with multiple versions or for multiple software programs that have a part of the testsuite in common. EAT is a project under the ΙΔΕΑ statement.

Possible tasks for this project :

Go through the EAT workshop, extending the existing AT testsuites, creating a new testsuite using the AT Structures, etc (the students should make their proposals)

Github repo: [https://github.com/EAT-JBCOMMUNITY/EAT](https://github.com/EAT-JBCOMMUNITY/EAT)

Contact / potential mentors: Panagiotis Sotiropoulos ([psotirop@redhat.com](mailto:psotirop@redhat.com))

Associated JBoss community project: EAT

**Classrooms and Doubt Forum Feature in Mobile Application**** **

**Classrooms and Doubt Forum Feature in Mobile Application**

**Summary of idea:**

Product focuses on 100% education as well as upskilling developing countries and rural areas. This idea expects completing mobile application features.

- Doubt Forum
- Gamification board (Scoring by helping others and being active)
- Contests and Statistics Dashboard
- Classrooms (For streaming lectures, managing recordings, managing assignments and contests)

Knowledge prerequisite:

- JavaScript
- ReactJS
- Mobile development Experience in Any Tech (optionally)
- Ionic / Capacitor (optionally)

Skill level: Medium

Project Chat: Discord #gsoc Channel at [https://discord.gg/dydQp2Q](https://discord.gg/dydQp2Q)

Github repo: [https://github.com/codeforcauseorg/edu-client](https://github.com/codeforcauseorg/edu-client)

Contact(s) / potential mentors(s): Anuj Garg ([anuj@codeforcause.org](mailto:anuj@codeforcause.org))

Associated Sub Organisation: Code for Cause [https://codeforcause.org](https://codeforcause.org)

**Create and Enhance APIs related to Education Platform**

**Create and Enhance APIs related to Education Platform**

**Summary of idea:**

Product focuses on 100% education as well as upskilling developing countries and rural areas. This idea expects completing NestJS server application.

- Doubt Forum API
- Scoring API
- Contest API
- Assignments API

Knowledge prerequisite:

- JavaScript
- NestJS
- Docker (Optionally)

Skill level: Medium

Project Chat: Discord #gsoc Channel at [https://discord.gg/dydQp2Q](https://discord.gg/dydQp2Q)

Github repo: [https://github.com/codeforcauseorg/edu-server](https://github.com/codeforcauseorg/edu-server)

Contact(s) / potential mentors(s): Anuj Garg ([anuj@codeforcause.org](mailto:anuj@codeforcause.org)), Ganga Chaturvedi ([ganga@codeforcause.org](mailto:ganga@codeforcause.org))

Associated Sub Organisation: Code for Cause [https://codeforcause.org](https://codeforcause.org)

### Drools - Executable Model Compiler 2.0

**Summary of the idea:**

Drools is a business rules management system that allows developers and business analysts to write business rules in an easy way and to evaluate such rules in the fastest way possible. With the “executable model” we provided a Java DSL to write such rules in a typesafe way, leveraging the javac compilation to get fast startup time while instantiating the engine. The original DRL (Drools Rules Syntax) language is supported: we provide a compiler to compile the DRL to Java Code.

The original executable model compiler needs some improvement: the idea is to generate the executable model code in the fastest way possible.

We targeted correctness rather than speed in 1.0, and by rewriting the type checker and leveraging a multi phase approach we could theoretically support parallel compilation. We also have some known performance issues in lambda externalisation - as it’s implemented as a post processing phase it adds extra time to the compilation. We’d love to have a performance oriented approach, in which we measure the build time from the start so that it should be easier to track the wanted speed. Correctness is guaranteed by the current test suite that should be supported 100%. We should avoid JavaParser AST generation in the processing phase, as its AST is not optimized for sharing and cloning it’s an expensive operation.

Project references:

[http://blog.athico.com/2018/02/the-drools-executable-model-is-alive.html](http://blog.athico.com/2018/02/the-drools-executable-model-is-alive.html)

**Knowledge Prerequisite:**

- The Java Programming Language
- Basic understanding of Pattern Matching
- Basic understanding of Rule Engine

**Skill Level: Intermediate**

**Contact:** Luca Molteni ([lmolteni@redhat.com](mailto:lmolteni@redhat.com))

**GitHub: **

[https://github.com/kiegroup/drools](https://github.com/kiegroup/drools)

**Associated JBoss community project(s):** [https://drools.org](https://drools.org/)

### 3scale - Envoy proxy authorization cache


**Summary of idea:**

3scale is an API management platform that provides API lifecycle management, access control, developer portal, and gateway integration. This project aims to implement an authorization cache locally accessible from Envoy proxy-wasm modules that contains 3scale-specific knowledge to intelligently cache request authorization results in order to minimize request latencies while keeping the 3scale control plane periodically synchronized.

As with many cache implementations, there are trade-offs to be made. In this case we strongly lean towards lower latencies rather than high accuracy, so we can take some design decisions that leverage this fact. The main goal of this cache layer is that it becomes usable locally from proxy-wasm modules, but having it also work standalone deployed as a separate HTTP or gRPC service is a nice extra. Having it return information to the caller so that a proxy can return rate-limiting headers is a requirement. Learning about the 3scale data model and its Service Management API is part of the learning process involved in this project.

References:

- Proxy-WASM:
[https://github.com/proxy-wasm/spec](https://github.com/proxy-wasm/spec), talk:[https://bit.ly/3a22R5B](https://bit.ly/3a22R5B)

- Design document for a similar authorization cache:
[https://github.com/3scale/3scale-authorizer/blob/master/pkg/backend/v1/docs/README.md](https://github.com/3scale/3scale-authorizer/blob/master/pkg/backend/v1/docs/README.md)

- Rate-limiting headers IETF draft:
[https://datatracker.ietf.org/doc/draft-ietf-httpapi-ratelimit-headers/](https://datatracker.ietf.org/doc/draft-ietf-httpapi-ratelimit-headers/)

**Knowledge Prerequisite:**

- Basic Envoy proxy knowledge
- Rust
- gRPC (optional)
- WebAssembly (optional)

**Github organization:** [https://github.com/3scale](https://github.com/3scale)

**Skill level:** Intermediate

**Contact(s) / potential mentors(s):** Alex Martinez Ruiz ([amr@redhat.com](mailto:amr@redhat.com))

**Associated JBoss community project(s):** 3scale API Management

__AeroGear - Apache Kafka and GraphQL quick-starts__

**Summary of idea:**

Apache Kafka is a popular messaging platform that can be used to build reactive backends.

This project aims to provide sample applications (quickstarts) for various programming languages that will use:

- Postgres (or MongoDb) Databases
- GraphQL Subscriptions
- Apache Kafka for eventing (might use Debezium for database driven events)


Candidates would also need to provide the modular architecture of the examples so they can be consumed with both REST (ServerSent events) and GraphQL subscriptions.

**Knowledge prerequisite:**

- Knowledge one of the languages used to write example (Node.js, Python, Golang, Kotlin, ?)
- Basic understanding of reactive programming
- Knowledge of GraphQL
- Familiarity AeroGear community projects like
[https://graphback.de](https://graphback.dev)v

Github org: [https://github.com/aerogear](https://github.com/aerogear)

Skill level: Beginner

Project Chat: [https://discord.com/invite/mJ7j84m](https://discord.com/invite/mJ7j84m)

Contact(s) / potential mentors(s): Wojciech Trocki (wtr@[redhat.com](http://redhat.com))

Associated JBoss community project(s): AeroGear

__AeroGear - KNative "Herd" CLI__

**Summary of idea:**

Knative is an serverless platform offering ability to deploy your projects to kubernetes.

In this project we would like to explore ability to build lighweight framework for connecting multiple serverless functions with underlying services and API gateway.

Candidates can work on providing new abstraction on top of the KNative offering ability to create "herd" of functions that can be written in more than one language.

Developers can provide custom configuration for functions and build wrapper for KNative CLI offering simplicity to build and deploy multiple functions as single application.

Serverless functions that can be automatically added to the API gateway serving both GraphQL and Rest endpoints.

Suggested languages that can be used for building this ecosystem:

- Node.js
- Quarkus (Java)
- Golang
- Python

Candidates would also need to provide examples of using eventing and database access for at least 1 of the languages.

**Knowledge prerequisite:**

- Knowledge one of the languages (Node.js, Python, Golang, Kotlin, ?)
- Basic understanding of KNative
- Knowledge of GraphQL
- Familiarity AeroGear community projects like
[https://graphback.de](https://graphback.dev)v

Github org: [https://github.com/aerogear](https://github.com/aerogear)

Skill level: Intermediate

Project Chat: [https://discord.com/invite/mJ7j84m](https://discord.com/invite/mJ7j84m)

Contact(s) / potential mentors(s): Wojciech Trocki (wtr@[redhat.com](http://redhat.com))

Associated JBoss community project(s): AeroGear

### Debezium Schema History Compaction Tool


**Summary of idea:**

[Debezium](https://debezium.io/) is an open-source platform for change data capture (CDC) and lets you stream data change events out of a variety of databases such as MySQL, Postgres, SQL Server, MongoDB and others. The idea of this proposal is to provide a stand-alone tool for compacting the schema history topic used by several Debezium connectors.

Your mission, should you decide to accept it, will be:

- Develop a tool – based on the Quarkus stack – which "compacts" a given schema history topic; this tool should
- Read a schema history topic from the beginning
- Build up the in-memory represntation of the database schema
- Serialize that schema into a new topic, only containing the current state of the schema

- Test that tool
- Document the usage of the tool, e.g. describing how to re-configure associated connectors, so to make use of the compacted topic, etc.
- Create a demo (e.g. as a video) and blog post show-casing how that tool can be used

See Jira issue [DBZ-747](https://issues.redhat.com/browse/DBZ-747) for further details of this project idea.

Knowledge prerequisite: Java, Git, Maven, at least one of the databases supported by Debezium

Github repo: [https://github.com/debezium/debezium](https://github.com/debezium/debezium)

Skill level: Intermediate/Advanced

Contact(s) Gunnar Morling (gmorling AT redhat DOT com)

Associated JBoss community project(s): [Debezium](https://debezium.io/)

### Porting the Debezium Cassandra Connector to Debezium Server


**Summary of idea:**

[Debezium](https://debezium.io/) is an open-source platform for change data capture (CDC) and lets you stream data change events out of a variety of databases such as MySQL, Postgres, SQL Server, MongoDB and others. The idea of this proposal is to port the existing stand-alone main class for the Debezium Cassandra connector to [Debezium Server](https://debezium.io/documentation/reference/operations/debezium-server.html) as its runtime environment.

Your mission, should you decide to accept it, will be:

- Implement an outbound adaptor for Debezium Server which sends change events to Apache Kafka (similar to the existing adaptors for Apache Pulsar, Amazon Kinesis, Google Cloud Pub/Sub etc.)
- Replace the existing stand-alone main class with the Debezium Server runtime
- Adapt Debezium Server, so that it not only can be used with the Kafka Connect based Debezium connectors, but also with the Cassandra connector implementation
- Replace means of configuration with those of Debezium Server (application.properties file, etc.)
- Update tests and documentation accordingly

- Optional: Refactor the Cassandra connector implementation to make use of Debezium's common connector framework as far as possible
- Create a demo (e.g. as a video) and blog post show-casing how the connector can be used after this re-implementation

See Jira issue [DBZ-2098](https://issues.redhat.com/browse/DBZ-2098) for further details of this project idea.

Knowledge prerequisite: Java, Git, Maven; ideally Cassandra

Github repo: [https://github.com/debezium/debezium](https://github.com/debezium/debezium)

Skill level: Intermediate/Advanced

Contact(s) Gunnar Morling (gmorling AT redhat DOT com)

Associated JBoss community project(s): [Debezium](https://debezium.io/)

### Create JWS Openshift Operator in Java


**Summary of idea:**

JWS can be deployed in Openshift via the JWS Operator. Currently, JWS Openshift operator is written in Golang using the operator-sdk. The mission of this project is to study and develop JWS Operator in Java, using java-operator-sdk ([https://github.com/java-operator-sdk/java-operator-sdk](https://github.com/java-operator-sdk/java-operator-sdk)).

Students can get the main idea from our Golang operator which is here: ** https://github.com/web-servers/jws-operator** and adapt its functionality to the new java-operator-sdk based one.

**Knowledge prerequisite: **Java, Golang, Kubernetes/Openshift, Operators(optional)

**Github repo: https://github.com/web-servers/jws-operator**



**Skill level: **Advanced

**Contact(s) / potential mentors(s):** Jean-Frederic Clere (jfclere AT redhat DOT com), George Zaronikas (gzaronik AT redhat DOT com)

__WildFly Elytron: Adding Encryption to the Filesystem Security Realm__

**Summary of idea:**

The [WildFly Elytron](https://wildfly-security.github.io/wildfly-elytron/) project provides a set of APIs, SPIs, and implementation to the [WildFly](https://www.wildfly.org/) application server to provide the required security capabilities in an application server environment. WildFly Elytron was integrated back during the development of WildFly 11. We are now getting ready to make a WildFly Elytron based configuration the default within WildFly and are looking to define our new out of the box security policies.

One of the components provided by WildFly Elytron is a security realm used to store representations of identities and their credentials using the local filesystem. For our new policy, we are looking to make use of this security realm instead of the previous approach of using property files. A missing feature in the [filesystem realm](https://github.com/wildfly-security/wildfly-elytron/blob/1.x/auth/realm/base/src/main/java/org/wildfly/security/auth/realm/FileSystemSecurityRealm.java) is the ability to securely encrypt the identities that are stored on the local filesystem. The purpose of this project is to work on the addition of this encryption support and related tasks required to make this available out of the box in WildFly.

A minimal level of support would be for a [SecretKey](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/javax/crypto/SecretKey.html) to be provided to the filesystem realm as it is initialized. The level of encryption required will need to be determined. Different levels could have different policies. Some examples of things to consider include:

- Encryption of credentials.
- Encryption of attributes.
- Complete obfuscation of the username.
- Signing of sections of an identity or the complete identity.
- Integrity of the whole realm.

Possible tasks for this project:

- Research data at rest recommendations for user credentials and sensitive data.
- Create a document that describes how you plan to approach the problem.
- Implement the ability to securely encrypt identities that are stored in the filesystem security realm.
- Implement appropriate test cases.
- Write documentation.
- Create a blog post that gives an overview of your project.
- Add the ability for the WildFly Elytron Tool to take an existing clear text filesystem realm and convert it to an encrypted one.

**Knowledge prerequisites:**

- Experience with Java
- Git
- Maven

**Github repo: **[https://github.com/wildfly-security/wildfly-elytron](https://github.com/wildfly-security/wildfly-elytron)

**Elytron website: **[https://wildfly-security.github.io/wildfly-elytron](https://wildfly-security.github.io/wildfly-elytron/)

**Elytron getting started guide:** [https://wildfly-security.github.io/wildfly-elytron/getting-started-for-developers](https://wildfly-security.github.io/wildfly-elytron/getting-started-for-developers)

**Skill level: **Intermediate

**Contact(s) / potential mentor(s):** Darran Lofthouse ([darran.lofthouse@redhat.com](mailto:darran.lofthouse@redhat.com)), Farah Juma ([fjuma@redhat.com](mailto:fjuma@redhat.com)), and Diana Krepinska ([dvilkola@redhat.com](mailto:dvilkola@redhat.com))

**Associated JBoss community project(s):** Elytron, WildFly

## Project Starfix - Open anything anywhere in any IDE/editor


**Summary of idea:**

Implement a client side app that supports urlhandlers (i.e. [ide://clone-url?url=](ide://clone-url?url=)[https://github...](https://github...) , [ide://open-file](ide://open-file)?, [ide://open-debugger?port=..&project=url](ide://open-debugger?port=..&project=url), etc.)

Then integrate these various actions to perform and setup in vscode, eclipse, intellij, emacs, vi, etc.

This would be a continuation of work done in 2020 where it was made to work across Linux, OSX and Windows so it can be used from anywhere.

Also a browser extensions to enable it on various websites like github, gitlab, etc.

Possible tasks for this project:

- Implement actual basic commands and have it work for all major IDE's
- Make distribution using jbang and/or jreleaser
- Integrate it with Quarkus open code in IDE feature
- Add tests
- Write documentation
- Prepare demos

Knowledge prerequisite:

- Java
- Basic understanding of IDE and/or Browser extensions
- Access to more than one of the Operating Systems, virtual machines okey.

Github repo:

[https://github.com/starfix/s](https://github.com/maxandersen/starfish)[tarfix](https://github.com/starfixdev/starfix) for having a place of discussion/conversion.

If you want to explore/work in this area and show your experience/interest you can look into contributing to projects like [https://github.com/maxandersen/jbang](https://github.com/maxandersen/jbang,) or [https://github.com/quarkusio](https://github.com/quarkusio). Basically any project that relates to developer tools, desktop tools, scripts or browser extensions will be useful experience.

Slides:

An outline of the idea with some screenshots/overview can be found [here](https://www.twint.ch/press/digitec-galaxus-verbreitet-unwahre-informationen/) - feel free to comment.


Skill level: Beginner/Intermediate

Contact(s) / potential mentors(s): Max Rydahl Andersen (manderse@[redhat.com](http://redhat.com))

Associated JBoss community project(s): Quarkus, vscode extensions, JBoss Tools

## Quarkus - API validation and tracking for Quarkus and Quarkiverse


**Summary of idea:**

Quarkus does timeboxed releases every 4 to 6 weeks which includes Quarkus core and 180+ extensions. We aim for not breaking users and extensions writers but we also don’t want to stand still and not be able to innovate. Today we manually maintain a migration wiki page on what needs migrating if anything between releases. Project idea is to utilize the already existing [revapi.org](http://revapi.org) setup and expand it to properly detect and generate documentation for api breakages in a way that help users and extension writers.

When this is done it will be a key central element in Quarkus releases and used heavily across all extensions. If done right it will have a massive impact on enabling Quarkus to continue to innovate.

Expected Technologies to be used: [revapi.org](http://revapi.org), java, quarkus, asciidoctor

#### Internship Tasks

- Learn to use revapi

- Enhance the current revapi reporting to be useful

- Automate revapi usage in Quarkus CI build

- Document and script for daily usage of revapi

Stretch goals:

- Implement additonal revapi checks for i.e. property, library and configuraton changes

#### Intern Benefits

You will get to work with one of the fastest growing Java frameworks in newer times.

You will work with a 100% remote and distributed team.

You will learn about how to write frameworks, how to keep API stable and how to evolve them.

When successful this revapi integration will have many year impact on ensuring Quarkus development team and users will be able to upgrade and migrate for years to come. It will be used daily by development team and on each monthly release of Quarkus the whole ecosystem will benefit from this work.

### Project Contribution Information

As part of the application process, all applicants must make at least one contribution to be accepted as an intern for this project. Only applicants who make a contribution will be eligible to be accepted as interns. This community requires applicants to complete a tutorial before they can make their contributions.

Please follow [https://quarkus.io/get-started/](https://quarkus.io/get-started/) and [https://quarkus.io/guides/rest-json](https://quarkus.io/guides/rest-json) to learn the basics of Quarkus.

You can read [https://github.com/quarkusio/quarkus/blob/master/CONTRIBUTING.md](https://github.com/quarkusio/quarkus/blob/master/CONTRIBUTING.md) to get an idea on how things works but not a first time requirement.

Applicants can contribute to this project through [the project repository or contribution page](https://github.com/quarkusio). The project uses an [issue tracker](https://github.com/quarkusio/issues) to keep information about bugs to fix, project features to implement, documentation to write, and more. Applicants can look for newcomer-friendly issues to use for their first contributions by looking for the following issue tags in the [project issue tracker](https://github.com/quarkusio/issues): good first issue

Work with your mentor on identifying and/or create github issues with description on what you plan to do.

You can see [https://quarkus.io/community/](https://quarkus.io/community/) for community resources.

Especially [https://groups.google.com/g/quarkus-dev](https://groups.google.com/g/quarkus-dev) is the mailing list and [https://quarkusio.zulipchat.com/login/](https://quarkusio.zulipchat.com/login/)

Contact "maxandersen" on Zulip to get started.

Skill level: Beginner/Intermediate

Contact(s) / potential mentors(s): Max Rydahl Andersen (manderse@[redhat.com](http://redhat.com)), Lukas Krejci ([lkrejci@redhat.com](mailto:lkrejci@redhat.com)) (co-mentor)

Associated JBoss community project(s): Quarkus, revapi
