# Open HealthCare Network — Project Ideas

**Source:** https://github.com/ohcnetwork/care_fe/issues?q=is%3Aissue%20state%3Aopen%20label%3AGSoC
**Scraped:** 2026-02-22T23:28:47.599478

---

## #10599: Whatsapp bot for CARE

**Labels:** blocked, GSoC

## Project Detail

CARE is a centralized capacity management and patient management system, central to the 10BedICU Project, integrating patients, doctors, hospitals, labs, specialized treatment centers, hospital administrators, and shifting control cells. Hospitals update crucial information about their assets, providing district administration with a comprehensive view of the healthcare system via smart dashboards. CARE digitizes patient records, streamlines workflows for pandemic management, and is deployed in remote areas, enabling Tele-ICU services for underserved citizens. It revolutionizes healthcare management, enhancing efficiency, accessibility, and patient outcomes.

## Features To Be Implemented

Build a wrapper on care that IM bots can use to get information or send a notification. The idea behind this feature is to ease and improve the user experience. 

- [ ] Build a generic IM wrapper for care which the respective bots can use to interact with care
- [ ] Build a WhatsApp bot which can be used by both patients and hospital staff
  
  For Patients
  - [ ] Should fetch their patient records
  - [ ] Should fetch their current medications
  - [ ] Should fetch their procedures
  
  For Users (Hospital Staff)
  - [ ] Should fetch their schedules (to be done after scheduling)
 
_The above-mentioned list of items (both For Patients and For Users) is subject to change, the mentioned features are just to give an idea of what needs to be done._

_While implementing this, a conscious effort should be taken to prevent the Private Personal Information (PPI) of other patients from being shared._


## Learning Path

|  | Details |
| :---:  | :---:  |
| Complexity       | Medium |
| Required Skills | Python, Django |
| Mentors            | @shivankacker @rithviknishad @tellmeY18 |
| Project Size      | 175 Hours |

## Link to documentation for Product Set-Up

1. For setting up the frontend, please refer to the readme file available at: https://github.com/coronasafe/care_fe
2. For setting up the backend, please refer to the readme file available at: https://github.com/coronasafe/care

## Acceptance Criteria

- Code is logically structured for long-term project sustainability.
- Proper descriptions should be included for review purposes.
- QA and Code Review

## Milestone

- [ ] Get to know CARE as a product and understand the workflow.
- [ ] Understand the requirements.
- [ ] Implement the tasks mentioned above
- [ ] Write tests for the implemented functionality
- [ ] Optimise the code
- [ ] Review and QA

---

## #10534: SSO Support

**Labels:** blocked, GSoC

#### Project Detail

The **SSO Support** project aims to integrate Single Sign-On (SSO) functionality into CARE to streamline user authentication and improve overall security. By enabling SSO, users can log in using a single set of credentials across multiple CARE services and applications, reducing password fatigue and simplifying user management. This integration will leverage industry-standard protocols such as OAuth, OpenID Connect, or SAML, ensuring a secure and scalable solution for both internal and external users.

#### Features To Be Implemented

- [ ] **SSO Integration Module:** Develop a robust SSO module that supports industry-standard protocols (OAuth, OpenID Connect, and/or SAML).
- [ ] **Unified Authentication Flow:** Implement a seamless authentication flow that allows users to sign in once and access all integrated CARE components.
- [ ] **Identity Provider (IdP) Integration:** Integrate with popular identity providers (e.g., Google, Microsoft, Okta) to facilitate centralized authentication.
- [ ] **Security Enhancements:** Ensure secure handling of tokens and sessions, with compliance to current security standards.
- [ ] **Role & Permission Management:** Extend the user management system to incorporate SSO-based roles and permission assignments.
- [ ] **Comprehensive Testing:** Write and execute unit and integration tests to guarantee the security and reliability of the SSO functionality.

**Note:** The SSO module should integrate seamlessly with the existing CARE architecture and provide a consistent, secure authentication experience.

#### Learning Path

|                | Details |
| -------------- | :-----: |
| **Complexity** | Large   |
| **Required Skills** | ReactJS, NodeJS, TypeScript, Django, OAuth, OpenID Connect, SAML, Security Standards |
| **Mentors** | @amit-kr-debug @sainak @dauntlessnomad  |
| **Project Size** | 350 hours |

#### Link to documentation for Product Set-Up

1. For setting up the frontend, please refer to the readme file available at: [CARE Frontend](/ideas/open-healthcare-network/ohcnetwork-care_fe)  
2. For setting up the backend, please refer to the readme file available at: [CARE Backend](https://github.com/ohcnetwork/care)

#### Acceptance Criteria

- The SSO integration supports one or more industry-standard protocols (OAuth, OpenID Connect, and/or SAML).
- Users can authenticate using SSO and seamlessly access various CARE modules.
- Secure token handling and session management are implemented.
- Role and permission management is integrated with the SSO authentication system.
- Comprehensive unit and integration tests are completed, with all CI/CD workflows passing.
- Detailed documentation and successful peer code reviews are provided.

#### Milestone

- [ ] Assess the current CARE authentication architecture and define SSO requirements.
- [ ] Design the SSO integration module and select appropriate protocols.
- [ ] Develop and integrate the SSO authentication flow into CARE.
- [ ] Implement integrations

*[truncated]*

---

## #10508: HR Management Module

**Labels:** question, blocked, GSoC, needs-triage

#### Project Detail

The **CARE HR Module** project aims to enhance the human resource management capabilities within CARE. This involves building backend models and API endpoints to handle employee data, developing a user-friendly frontend interface for HR tasks, and providing reporting and dashboard views for better HR oversight.

#### Features To Be Implemented

- [ ] **Employee Data Export and Reporting:**  
  Enable exporting of employee data and leave records, and provide meaningful reports for HR metrics.
- [ ] **Staff Profile Integration:**  
  Automatically populate staff profiles from user data, and allow uploading additional professional documents.
- [ ] **Leave Tracking:**  
  Add leave tracking functionality, leveraging existing scheduling exceptions to manage and approve leave requests.
- [ ] **HR Dashboard View:**  
  Implement a dashboard with visual insights into key HR data such as leave balances, employee roles, and departmental metrics.

**Note:** Ensure that all new features integrate seamlessly with existing CARE modules.

#### Learning Path

|                | Details |
| -------------- | ------- |
| **Complexity** | Medium  |
| **Required Skills** | ReactJS, NodeJS, TypeScript, Django, Data Export, and Dashboard Design |
| **Mentors** | Niel @amit-kr-debug @vigneshhari |
| **Project Size** | 175 hours |

#### Link to Documentation for Product Set-Up

1. For frontend setup, refer to: [CARE Frontend](/ideas/open-healthcare-network/ohcnetwork-care_fe)  
2. For backend setup, refer to: [CARE Backend](https://github.com/ohcnetwork/care)

#### Acceptance Criteria

- CI/CD workflows pass without issues.  
- Employee data export and reporting functionality is fully operational.  
- Staff profiles auto-fill accurately, with the ability to add additional documentation.  
- Leave tracking integrates seamlessly with the HR module.  
- The dashboard provides clear, actionable insights.  
- Complete documentation and comprehensive testing are in place.  
- Peer reviews and QA processes are successfully completed.

#### Milestone

- [ ] Understand the current HR module structure and data model.  
- [ ] Design and implement employee data export and reporting features.  
- [ ] Integrate staff profile auto-fill and professional documentation.  
- [ ] Add and test the leave tracking functionality.  
- [ ] Build and refine dashboard views and metrics.  
- [ ] Perform integration testing and finalize documentation.  
- [ ] Complete QA and final code reviews.

---
