# Submitty — Project Ideas

**Source:** https://submitty.org/developer/getting_started/project_ideas
**Scraped:** 2026-02-22T23:28:47.548656

---

**We are thrilled to announce that Submitty has been accepted to Google
Summer of Code (GSoC) 2026.**

*See also: How to Apply to Submitty for Google Summer of Code 2026*

The project ideas listed below target a variety of different topics and require different levels of prior experience. The scope of these projects varies, and may require different overall time commitments (varying full-time-work-equivalent from 1 month to 3 months). We are also interested in project proposals based on other topics from our list of open bugs and feature requests.

Prospective Submitty contributers are encouraged to
join our
[Zulip server](/ideas/submitty/contact) to meet the Submitty mentors and other new
developers. You may also submit questions or comments
on specific issues through our
[Submitty GitHub Issue Tracker](https://github.com/Submitty/Submitty/issues).


-
**Interactive User Interfaces With Vue.js**Submitty primarily uses server-side rendering via Twig. jQuery is used extensively throughout the site to add interactivity, but it is insufficient for the most complex pages. Instead, we we are moving forward with a redesign and refactor to

[Vue.js](https://vuejs.org/)for pages such as the TA grading interface, discussion forum, office hours queue, and rainbow grades customization interface. The goal of this project is to explore how we can add and improve interactivity to specific pages and support future development efforts involving the use of Vue.js within Submitty’s codebase.*Expected Outcomes*: This project is flexible in both scope and size. A successful proposal should include detailed information about the specific pages and components to be converted, including time estimates for the proposed conversion projects and common core logic improvements. Participants will gain a better understanding of the challenges involved in introducing new technologies to a large existing codebase, gain experience architecting a key part of a large project, and grow their knowledge of modern web frameworks.[Recent & Ongoing Work to Incorporate Vue.js](https://github.com/Submitty/Submitty/pulls?q=is%3Apr+vue)

[Open Issues related to Vue.js](https://github.com/Submitty/Submitty/issues?q=is%3Aissue%20state%3Aopen%20vue%20)*Skills & Experience Required*: Moderate to advanced programming skills, preferably with experience using modern client-side web frameworks.*Possible Mentors*: Justin Manion, William Allen, Chris Reed, Barb Cutler

*GSoC Project Size*: 175 or 350 hours

*Difficulty Level*: medium to challenging -
**Expand Testing of the Manual/TA Rubric Grading Interface**[Overview of Rubric Grading Interface](/ideas/submitty/grader-rubric_grading-index)Our TA grading interface is elaborate, highly-featured, and customizable. However, the interface is visually overwhelming to new graders and new instructors. We would like to simplify the default environment configuration and improve the on-page documentation to make Submitty more intuitive for new users.

Furthermore, some of our TA grading features are not adequately tested by automated unit and end-to-end (Cypress) regression testing. Our development environment includes a large variety of synthetic data for testing, but the coverage of that data for our large and growing feature set is incomplete. The scripts to randomly generate this synthetic data should be refactored to allow for more flexibility and control to ensure we can adequately test all new and existing functionality.

[Open Issues related to TA Grading](https://github.com/Submitty/Submitty/issues?q=is%3Aopen+is%3Aissue+label%3A%22TA+Grading+%2F+TA+UI%22)

[Open Issues related to Synthetic Sample Data](https://github.com/Submitty/Submitty/issues?q=is%3Aopen+is%3Aissue+label%3A%22Sample+Data%22)

[Related Prior GSoC Project: Cameron Peterson](/ideas/submitty/developer-google_summer_of_code-2023_cameron_peterson)

[Related Prior GSoC Project: Rahul Vishwakarma](/ideas/submitty/developer-google_summer_of_code-2024_rahul_vishwakarma)*Expected Outcomes*: The primary goals for this project include the expansion of our automated testing of the TA Grading pages and to patch bugs uncovered by this improved testing. The project may be expanded in scope to additionally propose and execute small or modest user interface revisions that enhance the TA experience, especially for graders who are new to the interface and grading process.*Skills & Experience Required*: Some programming experience, willingness to learn web and database development and the Cypress end-to-end automated testing framework. Having served as a teaching assistant with grading experience design will be beneficial.*Possible Mentors*: William Allen, Cameron Peterson, Barb Cutler

*GSoC Project Size*: 90 or 175 hours

*Difficulty Level*: introductory to medium -
**Refactor and Performance Improvements for the Manual/TA Rubric Grading Interface**[Overview of Rubric Grading Interface](/ideas/submitty/grader-rubric_grading-index)The Manual/TA rubric grading interface is elaborate, highly-featured, and customizable; however, the performance of these webpages is problematic for large courses due to inefficient database queries and server communication delays to load data that could/should be asynchronous. The manual/TA rubric pages could benefit from a significant technology refactor to use

[Vue.js](https://vuejs.org/), for example.We also have quality of life and efficiency feature requests for

*power user*graders and instructors teaching large enrollment courses with a sizeable team of teaching assistants and graders. Some of the advanced features include: Automated redaction of student names to facilitate anonymized grading, dynamic indicators to show when another grader is actively viewing/grading this student, and streamlining grading by showing individual pages of a student exam rather than the entire .pdf.[Open Issues related to TA Grading](https://github.com/Submitty/Submitty/issues?q=is%3Aopen+is%3Aissue+label%3A%22TA+Grading+%2F+TA+UI%22)

[Related Prior RCOS Project: Alexander Lavallee](/ideas/submitty/developer-rensselaer_center_for_open_source-2025_alexander_lavallee)*Expected Outcomes*: This project would first prepare a detailed software design plan for an organized, multi-stage incremental refactor of the manual/TA rubric pages and follow with the execution/implementation of a significant portion of the new design. The project could include the extension and/or updating of our automated end-to-end (Cypress) testing and patching bugs uncovered by this testing (as described in the previous project idea). The project should include benchmarking along the way to ensure that the refactor is improving the performance of the Manual/TA Rubric Grading interface. The general interface for TA/Manual grading should remain similar, but the project may include small user interface revisions.*Skills & Experience Required*: Web and database development experience and general software design and implementation experience. Experience with end-to-end automated testing (Cypress) and having served as a teaching assistant with grading experience design is beneficial but not required.*Possible Mentors*: William Allen, Barb Cutler

*GSoC Project Size*: 175 or 350 hours

*Difficulty Level*: medium to challenging -
**Notebook Builder: UI To Streamline Instructor Configuration of Automated Grading**Our system for automated testing and grading of student work is very powerful, but the configuration process that instructors must navigate is complex and time-consuming. While we provide a number of illustrative examples, the development of a new autograding configuration is overwhelming – even for an instructor with prior experience. The primary method for creating an autograding configuration is to prepare a

`config.json`

file (and any necessary additional files) and upload or store these files on the server file system. We have a prototype Web GUI interface we call the “Notebook Builder” but the current state of the feature is undocumented and functionality is limited. We would like to improve and expand this feature to facilitate instructor creation of basic and moderate complexity autograding configurations.[Assignment Autograding Configuration Instructions](/ideas/submitty/instructor-autograding-specification)

[Notebook Assignment Configuration](/ideas/submitty/instructor-assignment_configuration-notebook)

[Tutorial Autograding Configuration Examples](https://github.com/Submitty/Tutorial/tree/main/examples)This project will involve multiple modules of Submitty including web UI development, integration, documentation, additional tutorial examples, and extending output generation to instructor solutions in compiled languages.

[Open Issues related to Autograding](https://github.com/Submitty/Submitty/labels/Autograding)

[Open Issues related to Notebook / Notebook Builder](https://github.com/Submitty/Submitty/issues?q=is%3Aopen+is%3Aissue+label%3A%22Notebook+%2F+Notebook+Builder%22)

[Related Prior GSoC Project: Sahil Suman](/ideas/submitty/developer-google_summer_of_code-2024_sahil_suman)

[Related Prior RCOS Project: Justin Manion](/ideas/submitty/developer-rensselaer_center_for_open_source-2025_justin_manion)*Expected Outcomes*: The primary focus of the project is the revision and expansion of the Notebook Builder UI to increase the number of autograding features that are supported. The UI should be easy-to-use for instructors of non-computer-science/non-programming courses and also instructors of courses with introductory to moderate programming assignments. The size and scope for a proposal in this area is flexible, depending on the time commitment and prior skills of the applicant.*Skills & Experience Required*: Some programming experience, willingness to learn web and database development. Prior experience with user interface design and an eye for quality user design are beneficial. Having served as a teaching assistant or instructor with experience in programming assignment design will be beneficial but not required.*Possible Mentors*: Justin Manion, Barb Cutler, Chris Reed

*GSoC Project Size*: 90 or 175 or 350 hours

*Difficulty Level*: introductory or medium -
**Expansion of Examples and Documentation of Intermediate and Advanced Autograding Features**Our system for automated testing and automated grading of student work is very powerful and highly-customizable, but the documentation for our moderate and advanced autograding features is incomplete. While we provide a number of autograding examples, some of the examples are out-of-date and do not represent our current suggested best practices.

[Assignment Autograding Configuration Instructions](/ideas/submitty/instructor-autograding-specification)

[Submitty Autograding Tutorial Examples](https://github.com/Submitty/Tutorial)

[Additional Autograding Examples](https://github.com/Submitty/Submitty/tree/master/more_autograding_examples)

[Related Prior GSoC Project: Drumil Patel](/ideas/submitty/developer-google_summer_of_code-2019_drumilpatel)We would like to reduce the learning curve for new instructors and provide more tutorial examples of autograding for instructors teaching courses of any level. Automated testing and automated grading can be used in introductory programming courses in middle and high schools, including AP Computer Science. It can also be used by programming-intensive intermediate and upper level / senior university-level systems coursework. Assignments that require can be configured with custom Docker Images to provide access to specific programming languages and libraries.

[Open Issues related to Docker Image Autograding](https://github.com/Submitty/Submitty/issues?q=label%3A%22Docker+Container+Autograding%22+)

[Docker Images for Autograding Common Programming Languages](https://github.com/Submitty/DockerImages/tree/main)

[Example Custom Docker Images University](https://github.com/Submitty/DockerImagesRPI/tree/main/dockerfiles)

[Sample Java Assignments](/ideas/submitty/instructor-autograding-sample_assignments)

[Related Prior GSoC Project: Nithish Reddy Banda](/ideas/submitty/developer-google_summer_of_code-2024_nithish_reddy_banda)*Expected Outcomes*: The project should begin with a review and organization of existing sample and tutorial assignments and current autograding functionality documentation. Out-of-date or underdeveloped autograding configuration examples should be expanded as necessary, and features that are missing documentation and examples should be identified (e.g., generated random input and output from instructor solution, customized docker containers, autograding graphical output, autograding) and resolved by creating new examples. Finally, we would like to create and support a resource for the community of crowd-sourced complete programming assignments/exercises with included autograding configuration.*Skills & Experience Required*: Moderate to advanced programming experience, willingness to learn web and database development. Having served as a teaching assistant or instructor with experience in programming assignment design will be beneficial.*Possible Mentors*: Chris Reed, Barb Cutler

*GSoC Project Size*: 175 or 350 hours

*Difficulty Level*: medium to challenging -
**AI/ML to Enhance and Streamline Manual / TA Grading**The use of a unified and retroactively editable rubric for manual/TA grading can ensure consistency when grading large courses, especially when more than one grader is working on a single problem or assignment. However, it is usually still necessary for the graders to inspect the student work one-at-a-time and it can be difficult for the grader to remember the details of all previously graded assignments and recognize patterns that should be graded similarly. Furthermore, the process of manual grading is time-consuming and thus detailed and thoughtful constructive feedback to each individual is often not possible.

[Overview of Rubric Grading Interface](/ideas/submitty/grader-rubric_grading-index)The goal of this project is to explore the potential to leverage Artificial Intelligence and Machine Learning (AI/ML) to reduce the burden of manual grading in large courses with either programming or non-programming assignments. Automatically organizing student submissions into groups that contain similar patterns and have common strengths or flaws can ensure that student work is assessed consistently and students receive appropriate and in-depth feedback to aid their learning.

The Submitty project includes related technology for the static analysis of student’s code and tools to screen for plagiarism in both student-submitted plain text assignments and software. Note that the Submitty static analysis and plagiarism tools have been tested and validated with datasets of sample student submissions; however, for privacy and confidentiality reasons, these datasets are not and cannot be part of the Submitty open-source materials.

[Autograding using Static Analysis](/ideas/submitty/instructor-autograding-static_analysis-index)

[Plagiarism Detection](/ideas/submitty/instructor-course_management-plagiarism)*Expected Outcomes*: Detailed design plan for the integration of an AI/ML framework into Submitty for the analysis and clustering the assignment submissions by students based on common patterns in the text and/or code. Implementation of a prototype AI/ML tool to detect common patterns in student submissions and present this information to the grader in an organized way to allow streamlined bulk grading and feedback within the manual/TA grading interface. As time permits (and based on the scope and time commitment) evaluation of the effectiveness of this technique on real world data and the potential for improving the efficiency of the manual/TA grading process and the quality/accuracy and quantity of useful constructive feedback to students.*Skills & Experience Required*: Coursework and/or professional experience in AI/ML and modern AI/ML technology. Moderate to advanced programming experience, and willingness to learn web and database development. Having served as a teaching assistant for a large course with manual grading experience design will be beneficial.*Possible Mentors*: Barb Cutler, William Allen

*GSoC Project Size*: 175 or 350 hours

*Difficulty Level*: medium to challenging -
**Other Topics**The Submitty team welcomes GSoC project proposals on other topics requested by our student, TA, and instructor users. We track requests for new features in our

[Submitty GitHub Issue Tracker](https://github.com/Submitty/Submitty/issues). A successful application would select one or more issues of moderate scope proportional to the applicant’s time commitment and prior experience. Be sure to join our[Zulip server](/ideas/submitty/contact)to meet the Submitty mentors and other new developers and discuss your interests and project plans.*Skills & Experience Required*: Some prior programming experience, willingness to learn web and database development, and additional specific skills as appropriate.*Possible Mentors*: Barb Cutler, William Allen, Justin Manion, Cameron Peterson, Chris Reed, Shail Patel, Matthew Peveler, Preston Carman

*GSoC Project Size*: 90 or 175 or 350 hours

*Difficulty Level*: introductory to medium to challenging


See also:
