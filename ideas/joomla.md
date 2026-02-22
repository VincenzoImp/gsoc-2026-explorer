# Joomla! — Project Ideas

**Source:** https://community.joomla.org/gsoc/projects-2026.html
**Scraped:** 2026-02-22T23:28:47.618177

---

Welcome to the Joomla Google Summer of Code (GSoC) 2026 projects page. If you are interested in participating as a student, please review the materials on applying available at [Google](https://developers.google.com/open-source/gsoc/faq). We strongly encourage you to ask questions about the process and projects on our [Mattermost chat](https://joomlacommunity.cloud.mattermost.com/main/channels/gsoc-2026).


**Project I: Ajaxified Backend**

#ASYNC #Webcomponent #JavaScript

**Project Description:**

#### Backend actions without leaving the page

Saving and other actions that return to the same page can be done with Ajax, without leaving the page and being redirected back. Challenge: make this feature as an extra, while the current system keeps working.

#### Automatic Saving

Automatic saving of content while editing. Should work generally for all components. Challenge: find a solution for the interaction with versioning (not a new version for every edited character). Some Undo action would be great

#### Extend filter

Enhance the list filter function to support searching/filtering by custom fields.

**Knowledge Prerequisite:**

**Language Requisitions:**PHP, Javascript (Ajax)**Nice to have:**Webcomponents

**Expected Outcome:**

- List view backend actions (filter, publish, ...) are executed via Ajax and no site reload happens.
- Automatic saving of all content in a time period (enable/disable).
- Solutions for integration with versioning.

**Difficulty:** Hard | **Project Hours:** 350 Hrs

**Mentors: ** Shivam

**Project II: Automated Workflow**

#Automation #PHP #JavaScript

**Project Description:**

For a few years Joomla! Ships a Workflow feature and Scheduled Tasks. Now these two features should be combined, so that a user can set up assigned workflows in a way that the transitions are executed automatically offering a granular timing definition. It should be possible to create loops or straight scheduled workflows. The interface should consider a good UI, UX and modern accessibility standards

**Knowledge Prerequisite:**

**Language Requisitions:**PHP, JavaScript, HTML, CSS**Nice to have:**Joomla! workflow

**Expected Outcome:**

- A set-up area for timed workflow in categories and articles view
- This function should be easy adaptable for any extension using the workflow

**Difficulty:** Hard | **Project Hours:** 350 Hrs

**Mentors:** Tushar Malik, Dileepkumar Adari

**Project III: Multicategory**

#PHP #Routing

**Project Description: **

Joomla! currently lacks the ability to assign a single item to multiple categories. While the tagging system is often used as a substitute, there is a strong demand for native multicategory support to bring Joomla! in line with other modern content management systems.

**Knowledge Prerequisite:**

**Language Requisitions:**PHP**Nice to have:**Joomla! 6

**Expected Outcome:**

- Every Item in Joomla can be connected with different categories.
- The user must be able to connect/disconnect any item (also in batch mode) to different categories,
- Every article must show its categories and much more.
- For Routing reasons, there needs to be one main category defined.

**Difficulty:** Medium | **Project Hours:** 175 Hrs

**Mentors: **Christiane Maier-Stadtherr, Viviana

**Project IV: Reinforcement Learning from Translators Feedback**

#AI #LLM

**Project Description:**

We are going to use automatic translations for documentation. Every language has its own Joomla specific words. We want to train Language Models with feedback from our translators, to continuously improve the quality of our translations and to incorporate the Joomla specific language properties.

**Knowledge Prerequisite:**

**Language Requisitions:**AI knowledge, PHP, Joomla extensions, Joomla Events, calling APIs, Machine Learning**Nice to have**: knowledge about Reinforcement Learning from Human Feedback

**Expected Outcome:**

- A Joomla extension package, with a complete workflow of having the initial (English) text translated in multiple languages, giving feedback by human translators and learning from that feedback.
- This workflow is triggered by a Joomla Event when anything changes in the original, English text.
- Per language a translator's interface for feedback. The core of this application is language independent, and must work for multiple languages.
- The most important part of this system is the processing of the translator's feedback, so the (Joomla specific) translations will improve over time.

**Difficulty:** Hard | **Project Hours:** 350 Hrs

**Mentors: **Herman, Charvi
