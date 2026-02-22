# #22023

**Parent:** Oppia Foundation — Project Ideas
**Source:** https://github.com/oppia/oppia/issues/22023
**Scraped:** 2026-02-22T23:28:47.620392

---

## [Feature Request]: Consolidate entity migration jobs

**Labels:** enhancement, Impact: High, Work: Medium

### Is your feature request related to a problem? Please describe.

The Oppia codebase includes several different versioned entities which store learning material: explorations, skills, stories, subtopic pages, questions, topics, and collections. The infrastructure to maintain each of these versioned entities has been developed separately, and is a bit patchy (for example, migrations of old snapshots have not been implemented for some of the entities). This is making it difficult to remove some of the old version upgrade functions in the codebase which are no longer needed.

### Describe the solution (or solutions) you'd like

Standardize these migration jobs, so that there is a single, standard way to migrate and upgrade versioned models. This will (a) ensure that all the versioned models can be easily updated on a periodic basis, (b) let us delete the code for upgrading from old versions once all the entities of that version have been upgraded, and (c) simplify the remaining version upgrade code.

Specifically, we would like to do the following:

- Have a BaseMigrateVersionedModelJob and a BaseMigrateVersionedModelSnapshotsJob, and refactor the jobs and audit jobs for migrating models and snapshots (like MigrateExplorationJob, ExpSnapshotsMigrationAuditJob, etc.) to be subclasses of these two jobs. The bulk of the logic for all of these jobs should be in the two base classes, with the subclasses just pointing to the relevant storage models / domain object classes and having no custom logic – see `SNAPSHOT_METADATA_CLASS` in ExplorationModel for an example of this.
- Run all the jobs in production so that all the models and snapshots on the server are upgraded to use the latest schema versions.
- Clean out all the old conversion functions and the methods they call (see https://github.com/oppia/oppia/pull/12256/files for an example).

We would also like to standardize the infrastructure for migrating JSON properties. This entails the following:
- Create a BaseVersionedDomainObject whose subclasses declaratively specify a mapping from any versioned field to its corresponding schema version field. (These fields correspond to `JsonProperty` in the datastore’s storage model.) Un-versioned fields of type `Dict` or `List[Dict]` should be explicitly declared as un-versioned. Subclasses must also reference constants in feconf.py that specify the minimum and maximum version of each field.
- Write backend tests that:
  - Identify all subclasses of BaseVersionedDomainObject in the codebase and verify that every `Dict` or `List[Dict]` field contained in the object is either included in the mapping mentioned above or included in a list of un-versioned fields. This ensures that all versioned domain objects have the necessary infrastructure for performing schema upgrades for their respective JsonProperties.
  - Ensure that the relevant migration functions for each upgradable field are present in the corresponding domain object class with the function signatures (including type hints). Specifically, each conversion function should accept one parameter of the same type as the versioned field and should return one value of the same type. The migration functions can be named using a standard scheme, e.g. `_convert_{{field_name}}_v{{x}}_dict_to_v{{x+1}}_dict`, and the backend test can check for that. This test should also use the minimum and maximum schema versions to check that upgrade functions from the minimum up to the maximum version are present.
- Add a `migrate_to_latest_schema_versions` function to BaseVersionedDomainObject to handle schema upgrades in a generalized way across all domain objects.
- Ensure that all the different getter functions in the _services/fetchers.py files that convert storage models to domain objects also use `migrate_to_latest_schema_versions` to translate that object’s fields to use the latest schema versions.
- Replace all domain objects corresponding to VersionedModels with the new BaseVersionedDomainObject.

Here’s a schematic depiction of a possible end state for versioned domain models:

```
class BaseVersionedDomainObject:
   - Class Variables:
      - schema_versioned_attributes = {}
   - Methods:
      - def migrate_to_latest_schema_versions():
           - Use the versioned_attributes map to find versioned fields. Then call update functions on each of those until the entire domain object is fully upgraded.

class Exploration(BaseVersionedDomainObject:
  - Class Variables:
      - schema_versioned_attributes: {“states_dict”: {“version_field”: “states_schema_version”, “version_min”: 
feconf.MIN_STATE_SCHEMA_VERSION (e.g. 5), “version_max”: feconf.CURRENT_STATE_SCHEMA_VERSION (e.g. 10)}}
  - Methods:
     - def _convert_states_v5_dict_to_v6_dict
     - …
     - def _convert_states_v9_dict_to_v10_dict
```

### Describe alternatives you've considered and rejected

_No response_

### Additional context

See #17579 for an earlier issue filed about this. In that issue, the author posted the following:

- Each type of migration can supply parameters to the base class methods to specify fields to migrate, models to update, auxiliary methods to run after updating models (like updating the summary models). This will make the migration code more declarative and will reduce redundant code. 
- The auxiliary methods like _migrate_xx or _generate_xx_changes can be supplied by the subclass, or provided by the base class with only the type of migration being specified by the subclass.

Ideally, we would try to standardize as much as possible so that as little configuration is needed by the subclasses as possible. But in cases where additional per-model-type configuration is needed, the approach described in the "Describe the solution" part of the issue above could be extended to include any necessary hooks as described here.

