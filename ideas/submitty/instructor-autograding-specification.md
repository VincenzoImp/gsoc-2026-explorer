# Assignment Autograding Configuration Instructions

**Parent:** Submitty — Project Ideas
**Source:** https://submitty.org/instructor/autograding/specification
**Scraped:** 2026-02-22T23:28:47.549182

---

### Overall Specification of a `config.json`

file

You are allowed to have C/C++ style comments in a `config.json`

file.
These will be removed before compilation of the autograding
executables.

-
**field:**`"testcases"`


**type:***array of testcase objects*([defined below](https://submitty.org#specification-of-a-testcase))

**REQUIRED** -
**field:**`"notebook"`


**type:***array of notebook objects*([notebook docs](https://submitty.org/instructor/assignment_configuration/notebook)) -
**field:**`"assignment_message"`


**type:***string*

**default value:**`""`

-
**field**`"max_submission_size"`


**type:***integer*

**default value:**100000This is the max size in bytes of all files combined for a website submission.

-
**field:**`"grading_parameters"`


**type:***associative array / mapping from string to integer**NOTE: These fields are only used as helper checks summing the total of the test case points.*-
**field:**`"AUTO_POINTS"`


**type:***integer* -
**field:**`"EXTRA_CREDIT_POINTS"`


**type:***integer*

-
-
**field:**`"part_names"`


**type:***array of strings***default value:**empty array -
**field:**`"resource_limits"`


**type:***associative array / mapping from string to integer*The instructor can override / customize various resource limitations for the testing process. The default values for these resource limits are specified here: [grading/default_config.h][grading/default_config.h].

Depending on the testcase type, there is a minimum RLIMIT value that will be used, regardless if the limit it set lower in the configuration file.

If the Testcase is for compilation, it will use the following minimum RLIMIT values:

- RLIMIT_CPU: 60
- RLIMIT_FSIZE: 10MB
- RLIMIT_RSS: 1GB

If the Testcase is using the submitty_count utility, it will have the following minimum RLIMIT values:

- RLIMIT_NPROC: 1000
- RLIMIT_NOFILE: 1000
- RLIMIT_CPU: 60
- RLIMIT_AS: RLIM_INFINITY
- RLIMIT_SIGPENDING: 100

*FIXME: UPDATE & DOCUMENT*These resources can be for the overall assignment configuration, or per test case.

-
**field:**`"required_capabilities"`


**type:***string***default value:**`"default"`

*Helps define what machine this gradeable should run on. Each machine has a certain set of capabilities, so defining this properly will improve grading speed and reduce errors.* -
**field:**`"autograding_method"`


**type:***string***default value:**`"jailed_sandbox"`

*Defines how Submitty will grade this gradeable. Most commonly changed to*`"docker"`

for grading through Docker. -
**field:**`"container options"`


**type:***string***default value:**`"jailed_sandbox"`

*Defines how Submitty will grade this gradeable. Most commonly changed to*`"docker"`

for grading through Docker. -
**field:**`"autograding"`


**type:***associative array / mapping from string to array**These fields define how files are moved through the autograding process.*-
**field:**`"compilation_to_runner"`


**type:***array of strings* -
**field:**`"compilation_to_validation"`


**type:***array of strings* -
**field:**`"submission_to_compilation"`


**type:***array of strings* -
**field:**`"submission_to_runner"`


**type:***array of strings* -
**field:**`"submission_to_validation"`


**type:***array of strings* -
**field:**`"work_to_details"`


**type:***array of strings* -
**field:**`"use_checkout_subdirectory"`


**type:***string*

-
-
**field:**`"container_options"`


**type:***associative array / mapping from string to object*-
**field:**`"container_image"`


**type:***string**Set this field when using Docker grading to specify which image you would like to use for all testcases by default.* -
**field:**`"number_of_ports"`


**type:***integer* -
**field:**`"single_port_per_container"`


**type:***boolean* -
**field:**`"use_router"`


**type:***boolean*

-
-
**field:**`"allow_system_calls"`


**type:***array of strings*The instructor can also override / customize the default restrictions on use of system calls within the student code by allowing additional categories of system calls.


*See also:*[System Call Filtering](https://submitty.org/instructor/autograding/system_call_filtering)

### Specification of a Testcase

-
**field:**`"type"`


**type:***string*

**value:**`"Compilation"`

,`"FileCheck"`

, or`"Execution"`


**default value:**`"Execution"`

*Each test case has a type, the type dictates whether actions are necessary for that test case during the different phases of autograding (compilation, execution, and validation).* -
**field:**`"title"`


**type:***string*

**REQUIRED**for all testcases -
**field:**`"details"`


**type:***string*

**default value:**`""`

-
**field:**`"points"`


**type:***integer*

**default value:**`0`

-
**field:**`"hidden"`


**type:***boolean*

**default value:**`false`

*Students will not know how many points hidden test cases are worth or how many points they recieve for that test case. For similar functionality while still allowing students to see how many points they receive, adjust*`show_message`

,`show_actual`

, and`show_expected`

in validation instead. -
**field:**`"release_hidden_details"`


**type:***boolean*

**default value:**`false`

-
**field:**`"extra_credit"`


**type:***boolean*

**default value:**`false`

-
**field:**`"filename"`


**type:***string*or*array of strings*

**REQUIRED**for`"file_check"`

and`"execution"`

types -
**field:**`"executable_name"`


**type:***string*or*array of strings*

**REQUIRED**for`"compilation"`

testcases*FIXME: Should we rename/collapse this field to filename??* -
**field:**`"command"`


**type:***string*-or-*array of strings*

**REQUIRED**for`"compilation"`

and`"execution"`

testcases. Not allowed for`"file_check"`

testcases.*NOTE: simple wildcards allowed.**NOTE: Each string command should be a LINUX command line that will be executed during either the compilation or execution phases of automated grading.* -
**field:**`"containers"`


**type:***array of objects*

**REQUIRED**for`"compilation"`

and`"execution"`

testcases if not using`"command"`

*Specifies Docker containers for this testcase and what will be run in each of them. Each container is specified by an object with no key that contains the following fields.*-
**field:**`"commands"`


**type:***string*-or-*array of strings* -
**field:**`"container_name"`


**type:***string* -
**field:**`"container_image"`


**type:***string**Set this field when using Docker grading to specify which image you would like to use for a single test case.* -
**field:**`"number_of_ports"`


**type:***integer* -
**field:**`"outgoing_connections"`


**type:***array* -
**field:**`"server"`


**type:***boolean*

-
-
**field:**`"resource_limits"`


**type:***associative array / mapping from string to integer**NOTE: See details for assignment level description above.* -
**field:**`"validation"`


**type:***array of validation objects*(described below)

**default value:**automatic checks added for`STDOUT.txt`

, STDERR.txt, and the execution logfile. -
**field:**`"actions"`


**type:***array of action strings*(described below)

**default value:**`empty`

-
**field:**`"textboxes"`


**type:***array of textbox objects*(Described below)

**default value:**`empty`
