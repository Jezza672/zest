# Zest

A lightweight decorator based testing package for Python 3.5+.

## Installing

The easiest way to install is to use pip:
```
pip install zest
```
or
```
python3 -m pip install zest
```

You can also download the source and place it the directory of the module you want to use it in. An example directory structure is shown below:
- **project_directory**
  - **zest**
    - *zest's files here*
  - your_file.py
  - **your_test_file.py**

## Getting Started

A suggested workflow is to write the test first in a seperate *tests.py* file, like so:

```
from zest import tests, raises, test_all
import main

@tests(main.squared)
def test_squared(func = None):
    """Ensure squaring is done accureately and only squarable types are squared"""
    # Make sure ValueError is thrown if invalid imputs are given
    assert raises(TypeError, func, "NaN"), "Should raise TypeError when 'NaN' supplied"
    
    assert raises(TypeError, func, {1, 2, 3}), "Should raise TypeError when {1, 2, 3} supplied"

    assert func(4) == 16, "4^2 is 16, received %s" % func(4)
    assert func(5) == 25, "5^2 is 25, received %s" % func(5)

print(test_squared())
```

Note multiple tests can be placed in one test function.
main.py simply contains a function called squared that squares the input and returns it.

Zest keeps track of all registered testing functions, allowing you to run them all at once, and get grouped information on the results of the test, like so:
```
print(test_all())
```
At the moment test_all() only returns a pretty print output, but in the future this will be fleshed out to be more comprehensive

### Prerequisites

Python 3.5+

## Authors

**Jeremy Zolnai-Lucas** - *Initial work* - [Jezza672](https://github.com/Jezza672)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
