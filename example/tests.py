from zest import Tests, raises, Testable
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

print(test_squared())


@Testable
def example(x : int, y : int) -> int:
    return x + y

