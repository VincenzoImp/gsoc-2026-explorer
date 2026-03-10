# https://github.com/fossology/fossology/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22

**Parent:** FOSSology — Project Ideas
**Source:** https://github.com/fossology/fossology/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22
**Scraped:** 2026-03-10T16:58:40.264509

---

## #3418: Bucket Browser fails when no bucket analysis dataset exists for an upload

## Description

When opening the **Bucket Browser** for an upload where **Bucket Analysis was not selected during upload**, the page does not render correctly.

The Bucket Browser expects a valid bucket analysis dataset (`ars_pk`). If the bucket agent has not been executed yet (for example, when **Bucket Analysis is not checked in the upload analysis options**), the dataset does not exist and the page attempts to query `bucket_ars` using an undefined value.

This can result in an SQL error or an empty page.

As a consequence, users cannot access the Bucket Browser view for uploads that have not yet been analyzed by the bucket agent.

## Steps to Reproduce

1. Upload a file or archive in Fossology
2. In the **analysis options**, ensure that **Bucket Analysis is NOT selected**
3. Complete the upload
4. Navigate to:
`Browser->Bucket Browser`
5. Open the uploaded file or directory in the Bucket Browser

---

## Actual Behavior

The Bucket Browser fails to render correctly because no bucket dataset (`ars_pk`) exists for the upload.

Possible outcomes include:

- SQL errors
- blank page
- missing bucket results

## Expected Behavior

The Bucket Browser should handle the case where no bucket dataset exists for an upload and provide a clear user experience instead of failing.

---

## Screenshots

**Upload analysis options (Bucket Analysis not selected)**

<img width="1646" height="1074" alt="Image" src="https://github.com/user-attachments/assets/7ab1a4ba-7fa3-4e0d-abc5-ac50cc69d359" />

**Bucket Browser error / blank page**

<img width="1647" height="539" alt="Image" src="https://github.com/user-attachments/assets/1764b31c-e886-4ff2-8dbf-57163fe1456a" />
<img width="1646" height="562" alt="Image" src="https://github.com/user-attachments/assets/ee993722-12d3-49d9-ae73-9b67e897b9c1" />

---

---

## #3385: Bug(API): POST /api/v2/uploads returns 404 for negative folderId (should be 400)

## Description
`POST /api/v2/uploads` returns **HTTP 404 Not Found** when `folderId` is a **negative integer** (e.g., `-1`, `-5`).  
A negative `folderId` is invalid input, so the endpoint should return **HTTP 400 Bad Request** with the validation message `folderId must be a positive integer!`, instead of treating it as “not found”.

This happens because negative numeric values are not rejected by the current validation logic, so the request reaches the folder existence check and fails later with a **404**.

## How to Reproduce
1. Call `POST /api/v2/uploads` with a valid auth token.
2. Send a request body with a negative `folderId` (example `-1`).
3. Observe the response status code and message.

```bash
curl -X POST 'http://localhost:8081/repo/api/v2/uploads' \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "folderId": -1,
    "uploadType": "vcs",
    "location": { "vcsType": "git", "vcsUrl": "https://github.com/example/repo.git" }
  }'
```

## Expected Behavior
- Returns **HTTP 400 Bad Request**
- Message indicates `folderId` must be a positive integer (e.g., `folderId must be a positive integer!`)

## Actual Behavior
- Returns **HTTP 404 Not Found**
- Message indicates the folder does not exist (e.g., `folderId -1 does not exists!`)
- Example response:

```json
{"code":404,"message":"folderId -1 does not exists!","type":"ERROR"}
```
## Environment
- FOSSology `master` branch

---

## #3384: Unsafe Hash Table Lookup Leading to Incorrect Logical Evaluation

## Location
`src/scheduler/agent/database.c:1157-1158`

## Description

The code performs direct comparisons using values returned from `g_hash_table_lookup()` without verifying whether the keys exist in the hash table:

```c
if ((g_strcmp0((char *)g_hash_table_lookup(smtpvariables, "SMTPPort"), "25") != 0) 
    || g_strcmp0((char *)g_hash_table_lookup(smtpvariables, "SMTPStartTls"), "1") == 0)
```

If either key:
- "SMTPPort"
- "SMTPStartTls"

does not exist in the hash table,
 then g_hash_table_lookup(...)  →  NULL
And you are effectively doing:
```
g_strcmp0(NULL, "25")
g_strcmp0(NULL, "1")
```
Even though g_strcmp0() is designed to handle NULL safely, the problem is:

### Incorrect Logical Evaluation
Example:
```
g_strcmp0(NULL, "25") != 0
```
This evaluates to TRUE.
This means:
- If "SMTPPort" is missing, the condition behaves as if the port is not 25.
- The system may enable or alter SMTP/TLS behavior incorrectly.

### Silent Misconfiguration Risk

If both keys are missing:

(TRUE) || (FALSE)
The condition evaluates to TRUE, potentially:

Enabling TLS unexpectedly
Forcing non-default SMTP behavior
Causing incorrect mail configuration handling
This can lead to runtime issues that are difficult to trace.

---

## #3381: Undefined array key access in JobDao::hasActionPermissionsOnJob() when querying job table

The method `JobDao::hasActionPermissionsOnJob()` queries the `job` table but processes the result as if it contains fields `jq_pk` and `end_bits`, which are not part of the selected result set.

This appears to be a copy-paste artifact from methods that query the `jobqueue` table (e.g., `getAllJobStatus()`), where those fields are valid.

#### Current Behavior

* The query uses:

  ```sql
  SELECT * FROM job
  LEFT JOIN group_user_member gm ON gm.user_fk = job_user_fk
  ```
* Inside the loop, it accesses:

  ```php
  $row['jq_pk']
  $row['end_bits']
  ```
* These columns do not exist in the `job` table or the current query result.
* The method builds and returns an array even though it is used as a boolean permission check in callers (UI/API).

This can lead to:

* Undefined array key warnings (in strict error reporting)
* Unnecessary iteration and memory usage
* Misleading return type (array instead of boolean for a permission check)

#### Expected Behavior

* The method should only check whether a matching row exists (permission check).
* It should not access undefined columns from the result set.
* It should return a boolean (`true` if permission exists, otherwise `false`).

---

## #3378: UploadTreeProxy: Broken DB View Name instantiation and query parameter reuse

## Description
There are two distinct logic errors in `UploadTreeProxy.php` which impact DB View name uniqueness and Postgres parameter reuse string mapping.

### Bug 1: View Name overwrites suffixes with a generic string
When an `UploadTreeProxy` is instantiated without a specific view name, it builds a query string suffix in `createUploadTreeViewQuery()` to guarantee that multiple queries (e.g. `_realParent` vs `_alreadyCleared`) do not collide on the same Postgres view/statement name.
However, in the constructor, `$dbViewName` is evaluated **before** `createUploadTreeViewQuery()` is invoked, using `isset($this->dbViewName) ?: ''`, which evaluates the boolean return of `isset()` (so `1`). Then, it calls `parent::__construct(..., $dbViewName)`, inadvertently passing the string `'UploadTreeView'` and overriding the uniquely generated suffix created inside `createUploadTreeViewQuery()`.

**Consequence**: If multiple instances omitted the 4th constructor argument (e.g., `ui-clearing-view.php`), they both resolve to the default view name `UploadTreeView`. This can cause Postgres prepared statement collision errors.

### Bug 2: SQL Parameter Reuse Fails
The proxy attempts to reuse parameters (for performance optimization in parameterized execution) via `addParamAndGetExpr($key, $value)`. The intent is for it to verify if a `$key` exists and reuse the `$n` index:
```php
if (array_key_exists($key, $this->params)) {
   return '$' . (1 + array_search($key, array_keys($this->params)));
}
```
However, the values were pushed using array append `$this->params[] = $value;`, stripping the string key entirely. `array_key_exists` subsequently always fails, duplicating the query parameters inside `$this->params` array instead of reusing existing indexed values.

## Proposed Fix
* Correct the assignment of `$dbViewName` in `__construct` to use the property after `createUploadTreeViewQuery()` completes.
* Switch `$this->params[] = $value` to `$this->params[$key] = $value`, so the array index remains preserved for validation. Modify `countMaskedNonArtifactChildren` appropriately so it also binds the associative array index correctly.

---

## #3374: Fix email notification setup docs for modern Debian/Ubuntu compatibility

The [Email notification configuration](https://github.com/fossology/fossology/wiki/Email-notification-configuration) wiki page references `heirloom-mailx` as the mail client used by FOSSology for sending SMTP-based job completion notifications. This package is EOL on modern Debian/Ubuntu systems (include WSL), making the documented setup non-functional out of the box for new installations.

**Suggested Fix:**

- Update the wiki to mention `bsd-mailx` or `mailutils` as an alternatives with corresponding install commands.
- Audit any installation scripts (e.g. install.sh or CI configs) that may reference `heirloom-mailx` and update accordingly.
- Note any behavioral difference in SMTP configuration syntax b/w `heirloom-mailx` and the alternatives.

---

## #3358: Bug(API): Debug `echo` statement and wrong parameter in CopyrightController corrupts REST API responses

While working with the copyright REST endpoints, I noticed two problems in CopyrightController.php that affect all DELETE, UPDATE, and RESTORE operations.

Both issues are in:

src/www/ui/api/Controllers/CopyrightController.php

1) Debug echo left in production (breaks JSON responses)

