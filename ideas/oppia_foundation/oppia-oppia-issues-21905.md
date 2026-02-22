# #21905

**Parent:** Oppia Foundation — Project Ideas
**Source:** https://github.com/oppia/oppia/issues/21905
**Scraped:** 2026-02-22T23:28:47.621040

---

## Implement validation for all prod models

**Labels:** enhancement, Impact: High, Work: Medium

## Note For Contributors

* For any validation job you implement, the corresponding domain object of the prod model should be updated to do the following in the same PR:
    * Instead of throwing errors using utils.ValidationError("some message"), they should throw typed errors for each message category.
    * These error types should be defined in a new file as per the following example:
        * Domain class: `class Exploration`, file: `exp_domain.py`
        * Error class: `class ExplorationDomainError(utils.ValidationError)`, file: `exp_domain_errors.py`
----------------------------

 
- Implement validation jobs for all prod storage models. This includes implementing a base job first for a particular subest of models inheriting from the same base model and then using it as the super class for other validation jobs. 
  - [ ] BaseModel & sub-classes: Tracked in https://github.com/oppia/oppia/issues/21869. Note that, the base models listed below also inherit from `BaseModel` but are expected to serve as base for other storage models and hence a separate base validation job should exist for them which will act as the super class for validation jobs of all other storage models which inherit from the respective base model.
  - [ ] BaseHumanMaintainedModel
  - [ ] BaseCommitLogEntryModel
    - [ ] CollectionCommitLogEntryModel
    - [ ] ExplorationCommitLogEntryModel
    - [ ] QuestionCommitLogEntryModel
    - [ ] SkillCommitLogEntryModel
    - [ ] StoryCommitLogEntryModel
    - [ ] SubtopicPageCommitLogEntryModel
    - [ ] TopicCommitLogEntryModel
  - [ ] VersionedModel
    - [ ]  CollectionModel
    - [ ] CollectionRightsModel
    - [ ] PlatformParameterModel
    - [ ] ExplorationModel
    - [ ] ExplorationRightsModel
    - [ ] QuestionModel
    - [ ] SkillModel
    - [ ] StoryModel
    - [ ] SubtopicPageModel
    - [ ] TopicModel
    - [ ] TopicRightsModel
  - [ ] BaseSnapshotMetadataModel
    - [ ] CollectionSnapshotMetadataModel
    - [ ] CollectionRightsSnapshotMetadataModel
    - [ ] PlatformParameterSnapshotMetadataModel
    - [ ] ExplorationSnapshotMetadataModel
    - [ ] ExplorationRightsSnapshotMetadataModel
    - [ ] QuestionSnapshotMetadataModel
    - [ ] SkillSnapshotMetadataModel
    - [ ] StorySnapshotMetadataModel
    - [ ] SubtopicPageSnapshotMetadataModel
    - [ ] TopicSnapshotMetadataModel
    - [ ] TopicRightsSnapshotMetadataModel
  - [ ] BaseSnapshotContentModel
    - [ ] CollectionSnapshotContentModel
    - [ ] CollectionRightsSnapshotContentModel
    - [ ] PlatformParameterSnapshotContentModel
    - [ ] ExplorationSnapshotContentModel
    - [ ] ExplorationRightsSnapshotContentModel
    - [ ] QuestionSnapshotContentModel
    - [ ] SkillSnapshotContentModel
    - [ ] StorySnapshotContentModel
    - [ ] SubtopicPageSnapshotContentModel
    - [ ] TopicSnapshotContentModel
    - [ ] TopicRightsSnapshotContentModel
  - [ ] BaseMapReduceBatchResultsModel
    - [ ] FeedbackAnalyticsModel
    - [ ] ExplorationRecommendationsModel
    - [ ] ExplorationAnnotationsModel
    - [ ] StateAnswersCalcOutputModel
    - [ ] UserRecentChangesBatchModel
    - [ ] UserStatsModel
    
- Implement any missing domain layer validation for all domain objects corresponding to these prod models. For more details, on what goes in a validation job vs domain layer validation check out [this doc](https://docs.google.com/document/d/1u45oC6igsaTvQl4oNd8VvDiZe3JqeY3m_5n4QZ6d4rA/edit?tab=t.0#heading=h.zb8n5c4fg57z).


