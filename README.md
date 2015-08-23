# ITF1788 – Interval Test Framework for IEEE Std 1788-2015

* Create portable unit tests in an easy domain specific language
* Share unit tests between several (compatible) libraries
* Extend with plugins for additional interval arithmetic libraries


## Dependencies

* [PLY (Pyhton Lex-Yacc)](http://www.dabeaz.com/ply/ply.html) ≥ 3.4
* [PyYAML](http://pyyaml.org/) ≥ 3.11


## Overview

This framework can compile unit tests for a wide range of interval arithmetic libraries. Test cases can be written in a simple domain-specific language using polish prefix notation and interval literals. This way unit tests must not be written seperatley over and over again, but can be shared between libraries (where semantics and data types would allow it).

To give an example, the following simple unit test is compiled for several interval arithmetic libraries.
```
testcase example {
	disjoint [3.0,4.0] [1.0,2.0] = true;
}
```

### [C++ libieep1788](https://github.com/nehmeier/libieeep1788)
```
#include "p1788/p1788.hpp"
#include <limits>
template<typename T>
using I = p1788::infsup::interval<T, p1788::flavor::infsup::mpfr_flavor<T, p1788::flavor::infsup::subnormalize::yes>>;

BOOST_AUTO_TESTCASE(EXAMPLE)
{
	BOOST_CHECK_EQUAL(are_disjoint(I<double>(3.0, 4.0), I<double>(1.0, 2.0)), true);
}
```

### [C++ Gaol](https://sourceforge.net/projects/gaol/)
```
#include <gaol/gaol>
using namespace gaol;

BOOST_AUTO_TESTCASE(EXAMPLE)
{
	BOOST_CHECK_EQUAL(interval(3.0, 4.0).set_disjoint(interval(1.0, 2.0)), true);
}
```

### [GNU Octave interval package](http://octave.sourceforge.net/interval/)
```
## example

%!test
%! assert (isequal (disjoint (infsup (3.0, 4.0), infsup (1.0, 2.0)), true));
```

### [INTLAB](http://www.ti3.tu-harburg.de/rump/intlab/)
```
## example

%!test
%! assert (isequal (emptyintersect (infsup (3.0, 4.0), infsup (1.0, 2.0)), true));
```


## ITL – Interval Test Libraries

The itl subfolder contains examples of interval arithmetic unit tests, they serve as a demonstration of this framework's capabilites. If you are interested in sharing (large) test libraries, please contact interval arithmetic library maintainers on that topic. For example, the [GNU Octave interval package](http://octave.sourceforge.net/interval/) contains a collection of tests from various libraries, which are based on intervals with boundaries of type binary64.

Function names are based on IEEE Std 1788-2015, IEEE standard for interval arithmetic, and support for more functions can easily be added in plugins (see below). Operands and results are either intervals, numbers, boolean values or arrays. Intervals may be given in hexadecimal notation. Both, bare and decorated intervals are supported.

Simple test cases use a syntax of the type `function and operands = expected result`. Advanced test cases can be written as `function and operand = tight result <= accurate result`, where a tight result would be desired, but it suffices if the actual result is included in a wider, still accurate result.

For details read
> M. Kiesner, M. Nehmeier, J. Wolff von Gudenberg (2015). “ITF1788: An Interval Testframework for IEEE 1788.” https://se2.informatik.uni-wuerzburg.de/publications/tr495.pdf


## Plugins

Support for programming languages, test frameworks and interval arithmetic libraries is added via plugins. The src/plugin subfolder already contains support for some and more can be added using the template yaml files.

Plugins are independent of each other and are subdivided into (1) programming language, (2) testing framework and (3) interval arithmetic library. So, if you want to add support for another C++ interval library, you only need to customize the library's part, that is how constructors and arithmetic functions are used.


## Usage

The `defaultGenerator.sh` will compile all itl examples for all supported output formats. Custom itl files can be compiled for particular output formats via command line parameters (to be described, use `python3 main.py --help`).