Inside the deleteFileCX() method (around line 937), there is a leftover debug statement:
echo $uploadTreeId;
Since this is a REST API endpoint, this echo writes directly to the HTTP response body before the JSON response is returned.
As a result, every affected DELETE endpoint returns invalid JSON.
Example actual response:
12345{"code":200,"message":"Successfully removed copyright.","type":"INFO"}

Expected response:
{"code":200,"message":"Successfully removed copyright.","type":"INFO"}

Because of the prepended number, any JSON client fails to parse the response.
This affects all copyright DELETE endpoints (including user-copyright, scancode-copyright, email, url, author, ecc, keyword, ipra, etc.).

Fix:
Simply remove the debug line:
// Remove this line
echo $uploadTreeId;

2) Wrong parameter passed to getUploadTreeTableName()
In three methods:
deleteFileCX()
restoreFileCx()
updateFileCx()
getUploadTreeTableName() is called with $uploadTreeId instead of $uploadPk.

Current (incorrect):
$uploadTreeTableName = $uploadDao->getUploadTreeTableName($uploadTreeId);

However, getUploadTreeTableName() expects the upload primary key, not the upload tree item ID.
The correct usage is already present in the same file inside getFileCX():
$uploadTreeTableName = $this->restHelper->getUploadDao()->getuploadTreeTableName($uploadPk);

So the calls in the other methods should be:
$uploadTreeTableName = $uploadDao->getUploadTreeTableName($uploadPk); or
$uploadTreeTableName = $this->restHelper->getUploadDao()->getUploadTreeTableName($uploadPk);
Passing $uploadTreeId may cause the wrong upload tree table to be resolved, which could lead to modifying or deleting the wrong data.

How to reproduce:
For the debug echo issue
Upload and scan a package with copyright entries.
Send a DELETE request:
DELETE /api/v1/uploads/{uploadId}/item/{itemId}/copyrights/{hash}
The response body contains the raw uploadTreeId before the JSON.
JSON parsing fails in any proper client.
For the wrong parameter issue
Upload a package and run the copyright agent.
Try deleting, restoring, or updating a copyright entry via REST.
Internally, getUploadTreeTableName() receives $uploadTreeId instead of $uploadPk.
This can resolve to the wrong upload tree table depending on the ID values.

Impact:
Together, these issues affect all copyright-related:
DELETE
UPDATE
RESTORE

endpoints (including scancode, user-copyright, email, url, author, etc.).

Suggested fixes:
Remove the debug echo.
Replace $uploadTreeId with $uploadPk in:
deleteFileCX()
restoreFileCx()
updateFileCx()

---

## #3349: Enhance License Result Filtering & Search in Web UI

In the current FOSSology Web UI, when users scan a large project, the license results table becomes very long and difficult to navigate.

Current limitations:

No quick search inside license results table

No filter by license type (permissive, copyleft, unknown)

No sorting by confidence level

No highlight for high-risk licenses

This makes reviewing scan results time-consuming for compliance teams.

Proposed Enhancement

Improve the License Results page by adding:

Search bar to filter licenses instantly

Dropdown filter:

Permissive

Copyleft

Unknown

 Sort by:

Confidence

File name

License name

Technical Scope
1️⃣ Frontend (UI)

Modify License Results page (PHP + Twig/HTML)

Add:

Search input field

Filter dropdown

Sorting option

Backend (Optional Enhancement)

Add API parameter:
?license_type=copyleft

Styling

Add color indicators:

Red → Strong copyleft

Yellow → Weak copyleft

Green → Permissive

Expected Behavior

When user scans a project:

They can type “MIT” → only MIT files appear

Select “Copyleft” → only copyleft licenses show

Click “Sort by Confidence” → results reorder

GPL licenses appear highlighted

eliverables

Updated UI page

JS filtering logic

Updated API (if implemented)

Basic test cases

Documentation update

---

## #3348: Scheduler crashes whenever the priority of individual jobs is modified

The scheduler crashes whenever the priority of an individual job is modified. This issue occurs consistently when attempting to adjust the priority settings of a job, causing the system to become unresponsive and terminate the scheduling process unexpectedly.

Steps to Reproduce:
- Open the scheduler administration (?mod=admin_scheduler).
- Select an operation: Priority
- Select a job
- Select a priority level: (range -20 to 20)
- Submit

Result: The scheduler crashes immediately after the priority change.

**Expected Behavior:**
The scheduler should update the priority of the selected job without crashing, maintaining normal operation and ensuring that the system can continue to manage and execute jobs as expected.

**Actual Behavior:**
The scheduler crashes upon changing the priority of a job, leading to an application failure and loss of functionality until the system is restarted. It is not relevant if you choose positive or negative priority (niceness).

___

<img width="1853" height="723" alt="Image" src="https://github.com/user-attachments/assets/9a1ebad8-d0c8-4a14-ab47-457fdebdd4fd" />

---

## #3338: Potential unintended insertion into fileIdsMapReverse via operator[]

I noticed that ***_fileIdsMapReverse[fileName]_*** uses operator[]

In case ***fileName*** is unexpectedly missing or invalid, operator[] will create a default entry into hashMap

Would it be safer to use find() and a simple check before operator?

<img width="763" height="595" alt="Image" src="https://github.com/user-attachments/assets/263267d2-91ff-4686-86ae-00ba71c49e09" />

---

## #3337: [FIXME] Automate agent execution during Decision Import to improve workflow

**Description**
While auditing the DecisionImporterDataCreator.php file, I identified a FIXME at line 297 that currently limits the automation of the decision import process.

**Current Problem**
The createCopyrightData method (and similar methods for ECC/IPRA) throws an UnexpectedValueException if the respective agent's ARS table does not exist on the server. This results in a hard stop for the user, requiring them to manually trigger a scan for that agent before they can proceed with importing decisions.

**Proposed Solution**
To create a more seamless and autonomous workflow, I propose refactoring this check to automatically schedule the missing agent scan.

Instead of throwing an exception, the system should:

1.Verify if the agent scan is missing.

2.Automatically invoke the createCxJobs() method to schedule the required scan in the background.

3.Allow the import process to continue or provide a status update that the dependency is being handled automatically.

**Technical Impact**
Automation: Reduces the need for manual user intervention during data migration/import.

Stability: Replaces a "blocking" error with a proactive background task.

