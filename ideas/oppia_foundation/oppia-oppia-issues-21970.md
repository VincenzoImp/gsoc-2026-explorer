# #21970

**Parent:** Oppia Foundation — Project Ideas
**Source:** https://github.com/oppia/oppia/issues/21970
**Scraped:** 2026-02-22T23:28:47.620978

---

## Implement missing domain objects with full `validate()` function.

**Labels:** good first issue, enhancement, Impact: Medium, Work: Low

**Please note that for any model picked up, first describe in a comment what will be the domain object properties and what validation checks will be put in place and only after that is approved, the model can be assigned to you. Please avoid adding any code here to explain the checks. It is difficult to review that. So, stick to describing the checks as you would do in a design doc.**

Additionally, please note that you will need to ensure that, after your refactor, none of the instances of the corresponding storage model should be used in the rest of the codebase, except for the get/save methods that convert a datastore model to a domain object and vice versa. All other usages besides those two methods should be of the domain object. (See `ExplorationModel` and the `Exploration` domain object for an example.)

----

Implement missing domain objects for the following storage models with full `validate()` function:

- [ ] AnswerSubmittedEventLogEntryModel
- [ ] BlogPostReadEventLogEntryModel
- [ ] BlogPostViewedEventLogEntryModel
- [ ] BlogPostExitedEventLogEntryModel
- [ ] BulkEmailModel
- [ ] CollectionCommitLogEntryModel
- [ ] CollectionProgressModel
- [ ] CollectionRightsModel
- [ ] CollectionRightsSnapshotMetadataModel
- [ ] CollectionSnapshotContentModel
- [ ] CollectionSnapshotMetadataModel
- [ ] CompleteExplorationEventLogEntryModel
- [ ] CsrfSecretModel
- [ ] DeletedUserModel
- [ ] DeletedUsernameModel
- [ ] ExplorationActualStartEventLogEntryModel
- [ ] ExplorationAnnotationsModel
- [ ] ExplorationContextModel
- [ ] ExplorationIssuesModel
- [ ] ExplorationRecommendationsModel: @aasmaa11 
- [x] ExplorationRightsModel: @Somnath-Mishra 
- [ ] ExplorationRightsSnapshotMetadataModel
- [ ] ExplorationSnapshotMetadataModel
- [ ] ExplorationStatsTaskEntryModel
- [ ] ExplorationUserDataModel
- [ ] ExplorationVoiceArtistsLinkModel
- [ ] FirebaseSeedModel
- [ ] JobModel
- [ ] LearnerGoalsModel
- [ ] LearnerGroupsUserModel
- [ ] LearnerPlaylistModel
- [ ] LeaveForRefresherExplorationEventLogEntryModel
- [ ] MaybeLeaveExplorationEventLogEntryModel
- [ ] PinnedOpportunityModel
- [ ] PlatformParameterSnapshotMetadataModel
- [ ] PlaythroughModel
- [ ] PseudonymizedUserModel
- [ ] QuestionCommitLogEntryModel
- [ ] QuestionSnapshotMetadataModel
- [ ] RateExplorationEventLogEntryModel
- [ ] RoleQueryAuditModel
- [ ] SentEmailModel
- [ ] SkillCommitLogEntryModel
- [ ] SkillSnapshotMetadataModel
- [ ] SolutionHitEventLogEntryModel
- [ ] StartExplorationEventLogEntryModel
- [ ] StateCompleteEventLogEntryModel
- [ ] StateCounterModel
- [ ] StateHitEventLogEntryModel
- [ ] StoryCommitLogEntryModel
- [ ] StoryProgressModel
- [ ] StorySnapshotMetadataModel
- [ ] SubtopicPageCommitLogEntryModel
- [ ] SubtopicPageSnapshotMetadataModel
- [ ] TopicCommitLogEntryModel
- [ ] TopicRightsSnapshotMetadataModel
- [ ] TopicSimilaritiesModel
- [ ] TopicSnapshotMetadataModel
- [ ] TranslationCoordinatorsModel
- [ ] UnsentFeedbackEmailModel
- [ ] UserBulkEmailsModel
- [ ] UserEmailPreferencesModel (Assignee: @anushaa-m)
- [ ] UserIdByFirebaseAuthIdModel
- [ ] UserIdentifiersModel
- [ ] UsernameChangeAuditModel
- [ ] UserRecentChangesBatchModel
- [ ] UserStatsModel
- [ ] UserSubscribersModel
- [ ] UserSubscriptionsModel @FCancella 
- [ ] VoiceArtistMetadataModel
- [ ] VoiceoverAutogenerationPolicyModel: @aasmaa11 



