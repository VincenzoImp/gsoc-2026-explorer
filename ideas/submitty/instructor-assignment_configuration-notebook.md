# Notebook Assignment Configuration

**Parent:** Submitty — Project Ideas
**Source:** https://submitty.org/instructor/assignment_configuration/notebook
**Scraped:** 2026-02-22T23:28:47.549248

---

Submitty supports construction of mixed instructional and webform
gradeables called *Notebooks*. Notebooks can be used to create
tutorial teaching material interspersed with exercises or web-based
exams. Notebooks support basic markdown text formatting and collect
student input through multiple choice (radio button or multiple
selection checkboxes), single or multi-line short answers, and syntax
highlighted code boxes.

Submitty Notebooks also support url links and the display of images, which is useful for display of complex exam question formatting (e.g., examination questions prepared in LaTeX, Word, or another document formatting software).

# Complete Notebook Examples

Please refer to these complete sample notebook configurations:

-
[Notebook Basic Example](https://github.com/Submitty/Submitty/tree/master/more_autograding_examples/notebook_basic/config)

This example demonstrates markdown formatting, multiple choice (radio button and ‘select all’ checkbox), short answer, embedded images and url links, syntax highlighting for programming languages, automated grading of multiple choice answers, and automated grading of simple programming exercises. -
[Notebook with Time Limit](https://github.com/Submitty/Submitty/tree/master/more_autograding_examples/notebook_time_limit/config)

This example demonstrates enforcement of an exam time limit. The initial access time for the gradeable is recorded. The time difference between initial access and the current submission is monitored. If the instructor-specified time limit is exceeded an autograding point penalty is applied.

*TODO: The time limit example will likely be updated with a built-in autograding validation option in the near future.*

# Notebook Configuration

Notebooks are different from standard file submissions in that a
notebook may contain several different types of inputs or outputs.
The available types of input and outputs are defined by setting the
`type`

and are as follows:

| Label | Value |
|---|---|
| Short answer input | short_answer |
| Multiple choice input | multiple_choice |
| Markdown | markdown |
| Image | image |
| File Submission Area | file_submission |

### Notebook config.json example

*Some of the config fields have been truncated for brevity and not all possible options are shown*

### Short Answer Input

| Filename | |
|---|---|
| field | filename |
| required | true |
| type | string |
| value | Filename where results of submission will be saved. |

| Initial Value | |
|---|---|
| field | initial_value |
| required | false |
| type | string |
| value | A value to pre-populate into short answer box. |

| Programming Language | |
|---|---|
| field | programming_language |
| required | false |
| type | string |
| value | Programming language that will be entered into the short answer box and will be used for syntax highlighting. |
| notes |
|

| Rows | |
|---|---|
| field | rows |
| required | false |
| type | int |
| value | Height of the short answer box in rows. |

### Multiple Choice Input

| Filename | |
|---|---|
| field | filename |
| required | true |
| type | string |
| value | Filename where results of submission will be saved. |

| Choices | |
|---|---|
| field | choices |
| required | true |
| type | array |
| value | An array of javascript objects which describe a value and description for each choice. |
| notes | Each choice should take the form of `{"value": "1", "description": "Choice 1"}` |

| Allow multiple choices | |
|---|---|
| field | allow_multiple |
| required | false |
| default | false |
| type | bool |
| value | true or false |
| notes | If true allows multiple values to be selected, if false only one value may be selected. |

| Allow psuedo-randomization | |
|---|---|
| field | randomize_order |
| required | false |
| default | false |
| type | bool |
| value | true or false |
| notes | If true, choices are psuedo-randomized, i.e for given pair of gradeable and student, order of choices is always same. |

### Markdown

| Markdown | |
|---|---|
| field | markdown_string |
| required | true |
| type | string |
| value | A markdown string to be displayed. |

### Images

| Image | |
|---|---|
| field | image |
| required | true |
| type | string |
| value | The filename of the image to display. |

| Image Height | |
|---|---|
| field | height |
| required | false |
| default | native |
| type | int |
| value | The height in pixels the image should be displayed at. |

| Image Width | |
|---|---|
| field | width |
| required | false |
| default | native |
| type | int |
| value | The width in pixels the image should be displayed at. |

| Accessibility Text | |
|---|---|
| field | alt_text |
| required | false |
| default | “Instructor provided image” |
| type | string |
| value | The image’s alt text |
| notes | When displaying an image you should use this field to describe the contents of the image. Such a description is useful to visually impaired users who may be using screen reading software. |

### Testcase Labels and References

With testcase labels and references it is possible to display feedback messages to students next to items that an autograding submission found incorrect.

To do this first add a `testcase_label`

to a testcase item by creating a label, in this example “problem_1”:

Then using the label you selected earlier, add a `testcase_ref`

to the input/output item where you would like the
feedback message displayed:

### File Submission areas

Notebook gradeables, by default, do not have a file submission area like normal gradeables, however, they can be placed within a notebook through the *file_submission* cell type.

| Directory Name | |
|---|---|
| field | directory |
| required | true |
| type | string |
| value | The name of the directory associated with this submission area |
| notes | When students submit a file to this submission area, the files will be uploaded to this directory |

| Label | |
|---|---|
| field | label |
| required | false |
| type | string |
| value | An optional label to display within a submission area |
| notes | Submission areas will have the label “Drag and drop your label file(s) here or click to open file browser” |