I am familiar with the agent orchestration and DAO layers from my previous contributions to ClearingDao.php (#3284) and the SQLite driver (#3260). I would like to implement this fix.

@shaheemazmalmmd @Kaushl2208 @its-sushant @GMishx

---

## #3295: Automating Auditor Decisions: Integrating User-Defined License Policies into FOSSology’s Modern UI

While setting up FOSSology and running a few test scans on some common npm packages, I realized that the tool is incredibly powerful at finding licenses, but the actual clearing process felt very manual. Currently, FOSSology treats every license hit with the same visual priority. For a legal auditor, this means constant context-switching between the FOSSology UI and their own internal spreadsheet of 'Allowed vs. Banned' licenses."

The Proposal: I want to bridge this gap by introducing a Policy-Aware Workflow. The goal isn't to change how Nomos or Monk detect licenses, but to change how those results are presented to the human auditor.

I propose adding a lightweight Policy Management module where admins can categorize licenses (e.g., Approved, Restricted, Banned). This category would then 'bubble up' into the new React-based Clearing UI—flagging policy violations in real-time as the auditor browses the file tree.

The Implementation Plan: 
Since the project is moving toward a modern stack, I plan to implement this using:
API v2: Extending the REST API to handle policy CRUD operations.
React Frontend: Adding a 'Policy Overlay' to the Clearing View. Instead of just showing the license name, we can use color-coding (Red/Yellow/Green) or badges to indicate policy alignment.
Database: A simple mapping table in PostgreSQL to store user-defined license ranks.

Please do give me a heads up if you feel that this would improve the auditor experience.

---

## #3285: chore: Cleaning and Resolving upgrades for new OS versions

Debian Bullseye has long passed the EOL timeline. FOSSology needs to upgrade the dependencies according to the OS that we support or will come in future. We need to resolve this step by step so we should not loose progress and break builds.

As notified by one of the user `easyrdf/easyrdf` has issues with the `PHP 8.4.16` which is the current version of PHP available in Debian Trixie`stable` (which fossology has extended support to), The org has gone stale and there has been no releases since 2020. The alternative: `sweetrdf/easyrdf` is there for replacing.

Below is the Higher level Task list for completing the task:

- [x] We should drop the debian & ubuntu flavours which has crossed their EOL, Drop them from build, Release stages, Test Stage(if present)
- [ ] We should then update the php version according to least required by the supported OS(Debian & Ubuntu).
- [ ] Update the `build-test` stage with the updated PHP version testing
- [ ] Then `easyrdf/easyrdf` package should be updated to -->  `sweetrdf/easyrdf` with the test cases for the new package and required changes in the code (if any)
- [ ] Upgrade symfony packages linked with the version upgrade.


This issue is linked with a close PR and discussion with the contributor. PR: #3279

---

## #3281: High Severity SQL Injection in Tag Creation (ui-tags.php)

# Security Advisory: SQL Injection Vulnerability in FOSSology Tagging System

## 1. Vulnerability Overview
A **High-Risk SQL Injection** vulnerability was discovered in the tagging system of the FOSSology web interface. The vulnerability allows an authenticated user to execute arbitrary SQL commands, leak sensitive database information, and potentially cause data loss via stacked queries.

## 2. Technical Details

### 2.1 Vulnerable Code
- **File:** `src/www/ui/ui-tags.php`
- **Function:** `CreateTag($tag_array)`
- **Vulnerable Lines (83-85):**
  ```php
  $sql = "SELECT * FROM tag WHERE tag = '$tag_name'";
  $result = pg_query($PG_CONN, $sql);
  ```

### 2.2 Root Cause
The code uses manual string concatenation to build SQL queries. The `$tag_name` variable is retrieved from the user's input stream but is not properly sanitized or parameterized before being passed to `pg_query()`. 

Additionally, the use of `pg_query()` in this context permits **Stacked Queries** (multiple SQL statements separated by a semicolon), significantly increasing the exploit impact.

## 3. Proof of Concept (PoC)

### 3.1 Verification of Execution (Error-Based)
Entering the following payload into the "Tag Name" field triggers a database error, proving the text is executed:
- **Payload:** `' OR 1=(SELECT 1/0) --`
- **Result:** `ERROR: division by zero`

### 3.2 Data Extraction (Database Reconnaissance)
An attacker can extract the database version and system usernames:
- **Payload:** `' OR 1=CAST((SELECT version()) AS INT) --`
- **Result:** Leaks the exact PostgreSQL version string in the error message.

### 3.3 Stacked Query Attack (Data Destruction)
An attacker can attempt to delete system tables:
- **Payload:** `' ; DROP TABLE tag_file; --`
- **Result:** The system attempted to drop the table, failing only due to foreign key constraints.

---

## 4. Proposed Fix (Security Hardening)

### 4.1 Implementation Strategy
The fix involves migrating the legacy `pg_query()` calls to the modern FOSSology `DbManager` using **Parameterized Queries**.

#### Step 1: Update Class Constructor
In `src/www/ui/ui-tags.php`, inject the `DbManager` service:
```php
class ui_tag extends FO_Plugin
{
  private $dbManager;

  function __construct() {
    // ...
    $this->dbManager = $GLOBALS['container']->get('db.manager');
  }
}
```

#### Step 2: Replace Vulnerable Queries
Replace the concatenation logic with placeholders:
```php
// OLD (Vulnerable)
$sql = "SELECT * FROM tag WHERE tag = '$tag_name'";
$result = pg_query($PG_CONN, $sql);

// NEW (Secure)
$sql = "SELECT * FROM tag WHERE tag = $1";
$params = array($tag_name);
$tagRow = $this->dbManager->getSingleRow($sql, $params, __METHOD__ . ".checkTag");
```

## 5. Timeline & Reporting
- **Discovery Date:** 2026-01-29
- **Reporter:** @VineetBenz (GSoC 2026 Aspirant)
- **Status:** Pending Fix Implementation
## 6. Reference
<img width="1596" height="313" alt="Image" src="https://github.com/user-attachments/assets/64c48ec4-ca77-4608-aa2c-7bb92dbe9b2

*[truncated]*

---

## #3218: Fresh Docker setup: White page on Copyright/Email/URL scan – missing copyright_ars table

**Labels:** bug, needs test

### Description
On a fresh Docker setup of Fossology, after uploading a file and completing the scan successfully, navigating to **Copyright / Email / URL** results in a completely white page.

The browser console and backend logs show a critical PostgreSQL error indicating that the table `copyright_ars` does not exist.

### Steps to Reproduce
1. Perform a fresh Docker setup using `docker-compose up -d`
2. Open the Fossology web UI
3. Upload a input From File
4. Run a scan with **copyright / email / url**
5. Go to the **Browse** section and open the uploaded file
6. Click on the **Copyright / Email / URL** tab

### Expected Behavior
The scanned copyright, email, and URL results should be displayed correctly in the UI.

### Actual Behavior
- The page turns completely white after clicking the **Copyright / Email / URL** tab
- The following critical error appears in the backend / browser console:

 relation "copyright_ars" does not exist LINE 1: SELECT * FROM (SELECT agent_pk, agent_name FROM copyright_ar...  

<img width="1891" height="1052" alt="Image" src="https://github.com/user-attachments/assets/b9e6009f-ab62-4735-80b1-4b859fd06e50" />

---

## #3204: Scancode scan big tar ball file would consume huge memory - without params --max-in-memory=-1

**Labels:** bug, needs clarification

When start scan big file(5-6GB) which took very long time on scancode agent working and consume huge memory.

Totla 27GB memory used for the processing. Also the docker container consume 80GB memory(memory+ cache file)

```
:/home/fossy/fossology# docker stats fossy --no-stream
CONTAINER ID   NAME      CPU %     MEM USAGE / LIMIT     MEM %     NET I/O         BLOCK I/O        PIDS
cbf262291319   fossy     198.88%   80.24GiB / 251.6GiB   31.90%    27.5GB / 14GB   44.2GB / 734GB   22


fossy    3530134  0.0  0.2 584540 536896 ?       S    Dec24   0:23 /usr/local/etc/fossology/mods-enabled/scancode/agent/scancode --jobId=171 --config=/usr/local/etc/fossology --userID=3 --groupID=3 --scheduler_start -l
fossy    3530135  0.0  0.0   2584   924 ?        S    Dec24   0:00 sh -c PYTHONPATH='/home/fossy/pythondeps/' python3 runscanonfiles.py -l -m 50 /tmp/filemkqFAc /tmp/filebK6eJG
fossy    3530136 99.9 11.0 29147348 29102196 ?   R    Dec24 1061:01 python3 runscanonfiles.py -l -m 50 /tmp/filemkqFAc /tmp/filebK6eJG
root     3533024  0.0  0.0   4068  1856 ?        S    06:25   0:00 /usr/sbin/CRON
```

There have max-in-memory option for scanconde cli entrance, but no idea if fossolog runscancodeonfile.py could have this option passed?
https://scancode-toolkit.readthedocs.io/en/stable/cli-reference/core-options.html#max-in-memory-option

---

## #3158: Rename/re-map non spdx complaint licenses created by nomos

**Labels:** bug

Please refer to attached screenshot. 

Nomos agent in fossology is creating some licenses which are non SPDX complaint which needs a Rename/re-map. 

<img width="1897" height="498" alt="Image" src="https://github.com/user-attachments/assets/aa5ed10c-6fc1-415b-abc7-39a479de7d24" />

---

## #3139: Enhancement: Validate license identifiers and expressions for SPDX exports

**Labels:** enhancement

For many FOSSology installations it is a very common situation, that not all licenses do have a valid SPDX identifier set in the database. This specifically applies to license candidates. In these cases the shortname is converted by convertToSpdxId() when doing an SPDX export. The function adds a LicenseRef- prefix and converts '+' to '-or-later'. Apart from these changes the license name is not touched. This can result in invalid license IDs (such as LicenseRef-fossology-Public-Domain(c) or license IDs containing '_') and will make validation of the generated SPDX report fail.

To catch this type of error early and support people in maintaining their license database it would be very beneficial to have a (optional) validation connected to the SPDX export. This will help to fix issues with invalid SPDX license IDs before a generated document is being distributed.

@OliverFendt @shaheemazmalmmd @GMishx

---

## #3129: [BUG] Upload fails with "chown failed" on NFSv4 volume, even with no_root_squash and 777 permissions

**Labels:** bug

### Environment:

- Fossology official Docker image (version: latest)
- Deployment via Docker Swarm managed by Portainer.
- Volumes for /srv/fossology/repository and /srv/fossology/uploads are on an NFSv4 share.

### Problem:
The wget_agent fails during file upload with the error ERROR ... chown failed on /srv/fossology/uploads/..., error: Operation not permitted, followed by a FATAL ... Failed to import ... error.

### Troubleshooting Steps Taken:

- Confirmed no_root_squash is set on the NFS server export for the Docker Swarm nodes.
- Configured the Apache process inside the container to run as the same user as the backend agent (fossy) using APACHE_RUN_USER.
- Attempted to force correct ownership by using uid and gid options in the Docker volume's NFS driver options, matching the UID/GID of the fossy user on the NFS server.
- Set the target uploads directory permissions to 777 (drwxrwxrwx) on the NFS server itself.
- The chown failed error persists in all cases.

### Conclusion:
The hard-coded chown call in wget_agent.c (around line 118) appears to be incompatible with standard NFSv4 security configurations, as the operation is denied by the NFS server regardless of client-side user alignment or filesystem permissions. This prevents the use of Fossology with NFS volumes in a Docker Swarm environment.

---

## #3118: FOSSology didn't find licenses for installed R library or container image

Please correct me if I have understood something wrong. I am interested in analyzing a repository based mainly on R language. I tested the FOSSology at [https://fossology.osuosl.org/](https://fossology.osuosl.org/). I analyzed some files in a test project, the script.R containing:

`library(ggplot2)`

The Containerfile containing:

```
FROM rocker/r-ver:4.4.1

RUN R --slave -e 'remotes::install_version("nloptr", version = "2.1.1", repos = "https://ftp.acc.umu.se/mirror/CRAN/")'

RUN R --slave -e 'remotes::install_version("ggplot2", version = "3.5.1", repos = "https://ftp.acc.umu.se/mirror/CRAN/")'
```
And a parallelize.sh containing:

```
#!/bin/bash
#SBATCH --output=array_%A_%a.out
#SBATCH --mem=1G
#SBATCH --time=1-00:00:00

singularity exec --cleanenv --env TMP="/home/dir" --bind ./temp_data:/home/dir image.sif Rscript /home/dir/script.R ${SLURM_ARRAY_TASK_ID}
```

Despite selecting all the options under the "Select optional analysis" and "ScanCode Toolkit", the FOSSology scan was able to find only one MIT license while pointing to the script.R. The interface didn't emphasize the `library(ggplot2)` with gray as "license relevant text", but I believe it noticed the ggplot2's MIT license: [https://ggplot2.tidyverse.org/LICENSE.html](https://ggplot2.tidyverse.org/LICENSE.html). The FOSSology analysis didn't notice the installed `nloptr` R package defined in the Containerfile with LGPL 3 or higher: [https://cran.r-project.org/web/packages/nloptr/index.html](https://cran.r-project.org/web/packages/nloptr/index.html). Furthermore, the `rocker/r-ver:4.4.1` image is said to be lincensed under the GPL2 or newer, it wasn't spotted either: [https://rocker-project.org/](https://rocker-project.org/). And should the `singularity`* call also raise license findings, possibly also the `#SBATCH`*? Oh, and `remotes` package wasn't found either, used to install the other packages in the Containerfile (MIT + file LICENSE): [https://cran.r-project.org/web/packages/remotes/index.html](https://cran.r-project.org/web/packages/remotes/index.html)

Did I do something wrong, or should these kinds of license matters also be found by the FOSSology analysis? If should, it would be great to get it working. Also noticing the specific versions of the installed R packages and container images, if the licenses do not happen to match with the latest versions.

*Edit: I think the `singularity` or `#SBATCH` should not cause license findings, as these are separate programs called by using the standard commands. Reference: [https://softwareengineering.stackexchange.com/questions/110380/call-gpl-software-from-non-gpl-software ](https://softwareengineering.stackexchange.com/questions/110380/call-gpl-software-from-non-gpl-software )

---

## #3109: scanoss agent gets killed by segmentation fault

**Labels:** bug

## Problem Description
The SCANOSS agent consistently crashes with a general protection fault (error 4 in libcrypto.so.3) when executed by the FOSSology scheduler. The same files process successfully when the agent is executed directly from the command line.

## Environment
- **FOSSology Version**: 4.5.1.105
- **SCANOSS Agent Paths**: 
  - `/usr/local/share/fossology/scanoss/agent/scanoss` (installed)
  - `/usr/src/fossology/build/src/scanoss/agent/scanoss` (build directory)
- **Operating System**: Linux 6.1.0-37-cloud-amd64
- **Architecture**: x86_64
- **Distribution**: Debian 12
- **OpenSSL Version**: libcrypto.so.3
- **libcurl Version**: libcurl.so.4

## Reproducible Test Case

### Source Packages That Trigger the Crash
**Package that CRASHES in scheduler context:**
- **Package**: haveged version 1.9.14
- **File**: `haveged_1.9.14.orig.tar.gz`
- **URL**: http://deb.debian.org/debian/pool/main/h/haveged/haveged_1.9.14.orig.tar.gz
- **Size**: 496,346 bytes
- **MD5**: `f756474201bec9a46b41e8712f79468a`
- **Status**: Confirmed to cause segmentation fault when processed via FOSSology scheduler. Processes successfully with CLI. 

**Package that WORKS correctly:**
- **Package**: haveged debian patches 1.9.14-1
- **File**: `haveged_1.9.14-1.debian.tar.xz`
- **URL**: http://deb.debian.org/debian/pool/main/h/haveged/haveged_1.9.14-1.debian.tar.xz
- **Size**: 11,592 bytes
- **MD5**: `1ae254ce2353e3f5f80d9e0cde5ce70e`
- **Status**: Processes successfully in both CLI and scheduler context

### Direct Command Line Execution (SUCCESSFUL)
```bash
# Download test files
wget http://deb.debian.org/debian/pool/main/h/haveged/haveged_1.9.14.orig.tar.gz
wget http://deb.debian.org/debian/pool/main/h/haveged/haveged_1.9.14-1.debian.tar.xz

# Test with SCANOSS agent (works multiple times without crash in CLI)
/usr/local/share/fossology/scanoss/agent/scanoss -C haveged_1.9.14.orig.tar.gz

# Expected output:
100% matched with purls: pkg:github/vcborn/vclinux,
Writing results to /tmp/scanoss/XXXXXXXXX/result.json...
```


### FOSSology Scheduler Execution (CRASHES)
When the haveged_1.9.14.orig.tar.gz is processed through FOSSology scheduler using UI or REST API, the process crashes consistently:

**Latest crash example (Job ID: 153181, Aug 13 2025):**
```
2025-08-13 10:57:06 scanoss [0] :: JOB[153181].scanoss[3300849.localhost]: "Writing results to /tmp/scanoss/11005/results.csv..."
2025-08-13 10:57:06 scanoss [0] :: JOB[153181].scanoss[3300849.localhost]: "Searching /tmp/scanoss/11005 for files to fingerprint..."
2025-08-13 10:57:09 scanoss [0] :: JOB[153181].scanoss[3300849.localhost]: agent was killed by signal: 11.Segmentation fault
```

**Previous kernel crash (Job ID: 153166):**
```
kernel: scanoss[1414159]: segfault at 7f8100000019 ip 00007f9de6cc5fe0 sp 00007ffe866b69a8 error 4 in libcrypto.so.3[7f9de6a58000+2f8000] likely on CPU 23
```

---

## #3106: Declaring a license with custom text as main license

# Description
When declaring a license with a custom text as main license, the main license is not reflected correctly, neither in the UI, nor in the reports:

<img width="1108" height="149" alt="Image" src="https://github.com/user-attachments/assets/ce9a799d-2f7a-4bd6-9572-07c33ba7c5d4" />

The example above sets a custom text for a finding with the BSD-2-Clause license, which is being marked as the main license. In the corresponding SPDX2 TV export the main license is then stated as follows:
```
PackageLicenseConcluded: BSD-2-Clause
PackageLicenseDeclared: BSD-2-Clause
```
whereas the finding for the cleared file does refer correctly to the individual license:
```
LicenseConcluded: LicenseRef-fossology-BSD-2-Clause-a74867c030bca5bfabe0ab283782f619
```
The UI states the main license as follows for this example:

<img width="265" height="112" alt="Image" src="https://github.com/user-attachments/assets/17c45fa6-b8d5-4889-a6b0-1863ab512ee4" />

# Problem
The current implementation for setting a main license does not take licenses with a custom text into account. Instead of the individual license the "generic license" is set as the main license (which is not correct).

As always, please let me know if I can support with any further information.

---

## #3103: The "Edit Decisions" action does not affect files without a detected license.

### Description

When marking folders or files as "Irrelevant" "Do not use" or "Non-Functional" using the "Edit Decisions" action, they are ignored.
Therefore, the copyright entries contained in the affected files are not deactivated.

### Testet with

FreeRTOS V11.1.0 (https://github.com/FreeRTOS/FreeRTOS-Kernel/releases/tag/V11.1.0)
- folder: FreeRTOS-Kernel-11.1.0/portable/ThirdParty/xClang/XCOREAI

### How to reproduce

- Select a directory containing one or more files without a license found. At least one file must have a copyright entry without having a license.
(e.g., FreeRTOS V11.1.0 /portable/ThirdParty/xClang/XCOREAI)

- Check the copyright holders of the directory.
  - Copyright holders are active

- Check the clearing status of the file with the copyright entry.
  - Nothing is selected under "Clearing decision type"

- Select all files in the directory and set them to "Irrelevant," "Do not use," or "Non-Functional" using the "Edit Decisions" action.

- Check the copyright holders of the directory.
  - Copyright holders are active but should be deactivated.

- Check the clearing status of the file with the copyright entry.
  - Under "Clearing decision type" nothing is selected, but "Irrelevant" should be selected

- Check the file's clearing history.
  - No entry exists, but an "Irrelevant" entry should exist


### Screenshots

- Select a directory containing one or more files without a license found. At least one file must have a copyright entry without having a license.
(e.g., FreeRTOS V11.1.0 /portable/ThirdParty/xClang/XCOREAI)
<img width="486" height="232" alt="Image" src="https://github.com/user-attachments/assets/1a7fdf36-274f-42b1-8e58-05033bf408d2" />

- Check the copyright holders of the directory.
  - Copyright holders are active 
<img width="300" height="389" alt="Image" src="https://github.com/user-attachments/assets/d65dd821-e264-477c-8567-53a982090c27" />

- Check the clearing status of the file with the copyright entry.
  - Nothing is selected under "Clearing decision type"
<img width="499" height="206" alt="Image" src="https://github.com/user-attachments/assets/e75c627d-5d10-46b0-8922-8d758928f85a" />

- Select all files in the directory and set them to "Irrelevant," "Do not use," or "Non-Functional" using the "Edit Decisions" action.
<img width="477" height="167" alt="Image" src="https://github.com/user-attachments/assets/d5706ac1-b850-49fb-bf9c-30e28593a63a" />
<img width="200" height="66" alt="Image" src="https://github.com/user-attachments/assets/a55bce7d-1871-48d9-bc0a-335fbef018e4" />

- Check the copyright holders of the directory.
  - Copyright holders are active but should be deactivated.
<img width="300" height="389" alt="Image" src="https://github.com/user-attachments/assets/bf6d2949-17e3-4ff3-be28-8c007321b9cc" />

- Check the clearing status of the file with the copyright entry.
  - Under "Clearing decision type" nothing is selected, but "Irrelevant" should be selected
<img width="132" height="111" alt="Im

*[truncated]*

---

## #3082: Fossology has issues with OSS that contains a lot of archives in the code

**Labels:** bug, question

I tried to upload an OSS named hwloc from https://www.open-mpi.org/software/hwloc/v2.9/downloads/hwloc-2.9.3.tar.bz2 to my fossology server(4.5.1) running in container. The Fossology container keeps crashing after restarting. I found a lot of errors during ununpack  as the following. It seems that Fossology has issues with OSS that contains a lot of archives in the code. 
`2025-06-26 08:05:02 ununpack [0] :: JOB[237].ununpack[210.localhost]: "ERROR: /srv/fossology/repository/d6791c535dd6/ununpack/850995l/5c884bf8d4113cdcfd2887a6420a408f3b3570fb.84fa3067e97b2ca213debc3352cabbb3.5306064.dir/spdx_temp/hwloc-2.9.3/utils/hwloc/test-hwloc-dump-hwdata/knl-snc4h50.tar.bz2.dir/knl-snc4h50.tar.dir/knl-snc4h50/sys/firmware/dmi/entries/160-0/raw"
2025-06-26 08:05:02 ununpack [0] :: JOB[237].ununpack[210.localhost]: "Can not open the file as archive"
2025-06-26 08:05:02 ununpack [0] :: JOB[237].ununpack[210.localhost]: "ERROR: /srv/fossology/repository/d6791c535dd6/ununpack/850995l/5c884bf8d4113cdcfd2887a6420a408f3b3570fb.84fa3067e97b2ca213debc3352cabbb3.5306064.dir/spdx_temp/hwloc-2.9.3/utils/hwloc/test-hwloc-dump-hwdata/knl-snc4h50.tar.bz2.dir/knl-snc4h50.tar.dir/knl-snc4h50/sys/firmware/dmi/entries/14-0/raw"
2025-06-26 08:05:02 ununpack [0] :: JOB[237].ununpack[210.localhost]: "Can not open the file as archive"
2025-06-26 08:05:02 ununpack [0] :: JOB[237].ununpack[210.localhost]: "ERROR: /srv/fossology/repository/d6791c535dd6/ununpack/850995l/5c884bf8d4113cdcfd2887a6420a408f3b3570fb.84fa3067e97b2ca213debc3352cabbb3.5306064.dir/spdx_temp/hwloc-2.9.3/utils/hwloc/test-hwloc-dump-hwdata/knl-snc4h50.tar.bz2.dir/knl-snc4h50.tar.dir/knl-snc4h50/sys/firmware/dmi/entries/161-0/raw"
2025-06-26 08:05:02 ununpack [0] :: JOB[237].ununpack[210.localhost]: "Can not open the file as archive"
2025-06-26 08:05:04 ununpack [0] :: JOB[237].ununpack[210.localhost]: "ERROR: /srv/fossology/repository/d6791c535dd6/ununpack/850995l/5c884bf8d4113cdcfd2887a6420a408f3b3570fb.84fa3067e97b2ca213debc3352cabbb3.5306064.dir/spdx_temp/hwloc-2.9.3/tests/hwloc/x86+linux/64amd64-4p2n4ca2co.tar.bz2.dir/64amd64-4p2n4ca2co.tar.dir/64amd64-4p2n4ca2co/fsroot/sys/devices/virtual/dmi/id/chassis_asset_tag"
2025-06-26 08:05:04 ununpack [0] :: JOB[237].ununpack[210.localhost]: "Can not open the file as archive"
2025-06-26 08:05:04 ununpack [0] :: JOB[237].ununpack[210.localhost]: "ERROR: /srv/fossology/repository/d6791c535dd6/ununpack/850995l/5c884bf8d4113cdcfd2887a6420a408f3b3570fb.84fa3067e97b2ca213debc3352cabbb3.5306064.dir/spdx_temp/hwloc-2.9.3/tests/hwloc/x86+linux/64amd64-4p2n4ca2co.tar.bz2.dir/64amd64-4p2n4ca2co.tar.dir/64amd64-4p2n4ca2co/fsroot/sys/devices/virtual/dmi/id/board_asset_tag"
2025-06-26 08:05:04 ununpack [0] :: JOB[237].ununpack[210.localhost]: "Can not open the file as archive"
2025-06-26 08:05:04 ununpack [0] :: JOB[237].ununpack[210.localhost]: "ERROR: /srv/fossology/repository/d6791c535dd6/ununpack/850995l/5c884bf8d4113cdcfd2887a6420a408f3b3570fb.84fa3067e97b2ca213debc3352cabbb3

*[truncated]*

---

## #3062: Got CRITICAL ERROR while working deciderjob agent

**Labels:** needs clarification

_While using Fossology got CRITICAL ERROR_
2025-05-29 12:51:27 deciderjob [0] :: JOB[7281].deciderjob[74324.localhost]: "PHP Warning:  pg_execute(): Query failed: ERROR:  insert or update on table "clearing_decision" violates foreign key constraint "clearing_decision_pfile_fk_fkey""
2025-05-29 12:51:27 deciderjob [0] :: JOB[7281].deciderjob[74324.localhost]: "DETAIL:  Key (pfile_fk)=(0) is not present in table "pfile". in /usr/local/share/fossology/lib/php/Db/Driver/Postgres.php on line 59"
2025-05-29 12:51:27 deciderjob [0] :: JOB[7281].deciderjob[74324.localhost]: "[2025-05-29T12:51:27.711837+00:00] default.CRITICAL: ERROR:  insert or update on table "clearing_decision" violates foreign key constraint "clearing_decision_pfile_fk_fkey" DETAIL:  Key (pfile_fk)=(0) is not present in table "pfile". [] []"
2025-05-29 12:51:27 deciderjob [0] :: JOB[7281].deciderjob[74324.localhost]: "Caught exception while processing uploadId=409: error executing: Fossology\Lib\Dao\ClearingDao::createDecisionFromEvents: "
2025-05-29 12:51:27 deciderjob [0] :: JOB[7281].deciderjob[74324.localhost]: "INSERT INTO clearing_decision ("
2025-05-29 12:51:27 deciderjob [0] :: JOB[7281].deciderjob[74324.localhost]: "  uploadtree_fk,"
2025-05-29 12:51:27 deciderjob [0] :: JOB[7281].deciderjob[74324.localhost]: "  pfile_fk,"
2025-05-29 12:51:27 deciderjob [0] :: JOB[7281].deciderjob[74324.localhost]: "  user_fk,"
2025-05-29 12:51:27 deciderjob [0] :: JOB[7281].deciderjob[74324.localhost]: "  group_fk,"
2025-05-29 12:51:27 deciderjob [0] :: JOB[7281].deciderjob[74324.localhost]: "  decision_type,"
2025-05-29 12:51:27 deciderjob [0] :: JOB[7281].deciderjob[74324.localhost]: "  scope"
2025-05-29 12:51:27 deciderjob [0] :: JOB[7281].deciderjob[74324.localhost]: ") VALUES ("
2025-05-29 12:51:27 deciderjob [0] :: JOB[7281].deciderjob[74324.localhost]: "  $1,"
2025-05-29 12:51:27 deciderjob [0] :: JOB[7281].deciderjob[74324.localhost]: "  (SELECT pfile_fk FROM uploadtree WHERE uploadtree_pk=$1),"
2025-05-29 12:51:27 deciderjob [0] :: JOB[7281].deciderjob[74324.localhost]: "  $2,"
2025-05-29 12:51:27 deciderjob [0] :: JOB[7281].deciderjob[74324.localhost]: "  $3,"
2025-05-29 12:51:27 deciderjob [0] :: JOB[7281].deciderjob[74324.localhost]: "  $4,"
2025-05-29 12:51:27 deciderjob [0] :: JOB[7281].deciderjob[74324.localhost]: "  $5) RETURNING clearing_decision_pk"
2025-05-29 12:51:27 deciderjob [0] :: JOB[7281].deciderjob[74324.localhost]: "   -- -- Array"
2025-05-29 12:51:27 deciderjob [0] :: JOB[7281].deciderjob[74324.localhost]: "("
2025-05-29 12:51:27 deciderjob [0] :: JOB[7281].deciderjob[74324.localhost]: "    [0] => 1257971"
2025-05-29 12:51:27 deciderjob [0] :: JOB[7281].deciderjob[74324.localhost]: "    [1] => 6"
2025-05-29 12:51:27 deciderjob [0] :: JOB[7281].deciderjob[74324.localhost]: "    [2] => 4"
2025-05-29 12:51:27 deciderjob [0] :: JOB[7281].deciderjob[74324.localhost]: "    [3] => 5"
2025-05-29 12:51:27 deciderjob [0] :: JOB[7281].deciderjob[74324.localhost]: "    [4] =

*[truncated]*

---

## #3051: Data Pipeline For Safaa

**Labels:** enhancement, GSOC-25

### Pipeline
 - [ ] Create Scripts to fetch the copyright data from FOSSology Server copyright table (localhost)
 - [ ] Clean and preprocess fetched copyright data (utilize prewritten processing functions) 
         - Preprocess data should have label and clean text.
 - [ ] Split data for training/validation/test. 
 - [ ] Train false/positive model as well as declutter model (utilize prewritten train functions)
 - [ ] Model evaluation (check for precision, recall etc..)
 - [ ] Model versioning and release.  
 - [ ] Should work for both Gitlab and Github.
       - Manual trigger.
       - Should also have a functionality to work as cron job.
### Others
 - [ ] API needs to be created to fetch required data for based on time stamp for data training.

---

## #3050: Support text phrases and bulk based scanning for MONK a like agent

**Labels:** enhancement, in review, GSOC-25

###  UI
  - [x] Create a UI to accept (text, acknowledgement, comments)
       - Select a license (existing licenses from database)(Multiple).  
       - Add & save text, acknowledgement, comments for selected license. (Validation needed for license text).
       - User should have a option to pull text, acknowledgement, comments & licenses from Bulk data.
          (A license like page can be created where user can view the license text and pull it(to: create text phases page and save.))
       - An option in settings page to also scan for specific users or groups bulk phases along with created ones.
  - [ ] Choice for the user to detect (agent finding) from text phrase scanning file upload & schedule agent.
  - [ ] Choice for user to select the conclude option from agent findings of text phrases to conclude in both pages file upload & schedule agent. 
  - [ ] General UI to manage all the Text phrases for a specific license.
      - For a selected license show all the text phrases in UI to manage (edit, deactivate and delete).
### Backend 
  - [ ] Monk a like agent should be developed to scan and detect & stamp this text phrases a agent finding.
  - [ ] Conclusions from text phrase agent findings should be made using decider 
  - [ ] Provide the testcases for both agent and decider.
  - [ ] All the relevant API'S needs to be provided for automation.
### Documentation
  - [ ] Create a detailed documentation for users and developers. 

- Assigned-to : @harshitg927

---

## #3041: feat/API: missing patchUploadbyId method in API (corresponding to organize -> uploads -> edit properties)

**Labels:** enhancement

in REST API V2 https://github.com/fossology/fossology/blob/master/src/www/ui/api/documentation/openapiv2.yaml the following methods are currently implemented within the "Organize" category/tag:

- createFolder
- deleteFolderById
- moveFolderById
- patchFolderById -> change name and description of a folder, not of an upload
- createGroup

- deleteUploadById
- moveUploadById
- updateUploadById -> change upload status and assignee, not name and description

A patchUploadbyId method is missing, that should allow to change name and description of an upload via API

---

## #3032: scheduler: agents get killed if ldap authentication is active

**Labels:** bug

With ldap authentication activated like in the manual a lot of error messages occur when starting the scheduler:

```
2025-04-10 12:33:01 scheduler [9] :: NOTE: *****************************************************************                                                                                                                              │
│ 2025-04-10 12:33:01 scheduler [9] :: NOTE: ***                FOSSology scheduler started                ***                                                                                                                              │
│ 2025-04-10 12:33:01 scheduler [9] :: NOTE: ***        pid:      9                                        ***                                                                                                                              │
│ 2025-04-10 12:33:01 scheduler [9] :: NOTE: ***        verbose:  3                                        ***                                                                                                                              │
│ 2025-04-10 12:33:01 scheduler [9] :: NOTE: ***        config:   /usr/local/etc/fossology                 ***                                                                                                                              │
│ 2025-04-10 12:33:01 scheduler [9] :: NOTE: *****************************************************************                                                                                                                              │
│ 2025-04-10 12:33:01 scheduler [9] :: JOB[-7].decider[53.localhost]: agent didn't send version information: "PHP Warning:  Undefined array key "AUTHENTICATE_UID" in /usr/local/share/fossology/lib/php/common-auth.php on line 48"        │
│ 2025-04-10 12:33:01 scheduler [9] :: ERROR /fossology/src/scheduler/agent/agent.c.310: agent localhost.clixml has been invalidated, removing from agents                                                                                  │
│ 2025-04-10 12:33:01 scheduler [9] :: JOB[-3].clixml[44.localhost]: agent didn't send version information: "PHP Warning:  Undefined array key "AUTHENTICATE_UID" in /usr/local/share/fossology/lib/php/common-auth.php on line 48"         │
│ 2025-04-10 12:33:01 scheduler [9] :: ERROR /fossology/src/scheduler/agent/agent.c.310: agent localhost.deciderjob has been invalidated, removing from agents                                                                              │
│ 2025-04-10 12:33:01 scheduler [9] :: JOB[-8].deciderjob[56.localhost]: agent didn't send version information: "PHP Warning:  Undefined array key "AUTHENTICATE_UID" in /usr/local/share/fossology/lib/php/common-auth.php on line 48"     │
│ 2025-04-10 12:33:01 scheduler [9] :: JOB[-7].decider[53.localhost]: agent was killed by signal: 9.Killed                                                                                                                                  │
│ 2025-04-10 12:33:01 schedu

*[truncated]*

---

## #3025: Improvement (reportImport): Handling of new / unknown licenses with custom text

**Labels:** bug, in review

# Description
## Background
With the [OSSelot project](https://www.osselot.org) we stumbled accross a use-case for which see some possible improvements for the import of SPDX reports.  The situation is as follows: In some specific cases contributors create a license as a "placeholder". These licenses are only being used with a custom text. One example is "Permission-Notice" which is being used to mark findings with individual permission notices. The related text is always individual and is set by the contributor as a custom text during the clearing process.

## Scenario
Users of the generated SPDX reports obviously don't have that custom license in their database. Usually new licenses are created during the import process. But new licenses (or candidates) are only created for findings without a custom  text. For findings with a custom text the import code expects the license to be existent and only adds the extracted custom text to the existing license. This is the relevant code for importing SPDX2 reports:

Custom text:

```php
      if ($license->isA('spdx:ExtractedLicensingInfo') &&
        (strlen($licenseId) > 33 &&
          substr($licenseId, -33, 1) === "-" &&
          ctype_alnum(substr($licenseId, -32))
        )) {
        $licenseId = substr($licenseId, 0, -33);
        $item = new ReportImportDataItem($licenseId);
        $item->setCustomText($licenseTextLiteral->getValue());
```

No custom text:

```php
      } else {
        $item = new ReportImportDataItem($licenseId);
        $item->setLicenseCandidate($licenseNameLiteral->getValue(),
          $licenseTextLiteral->getValue(),
          strpos($rawLicenseId, LicenseRef::SPDXREF_PREFIX),
          ($seeAlsoLiteral != null) ? $seeAlsoLiteral->getValue() : ""
        );
      }
```

For the previously described use-case ("Permission-Notice") there are only findings with custom text in the report, which prevents the license from being created and the related findings will silently be ignored, resulting in missing clearing decisions (which are present in the imported report).

## Reproducing the scenario
1. Download the [SPDX2 RDF report for busybox-1.36.1](https://raw.githubusercontent.com/Open-Source-Compliance/package-analysis/refs/heads/main/analysed-packages/busybox/version-1.36.1/busybox-1.36.1.spdx.rdf.xml) from the OSSelot project
2. Upload [busybox-1.36.1.tar.bz2](https://busybox.net/downloads/busybox-1.36.1.tar.bz2) to your FOSSology instance (without running any agents)
3. Import the previously (in step 1) downloaded RDF file for this upload
4. Navigate to busybox-1.36.1/editors/ed.c (which won't show any finding)

The RDF report contains the following entry for busybox-1.36.1/editors/ed.c

```xml
[...]
    <spdx:fileName>busybox-1.36.1.tar.bz2/busybox-1.36.1.tar/busybox-1.36.1/editors/ed.c</spdx:fileName>
     <spdx:checksum>
       <spdx:Checksum>
         <spdx:algorithm rdf:resource="http://spdx.org/rdf/terms#checksumAlgorithm_md5"/>
         <spdx:checksumValue>e0d3de

*[truncated]*

---

## #3002: Bug: Unable to clear upload description and comment

**Labels:** bug, good first issue

## Description
When attempting to clear the upload description and comment fields, they remain populated instead of resetting to an empty state. This issue occurs even after manually deleting the text.

## Steps to Reproduce

### Upload Description
- Navigate to `Organize` -> `Uploads` -> `Edit Properties`.
- Attempt to clear the text in the Upload Description field and click on `Edit` button.
- Observe that the Description retains the previous text instead of being cleared.

### Upload Comment
- Navigate to `Browse` tab.
- Locate an upload and double-click on the Comment cell to edit it.
- Clear the text in the Comment modal.
- Click `OK` to save the changes.
- Observe that the Comment field retains the previous text instead of being cleared.

## Expected Behavior
The upload description and comment fields should reset to an empty state when cleared manually.

## Actual Behavior
The fields retain the previously entered text, preventing users from properly resetting them.

### Reference

https://github.com/user-attachments/assets/f7aad499-e3f4-4c29-9b29-490b84dfe1d5

https://github.com/user-attachments/assets/ae442892-0797-4b36-8201-01b2430c1969

---

## #2945: SSO Login Redirects to HTTP Instead of HTTPS

**Description**

We have configured Azure SSO for Single sign-On, and the Microsoft login is using HTTP instead of HTTPS. We have checked the redirect URL and verified that all configurations explicitly use HTTPS, but the authentication flow still redirects to HTTP unexpectedly.
 
**How to Reproduce**

1. Configure Azure SSO for FOSSology authentication.

2. Set the redirect URL to use HTTPS.

3. Attempt to log in using Microsoft credentials.

4. Observe that the login redirection unexpectedly uses HTTP from inspect mode (network) mode.(Attached screenshot for more details)

![Image](https://github.com/user-attachments/assets/54a86ecf-2b8b-465d-9c79-8afe94b71af9)

**Expected Behavior**

The login flow should consistently use HTTPS instead of HTTP.
 
**Version**

FOSSology Version: 4.4.0
Deployment: Docker Swarm. We are using traefik as a reverse proxy in our docker swarm cluster.

We started facing this difficulty once our machine's port 80 was blocked.
If anyone is using Azure SSO for single sign-on, could you please check in the inspect/developer mode whether the request is passing over HTTP and let us know?

Thanks in Advance!

---

## #2853: Enhancement: Reporting

**Labels:** enhancement

<!-- SPDX-FileCopyrightText: © Fossology contributors

     SPDX-License-Identifier: GPL-2.0-only
-->

<!-- Before filling this issue, please read the Wiki (https://github.com/fossology/fossology/wiki)
and search if the bug do not already exists in the issues (https://github.com/fossology/fossology/issues). -->

### Description

Reports 
a. More reports which do not include files marked as irrelevant into the reports, or allow the user to make a selection to include/exclude irrelevant files for all reports

---

## #2852: Enhancement: UI Improvements

**Labels:** enhancement

<!-- SPDX-FileCopyrightText: © Fossology contributors

     SPDX-License-Identifier: GPL-2.0-only
-->

<!-- Before filling this issue, please read the Wiki (https://github.com/fossology/fossology/wiki)
and search if the bug do not already exists in the issues (https://github.com/fossology/fossology/issues). -->

### Description

UI Improvements 
a. It should be possible to highlight and cycle through individual evidence found in file. E.g. cycle through all copyrights, Emails and URLs, Licenses etc.
b. Introduce support for operations from the context menu.

---

## #2851: Enhancement: Automatic Detection

<!-- SPDX-FileCopyrightText: © Fossology contributors

     SPDX-License-Identifier: GPL-2.0-only
-->

<!-- Before filling this issue, please read the Wiki (https://github.com/fossology/fossology/wiki)
and search if the bug do not already exists in the issues (https://github.com/fossology/fossology/issues). -->

### Description

Automatic detection 
a. The product should be able to detect OSS components based on metadata, e.g. by using pom.xml, package.json, etc.
b. Gauge similarity to open-source component, i.e. 50% similar, 90% similar etc.

---

## #2850: Enhancement: Operations on files and licenses

**Labels:** enhancement

<!-- SPDX-FileCopyrightText: © Fossology contributors

     SPDX-License-Identifier: GPL-2.0-only
-->

<!-- Before filling this issue, please read the Wiki (https://github.com/fossology/fossology/wiki)
and search if the bug do not already exists in the issues (https://github.com/fossology/fossology/issues). -->

### Description

Operations on files 
a. It should be possible to apply multiple filter conditions to files, i.e. filter by various evidence found in them (not just by one type of evidence)
b. It should be possible to disassociate files from licenses in a much more intuitive way and more efficiently. 
c. It should be easier and more intuitive to mark files as irrelevant or identified, e.g. by right clicking on a file or directory.
d. If a file is identified it should be associated with a specific license or set of licenses (even if such license is unknown)

Operations on licenses
a. It should be possible to customise license texts of template licenses (such as MIT, ISC, BSD-family, etc) without having to create a new license-ref and for that we need groups which would contain association of files to a license, component and version (see Nr. 3).

---

## #2849: Enhancement: Copyright can be associated with the license to which it belongs to.

**Labels:** enhancement

<!-- SPDX-FileCopyrightText: © Fossology contributors

     SPDX-License-Identifier: GPL-2.0-only
-->

<!-- Before filling this issue, please read the Wiki (https://github.com/fossology/fossology/wiki)
and search if the bug do not already exists in the issues (https://github.com/fossology/fossology/issues). -->

### Description

Copyright can be associated with the license to which it belongs to.
Currently, we have a list of copyrights and the files where it is found in “Copyright” screen.

---

## #2847: Enhancement: Grouping of files

**Labels:** enhancement

<!-- SPDX-FileCopyrightText: © Fossology contributors

     SPDX-License-Identifier: GPL-2.0-only
-->

<!-- Before filling this issue, please read the Wiki (https://github.com/fossology/fossology/wiki)
and search if the bug do not already exists in the issues (https://github.com/fossology/fossology/issues). -->

### Description

Group multiple files which have the same license and copyright information.
Currently, each file is reported separately.  

Operation on Groups of files 
a. It should be possible to name groups of files, i.e. set name for the group.
b. It should be possible to associate one or more licenses with group of files.
c. Metadata field representing curations notes should be associated with a group of files.
d. Groups of files should have an attribute which would allow them to be present in the reports or not.

---

## #2820: Add integration tests for all functionalities.

**Labels:** enhancement

### Description

As the FOSSology project continues to grow, the complexity of its components and interactions between them increase correspondingly. Ensuring the correct functionality and interaction of these components including databases is critical to embracing and maintaining the project's  reliability. Since the unit test coverage for these models and controllers is almost done , integration test cases can also be added to verify that all functionalities meet the functional requirements and work as expected. 

## Proposed Solution
**Enhance Existing Test Cases**: Improve the current test suite to cover more scenarios and edge cases.
**Add New Test Cases**: Create additional tests to ensure all the integration of all components of the system including databases are effectively working together and  working as expected.

---

## #2817: Concluded GPL and LGPL licenses are not visible.

The GPL and LGPL licenses were identified but still those licenses are not appearing in Concluded licenses. 
For the OSS package, (Example: Coreutils-9.4) GPL 3.0 or later license was concluded and license clearing was done on 4/4/2024. When I tried to reuse the license clearing, noticed the above mention discrepancy.

Have attached the screenshot for your reference.
Image 1: ![image](https://github.com/user-attachments/assets/5089f1a2-f017-4383-a34b-e2f633a26d1b)
Image 1 shows that GPL license is identified and marked as Main License.

Image 2: ![image](https://github.com/user-attachments/assets/f1d7d776-2d2a-4f88-8a07-3cdd5a828154)
Image 2 shows even after clearing the license, GPL is not listed in concluded license.

We are seeing this discrepancy after PostgreSQL upgrade.

Is any other organisation or people facing the same issue? If yes, how did you fix it? Is there any workaround or fixes for this issue.?

Thank you
Adarsh M

---

## #2812: How to enable https for fossology application?

### Description

I am looking to enable https for fossology web application (docker deploy)? Please is there any help/pointers to enable https from http?
Thanks

---

## #2801: Fossology postinstall fails after restarting container

**Labels:** bug

<!-- SPDX-FileCopyrightText: © Fossology contributors

     SPDX-License-Identifier: GPL-2.0-only
-->

<!-- Before filling this issue, please read the Wiki (https://github.com/fossology/fossology/wiki)
and search if the bug do not already exists in the issues (https://github.com/fossology/fossology/issues). -->

### Description

We built a Helm chart deploying Fossology to our cluster. We connect to a external database running in Google Cloud. The `web` process and the `scheduler` process are running in different containers, but in the same Kubernetes pod.

When we first start the deployment, everything works find and the app is reachable. During the first start, the logs also show that the database has been successfully initialized. However, if we restart the Kubernetes Pod (eg. on a node switch or something similar), the `postinstall` fails with the error message below:

```
*** Running postinstall for common actions***
*** Creating user and group ***
NOTE: group 'fossy' already exists, good.
NOTE: user 'fossy' already exists, good.
*** Making sure needed dirs exist with right ownership/permissions ***
*** clearing file cache ***
NOTE: Repository already exists at /srv/fossology/repository
NOTE: Running the PostgreSQL vacuum and analyze command can result in a large database performance improvement.
      We suggest that you either configure postgres to run its autovacuum and autoanalyze daemons, or maintagent -D in a cron job, or run Admin > Maintenance on a regular basis.
      Admin > Dashboard will show you the last time vacuum and analyze have been run.
NOTE: using external DB on host staging-fossology-postgresql.planqk-testing.svc.cluster.local
*** update the database and license_ref table ***
Old release was 
PHP Warning:  pg_query(): Query failed: ERROR:  column "rf_spdx_id" of relation "license_ref" already exists in /usr/local/share/fossology/lib/php/Db/Driver/Postgres.php on line 68
[2024-07-30T17:42:33.984601+00:00] /usr/local/share/fossology/lib/php/libschema.php.CRITICAL: ERROR:  column "rf_spdx_id" of relation "license_ref" already exists ] ]
PHP Fatal error:  Uncaught Fossology\Lib\Exception: error executing: ALTER TABLE "license_ref" ADD COLUMN "rf_spdx_id" text DEFAULT NULL

ERROR:  column "rf_spdx_id" of relation "license_ref" already exists in /usr/local/share/fossology/lib/php/Db/DbManager.php:133
Stack trace:
#0 /usr/local/share/fossology/lib/php/Db/DbManager.php(192): Fossology\Lib\Db\DbManager->checkResult()
#1 /usr/local/share/fossology/lib/php/libschema.php(320): Fossology\Lib\Db\DbManager->queryOnce()
#2 /usr/local/share/fossology/lib/php/libschema.php(170): fo_libschema->applyTables()
#3 /usr/local/lib/fossology/fossinit.php(189): fo_libschema->applySchema()
#4 {main}
  thrown in /usr/local/share/fossology/lib/php/Db/DbManager.php on line 133
```

Do we miss something here? Any help is appreciated.

#### How to reproduce

- Deploy the helm chart to your cluster: [fossolog

*[truncated]*

---

## #2795: nomos notes out of date

### Description

The documentation at https://github.com/fossology/fossology/blob/master/src/nomos/agent/Notes appears to be rather outdated and refers to a non-existent Makefile as well as not having any integration into the remaining code. This does not seem to hold true any more, as some shorts tests have shown that building requires the PostgreSQL headers to be available on the system and running the binaries embedded into the DEB files in the releases section expects some `fossology.conf` file at a hard-coded location. (My goal is similar to #2508, but I am going to limit this issue to the apparently outdated developers notes.)

#### How to reproduce

Clone the repository, `cd src/nomos/agent`, then run `make`. No Makefile will be found.

For the PostgreSQL case: Just run `cmake .` from the directory `src/nomos` without having PostgreSQL installed on your system.

For the `fossology.conf` case: Download one of the provided binary distributions, unpack the DEB file referring to `nomos`, unpack `data.tar.xz` and navigate to the `nomos` binary. Try to run this binary using `./nomos`, which fails even if all shared objects (`ldd nomos`) can be resolved.

### Versions

* Last commit id on master: [ac8b4b8](https://github.com/fossology/fossology/commit/ac8b4b8558aaf3b0610d5322de735071ee6161e5)
* Operating System (lsb_release -a): openSUSE Leap

---

## #2788: Add support of version 2 for all possible controller test cases.

<!-- SPDX-FileCopyrightText: © Fossology contributors

     SPDX-License-Identifier: GPL-2.0-only
-->

<!-- Before filling this issue, please read the Wiki (https://github.com/fossology/fossology/wiki)
and search if the bug do not already exists in the issues (https://github.com/fossology/fossology/issues). -->

### Description

Even though most of the REST APIs have now migrated to version 2, some corresponding test cases have not yet been updated to support both versions. Hence, there is a need to make all possible test cases version-aware, ensuring they are effective and bug-free.

---

## #2763: Add more unit test cases for maintenance & upload tree APIs

<!-- Before filling this issue, please read the Wiki (https://github.com/fossology/fossology/wiki)
and search if the bug do not already exists in the issues (https://github.com/fossology/fossology/issues). -->

### Description

Add more unit test cases for maintenance and upload tree APIs to enhance the coverage.

---

## #2755: Add more unit test cases for upload, group, license and folder APIs.

<!-- Before filling this issue, please read the Wiki (https://github.com/fossology/fossology/wiki)
and search if the bug do not already exists in the issues (https://github.com/fossology/fossology/issues). -->

### Description

Add more unit test cases for upload, group, folder and license APIs to enhance the coverage.

---

## #2733: Docker image build failed while upgrading from bullseye to bookworm

### Description

The Docker image build encountered failure during the upgrade from Bullseye to Bookworm. 

#### How to reproduce

Please make the following modifications to the master branch,

Made the below changes in the following file, https://github.com/fossology/fossology/blob/master/Dockerfile
```
- FROM debian:bullseye-slim as builder
+ FROM debian:bookworm-slim as builder
```
and 
```
- FROM debian:bullseye-slim
+ FROM debian:bookworm-slim
```

### Logs

Error logs:

Bookworm build failure,

```
-- Generating fossdash-publish.py
-- Found CMake 3.25.1. Adding FOSSology packaging configs ...
-- Configuring done
-- Generating done
-- Build files have been written to: /fossology/build
[1/306] Generating changelog for packages...
FAILED: CMakeFiles/changelog /fossology/build/CMakeFiles/changelog 
cd /fossology/build/pack && /usr/bin/cmake -E tar czf changelog.Debian.gz changelog.Debian && /usr/bin/cmake -E tar czf README.md.gz /fossology/README.md
CMake Error: Unable to read from file '../../README.md': Can't lstat ../../README.md
CMake Error: Problem creating tar: README.md.gz
[2/306] Building C object src/lib/c/CMakeFiles/fossology.dir/libfossdb.c.o
[3/306] Building C object src/lib/c/CMakeFiles/fossology.dir/libfossagent.c.o
[4/306] Building C object src/lib/c/CMakeFiles/fossology.dir/libfossscheduler.c.o
[5/306] Building C object src/lib/c/CMakeFiles/fossology.dir/libfossdbmanager.c.o
[6/306] Building C object src/lib/c/CMakeFiles/fossology.dir/libfossrepo.c.o
/fossology/src/lib/c/libfossrepo.c: In function 'fo_RepImport':
/fossology/src/lib/c/libfossrepo.c:876:9: warning: pointer 'Fout' used after 'fclose' [-Wuse-after-free]
  876 |         fo_RepFclose(Fout);
      |         ^~~~~~~~~~~~~~~~~~
/fossology/src/lib/c/libfossrepo.c:875:9: note: call to 'fclose' here
  875 |         fclose(Fout);
      |         ^~~~~~~~~~~~
ninja: build stopped: subcommand failed.
The command '/bin/sh -c cmake -DCMAKE_BUILD_TYPE=MinSizeRel -S. -B./build -G Ninja  && cmake --build ./build --parallel  && cmake --install build' returned a non-zero code: 1
```
**We noticed a discrepancy in the Fossology Jenkins build for Bullseye. Specifically, while the CMake file is being skipped during the build for Bullseye, it is failing during the build for Bookworm,**

**Refer:** Fossology Jenkins build log,
https://productionresultssa6.blob.core.windows.net/actions-results/0755d7cc-2c55-48c4-a9af-27f60824e9ef/workflow-job-run-23dc78bf-9cda-5ff7-2aa2-5aa742c32163/logs/job/job-logs.txt?rsct=text%2Fplain&se=2024-05-06T07%3A00%3A01Z&sig=6NXeGoBCgoZgCPHblmF5iTpjYv%2FnMHDW3laGQzWIS5M%3D&sp=r&spr=https&sr=b&st=2024-05-06T06%3A49%3A56Z&sv=2021-12-02

Bullseye build log,
```
2024-04-24T13:25:29.5905672Z #26 2.794 -- Generating fossdash-publish.py
2024-04-24T13:25:29.5906327Z #26 2.794 -- Installing Db.conf
2024-04-24T13:25:29.5906920Z #26 2.794 -- Installing fossology.conf
2024-04-24T13:25:29.5907558Z #26 2.794 -- Inst

*[truncated]*

---

## #2725: cp2foss does not work from 4.3.0-rc1

<!-- SPDX-FileCopyrightText: © Fossology contributors

     SPDX-License-Identifier: GPL-2.0-only
-->

<!-- Before filling this issue, please read the Wiki (https://github.com/fossology/fossology/wiki)
and search if the bug do not already exists in the issues (https://github.com/fossology/fossology/issues). -->

### Description

Hi 

I have tried some tag versions by using docker image, the cp2foss does not work from v4.3.0-rc1, it works on v4.2.1.


#### How to reproduce

it always reports "invalid user name"
```
$ cp2foss --username fossy --password fossy -d 'test' -A test.tar.gz
invalid user name
```

if write username/password into ~/.fossology.rc, it'll always reports file not exist.
```
$ cp2foss -d 'test' -A test.tar.gz
Note: it seems that what you want to upload ''test.tar.gz'' does not exist.
```

---

## #2700: Scancode copyright findings are ignored in ReadmeOSS, SPDX, REST API; user copyright findings are ignored in REST API

**Labels:** enhancement

<!-- SPDX-FileCopyrightText: © Fossology contributors

     SPDX-License-Identifier: GPL-2.0-only
-->

<!-- Before filling this issue, please read the Wiki (https://github.com/fossology/fossology/wiki)
and search if the bug do not already exists in the issues (https://github.com/fossology/fossology/issues). -->

### Description

Copyright findings by Scancode are visualized in the WebUI but it seems that they are not output anywhere: if one exports ReadmeOSS or SPDX reports, or if one uses the `/uploads/{id}/item/{itemId}/copyrights` endpoint, such findings are not used at all.

This inconsistency is particularly problematic, because - at least for us - the main reason to use Scancode is its better copyright scanner, but if the corresponding results cannot be used anywhere, the Scancode integration becomes mostly useless.

Moreover, user copyright findings are exported in ReadmeOSS and SPDX, but not when using the REST API.

#### How to reproduce

Upload whatever source package, run only the Scancode copyright scanner (or deactivate all findings by Fossology's copyright scanner), check results in the WebUI (Scancode findings should be there) and add some fake user copyright findings.

Generate and check ReadmeOSS and SPDX reports of the upload, and make REST API calls to ``/uploads/{id}/item/{itemId}/copyrights` for files/items that do have scancode copyright findings and user copyright findigs, and check the response.

The expected results would be to see all copyright findings (Fossology's, Scancode's, User's), but this is not the case.

### Versions

* 4.4.0
* Debian 11

### Where's the problem in the code

REST API: `Fossology\UI\Api\Controllers\CopyrightController\getFileCX()`:   dataType "scancode_statement" (which corresponds to the "scancode_copyright" table) is absent

Report generation: (I did not investigate it yet)

---

## #2695: Create User Documentation

**Labels:** Documentation

<!-- SPDX-FileCopyrightText: © Fossology contributors

     SPDX-License-Identifier: GPL-2.0-only
-->

<!-- Before filling this issue, please read the Wiki (https://github.com/fossology/fossology/wiki)
and search if the bug do not already exists in the issues (https://github.com/fossology/fossology/issues). -->

### Description

The User Documentation will created here: https://github.com/fossology/user-docs

---
