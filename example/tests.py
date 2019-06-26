from zest import Tests, raises, test_all, Test, Testable
import main

@Tests(main.squared)
def test_squared(func = main.squared):
    """Ensure squaring is done accureately and only squarable types are squared"""

    # Make sure correct values are created
    assert func(4) == 16, "4^2 is 16, received %s" % func(4)
    assert func(5) == 25, "5^2 is 25, received %s" % func(5)

    # Make sure ValueError is thrown if invalid inputs are given
    assert raises(TypeError, func, "NaN"), "Should raise TypeError when 'NaN' supplied"
    assert raises(TypeError, func, {1, 2, 3}), "Should raise Ty5peError when {1, 2, 3} supplied"


@Test
def other_test():
    "Ensure sum evaluates sum(5, 7) to 12"
    assert main.sum(5, 7) == 12

@Testable
def thing(x, y):
    return x - y

@thing.test
def test1(func = None):
    "Gives correct output with 7, 5"
    assert func(7, 5) == 2, f"func(7, 5) should give 2, gave {func(7, 5)}"

@thing.test
def test2(func = None):
    "Gives correct output with 8, 19"
    assert func(8, 19) == -11, f"Should give -11, gave {func(8, 19)}"

@Testable
def other_thing(y):
    return y + 2

@other_thing.test
def test3(func = None):
    "Gives correct output"
    assert func(7) == 9

print(thing.run())
print(other_thing.run())