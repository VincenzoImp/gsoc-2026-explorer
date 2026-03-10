# #21869

**Parent:** Oppia Foundation — Project Ideas
**Source:** https://github.com/oppia/oppia/issues/21869
**Scraped:** 2026-03-10T16:58:40.308618

---

## Implement validation job for prod models inheriting from base models

**Labels:** good first issue, enhancement, Impact: High, Work: Medium

### NOTE TO CONTRIBUTORS:

* Please use #22225 as a base for creating any new jobs.
* For any validation job you implement, the corresponding domain object of the prod model should be updated to do the following in the same PR:
    * Instead of throwing errors using utils.ValidationError("some message"), they should throw typed errors for each message category.
    * These error types should be defined in a new file as per the following example:
        * Domain class: `class Exploration`, file: `exp_domain.py`
        * Error class: `class ExplorationDomainError(utils.ValidationError)`, file: `exp_domain_errors.py`
----------------------------

This issue aims to serve as a checklist for implementing prod validation for all models inheriting from base model.

[Here](https://docs.google.com/document/d/1u45oC6igsaTvQl4oNd8VvDiZe3JqeY3m_5n4QZ6d4rA/edit?usp=sharing) is an umbrella doc describing the design for validation and further elaborating on next steps of migration and fixing root cause. Note that, migration and root cause fixing is out of scope for this issue but contributors can feel free to attempt if they would like to.

Note, for any model that you end up picking, before starting with code, list down the validation you will be implementing as described in the above doc and get it approved from me. Post that you will be assigned to the model in the list. After implementing the job, you should also be [submitting a request to test it on backup server](https://github.com/oppia/oppia/wiki/Testing-jobs-and-other-features-on-production).

Implement Audit job for:
- [x]  BaseModel: @ankita240796 
- [ ]  ActivityReferencesModel @ankita240796  - work on sample PR to show how domain errors should be defined and link it as an example
- [ ]  AnswerSubmittedEventLogEntryModel
- [ ]  AppFeedbackReportModel
- [ ]  AppFeedbackReportStatsModel
- [ ]  AppFeedbackReportTicketModel
- [ ]  AuthorBlogPostAggregatedReadingTimeModel
- [ ]  AuthorBlogPostReadsAggregatedStatsModel
- [ ]  AuthorBlogPostViewsAggregatedStatsModel
- [ ]  BeamJobRunModel
- [ ]  BeamJobRunResultModel
- [ ]  BlogAuthorDetailsModel
- [ ]  BlogPostExitedEventLogEntryModel
- [ ]  BlogPostModel
- [ ]  BlogPostReadEventLogEntryModel
- [ ]  BlogPostReadingTimeModel
- [ ]  BlogPostReadsAggregatedStatsModel
- [ ]  BlogPostRightsModel
- [ ]  BlogPostSummaryModel
- [ ]  BlogPostViewedEventLogEntryModel
- [ ]  BlogPostViewsAggregatedStatsModel
- [ ]  BulkEmailModel
- [ ]  ClassroomModel
- [ ]  CollectionProgressModel
- [ ]  CollectionSummaryModel
- [ ]  CommunityContributionStatsModel
- [ ]  CompletedActivitiesModel
- [ ]  CompleteExplorationEventLogEntryModel
- [ ]  CsrfSecretModel   Assignee: @bswathii
- [ ]  DeletedUserModel
- [ ]  DeletedUsernameModel
- [ ]  EntityTranslationsModel
- [ ]  EntityVoiceoversModel
- [ ]  ExplorationActualStartEventLogEntryModel
- [ ]  ExplorationContextModel
- [ ]  ExplorationIssuesModel
- [ ]  ExplorationOpportunitySummaryModel
- [ ]  ExplorationStatsModel
- [ ]  ExplorationStatsTaskEntryModel
- [ ]  ExplorationUserDataModel
- [ ]  ExplorationVersionHistoryModel
- [ ]  ExplorationVoiceArtistsLinkModel
- [ ]  ExpSummaryModel
- [ ]  ExpUserLastPlaythroughModel
- [ ]  FeatureFlagConfigModel
- [ ]  FirebaseSeedModel
- [ ]  GeneralFeedbackMessageModel
- [ ]  GeneralFeedbackThreadModel
- [ ]  GeneralFeedbackThreadUserModel
- [ ]  GeneralSuggestionModel
- [ ]  IncompleteActivitiesModel
- [ ]  JobModel
- [ ]  LearnerAnswerDetailsModel
- [ ]  LearnerGoalsModel
- [ ]  LearnerGroupModel
- [ ]  LearnerGroupsUserModel
- [ ]  LearnerPlaylistModel
- [ ]  LeaveForRefresherExplorationEventLogEntryModel
- [ ]  MachineTranslationModel
- [ ]  MaybeLeaveExplorationEventLogEntryModel
- [ ]  PendingDeletionRequestModel
- [ ]  PinnedOpportunityModel
- [ ]  PlaythroughModel
- [ ]  PseudonymizedUserModel
- [ ]  QuestionContributionStatsModel
- [ ]  QuestionReviewerTotalContributionStatsModel
- [ ]  QuestionReviewStatsModel
- [ ]  QuestionSkillLinkModel
- [ ]  QuestionSubmitterTotalContributionStatsModel
- [ ]  QuestionSummaryModel
- [ ]  RateExplorationEventLogEntryModel
- [ ]  RoleQueryAuditModel
- [ ]  SentEmailModel
- [ ]  SkillOpportunityModel
- [ ]  SkillSummaryModel
- [ ]  SolutionHitEventLogEntryModel
- [ ]  StartExplorationEventLogEntryModel
- [ ]  StateAnswersModel
- [ ]  StateCompleteEventLogEntryModel
- [ ]  StateCounterModel
- [ ]  StateHitEventLogEntryModel
- [ ]  StoryProgressModel
- [ ]  StorySummaryModel
- [ ]  TopicSimilaritiesModel
- [ ]  TopicSummaryModel
- [ ]  TransientCheckpointUrlModel
- [ ]  TranslationContributionStatsModel
- [ ]  TranslationCoordinatorsModel
- [ ]  TranslationReviewerTotalContributionStatsModel
- [ ]  TranslationReviewStatsModel
- [ ]  TranslationSubmitterTotalContributionStatsModel
- [ ]  UnsentFeedbackEmailModel
- [ ]  UserAuthDetailsModel
- [ ]  UserBulkEmailsModel
- [ ]  UserContributionProficiencyModel
- [ ]  UserContributionRightsModel
- [ ]  UserContributionsModel
- [ ]  UserEmailPreferencesModel
- [ ]  UserGroupModel
- [ ]  UserIdByFirebaseAuthIdModel
- [ ]  UserIdentifiersModel
- [ ]  UsernameChangeAuditModel
- [ ]  UserQueryModel
- [ ]  UserSettingsModel
- [ ]  UserSkillMasteryModel
- [ ]  UserSubscribersModel
- [ ]  UserSubscriptionsModel
- [ ]  VoiceArtistMetadataModel
- [ ]  VoiceoverAutogenerationPolicyModel



