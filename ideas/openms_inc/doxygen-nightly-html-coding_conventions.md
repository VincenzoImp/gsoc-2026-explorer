# https://openms.de/doxygen/nightly/html/coding_conventions.html

**Parent:** OpenMS Inc — Project Ideas
**Source:** https://openms.de/doxygen/nightly/html/coding_conventions.html
**Scraped:** 2026-02-22T23:28:47.594944

---

|
OpenMS
|

Coding Conventions

Use the following code conventions when contributing to [OpenMS](https://openms.de/namespaceOpenMS.html).

[OpenMS](https://openms.de/namespaceOpenMS.html) uses coding conventions that are automatically checked using `cpplint`

(`/src/tests/coding/cpplint.py`

). You can find a configuration file for the `CLion IDE`

here. You can import it by selecting **Preferences** > **Code Style** > **Manage**.

The following section focuses on formatting and style.

Use two spaces to indent. Tabulators in string literals should use the escape character `\t`

.

Use spaces after built-in key words (e.g. `for`

, `if`

, `else`

, etc.), and before and after binary mathematical operators.

Native line endings should be allowed on each platform. This is desirable as Visual Studio for example will always insert `CRLF`

even if the file is `LF`

only, leading to a mixed line ending style for this file. Native `eol`

style avoids this problem.

Matching pairs of opening and closing curly braces should be set to the same column. See the following example:

while (continue == true)

{

for (int i = 0; i < 10; i++)

{

...

}

if (x < 7)

{

....

}

}

The main reason for this rule is to avoid constructions like:

if (isValid(a))

error = 0;

return 0;

that might later be changed to something like:

if (isValid(a))

error = 0;

return 0;

Use braces around a block even if you use only single line. Single line constructs for trivial tests like:

are allowed.

One exception is several if/else statements, which can be written as:

if (cond1)

{

...

}

else if (cond2)

{

...

}

else if (cond3)

{

...

}

else

{

...

}

This is safe because the first statement in each else branch is used, which is itself braced by the if branch.

The following section describes the naming conventions followed by [OpenMS](https://openms.de/namespaceOpenMS.html) developers.

Reserved words of the C++ language and symbols defined e.g. in the `STL`

or in the standard C library must not be used as names for classes or class members. Examples include but are not limited to: `set`

, `map`

, `exp`

and `log`

.

Header files and source files should have the same name as the classes they contain. Source files end in `.cpp`

, while header files end in `.h`

. File names should be capitalised exactly as the class they contain (see below). Each header/source file should contain one class only, although exceptions are possible for light-weight classes.

The usage of underscores in names has two different meanings: A trailing "_" at the end indicates that something is protected or private to a class. Apart from that, different parts of a name are sometimes separated by an underscore, and sometimes separated by capital letters.

- Note
- According to the C++ standard, names that start with an underscore are reserved for internal purposes of the language and its standard library, so you should never use them.

Class names and type names always start with a capital letter. Different parts of the name are separated by capital letters at the beginning of the word. No underscores are allowed in type names and class names, except for the names of protected types and classes in classes, which are suffixed by an underscore. The same conventions apply for namespaces.

Here is an example of some classes written using the conventions described above:

class Simple; //ordinary class

class SimpleThing; //ordinary class

class PDBFile; //using an abbreviation

class Buffer_; //protected or private nested class

class ForwardIteratorTraits_; //protected or private nested class

Function names (including class method names) always start with a lower case letter. Parts of the name are separated using capital letters (as are types and class names). They should be comprehensible, but as short as possible. The same variable names must be used in the declaration and in the definition. Arguments that are actually not used in the implementation of a function have to be commented out - this avoids compiler warnings. The argument of void functions (empty argument list) must be omitted in both the declaration and the definition. If function arguments are pointers or references, the pointer or reference qualifier is appended to the variable type. The pointer or reference qualifier should not prefix the variable name.

Here is an example of some method names written using the conventions described above:

void hello(); //ordinary function, no arguments

int countPeaks(PeakArray const& p); //ordinary function

bool ignore(string& /* name */); //ordinary function with an unused argument

bool isAdjacentTo(Peak const* const* const& p) const; //an ordinary function

bool doSomething_(int i, string& name); //protected or private member function

Variable names are written in lower case letters. Distinguished parts of the name are separated using underscores. If parts of the name are derived from common acronyms (e.g. MS) they should be in upper case. Private or protected member variables of classes are suffixed by an underscore.

Here is an example of some variable names written using the conventions described above:

int simple; //ordinary variable

bool is_found; //ordinary variable

string MS_instrument; //using an abbreviation

int counter_; //protected or private member

int persistent_id_; //protected or private member

Enumerated values and preprocessor constants are all upper case letters. Parts of the name are separated by underscores.

Here is an example of some enumerated values and preprocessor constants written using the conventions described above:

#define MYCLASS_SUPPORTS_MIN_MAX 0 //preprocessor constant

enum DimensionId { DIM_MZ = 0, DIM_RT = 1 }; //enumerated values

enum DimensionId_ { MZ = 0, RT = 1 }; //enumerated values

Avoid using the preprocessor. Normally, `const`

and `enum`

will suffice for most cases.

Parameters should consist of lower-case letters and underscores only. For numerical parameters, the range of reasonable values is given. Where applicable units are given in the description. This rule applies to all kinds of parameter strings, both keys and string-values.

The correct capitalization of all data file extensions supported by [OpenMS](https://openms.de/namespaceOpenMS.html) is documented in `FileHandler::NamesOfTypes[]`

. The convention is to use only lowercase letters for file extensions. There are three exceptions: "ML" and "XML" are written in uppercase letters and "mzData" keeps its capital "D". Remember to keep this consistent when adding new data files or writing new TOPP tools (use correct capitalization for file type restrictions, here).

The following section outlines the class requirements with examples.

Each [OpenMS](https://openms.de/namespaceOpenMS.html) class should provide the following interface:

class OPENMS_DLLAPI Test

{

public:

// default constructor

Test();

// copy constructor

Test(const Test& [test](https://openms.de/namespaceOpenMS_1_1Internal_1_1ClassTest.html#a69f942d7289d5ed2ffe3a00b12235d04));

// destructor

virtual ~Test();

// assignment operator

Test& operator=(const Test& [test](https://openms.de/namespaceOpenMS_1_1Internal_1_1ClassTest.html#a69f942d7289d5ed2ffe3a00b12235d04))

{

//ALWAYS CHECK FOR SELF ASSIGNMENT!

//...

return *this;

}

};

However, the following exceptions exist:

- Default constructor: Can be omitted when the class is entirely dependent on some information or another class. In this case you should declare the default constructor private.
-
Destructor: Should be a virtual function, unless you have a very good reason why it shouldn't (e.g., saving a
`vtable`

pointer.) Otherwise a delete invocation on a pointer to a base class will call the wrong destructor. View more details[here](https://isocpp.org/wiki/faq/virtual-functions#virtual-dtors) - Copy constructor: Can be omitted when it will not be used anyway, e.g. for classes that represent an algorithm. In this case you should declare the copy constructor private.
-
Assignment operator: Can be omitted when it will not be used anyway, e.g. for classes that represent an algorithm. In this case, you should declare the assignment operator
`private`

. The`OPENMS_DLLAPI`

macro on the first line is required for correctly building the DLL. The correct usage of this macro is explained in the[OpenMS](https://openms.de/namespaceOpenMS.html)C++ guide.

In [OpenMS](https://openms.de/namespaceOpenMS.html), every `.h`

file must be accompanied by a `.cpp`

file, even if is just a ''dummy''. This way a global `make`

will stumble across errors.

Here is an example of a correctly structured `.h`

file:

... copyright header, not shown ...

//

// --------------------------------------------------------------------------

// $Maintainer: Heinz Erhardt $

// $Authors: Heinz Erhardt $

// --------------------------------------------------------------------------

#pragma once

#include <[OpenMS/CONCEPT/Types.h](https://openms.de/Types_8h.html)>

#include <functional>

#include <sstream>

namespace [OpenMS](https://openms.de/namespaceOpenMS.html)

{

... the actual code goes here ...

} // namespace OpenMS

#endif // OPENMS_KERNEL_DPEAK_H

Here is an example of a correctly structured `.cpp`

file:

... copyright header, not shown ...

//

// --------------------------------------------------------------------------

// $Maintainer: Heinz Erhardt $

// $Authors: Heinz Erhardt $

// --------------------------------------------------------------------------

#include <[OpenMS](https://openms.de/namespaceOpenMS.html)/KERNEL/DPeak.h>

namespace [OpenMS](https://openms.de/namespaceOpenMS.html)

{

... the actual code goes here ...

} // namespace OpenMS

For template classes, default instances with common template arguments should be put into the `.cpp`

file. The variable names of these instances start with `default_`

. Here is an example for the `DPeak`

class:

#include <[OpenMS/KERNEL/DPeak.h](https://openms.de/DPeak_8h.html)>

namespace [OpenMS](https://openms.de/namespaceOpenMS.html)

{

DPeak<1> default_dpeak_1;

DPeak<2> default_dpeak_2;

}

The compiler does instantiate the template and detects errors at compile time, which saves time. Otherwise the error is detected much later, when the test is compiled.

For template classes, you should include an `_impl.h`

file. An `_impl.h`

file for a template is like a `.cpp`

file for an ordinary class. Remember that the definition of a class or function template has to be known at its point of instantiation. Therefore, the implementation of a template is normally contained in the `.h`

file. For template classes, declaration and definition are given in the same file. Things get more complicated when certain design patterns (e.g., the factory pattern) are used which lead to "circular dependencies". This is only a dependency of names, but it has to be resolved by separating declarations from definitions, at least for some of the member functions. In this case, a `.h`

file can be written that contains most of the definitions as well as the declarations of the peculiar functions. Their definition is deferred to the `_impl.h`

file ("impl" for "implementation"). The `_impl.h`

file is included only if the peculiar member functions have to be instantiated. Otherwise the `.h`

file should be sufficient. No `.h`

file should include an `_impl.h file`

.

The following section discusses rules around the use of primitives, namespaces, accessors to members and the STL.

[OpenMS](https://openms.de/namespaceOpenMS.html) uses its own type names for primitive types. Use only the types defined in `OpenMS/include/OpenMS/CONCEPT/Types.h`

.

The main [OpenMS](https://openms.de/namespaceOpenMS.html) classes are implemented in the namespace [OpenMS](https://openms.de/namespaceOpenMS.html). Auxiliary classes are implemented in

. There are some other namespaces e.g. for constants and exceptions.[OpenMS::Internal](https://openms.de/namespaceOpenMS_1_1Internal.html)

Importing a whole namespace in a header files is forbidden. For example:

Using the directive on C++ standard library datatypes in header files is forbidden. For example:

// sample.h

using std::vector; //< Don't do this shorthand!

void sampleFunction1(vector &v1); //< bad: Shorthand leads to a confusing datatype. Don't do this.

void sampleFunction2(std::vector &v1); //< good: Full namespacing of datatype prevents confusion. Be explicit.

This could lead to name clashes when [OpenMS](https://openms.de/namespaceOpenMS.html) is used together with other libraries. In source files (`.cpp`

) it is however allowed.

Accessors to protected or private members of a class are implemented as a pair of get-method and set-method. This is necessary as accessors that return mutable references to a member cannot be wrapped with Python.

class Test

{

public:

// always implement a non-mutable get-method

{

return member_;

}

// always implement a set-method

void setMember([UInt](https://openms.de/group__Concept.html#gaba0996d26f7be2572973245b51852757) name)

{

member_ = name;

}

protected:

};

For members that are too large to be read with the get-method or modified and written back with the set-method, an additional non-const get-method can be implemented.

For primitive types, a non-const get-method is strictly forbidden. For more complex types it should be present only when necessary.

class Test

{

public:

const vector<String>& getMember() const

{

return member_;

}

void setMember(const vector<String>& name)

{

member_ = name;

}

// if absolutely necessary implement a mutable get-method

vector<String>& getMember()

{

return member_;

}

protected:

vector<String> member_;

};

Many [OpenMS](https://openms.de/namespaceOpenMS.html) classes base on `STL`

classes. However, only the C++ Standard Library part of the `STL`

must be used. This means that SGI extensions like `hash_set`

, `hash_multiset`

, `hash_map`

and `hash_multimap`

are not allowed; use `std::unordered_...`

instead.

The following section describes how to handle exceptions and create exception classes.

No [OpenMS](https://openms.de/namespaceOpenMS.html) program should dump a core if an error occurs. Instead, it should attempt to die as gracefully as possible. Furthermore, as [OpenMS](https://openms.de/namespaceOpenMS.html) is a framework rather than an application, it should give the programmer ways to catch and correct errors. The recommended procedure to handle - even fatal - errors is to throw an exception. Uncaught exception will result in a call to abort thereby terminating the program.

To simplify debugging, use the following throw directive for exceptions:

throw AnyException(__FILE__, __LINE__, OPENMS_PRETTY_FUNCTION);

`__FILE__`

and `__LINE__`

are standard-defined preprocessor macros. The macro `OPENMS_PRETTY_FUNCTION`

wraps Boost's version of a platform independent `__PRETTY_FUNCTION__`

macro, that works similar to a `char*`

and contains the type signature of the function as well as its bare name, if the GNU compiler is being used. It might differ on other platforms. `Exception::Base`

provides methods (`getFile`

, `getLine`

, `getFunction`

) that allow the localisation of the exception's cause.

The standard way to catch an exception should be by reference (and not by value), as shown below:

try

{

// some code which might throw

}

catch (Exception& e)

{

// Handle the exception, then possibly re-throw it:

// throw; // the modified e

}

Don't use the throw statement to specify exceptions, as this forces the compiler to check that only the specified exceptions are thrown. This check not only increases the runtime, but may prevent efficient optimization of the code by the compiler.

However, thrown exceptions must be documented to tell the user which exceptions can be caught.

void myFunction()

{

throw Foo(__FILE__, __LINE__, OPENMS_PRETTY_FUNCTION);

}

All exceptions used in [OpenMS](https://openms.de/namespaceOpenMS.html) are derived from `Exception::Base`

defined in

. A default constructor should not be implemented for these exceptions. Instead, the constructor of all derived exceptions should have the following signature:[CONCEPT/Exception.h](https://openms.de/Exception_8h.html)

AnyException(const char* file, int line, const char* function[, ...]);

Additional arguments are possible but should provide default values (see `IndexOverflow`

for an example).

C++ classes and their methods can be exposed to python via pyOpenMS. If you are interested in exposing your algorithms to python, view the [pyopenms documentation](https://pyopenms.readthedocs.io/en/latest/wrap_classes.html) for the coding conventions and examples.

To generate UML diagrams, use yEd and export the diagrams in PNG format. Do not forget to save also the corresponding `.yed`

file.

Each [OpenMS](https://openms.de/namespaceOpenMS.html) class has to be documented using Doxygen. The documentation is inserted in Doxygen format in the header file where the class is defined. Documentation includes the description of the class, each method, type declaration, enum declaration, each constant, and member variable.

Longer pieces of documentation start with a brief description, followed by an empty line and a detailed description. The empty line is needed to separate the brief from the detailed description.

Descriptions of classes always have a brief section.

Use the doxygen style of the following example for [OpenMS](https://openms.de/namespaceOpenMS.html):

class Test

{

public:

enum EnumType

{

int EVal1,

int EVal2

};

Test();

int dummy(int dummy_a, const char* dummy_s);

int isDummy();

void dummy2();

void dummy3();

protected:

int value;

};

The `defgroup`

command indicates that a comment block contains documentation for a group of classes, files or namespaces. This can be used to categorize classes, files or namespaces, and document those categories. You can also use groups as members of other groups, thus building a hierarchy of groups. By using the `ingroup`

command, a comment block of a class, file or namespace will be added to the group or groups.

The groups (or modules as doxygen calls them) defined by the `ingroup`

command should contain only the classes of special interest to the [OpenMS](https://openms.de/namespaceOpenMS.html) user. Helper classes and such must be omitted.

Documentation that does not belong to a specific `.cpp`

or `.h`

file can be written into a separate Doxygen file (with the ending ".doxygen"). This file will also be parsed by Doxygen.

Open tasks are noted in the documentation of a header or a group using the todo command. The ToDo list is then shown in the doxygen menu under 'Related pages'. Each ToDo should be followed by a name in parentheses to indicated who is going to handle it.

You can also use these commands:

@todo Necessary todo for the the next release. Should be done as soon as possible.

Please add the name of the responsible person in parentheses!

@improvement Possible improvement, but not really necessary.

Please add the name of the responsible person in parentheses!

@deprecated Deprecated class, that must be removed in the next release.

@experimental Experimental class, that will perhaps not make it to the library.

@bug Description of a bug in the class/method.

Please add the name of the finder in parentheses!

Doxygen is not hard to learn, have a look at the manual :-)

The code for each `.cpp`

file has to be commented. Each piece of code in [OpenMS](https://openms.de/namespaceOpenMS.html) has to contain at least 5% of comments. The use of:

// Comment text

instead of:

/* Comment text */

is recommended to avoid problems arising from nested comments. Comments should be written in plain english and describe the functionality of the next few lines.

Instructive programming examples are provided in the `doc/code_examples`

directory

View the [How To Write Tests](https://openms.de/how_to_write_tests.html) guidelines to learn how to write tests.

[OpenMS](https://openms.de/namespaceOpenMS.html) uses [git](https://git-scm.com/) to manage different versions of the source files. For easier identification of the responsible person each [OpenMS](https://openms.de/namespaceOpenMS.html) file contains the `$Maintainer:$`

string in the preamble.

Examples of `.h`

and `.cpp`

files have been given above. In non-C++ files (`CMake`

files, (La)TeX-Files, etc.) the C++ comments are replaced by the respective comment characters (e.g. ``#'' for `CMake`

files, % for (La)TeX).
