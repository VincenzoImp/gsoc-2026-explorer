# Open HealthCare Network — Project Ideas

**Source:** https://github.com/ohcnetwork/care_fe/issues?q=is%3Aissue%20state%3Aopen%20label%3AGSoC
**Scraped:** 2026-03-10T16:58:40.257235

---

## #10599: Whatsapp bot for CARE

**Labels:** question, blocked, GSoC, needs-triage

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
