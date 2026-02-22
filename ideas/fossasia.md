# FOSSASIA — Project Ideas

**Source:** https://docs.google.com/document/d/1Tz1KxYefreKzBr98C4vbCv9UwnchZoyTwO8rBrz_lmg/edit?tab=t.0#heading=h.9sjk3ie7l2o2
**Scraped:** 2026-02-22T23:28:47.543466

---

FOSSASIA GSoC 2026 Ideas List

Please submit your proposal on the GSoC website: [https://summerofcode.withgoogle.com](https://www.google.com/url?q=https://summerofcode.withgoogle.com&sa=D&source=editors&ust=1771800528786399&usg=AOvVaw1gbnNncExfJsKWQ9LTF6BY)

Ideas Overview

[1. Publication & Reproducibility Suite for Visdom 2](https://docs.google.com#h.56cwgo6yges5)

[2. PyTorch-Native Deep Integration & Auto-Logging 3](https://docs.google.com#h.2vdtm17vgtvq)

[3. Collaborative Lab Server Platform 4](https://docs.google.com#h.78ekcleaz8r3)

[4. Smart Experiment Management & Meta-Analysis 5](https://docs.google.com#h.lacahwqkcjnz)

[1. Enhance Usability of the eventyay Badge Creator 6](https://docs.google.com#h.2b1z5hajeqde)

[2. Convert eventyay-tickets VueJS implementation to Single Page application 7](https://docs.google.com#h.ff62tnufhl9m)

[3. Implement eventyay features as a plugin in eventyay-talk 8](https://docs.google.com#h.9m16whowoep4)

[5. Add New Integrations of Talks and Speakers component with eventyay Video 11](https://docs.google.com#h.kno6yscvtu64)

[6. Extend Features of the Exhibition Plugin for eventyay 13](https://docs.google.com#h.r9jfy9fdcnui)

[SUSI Interpretation Project 14](https://docs.google.com#h.392gk7jfpmv6)

[1. Enhance the feature set of the Flutter Badge Magic Application 16](https://docs.google.com#h.o7atuzk52pn4)

[2. Simplifying Bootloader Entry for LED Badge Magic Devices 17](https://docs.google.com#h.3v26mty7ule9)

[3. Enable New Hardware Features in LED Badge Magic Firmware 19](https://docs.google.com#h.wep0zvdbbb2p)

[1. Improve the Magic ePaper Badge app into a User friendly Functional App 19](https://docs.google.com#h.paukvw2oan9e)

[2. Enhance the Firmware of the Magic epaper Badge 21](https://docs.google.com#h.xve4wzikgiwx)

[1. PSLab: Extend Firmware to support standalone mode 23](https://docs.google.com#h.cuk6laohpud8)

[2. Common Unified USB/WiFi firmware 24](https://docs.google.com#h.nm4w0566v90d)

[3. Finalize and Release Desktop & Web Versions of the PSLab App 24](https://docs.google.com#h.i86wpja9wvu1)

[4. PSLab: Add VCD data export / import to the app 25](https://docs.google.com#h.a8ucfno51ed0)

[1. Extend Features of the Scrum Helper Chrome Extension 27](https://docs.google.com#h.3ip5tbre55fb)

Difficulty: Medium

Project Size: 350 hours

Required Skills: Python, React/JavaScript, LaTeX, Scientific Computing

Preferred Skills: Experience with academic research workflows, Plotly.js, Export libraries

Possilbe Mentors:[ ](https://www.google.com/url?q=https://github.com/marcoag&sa=D&source=editors&ust=1771800528791071&usg=AOvVaw1EiPKtyftoshBl2HojmTB0)[marcoag](https://www.google.com/url?q=https://github.com/marcoag&sa=D&source=editors&ust=1771800528791147&usg=AOvVaw06xxACerRgx2b_XUC9VE4U),[ ](https://www.google.com/url?q=https://github.com/norbusan&sa=D&source=editors&ust=1771800528791207&usg=AOvVaw2E8j7nXMdiJmj156WTGyUN)[norbusan](https://www.google.com/url?q=https://github.com/norbusan&sa=D&source=editors&ust=1771800528791286&usg=AOvVaw2Fb8DcnSyjgQceupb1v-mM), [mariobehling](https://www.google.com/url?q=https://github.com/mariobehling&sa=D&source=editors&ust=1771800528791414&usg=AOvVaw231V9sh7hhoPwlXl-XA9tG)

Repository: [https://github.com/fossasia/visdom](https://www.google.com/url?q=https://github.com/fossasia/visdom&sa=D&source=editors&ust=1771800528791575&usg=AOvVaw2P9VyrRy34sQ8Nob0dNLm2)

Description: Modern machine learning research relies heavily on interactive visualization tools during model training and experimentation. While Visdom is widely used for real-time monitoring and exploration, researchers must still rely on external tools and manual workflows to turn these visualizations into publication-quality figures and reproducible research artifacts.

Project Goals

This project aims to extend Visdom into a full experiment-to-publication workflow, enabling researchers to move from live training plots to paper-ready figures, reproducible experiment records, and LaTeX-ready outputs without duplicating work or losing metadata.

- Enable direct export of publication-quality figures from Visdom
- Introduce automatic experiment tracking that records configurations, metrics, and environment details required for reproducibility
- Support comparative analysis across multiple experiments, including aggregated statistics
- Provide tools to generate LaTeX-ready figures and snippets for academic papers
- Allow researchers to archive and reload experiments for long-term reference and review

Prerequisites

Required:

- Strong Python skills (comfortable with classes, async/await)
- JavaScript/React experience (Hooks, state management)
- Git proficiency
- Understanding of ML training workflows
- LaTeX experience (have written papers in LaTeX)

Preferred:

- Experience with Tornado or similar async web frameworks
- Plotly.js familiarity
- Published academic papers (understand the pain points)
- Contribution to open source projects

Getting Started Tasks

1. Set up Visdom development environment

2. Run the demo: python example/demo.py

3. Attempt to export a plot manually (identify current pain points)

4. Read Plotly export documentation

5. Complete this starter task: "Add a basic SVG export button to PlotPane.js"

Difficulty: Advanced

Project Size: 350 hours

Required Skills: Python, PyTorch, Deep Learning, Tornado

Preferred Skills: PyTorch Lightning, Hooks/Callbacks, Performance optimization

Possilbe Mentors: [marcoag](https://www.google.com/url?q=https://github.com/marcoag&sa=D&source=editors&ust=1771800528800078&usg=AOvVaw3aukjP6itRWV3VYPhCf1LH), [norbusan](https://www.google.com/url?q=https://github.com/norbusan&sa=D&source=editors&ust=1771800528800172&usg=AOvVaw12VV8aa-M98zkP6bVViInv), [mariobehling](https://www.google.com/url?q=https://github.com/mariobehling&sa=D&source=editors&ust=1771800528800243&usg=AOvVaw2sGCSi7ZH0L5cio20XrSOb)

Repository: [https://github.com/fossasia/visdom](https://www.google.com/url?q=https://github.com/fossasia/visdom&sa=D&source=editors&ust=1771800528800368&usg=AOvVaw18weEEPmzHQ3UpaJ1stDyR)

Description: Visdom is widely used for visualizing training progress, its current usage requires significant manual instrumentation. Users must explicitly log each metric, resulting in repetitive boilerplate code. For example, tracking even basic metrics such as loss and accuracy requires manual calls at every iteration:

# Current: Manual and repetitive logging for epoch in range(100): loss = train_epoch() vis.line(Y=[loss], X=[epoch], win='loss', update='append') acc = validate() vis.line(Y=[acc], X=[epoch], win='acc', update='append') # ...repeat for every metric
# Desired: Zero-config logging trainer = Trainer(model, logger=VisdomLogger(port=8097)) trainer.fit() # Automatically logs everything |

Project Goals

The goal of this project is to make Visdom the easiest visualization tool to use with PyTorch by introducing deep framework integration that minimizes or eliminates boilerplate code.

- Provide automatic detection and logging of common training metrics (e.g. loss, accuracy, learning rate)
- Integrate with PyTorch training workflows
- Reduce manual instrumentation while maintaining flexibility and transparency
- Encourage consistent and complete experiment tracking with minimal developer effort

Prerequisites

Required:

- Strong PyTorch experience (have trained models)
- Python proficiency
- Understanding of backpropagation and gradient flow
- Experience with training deep neural networks


Preferred:

- PyTorch Lightning experience
- Contribution to PyTorch ecosystem
- Understanding of training diagnostics
- Performance optimization experience


Getting Started Tasks

1. Train a simple CNN on MNIST with Visdom logging (manual)

2. Install PyTorch Lightning and understand logger interface

3. Implement a basic custom Lightning logger

4. Profile hook overhead in PyTorch

5. Complete starter task: "Add a gradient norm logger to Visdom client"

Difficulty: Advanced

Project Size: 350 hours

Required Skills: Python, React/JavaScript, LaTeX, Scientific Computing

Preferred Skills: Experience with academic research workflows, Plotly.js, Export libraries

Possilbe Mentors:[ ](https://www.google.com/url?q=https://github.com/marcoag&sa=D&source=editors&ust=1771800528815214&usg=AOvVaw3i7D5ijOvEW9Mx6ygUrC5C)[marcoag](https://www.google.com/url?q=https://github.com/marcoag&sa=D&source=editors&ust=1771800528815294&usg=AOvVaw3dXk2Ju5CT_vg6LSoPavHz),[ ](https://www.google.com/url?q=https://github.com/norbusan&sa=D&source=editors&ust=1771800528815352&usg=AOvVaw35EwPFLFmalt5R-dEbNNXf)[norbusan](https://www.google.com/url?q=https://github.com/norbusan&sa=D&source=editors&ust=1771800528815400&usg=AOvVaw1TaF__f3zzP8aiN47CXbrp), [mariobehling](https://www.google.com/url?q=https://github.com/mariobehling&sa=D&source=editors&ust=1771800528815475&usg=AOvVaw2hJTGlXPHwKix6zPuPP8ps)

Repository: [https://github.com/fossasia/visdom](https://www.google.com/url?q=https://github.com/fossasia/visdom&sa=D&source=editors&ust=1771800528815618&usg=AOvVaw2_PzHrRThKOFOEkp8DBzw1)

Description: Academic research labs often have 5–20 students sharing GPU servers to train models. Visdom is designed as a single-user tool and does not scale well to collaborative lab environments. Current limitations include:

- No user isolation or access control
- No selective sharing of experiments
- Limited collaboration features (comments, annotations)
- Difficult presentation of results in group meetings
- Poor integration with common lab workflows

Labs need a lightweight, self-hosted platform that is easy to deploy and designed specifically for academic collaboration, rather than enterprise-scale MLOps.

Project Goals

Transform Visdom into a lab-friendly collaboration platform by adding:

- User and workspace management
- Controlled experiment sharing
- Basic collaboration and presentation features

Prerequisites

Required:

- Strong Python and web development skills
- Understanding of authentication/authorization
- Database experience (SQL, ORM)
- React proficiency
- Git and Docker basics

Preferred:

- Experience with multi-user systems
- Security knowledge
- DevOps experience
- Have deployed web applications
- Used university SSO systems


Getting Started Tasks

1. Set up Visdom with existing authentication enabled

2. Deploy a simple multi-user web app with Docker

3. Implement JWT authentication in a toy project

4. Design database schema for users/workspaces

5. Complete starter task: "Add a user dropdown menu to Visdom UI"

Difficulty: Advanced

Project Size: 350 hours

Required Skills: Python, React, Authentication, Docker, Web Development

Preferred Skills: DevOps, Security, Multi-user systems, Nginx

Possilbe Mentors:[ ](https://www.google.com/url?q=https://github.com/marcoag&sa=D&source=editors&ust=1771800528823716&usg=AOvVaw2BOup479Lauxy9Pi5Q59sV)[hongquan](https://www.google.com/url?q=https://github.com/hongquan/&sa=D&source=editors&ust=1771800528823807&usg=AOvVaw3F2gP_wxP6NNJrJpICUoJ6), [mariobehling](https://www.google.com/url?q=https://github.com/mariobehling&sa=D&source=editors&ust=1771800528823881&usg=AOvVaw3T685Rgw4-GAke7osLVo85), [marcoag](https://www.google.com/url?q=https://github.com/marcoag&sa=D&source=editors&ust=1771800528823947&usg=AOvVaw1nz7smh2XnRTOtXo_0Q57B),[ ](https://www.google.com/url?q=https://github.com/norbusan&sa=D&source=editors&ust=1771800528824004&usg=AOvVaw0L9g0Ec3V3x9VOq1zcLRA8)[norbusan](https://www.google.com/url?q=https://github.com/norbusan&sa=D&source=editors&ust=1771800528824053&usg=AOvVaw3lBQUms41l6jP37BABLcCU)

Repository: [https://github.com/fossasia/visdom](https://www.google.com/url?q=https://github.com/fossasia/visdom&sa=D&source=editors&ust=1771800528824214&usg=AOvVaw0K2av1cbO8K4j7PXy5eB9H)

Description: Machine learning researchers routinely run hundreds of experiments with different hyperparameter settings. However, Visdom currently provides limited support for managing and analyzing these runs at scale. As a result, researchers face several challenges:

- No structured way to record which hyperparameters were used
- Difficulty answering simple questions such as “Which runs used learning_rate = 0.001?”
- No visualization of relationships between hyperparameters and outcomes
- Manual hyperparameter tuning that is time-consuming and inefficient
- Limited ability to identify patterns across large numbers of experiment

Project Goals

The goal of this project is to enhance Visdom with intelligent experiment management capabilities that help researchers understand, compare, and optimize large numbers of training runs.

Introduce structured metadata tracking for experiments and hyperparameters

Enable powerful search and filtering across runs

Visualize hyperparameter spaces and performance trends

Integrate with hyperparameter optimization tools to guide future experiments

Prerequisites

Required:

- Strong Python and data analysis skills
- Database experience (SQL, ORM)
- Understanding of statistics
- React proficiency
- Experience with ML training workflows

Preferred:

- Used hyperparameter optimization tools
- Data visualization experience
- Worked with large datasets
- Understanding of Bayesian optimization

Getting Started Tasks

1. Design database schema for experiment tracking 2. Implement simple query parser for key-value searches 3. Create parallel coordinates plot with Plotly.js 4. Run Optuna optimization and visualize results 5. Complete starter task: "Add experiment tagging to Visdom"

The goal of the Eventyay Open Event project is to provide an event management solution for community events. It is used by events such as the annual Wikipedia conference Wikimania and the FOSSASIA Summit. The platform offers features such as ticketing, scheduling and online events with several tracks and venues. Event managers can create invitation forms for speakers and build schedules in a drag and drop interface. The event information is stored in a database. The system provides API endpoints to fetch the data, and to modify and update it. Organizers can import and export event data in a standard compressed file format that includes the event data in JSON and binary media files like images and audio.

Project Ideas

Description: The goal of this project is to streamline the process of generating and printing badges for eventyay. Organizers often need to print badges on the spot for attendees and speakers during check-in. The project will focus on adding a user-friendly badge customization feature in the frontend, ensuring seamless badge generation in the backend, and integrating with the check-in system to allow for on-site printing. Specifically, the tasks include:

- Badge Design and Customization
- Backend API Enhancements
- Check-In App Integration for On-Site Printing
- Print Service and Configuration
- Containerization & Deployment
- Performance and Scalability
- Documentation and Testing

Repository URLs:

1. [https://github.com/fossasia/eventyay-tickets](https://www.google.com/url?q=https://github.com/fossasia/eventyay-tickets&sa=D&source=editors&ust=1771800528833405&usg=AOvVaw3JPzexfjiOHdutg1dhSOIz)

2.[https://github.com/fossasia/eventyay-tickets-exhibitors](https://www.google.com/url?q=https://github.com/fossasia/eventyay-tickets-exhibitors&sa=D&source=editors&ust=1771800528833634&usg=AOvVaw3bBJQwfA_byQARQ-cfg45U)

Expected outcome:

- Organizers can create custom badges for different user groups (speakers, attendees, volunteers, etc.).
- Attendees are able to check in quickly and receive a printed badge on the spot via the integrated check-in app.
- The system is fully documented and containerized, making it easy to set up for events of varying sizes.
- Comprehensive tests ensure reliability and maintainability of the new badge-related features.

Skills required/preferred:

- Python (Django backend)
- JavaScript (Ember.js for frontend in open-event-frontend)
- Docker & Kubernetes (containerization and deployment)
- CI/CD (to automate builds, tests, and deployments)
- Familiarity with printing workflows and/or label printing software (preferred)

Possible mentors: [hongquan](https://www.google.com/url?q=https://github.com/hongquan/&sa=D&source=editors&ust=1771800528835111&usg=AOvVaw09DwSnORNQVQHfVQpcSkEQ), [marcoag](https://www.google.com/url?q=https://github.com/marcoag&sa=D&source=editors&ust=1771800528835191&usg=AOvVaw3gKIl8FjxT5x8_lmxwmAmy), [norbusan](https://www.google.com/url?q=https://github.com/norbusan&sa=D&source=editors&ust=1771800528835261&usg=AOvVaw2Ja6tH3fhNeuieYG9Yya6W), [cweitat](https://www.google.com/url?q=https://github.com/cweitat&sa=D&source=editors&ust=1771800528835331&usg=AOvVaw32TLB2XUIK1VKeY0xFsw1n), [DonChiaQE](https://www.google.com/url?q=https://github.com/DonChiaQE&sa=D&source=editors&ust=1771800528835401&usg=AOvVaw3dy_yFaLbEdhWL_vLBv-yZ), [shaunBoahCodes](https://www.google.com/url?q=https://github.com/shaunBoahCodes&sa=D&source=editors&ust=1771800528835488&usg=AOvVaw1UN-Y70QD3Lqsj4E3PmkdV)

Project Size: 350 hours

Difficulty level: Intermediate

Description: The current eventyay-tickets system, built with VueJS, uses a traditional multi-page approach. While functional, this architecture can lead to slower page transitions, higher latency, and a less responsive user experience. The proposed project aims to refactor the existing implementation into a full Single Page Application (SPA) that leverages modern VueJS techniques for client-side routing, state management, and lazy loading.

Key components of the project include:

- Routing and Navigation

- Integrate Vue Router to handle all in-app navigation without full page reloads.
- Design a smooth and intuitive navigation experience that includes dynamic routing for ticket details, user profiles, and event overviews.

- State Management

- Utilize Vuex (or an equivalent state management solution) to manage application-wide state.
- Ensure that ticket data, user sessions, and event information are synchronized across all components.

- Performance Optimization

- Implement code splitting and lazy loading to minimize initial load times and improve overall performance.
- Optimize API interactions to efficiently fetch and update data without redundant network requests.

- UI/UX Enhancements

- Redesign critical user interfaces to align with SPA principles, offering a more fluid and interactive experience.
- Enhance error handling, loading indicators, and overall responsiveness to create a seamless experience for users on various devices.

- Progressive Enhancement and Backward Compatibility

- Ensure that the new SPA implementation gracefully degrades for users with JavaScript disabled or limited browser support.
- Provide fallbacks and clear communication for any features that depend on modern browser capabilities.

- Testing and Documentation

- Develop a suite of unit, integration, and end-to-end tests to ensure robust functionality throughout the transition.
- Update documentation to reflect the new SPA architecture and guide future contributors in maintaining the codebase.

Repository URL

Expected Outcome

At the end of the project, the eventyay-tickets system will:

- Operate as a fully functional Single Page Application, resulting in faster navigation and a more engaging user experience.
- Offer a robust and maintainable codebase with modern state management and routing practices.
- Include comprehensive testing and clear documentation to facilitate future development and onboarding of contributors.
- Seamlessly integrate with existing eventyay services while ensuring backward compatibility where needed.

Skills Required/Preferred

- JavaScript & VueJS: Deep understanding of VueJS, including Vue Router and Vuex (or similar state management libraries).
- Front-End Development: Strong grasp of modern front-end development best practices, including component-based architecture and performance optimization.
- Testing Frameworks: Experience with testing tools (e.g., Jest, Cypress) for ensuring code reliability and robustness.
- API Integration: Familiarity with RESTful APIs and efficient data handling in client-side applications.
- UI/UX Design: Ability to create intuitive and responsive interfaces, with attention to detail for user experience improvements.

Possible mentors: [hongquan](https://www.google.com/url?q=https://github.com/hongquan/&sa=D&source=editors&ust=1771800528841251&usg=AOvVaw3ulSqRWH5v3Lv-8Lk_NE4-), [marcoag](https://www.google.com/url?q=https://github.com/marcoag&sa=D&source=editors&ust=1771800528841338&usg=AOvVaw1a6W9O0QHNiPb7IDt_jd4n), [norbusan](https://www.google.com/url?q=https://github.com/norbusan&sa=D&source=editors&ust=1771800528841408&usg=AOvVaw1SFpw_i6dzyprTgdeHMrE0), [cweitat](https://www.google.com/url?q=https://github.com/cweitat&sa=D&source=editors&ust=1771800528841476&usg=AOvVaw3GUllRJ1E9SaND32bu2Sqo), [mohit](https://www.google.com/url?q=https://github.com/mohitk05&sa=D&source=editors&ust=1771800528841542&usg=AOvVaw314_fuOh6M488c7EelqtQp)

Project Size: 350 hours

Difficulty level: Advanced

Description: The goal of this project is to enhance the design and functionality of eventyay-talk and to integrate it more closely with eventyay-tickets and eventyay-video. While in the first version we already implemented some integration features, this project aims to expand on that work by decoupling the custom functionalities from the core eventyay-talk component. The approach will be to create a modular, admin-manageable plugin that provides seamless integrations without compromising upstream updates.

Objectives:

- Modular Plugin Architecture:

Develop an independent admin plugin that encapsulates all eventyay-specific integrations. This ensures that custom features remain separate from the core eventyay-talk codebase, facilitating easier updates and maintenance. - Enhanced Integration with eventyay-tickets and eventyay-video:

- Integrate ticketing data to display attendee information, session details, and speaker profiles within the discussion threads of eventyay-talk.
- Integrate video content so that related event sessions or live streams are readily accessible from within the talk platform.
- Synchronize user profiles and session metadata across these services for a consistent experience.

- Improved Design and Usability:

- Enhance the overall UI/UX of eventyay-talk to match the branding and design language of the eventyay ecosystem.
- Provide a centralized admin interface where event organizers can configure and control integrations, toggle features, and manage settings without modifying core code.

- Future-Proof and Maintainable Code:

- Keep the integration functionality in-line with upstream eventyay-talk releases, ensuring compatibility and ease of updates.
- Write comprehensive documentation and tests to support long-term maintenance and community contributions.

Repositories:

Expected Outcome:

At the end of the project, the eventyay-talk platform will have a standalone, well-documented plugin that:

- Integrates ticketing and video functionalities directly within the environment.
- Offers a seamless and consistent user experience across eventyay components.
- Is easily configurable through an admin interface, reducing the need to modify core eventyay-talk code.
- Maintains alignment with upstream changes, ensuring long-term compatibility and simplified maintenance.
- Includes robust testing and clear documentation to facilitate future enhancements and community contributions.

Skills Required/Preferred:

- JavaScript & Frameworks: Strong knowledge of JavaScript and experience with the framework used in eventyay-talk using Vue.js).
- Plugin Architecture: Familiarity with creating modular plugins and extension points in a larger application ecosystem.
- API Integration: Experience with RESTful APIs and backend integrations.
- UI/UX Design: Ability to enhance user interfaces for better usability and consistency across platforms.
- DevOps: Familiarity with Docker, CI/CD, and automated testing to ensure reliable deployment and maintenance.

Possible mentors: [hongquan](https://www.google.com/url?q=https://github.com/hongquan/&sa=D&source=editors&ust=1771800528846944&usg=AOvVaw1mBZTXdeXk1U9PCV595xXY), [marcoag](https://www.google.com/url?q=https://github.com/marcoag&sa=D&source=editors&ust=1771800528847021&usg=AOvVaw2vPgUuwa3wTsq4zcxPNe4y), [norbusan](https://www.google.com/url?q=https://github.com/norbusan&sa=D&source=editors&ust=1771800528847089&usg=AOvVaw3eCOyeR9HK_Ji3W4y_wfgy), [cweitat](https://www.google.com/url?q=https://github.com/cweitat&sa=D&source=editors&ust=1771800528847157&usg=AOvVaw1NB3985SnDXVJddl7Iswvw), [mohit](https://www.google.com/url?q=https://github.com/mohitk05&sa=D&source=editors&ust=1771800528847215&usg=AOvVaw1VqCZpElxI1b_4eQwCf1es)

Project Size: 175 hours

Difficulty level: Intermediate

Description: The current eventyay-video implementation provides basic video functionalities for event streaming and management. However, it lacks an integrated, user-friendly dashboard and administrative interface. This project aims to transform eventyay-video into a modern Single Page Application (SPA) that offers comprehensive dashboards and configuration options for organisers and admins. By upgrading the UI/UX and incorporating advanced settings, the platform will allow seamless management of video content and live sessions, as well as integration with the broader eventyay ecosystem.

Objectives:

- SPA Conversion and Modernization:

- Refactor the existing eventyay-video codebase to a Single Page VueJS Application.
- Implement client-side routing, lazy loading, and state management to ensure fast, smooth interactions and a responsive user experience.

- Dashboard and Administrative Interface:

- Develop intuitive and fully functional dashboards for organisers and admins to manage video sessions, live streams, and related content.
- Create comprehensive settings and configuration panels that allow users to customize video parameters, manage integrations, and monitor streaming analytics.
- Ensure that the dashboards are secure, scalable, and aligned with eventyay’s overall design language.

- Integration with eventyay Ecosystem:

- Seamlessly integrate with eventyay-tickets and other eventyay modules to synchronize data (e.g., event schedules, session details, user profiles).
- Enable automated configuration and updates from central eventyay administration systems, reducing manual maintenance.

- Enhanced UI/UX and Performance Optimization:

- Redesign the video interface to be more interactive and user-friendly, with emphasis on accessibility and responsiveness across devices.
- Optimize performance using code splitting, efficient API calls, and caching strategies to support large-scale live events and high traffic.

- Testing, Documentation, and Deployment:

- Write comprehensive unit, integration, and end-to-end tests to ensure reliability and performance.
- Document the new features, installation procedures, and administration guides to support future development and community onboarding.
- Leverage Docker and CI/CD pipelines to automate the build, testing, and deployment process, ensuring a robust development workflow.

Repositories:

Expected Outcome:

By the end of the project, eventyay-video will:

- Be transformed into a Single Page Application.
- Offer fully functional dashboards for organisers and admins, including robust settings and configuration options.
- Seamlessly integrate with the broader eventyay ecosystem to synchronize event data and manage video content efficiently.
- Include comprehensive testing and documentation, ensuring ease of maintenance and further development.

Skills Required/Preferred:

- JavaScript & SPA Frameworks: Expertise in VueJS for SPA development, including client-side routing and state management.
- Front-End Development: Strong experience with modern UI/UX design principles and performance optimization.
- Backend Integration: Familiarity with RESTful APIs and integrating front-end applications with backend services.
- DevOps & CI/CD: Knowledge of Docker, Kubernetes, and continuous integration/deployment pipelines.
- Testing & Documentation: Experience writing comprehensive tests (unit, integration, e2e) and maintaining technical documentation.

Possible mentors: [hongquan](https://www.google.com/url?q=https://github.com/hongquan/&sa=D&source=editors&ust=1771800528852856&usg=AOvVaw0XSLhTdfbz_PQ8kCCfOh_j), [marcoag](https://www.google.com/url?q=https://github.com/marcoag&sa=D&source=editors&ust=1771800528852930&usg=AOvVaw0yA6zAnjC26myjKB4WJR60), [norbusan](https://www.google.com/url?q=https://github.com/norbusan&sa=D&source=editors&ust=1771800528853001&usg=AOvVaw2XeNz0uZf5xxI0TsD0KeAr), [cweitat](https://www.google.com/url?q=https://github.com/cweitat&sa=D&source=editors&ust=1771800528853060&usg=AOvVaw0bTaxuvPGTslwEtykxgyOZ), [mohit](https://www.google.com/url?q=https://github.com/mohitk05&sa=D&source=editors&ust=1771800528853119&usg=AOvVaw0G6GDp8I4RH4H7p64OpKSK)

Project Size: 350 hours

Difficulty level: Intermediate

Description: The goal of this project is to seamlessly integrate eventyay-talk with the eventyay-video component, ensuring a unified experience for event organisers and attendees. The project focuses on automating the synchronization between talks and video rooms, as well as enhancing speaker integration. For instance, when rooms are created in eventyay-talk, they should automatically appear in eventyay-video. Additionally, event organisers will have the ability to assign team members as MCs (Masters of Ceremonies) for different rooms, streamlining room management and improving live event coordination. This integration will reduce manual work, ensure data consistency, and provide a coherent user experience across eventyay components.

Objectives:

- Automatic Room Synchronization:

- Develop functionality to automatically sync room creation and updates from eventyay-talk to eventyay-video.
- Ensure that any changes in the talk component (e.g., room details, schedule updates) reflect in real time on the video side.

- Speaker and Talk Data Integration:

- Integrate detailed talk and speaker information within the eventyay-video interface.
- Display session titles, descriptions, and speaker profiles alongside corresponding video rooms, providing context for viewers.

- MC Assignment Feature:

- Create an admin dashboard interface that enables organisers to assign team members as MCs for various video rooms.
- Implement notifications and role-based permissions to ensure that MCs have the tools and access needed to manage live sessions effectively.

- Unified User Experience:

- Design a consistent and intuitive UI/UX that bridges the gap between eventyay-talk and eventyay-video.
- Include visual cues and real-time status updates to help users navigate between talk sessions and their video counterparts.

- Backend Synchronization & API Enhancements:

- Enhance existing APIs or develop new endpoints to facilitate seamless data exchange between eventyay-talk and eventyay-video.
- Ensure robust error handling and data validation to maintain system reliability.

- Testing, Documentation, and Maintenance:

- Develop comprehensive unit, integration, and end-to-end tests covering all new integration functionalities.
- Provide clear documentation for developers and administrators to ensure ease of future maintenance and onboarding.

Repositories:

Expected Outcome:

At the end of the project, the eventyay ecosystem will benefit from:

- Automatic synchronization of rooms between eventyay-talk and eventyay-video, reducing manual intervention.
- Enhanced display of talk and speaker information in the video component.
- A dedicated admin interface for assigning MCs to rooms, ensuring better event management.
- A unified and consistent experience across the eventyay platforms, bolstered by robust API integrations, thorough testing, and clear documentation.

Skills Required/Preferred:

- JavaScript & Front-End Frameworks: Experience with modern JavaScript frameworks (e.g., Vue.js) used in eventyay components.
- Backend Development: Experience in RESTful API design and integration.
- Integration Development: Experience in connecting disparate systems and ensuring smooth data synchronization.
- UI/UX Design: Strong skills in creating intuitive, responsive, and consistent user interfaces.
- Testing & Documentation: Ability to write comprehensive tests (unit, integration, and end-to-end) and maintain clear technical documentation.

Possible mentors: [hongquan](https://www.google.com/url?q=https://github.com/hongquan/&sa=D&source=editors&ust=1771800528858716&usg=AOvVaw1S2wBGZAt8I3I02yvKOp_2), [marcoag](https://www.google.com/url?q=https://github.com/marcoag&sa=D&source=editors&ust=1771800528858791&usg=AOvVaw3F15KZ6i6obnPY57dxEADw), [norbusan](https://www.google.com/url?q=https://github.com/norbusan&sa=D&source=editors&ust=1771800528858864&usg=AOvVaw3AMy5mv6EqiwOpQnRsiDDs), [cweitat](https://www.google.com/url?q=https://github.com/cweitat&sa=D&source=editors&ust=1771800528858931&usg=AOvVaw0B6G_NEQaCrzPwJ5BgPVN5), [mohit](https://www.google.com/url?q=https://github.com/mohitk05&sa=D&source=editors&ust=1771800528859004&usg=AOvVaw27ItZytRFOhutohhVIS5vY)

Project Size: 175 hours (medium project)

Difficulty level: Intermediate

Description: eventyay currently includes an exhibition system designed to showcase exhibitors during events. This project aims to significantly enhance the existing exhibition plugin by expanding its feature set and improving its usability for both exhibitors and organizers. The new features will empower exhibitors to register and manage their own profiles, add detailed content, embed video links, and link to their social media channels. At the same time, event organizers will gain better control over exhibitor signups, payments, and the publication process. Additionally, the plugin will support integration with event sessions, allowing related sessions to be showcased on the exhibitor’s page, along with the ability to feature an exhibitor video directly on their profile.

Objectives:

- Enhance the Exhibitor Registration & Profile Management:

- Develop a user-friendly registration process for exhibitors, allowing them to submit detailed profiles, including company information, content, and social media links.
- Allow exhibitors to edit and update their profiles through a dedicated dashboard.

- Integration of Multimedia Content:

- Enable exhibitors to embed video links (e.g., from YouTube or Vimeo) directly on their public exhibitor page.
- Support the addition of rich content (images, descriptions, documents) to provide a comprehensive overview of each exhibitor.

- Organizers’ Administrative Tools:

- Create an admin interface that enables organizers to review, approve, and manage exhibitor signups.
- Integrate payment processing options to manage exhibitor fees, if applicable, ensuring a secure and streamlined financial workflow.
- Provide tools for organizers to publish approved exhibitor profiles to the public website.

- Integration with Event Sessions:

- Implement a feature to associate related event sessions with exhibitor profiles. This will allow attendees to see relevant sessions alongside exhibitor details, fostering deeper engagement.
- Design intuitive navigation between exhibitor pages and session details.

- Responsive & Modern UI/UX:

- Redesign the exhibitor plugin interface to align with eventyay’s overall design language, ensuring a modern, accessible, and responsive user experience across all devices.
- Focus on usability for both exhibitors and event organizers through clear workflows and consistent design elements.

- Robust Testing & Documentation:

- Develop comprehensive unit, integration, and end-to-end tests to ensure reliability of all new features.
- Write detailed documentation for both developers and end-users to support future maintenance and community contributions.

Repository:

Expected Outcome:

Upon completion of the project, the extended exhibition plugin will provide:

- A complete exhibitor registration system with rich profile management capabilities.
- An administrative interface for organizers to manage exhibitor applications, process payments, and publish profiles.
- Enhanced exhibitor pages that integrate multimedia content, social media links, and related event sessions.
- A modern, responsive UI that offers a seamless experience for both exhibitors and event attendees.
- Comprehensive testing and documentation that ensure maintainability and facilitate future enhancements.

Skills Required/Preferred:

- Web Development: Strong experience with front-end technologies (JavaScript frameworks, HTML, CSS) and back-end development.
- Frameworks & Libraries: Familiarity with frameworks used in eventyay (e.g., Ember.js, Vue.js, or similar) and RESTful API integration.
- Payment Integration: Knowledge of integrating payment systems (e.g., Stripe, PayPal) for secure transaction processing.
- UI/UX Design: Ability to create intuitive and responsive interfaces.
- Testing & Documentation: Experience with writing unit, integration, and end-to-end tests as well as technical documentation.

Possible mentors: [hongquan](https://www.google.com/url?q=https://github.com/hongquan/&sa=D&source=editors&ust=1771800528865292&usg=AOvVaw2ynUd1bErgYBhvcqH_CwHx), [marcoag](https://www.google.com/url?q=https://github.com/marcoag&sa=D&source=editors&ust=1771800528865370&usg=AOvVaw3VIGOf8nayuJMjO9l028ZQ), [norbusan](https://www.google.com/url?q=https://github.com/norbusan&sa=D&source=editors&ust=1771800528865433&usg=AOvVaw0biDxxLigEOxemcMJrtYnN), [cweitat](https://www.google.com/url?q=https://github.com/cweitat&sa=D&source=editors&ust=1771800528865502&usg=AOvVaw0Xgm_lP-EMy_rO7MzGfPb1), [mohit](https://www.google.com/url?q=https://github.com/mohitk05&sa=D&source=editors&ust=1771800528865569&usg=AOvVaw0YIamW0Aq697xl4JEBsr2w)

Project Size: 175 hours (medium size)

Difficulty: Advanced

Project Size: 350 hours

Required Skills: Python, JavaScript, APIs, AI/LLM

Preferred Skills: WebRTC, SRT

Possilbe Mentors:[ ](https://www.google.com/url?q=https://github.com/marcoag&sa=D&source=editors&ust=1771800528866926&usg=AOvVaw0PUGh7WvcPFr-AmT1Oe2tk)[Orbiter](https://www.google.com/url?q=https://github.com/Orbiter&sa=D&source=editors&ust=1771800528867017&usg=AOvVaw0LuXL5B8sG8cmd5mdVEBHQ)

Repository: [SUSI Translator Repository](https://www.google.com/url?q=https://github.com/susiai/susi_translator&sa=D&source=editors&ust=1771800528867141&usg=AOvVaw2iBh1LOQm9pbpMavkIdASX)

Description: The SUSI AI Translator project aims to build an interpretation assistant that leverages large language models (LLMs) to enable automated, real-time live interpretation on top of the eventyay video component. The system integrates advanced speech-to-text technology with AI-powered language translation, allowing for the seamless display of interpreted text (e.g., translated subtitles) during live event video sessions. By bridging the gap between live audio streams and real-time translation, this project will significantly enhance accessibility and engagement for multilingual audiences at events.

Scope:

The scope of your specific work on this project should be discussed with your mentor.

Objectives:

- Real-Time Speech Recognition:

- Integration: Evaluate and integrate state-of-the-art speech-to-text engines (such as OpenAI’s Whisper or other open-source alternatives) to capture live audio streams from event videos with minimal latency.
- Optimization: Optimize for high accuracy and performance under varying noise and speech conditions.

- AI-Powered Translation & Interpretation:

- LLM Integration: Leverage large language models or dedicated translation APIs to interpret and translate the transcribed text in near real-time.
- Context Preservation: Ensure that the translation maintains context and clarity, offering accurate subtitles that enhance audience understanding.

- Subtitle Overlay & UI Integration:

- Eventyay Video Integration: Develop a module that overlays interpreted subtitles onto the live video stream from the eventyay video platform.
- Customization: Provide configurable options (e.g., font size, color, position, language selection, and toggle controls) to optimize subtitle display for diverse event settings.

- System Optimization and Latency Reduction:

- Pipeline Efficiency: Optimize data pipelines and processing workflows to minimize end-to-end latency, ensuring a smooth live interpretation experience.
- Caching & Asynchronous Processing: Implement techniques to handle network delays and processing loads effectively.

- Testing, Documentation, and Community Engagement:

- Comprehensive Testing: Develop unit, integration, and end-to-end tests to ensure system reliability and performance across various scenarios.
- Documentation: Create detailed guides on system setup, configuration, troubleshooting, and customization.
- Tutorials & Demos: Produce step-by-step tutorials and demo videos showcasing how to deploy and use the live interpretation feature.

- Additional Features (Exploratory):

- Admin Controls: Design an admin panel for event organizers to manage language pairs, thresholds, and real-time translation settings.
- Multi-Language Support: Expand the system to support multiple target languages and easy language switching during live events.

Repositories:

[SUSI Translator Repository](https://www.google.com/url?q=https://github.com/susiai/susi_translator&sa=D&source=editors&ust=1771800528871244&usg=AOvVaw0uuioXnYgPrXgt7VREh-Qt)[eventyay-video Repository](https://www.google.com/url?q=https://github.com/fossasia/eventyay-video&sa=D&source=editors&ust=1771800528871384&usg=AOvVaw2_XAHXF7cDJJpfk7EqthmY)- (Additional modules or repositories may be created as the project evolves.)

Expected Outcome:

- An improved prototype fully integrated, real-time AI live interpretation system that displays translated subtitles on the eventyay video platform.
- Enhanced accessibility and engagement for multilingual audiences through automated, low-latency speech recognition and translation.
- A robust, well-documented codebase accompanied by comprehensive tests and tutorials, fostering further community contributions and improvements.

Skills Required/Preferred:

- Speech Recognition & Audio Processing: Familiarity with integrating and optimizing speech-to-text systems.
- AI & Machine Learning: Experience working with large language models, translation APIs, or similar AI-driven solutions.
- Programming & API Integration: Proficiency in Python and/or other relevant languages for backend processing and API development.
- Front-End Development: Skills in integrating real-time UI overlays within video platforms.
- DevOps & Testing: Experience with CI/CD pipelines and automated testing frameworks.
- Open Source Collaboration: Prior experience contributing to or managing open-source projects.

The Badge Magic Android app lets you create moving text and draw clipart for LED name badges. The app provides options to portray names, cliparts, and simple animations on the badges. For the data transfer from the smartphone to the LED badge it uses Bluetooth.

Project Ideas

Difficulty: Medium

Project Size: 175 hours

Required Skills: Flutter/Dart, CI/CD

Preferred Skills: UI/UX Design, Bluetooth Communication

Possilbe Mentors: [Jhalakupadhyay](https://www.google.com/url?q=https://github.com/Jhalakupadhyay&sa=D&source=editors&ust=1771800528874595&usg=AOvVaw07RJWyn6_KO7MoyKrgW19E), [cweitat](https://www.google.com/url?q=https://github.com/cweitat&sa=D&source=editors&ust=1771800528874681&usg=AOvVaw3soc-fDfVT4Rp0q5EU2NKM)

Repository: [https://github.com/fossasia/badgemagic-app](https://www.google.com/url?q=https://github.com/fossasia/badgemagic-app&sa=D&source=editors&ust=1771800528874949&usg=AOvVaw1NHRLOxf66rk2ndUEGmHk-)

Badge Magic is a Flutter based application that controls LED name badges via Bluetooth, allowing users to upload text, graphics, and animations. Users report reliability issues (transfer errors), inconsistent or non-functional animations, and gaps in the overall viewing and editing experience.

Project Goals

The goal of this project is to make the app significantly more robust and user-friendly by systematically testing all core functions, fixing transfer and animation-related bugs, improving the animation preview and user workflow, and enabling users to load, share, and manage multiple animation designs more easily. In addition, the project will establish a repeatable release process to push development updates reliably to app stores, and introduce useful testing, logging, and error tracking so bugs can be diagnosed and resolved faster.

Objectives

Reliability and Bug Fixes

- Investigate and fix Bluetooth transfer errors (e.g., partial uploads, corrupted frames, timeouts, reconnect issues).
- Run a structured test pass across all major features (connect, write text, upload animation, save slots, preview, delete/overwrite, etc.) and fix regressions.
- Improve robustness for different badge models and phone OS versions where applicable.

Animation Functionality and User Viewing Experience

- Fix broken or inconsistent animation behaviors and ensure animations render as intended on the badge.
- Improve animation preview and playback controls in the app (e.g., frame timing, looping, zoom, navigation).
- Streamline the workflow for creating, selecting, and deploying animations to the badge

Sharing and Loading Animation Designs

- Enable exporting and importing animation designs (e.g., shareable files or links).
- Support organizing multiple animation presets and loading them onto the badge reliably.
- Add clear UI for managing designs (rename, duplicate, version, delete, reorder).

Release Process and Quality Infrastructure

- Improve CI/CD workflows for building and publishing releases (test → build → signed artifacts → store submission).
- Add automated tests (unit + integration where feasible) and define basic release checks.
- Add structured logging and error reporting to track transfer failures and app-side crashes, with actionable diagnostics for maintainers.

Documentation

- Update user documentation for animation workflows and troubleshooting.
- Update contributor documentation for testing, debugging, and releasing to app stores.

Skills Required/Preferred:

- Flutter/Dart: Advanced knowledge in Flutter development and Dart programming.
- Bluetooth Communication: Experience with Bluetooth integration in mobile applications.
- UI/UX Design: Strong design skills for building intuitive and responsive mobile interfaces.
- Mobile and Multi-Platform App Development: Proven experience in Android, iOS, and cross-platform development (Windows, Linux, MacOS, and Web).
- CI/CD & Deployment: Familiarity with automated deployment pipelines and multi-app store submissions.
- Testing & Documentation: Experience in writing unit, integration, and end-to-end tests, as well as maintaining detailed project documentation.

Difficulty: Easy-Medium

Project Size: 90 hours

Required Skills: Embedded C / C++

Preferred Skills: Basic electronics and PCB design

Possilbe Mentors: [weberval](https://www.google.com/url?q=https://github.com/weberval&sa=D&source=editors&ust=1771800528880421&usg=AOvVaw1ub27uR7uhh-vdPiw7NO9M), [padmal](https://www.google.com/url?q=https://github.com/CloudyPadmal&sa=D&source=editors&ust=1771800528880504&usg=AOvVaw0VhylynZaQRj49isvILek4)

Repository: [https://github.com/fossasia/badgemagic-firmware](https://www.google.com/url?q=https://github.com/fossasia/badgemagic-firmware&sa=D&source=editors&ust=1771800528880645&usg=AOvVaw3u_plNJiWLdOcxhvAvAfDX)

Description: Entering bootloader (ISP) mode on LED Badge Magic devices is quite complex and error-prone, especially for beginners and workshop participants. There are currently two ways to do this:

- Disconnect the battery, press and hold KEY2 while plugging in USB
- Connect USB, press and hold KEY2, then briefly short and release the C3 capacitor

Disconnecting the battery is inconvenient and risky during frequent firmware updates. The press-and-hold timing required is difficult to perform consistently. Shorting a capacitor is unsafe and unintuitive, making it especially unsuitable for workshops and classroom settings. Overall, the process is hard to explain, easy to get wrong, and often results in failed bootloader entry.

Project Goals

The goal of this project is to redesign the bootloader entry mechanism so that users can reliably enter firmware flashing mode without battery removal, precise timing, or unsafe actions. The project will introduce a clear, hardware-assisted method to enter bootloader mode, supported by firmware changes and documentation.

Expected Outcomes

1. Design a new mechanism to enter bootloader mode that:

- Does not require disconnecting the battery
- Does not require precise button timing
- Avoids unsafe actions (e.g. shorting components)

2. Firmware & Bootloader Support

- Modify firmware and/or bootloader logic to:

- Reliably detect the new bootloader entry mechanism
- Enter ISP mode deterministically

- Maintain compatibility with existing flashing tools

3. Usability Validation

- Test the new process with first-time users
- Ensure bootloader entry is fast, repeatable and easy to explain

4. Documentation & Guidance

- Update documentation with: Clear diagrams, step-by-step instructions and troubleshooting notes

Prerequisites

Required:

- Embedded C / C++
- Microcontroller bootloader concepts
- Reading schematics and hardware datasheets
- Hardware–firmware interaction
- Debugging firmware flashing workflows

Preferred:

- Basic electronics and PCB design
- Experience with USB flashing tools
- Experience designing beginner-friendly hardware workflows

Difficulty: Medium

Project Size: 175 hours

Required Skills: Embedded C / C++

Preferred Skills: Basic electronics and PCB design

Possilbe Mentors: [padmal](https://www.google.com/url?q=https://github.com/CloudyPadmal&sa=D&source=editors&ust=1771800528886328&usg=AOvVaw1jNtR0l6wByZk_Z_-gWzXn), [weberval](https://www.google.com/url?q=https://github.com/weberval&sa=D&source=editors&ust=1771800528886408&usg=AOvVaw1WcXRNwf4ufDEhrXDTtgtw)


Repository:


Desecription: Recent revisions of the LED Badge Magic hardware introduce several new components, but the firmware does not yet support them e.g. onboard microphone, external storage, two additional buttons. The goal of this project is to extend the LED Badge Magic firmware to support newly added hardware components, making them usable, documented, and accessible to users

Prerequisites

Required:

- Embedded C / C++
- Microcontroller firmware development
- Peripheral drivers (GPIO, ADC, storage interfaces)
- Reading hardware schematics and datasheets


Preferred:

- Experience with audio input or signal processing
- Filesystems or external storage devices
- Experience designing APIs for embedded systems

Description: The Magic ePaper Badge is a unique hardware platform featuring a tri-color ePaper display, NFC capabilities, and battery-free operation. The goal of this project is to build an open source Flutter application that allows users to interact with and control the badge with rich, customizable content. The app will enable users to create and edit content through drawing tools, text inputs, emojis, and image import functionalities—with various effects (none, semi-transparent, block, portrait). Additional features include adjusting contrast, colors, image rotation, and text customization (font and size). Finally, the app will support transferring the composed content to the badge via NFC. This project is especially suited for contributors with an electronics background who are also interested in modern mobile app development using Flutter.

Objectives:

- User Interface & Drawing Tools:

- Develop an intuitive Flutter UI for creating badge content.
- Implement drawing functionalities, text input, and emoji insertion.
- Integrate a color picker to easily change colors by tapping on a color button.

- Image Import and Editing:

- Enable users to import images from their devices.
- Support multiple image display effects: none, semi-transparent, block, and portrait.
- Provide features for rotating images and adjusting brightness, contrast, and overall color balance.

- Text Customization:

- Allow users to change fonts and text sizes to match their design needs.
- Ensure text overlays are compatible with the tri-color ePaper display.

- NFC-Based Content Transfer:

- Integrate NFC functionalities to enable the transfer of created content from an NFC-enabled phone directly to the Magic ePaper Badge.
- Ensure a smooth, secure, and reliable connection between the mobile device and the badge hardware.

- Support for Tri-Color ePaper Displays:

- Ensure that all drawing, text, image, and animation functionalities are fully optimized for the unique constraints of tri-color ePaper displays.

- Testing, Bug Fixes & Feature Enhancements:

- Identify and resolve existing bugs, particularly issues around storing and editing animations.
- Continuously refine and enhance features based on user feedback and testing results.

- Multi-Platform Deployment & Automation:

- Adapt the app to run on all platforms supported by Flutter (Android, iOS, Windows, Linux, MacOS, and Web).
- Set up an automated deployment pipeline to generate installation files in the app branch for all target platforms.
- Ensure that the deployment process is smooth and maintainable for future updates.

- Documentation & Community Engagement:

- Produce comprehensive documentation covering installation, usage, and NFC transfer processes.
- Provide guidelines for future contributions and ensure robust testing strategies are in place.

Repository:

Resources:

Expected Outcome:

By the end of the project, the Magic ePaper Badge Flutter App will:

- Offer a complete suite of content creation tools (drawing, text, emoji, image editing) tailored for the tri-color ePaper display.
- Provide robust customization options including color adjustments, image effects, and text formatting.
- Seamlessly transfer content to the badge via NFC.
- Run across all major platforms supported by Flutter, with autogenerated installation files maintained in the app branch.
- Include comprehensive documentation, a solid testing framework, and a refined UI/UX for an engaging user experience.

Skills Required/Preferred:

- Flutter & Dart Development: Knowledge in building cross-platform apps with Flutter.
- Mobile & Multi-Platform App Development: Experience in deploying applications on Android, iOS, Windows, Linux, MacOS, and Web.
- NFC Integration: Understanding of NFC communication and its implementation on mobile devices.
- UI/UX Design: Skills in creating intuitive and responsive user interfaces.
- Image Processing & Drawing: Experience with image editing, drawing functionalities, and handling various display effects.
- Electronics & ePaper Displays: Basic knowledge of ePaper technology and hardware integration is a plus.
- Testing & Documentation: Proven ability to write comprehensive tests and maintain clear, detailed documentation.

Possible mentors: Aditya, MarioB, [cweitat](https://www.google.com/url?q=https://github.com/cweitat&sa=D&source=editors&ust=1771800528896163&usg=AOvVaw2IuN-K_w-ofig-Fa9hJPbA)

Project Size: 350 hours (large project)

Difficulty level: Intermediate

Description: The Magic Epaper Firmware is a fully customizable and efficient firmware designed to control FOSSASIA's ePaper displays. It serves as the backbone for smart signage, dashboards, IoT devices, and various applications that require low-power, high-performance e-ink display control. The firmware is optimized for FOSSASIA ePaper displays, ensuring smooth rendering while consuming minimal power, and features a modular codebase that allows easy adaptation to different e-paper sizes and types. With flexible connectivity options supporting SPI, I2C, or UART interfaces, and compatibility with various microcontrollers, the firmware is capable of rich content rendering including text, images, and custom graphics—with support for grayscale and partial refresh (depending on display capabilities). Fully open-source under the Apache2 license, the firmware invites contributors to extend its capabilities and enhance its reliability.

Objectives:

- Reliability and Stability Enhancements:

- Audit the current firmware codebase to identify and resolve bugs affecting rendering, connectivity, and power consumption.
- Optimize the code for smoother rendering and enhanced stability across various hardware configurations.

- Modular Codebase Improvements:

- Refactor and document the modular components to simplify customization for different e-paper display sizes and types.
- Enhance configurability to allow easier integration with new microcontrollers and communication protocols (SPI, I2C, UART).

- Low-Power Optimization:

- Fine-tune power management routines to further reduce energy consumption, making the firmware even more suitable for battery-powered devices.
- Implement advanced sleep and wake-up cycles tailored for e-ink display operations.

- Advanced Content Rendering:

- Improve support for rich content rendering including text, images, and custom graphics.
- Enhance grayscale rendering capabilities and optimize partial refresh functionality to reduce ghosting and improve update speed.

- Connectivity and Integration Enhancements:

- Ensure robust communication over SPI, I2C, or UART, adding diagnostics or fallback mechanisms to handle connection interruptions.
- Develop test cases and debugging tools to facilitate easier firmware integration with different hardware setups.

- Documentation and Community Support:

- Update and expand technical documentation, providing detailed guides on customizing and extending the firmware.
- Create a set of example projects and usage scenarios for smart signage, dashboards, and IoT devices to encourage community contributions.

Repository:

Expected Outcome:

By the end of the project, the enhanced Magic Epaper Firmware will:

- Deliver a more stable and reliable performance with optimized rendering and low-power operation.
- Feature a thoroughly documented and modular codebase that simplifies customization for various e-paper displays and microcontrollers.
- Offer improved content rendering capabilities, including refined support for grayscale and partial refresh.
- Provide robust connectivity with diagnostics and enhanced support for SPI, I2C, and UART interfaces.
- Include comprehensive documentation and example projects, fostering further development and community engagement.

Skills Required/Preferred:

- Embedded Systems & Firmware Development: C/C++ or similar languages used in microcontroller programming.
- Electronics & Hardware Integration: Experience with ePaper displays, low-power device design, and understanding of communication protocols (SPI, I2C, UART).
- Optimization & Debugging: Skills in debugging firmware and optimizing performance for resource-constrained devices.
- Documentation & Open-Source Collaboration: Ability to write clear technical documentation and collaborate with a global open-source community.

Possible mentors: [fcartegnie](https://www.google.com/url?q=https://github.com/fcartegnie&sa=D&source=editors&ust=1771800528901781&usg=AOvVaw2KV5kFZdS0Kb2M6tr7RJ0D), [Benjamin Henrion](https://www.google.com/url?q=https://github.com/zoobab&sa=D&source=editors&ust=1771800528901858&usg=AOvVaw2e5VETAbiyQxKnzDN-GZq8), [Simon Budig](https://www.google.com/url?q=https://github.com/simon-budig&sa=D&source=editors&ust=1771800528901926&usg=AOvVaw2T8fjeAFYcaHMwMS1Fy9rY), [danielm](https://www.google.com/url?q=https://github.com/orangecms&sa=D&source=editors&ust=1771800528901994&usg=AOvVaw0fQ4y1LJcm0mHMx3utcVkZ)

Project Size: 350 hours

Difficulty level: Difficult

In the Pocket Science Lab Project we create phone and desktop applications to collect measurements and data to solve global problems with science and build a sustainable world. With the PSLab mobile and desktop apps it is possible to use sensors of a phone or desktop PC to collect measurements and data. The app comes with a built-in Oscilloscope, Multimeter, Wave Generator, Logic Analyzer, Power Source, and we are constantly adding more digital instruments or even robotic controls. With PSLab applications your phone or PC becomes like many devices in one.

Project Ideas

Difficulty: Advance

Project Size: 350 hours

Required Skills: Embedded C / C++

Preferred Skills: Hardware & IoT Integration

Possilbe Mentors: [marcnause](https://www.google.com/url?q=https://github.com/marcnause&sa=D&source=editors&ust=1771800528903921&usg=AOvVaw0DHg_jTMcYkOdX6KuDXBA5), [padmal](https://www.google.com/url?q=https://github.com/CloudyPadmal&sa=D&source=editors&ust=1771800528903997&usg=AOvVaw00aexda90Hsq7s4jA8zh9c), [bessman](https://www.google.com/url?q=https://github.com/bessman&sa=D&source=editors&ust=1771800528904060&usg=AOvVaw3JoyvjSwN7A6S8zsS-wCqZ)

Repository: [https://github.com/fossasia/pslab-firmware](https://www.google.com/url?q=https://github.com/fossasia/pslab-firmware&sa=D&source=editors&ust=1771800528904191&usg=AOvVaw1cMQtgZwLawxvchIPC3G4Z)

Description: The PSLab v6 hardware includes an onboard SD card slot that enables local data storage, but the current firmware does not yet support SD card access. This project aims to extend the PSLab firmware to support SD card based data logging and enable a true standalone operating mode, where the device can continue collecting and publishing data even when disconnected from a host computer.

In addition, the project will integrate optional IoT connectivity by publishing collected sensor data to Home Assistant via MQTT, using an external ESP-01 Wi-Fi module. This will allow PSLab to be used in long-running experiments, environmental monitoring, and home automation scenarios without requiring a permanent USB connection. The project involves:

- write and read SD card
- allow external applications (python-lib, app) to start logging to SD card after external device is detached
- on power on search and read configuration file from SD card which contains information about what data shall be logged to SD card
- send data to Home Assistant via MQTT (requires ESP01 which connects to home Wifi)

Skills Required/Preferred:

- Embedded C / C++
- Microcontroller firmware development
- Filesystems (FAT) and SD card interfaces
- Basic networking concepts (MQTT, Wi-Fi modules)
- Python for integration with existing PSLab tools
- Open Source Collaboration: Familiarity with contributing to and managing open source projects.

Difficulty: Advance

Project Size: 175 hours

Required Skills: Embedded C / C++

Preferred Skills: Hardware & IoT Integration

Possilbe Mentors: [padmal](https://www.google.com/url?q=https://github.com/CloudyPadmal&sa=D&source=editors&ust=1771800528907484&usg=AOvVaw3i6nLXpxyzMCpB36G_zdvU), [bessman](https://www.google.com/url?q=https://github.com/bessman&sa=D&source=editors&ust=1771800528907555&usg=AOvVaw0f3EPc7AiyLvG-O7VPzC1o), [marcnause](https://www.google.com/url?q=https://github.com/marcnause&sa=D&source=editors&ust=1771800528907624&usg=AOvVaw2E3EFZAbPe3Nj7oOD1U7_W)

Repository: [https://github.com/fossasia/pslab-firmware](https://www.google.com/url?q=https://github.com/fossasia/pslab-firmware&sa=D&source=editors&ust=1771800528907759&usg=AOvVaw3TXd5f-wBoaCrGYk6lUBRI)

Description: Currently, the PSLab has separate firmware images depending on whether USB or WiFi is used as command interface. Which image is built is controlled by a compile-time switch. The goal of the project is to make the control interface runtime-settable, possibly automatically by monitoring both interfaces and using whichever first receives a valid command.

This can be achieved in a variety of ways, but a good starting point is likely to change the signature of the command_t function pointer typedef to take a EUxSelect enum input argument. Every command_t type function would then need to be updated to use UART_*(EUxSelect select) functions instead of UART1_*().

Objectives

- The changes need to be thoroughly tested to ensure both USB and WiFi functionality remains on par with the separate firmware images.
- Build scripts need to be updated to produce a single artifact instead of one per interface.
- Documentation needs to be updated to reflect how USB / WiFi control works.

Skills Required/Preferred:

- Embedded C / C++
- Microcontroller firmware development
- Understanding of UART and serial communication
- Experience with refactoring legacy codebases
- Build systems (Make, CMake, or similar)
- Debugging and testing embedded systems

Difficulty: Intermediate

Project Size: 175 hours

Required Skills: Flutter/Dart,Testing & CI/CD

Preferred Skills: Hardware & IoT Integration

Possilbe Mentors: [padmal](https://www.google.com/url?q=https://github.com/CloudyPadmal&sa=D&source=editors&ust=1771800528911044&usg=AOvVaw0nvDx3v2KPAEZ5W9OJacaW), [bessman](https://www.google.com/url?q=https://github.com/bessman&sa=D&source=editors&ust=1771800528911131&usg=AOvVaw15Z7xtv_WGJpNGpJTcqZl-), [marcnause](https://www.google.com/url?q=https://github.com/marcnause&sa=D&source=editors&ust=1771800528911211&usg=AOvVaw0tArHs-LR50UIRyUX1l3bw)

Repository: [PSLab Android Repository](https://www.google.com/url?q=https://github.com/fossasia/pslab-android&sa=D&source=editors&ust=1771800528911338&usg=AOvVaw0-GiwbB0dCs8vyaln93VNI) (Check the flutter branch)

Description: The PSLab application is implemented using Flutter, which allows it to target not only Android and iOS, but also Linux, Windows, macOS, and the web (Chromium-based browsers). While the mobile versions are actively used, the desktop and web variants have not yet been thoroughly tested or polished, and currently suffer from usability and compatibility issues.

This project aims to stabilize, improve, and officially release the non-mobile versions of the PSLab app, making PSLab more accessible in classrooms, laboratories, and workshops where desktop or browser-based usage is preferred.

The focus is on testing, fixing platform-specific issues, improving input handling, and establishing a repeatable release and distribution process for desktop and web platforms.

Expected Outcomes / Deliverables

- Desktop & Web Testing: Test the PSLab app on: Linux, Windows, macOS, Web (Chromium-based browsers) and identify platform-specific issues and limitations
- Usability & Compatibility Fixes

- Fix issues specific to non-touch input, such as:

- Oscilloscope zooming and panning using mouse and keyboard
- Window resizing and scaling

- Investigate and resolve connection issues, especially for: Web version communication with PSLab hardware
- Ensure feature parity where feasible with the mobile app

- Release Process for Non-Mobile Platforms: Define a reproducible release workflow for: Desktop binaries, Web builds, Provide official releases via GitHub
- Distribution & Packaging

Package and distribute the app through: Platform-native installers (Linux, Windows, macOS)

Package managers or app stores where appropriate (e.g. WinGet, Microsoft Store, macOS App Store)

Skills Required/Preferred:

- Flutter and Dart
- Cross-platform application development
- Debugging UI and input handling across platforms
- Basic understanding of hardware communication (USB / WebSerial / WebUSB)
- GitHub-based release workflows

Difficulty: Intermediate

Project Size: 90 hours

Required Skills: Dart/Flutter

Preferred Skills: CD (Value Change Dump), GTKWave, Sigrok,

Possilbe Mentors: [padmal](https://www.google.com/url?q=https://github.com/CloudyPadmal&sa=D&source=editors&ust=1771800528915404&usg=AOvVaw3XYW8oDlo9eoje4up7tle7), [bessman](https://www.google.com/url?q=https://github.com/bessman&sa=D&source=editors&ust=1771800528915491&usg=AOvVaw3nU8lKR_-LiVMEDM8gxPw0), [marcnause](https://www.google.com/url?q=https://github.com/marcnause&sa=D&source=editors&ust=1771800528915562&usg=AOvVaw3asntoaymvOjT-7uAgyq9V)

Repository: [PSLab Android Repository](https://www.google.com/url?q=https://github.com/fossasia/pslab-android&sa=D&source=editors&ust=1771800528915712&usg=AOvVaw0Y2ZMK0HSpnOg3buOMCsrl) (Check the flutter branch)

Description: The PSLab app allows to write data to text and CSV files. VCD (Value Change Dump) is a rather old ASCII based format (~ 30 years) which is supported by several tools like Sigrok and GTKWave.

Supporting VCD allows recording data with the PSLab logic analyzer and analyzing it in 3rd party software without an extra integration of the PSLab in said software.

Skills Required/Preferred:

- Python or Dart/Flutter
- Understanding of digital logic and logic analyzers (signals, timing, sampling, edges)
- File formats and data serialization (text-based formats, CSV-like structures)
- Basic data processing (timestamps, channels, value changes)
- Familiarity with the VCD (Value Change Dump) format
- Experience with GTKWave, Sigrok, or similar logic analysis tools
- Knowledge of digital protocols (I²C, SPI, UART)
- Experience working with open-source hardware or measurement tools

Difficulty: Intermediate

Project Size: 350 hours

Required Skills: Flutter/Dart,Testing & CI/CD

Preferred Skills: Hardware & IoT Integration

Possilbe Mentors: [padmal](https://www.google.com/url?q=https://github.com/CloudyPadmal&sa=D&source=editors&ust=1771800528918366&usg=AOvVaw3wji-pK3z4VRpQtlE-cVWe), [bessman](https://www.google.com/url?q=https://github.com/bessman&sa=D&source=editors&ust=1771800528918440&usg=AOvVaw2d-gGtdhV0PHPkVPTYgHHQ)

Repository: [PSLab Android Repository](https://www.google.com/url?q=https://github.com/fossasia/pslab-android&sa=D&source=editors&ust=1771800528918646&usg=AOvVaw2K8R7_8sV4tjBBD4T2CHoU) (Check the flutter branch)

Description: The PSLab Flutter app provides a cross-platform interface to control PSLab hardware and access measurement features, but not all functions have been thoroughly tested across devices and platforms. Users reported bugs, inconsistent behavior, and usability friction that makes it harder to use PSLab effectively especially for first-time users. This project focuses on improving the app as a reliable daily driver by systematically testing and fixing issues across core workflows, refining the user experience, extending support for additional sensors and capabilities exposed by the PSLab hardware/firmware, and implementing interactive in-app guided tutorials that walk users through each major function directly inside the UI.

Expected Outcomes / Deliverables

1. Testing-Driven Bug Fixes and Stability

- Run structured testing across all core app features (connectivity, views, measurement tools, configuration flows, and device interactions) on supported platforms
- Identify, reproduce, and fix high-impact bugs and regressions
- Improve error handling and resilience for common failure modes (disconnects, timeouts, unsupported states)

2. User Experience Improvements

- Streamline key workflows (connecting, switching instruments, starting/stopping measurements, saving/exporting results)
- Improve responsiveness, input handling, and clarity of UI states
- Make instrument views easier to interpret and operate for both beginners and advanced users

3. Expanded Sensor and Feature Support

- Add or complete support for additional sensors/instruments already available in PSLab hardware/firmware but not fully exposed in the Flutter app
- Ensure consistent behavior and UI parity across platforms where feasible
- Validate sensor accuracy and usability through test scenarios

4. In-App Guided Tutorials (Interactive Onboarding)

- Implement guided, interactive walkthroughs inside the app for major PSLab functions (e.g., oscilloscope, logic analyzer, waveform generator, sensor readings)
- Make tutorials contextual (triggered per feature) and actionable (highlight UI elements, guide steps, confirm completion)
- Ensure tutorials are maintainable and can evolve with features over time

Skills Required/Preferred:

- Flutter/Dart Development: Knowledge in building cross-platform applications.
- Mobile, Desktop & Web Development: Experience in deploying apps across various platforms.
- Hardware & IoT Integration: Understanding of connectivity protocols (USB, WiFi) and interfacing with scientific instruments.
- UI/UX Design: Ability to design responsive and intuitive interfaces.
- Testing & CI/CD: Experience with automated testing frameworks and deployment pipelines.
- Open Source Collaboration: Familiarity with contributing to and managing open-source projects.

Difficulty: Medium

Project Size: 175 hours

Required Skills: JavaScript / TypeScript

Possilbe Mentors: [rolandturner](https://www.google.com/url?q=https://github.com/rolandturner&sa=D&source=editors&ust=1771800528926039&usg=AOvVaw067oO01FKBVKfc3JrvKdgO), [hpdang](https://www.google.com/url?q=https://github.com/hpdang&sa=D&source=editors&ust=1771800528926235&usg=AOvVaw3NXj7ojZDWjWLYojnJcCEA), [mohit](https://www.google.com/url?q=https://github.com/mohitk05&sa=D&source=editors&ust=1771800528926395&usg=AOvVaw0yXw2aRQaThruyrZHhDuFY)

Repository: [Scrum Helper Repository](https://www.google.com/url?q=https://github.com/fossasia/scrum_helper&sa=D&source=editors&ust=1771800528926610&usg=AOvVaw0CMc2DtqOTnrkE6XOoB3x5)

Description: Scrum Helper currently works well with GitHub. We want to extend it other source code management (SCM) platforms such as GitLab, Gitea, or Bitbucket.

Expected Outcomes:

- Unified Scrum reports across GitHub, GitLab, and Gitea
- Clean, extensible SCM integration architecture
- Documentation and examples for each supported platform

Required Skills

- JavaScript / TypeScript
- REST APIs
- Familiarity with Git workflows and SCM platforms
- Experience with GitLab or Gitea APIs

Difficulty: Advanced

Project Size: 175 hours

Required Skills: JavaScript / TypeScript

Possilbe Mentors: [rolandturne](https://www.google.com/url?q=https://github.com/rolandturner&sa=D&source=editors&ust=1771800528930410&usg=AOvVaw1ApXpdaFpNN7Fg-FwjOyiI)[r](https://www.google.com/url?q=https://github.com/rolandturner&sa=D&source=editors&ust=1771800528930496&usg=AOvVaw1yDAxba_32gla-WhG00Iuc) [hpdang](https://www.google.com/url?q=https://github.com/hpdang&sa=D&source=editors&ust=1771800528930573&usg=AOvVaw0Co6UqKWCO6iYssv4XBYRJ), [mohit](https://www.google.com/url?q=https://github.com/mohitk05&sa=D&source=editors&ust=1771800528930646&usg=AOvVaw1JxvT3B5D090JkUsv6q69N),

Repository: [Scrum Helper Repository](https://www.google.com/url?q=https://github.com/fossasia/scrum_helper&sa=D&source=editors&ust=1771800528930773&usg=AOvVaw2JF6Z0QRKuYWTftuhr9oZD)

Description: Scrum Helper can generate activity based reports but it does not help teams assess whether their work is aligned with sprint goals. Scope creep and off-goal work often go unnoticed until the sprint review.

Objectives: The goal of this project is to enhance Scrum Helper with goal-aware sprint tracking and work-type composition analysis, enabling teams to evaluate both focus and balance in their sprints.

Expected Outcomes:

- Allow teams to define and manage sprint goals
- Track issues, pull requests, and reviews against those goals
- Automatically classify work into categories such as: feature development, bug fixing, refactoring / technical debt, documentation
- Visualize sprint progress, alignment, and work composition
- Highlight off-goal work and potential scope creep

Required Skills

- JavaScript / TypeScript
- Data analysis and visualization
- Familiarity with Scrum practices
