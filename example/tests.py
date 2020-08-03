from zest import Tests, raises, Testable, all_tests, test, Test
import main

@Tests(main.squared)
def test_squared(func = main.squared):
    """Ensure squaring is done accurately and only squarable types are squared"""

    # Make sure correct values are created
    assert func(4) == 16, f"4^2 is 16, received {func(4)}"
    assert func(5) == 25, f"5^2 is 25, received {func(5)}"

    # Make sure ValueError is thrown if invalid inputs are given
    assert raises(TypeError, func, "NaN"), "Should raise TypeError when 'NaN' supplied"
    assert raises(TypeError, func, {1, 2, 3}), "Should raise TypeError when {1, 2, 3} supplied"

# main.summed was decorated with @Testable to enable the following:
@main.summed.test
def test1(summed):
    assert summed(5, 7) == 12, f"Incorrect result, should give 12, gave {summed(5, 7)}"

@main.summed.test
def test2(summed):
    assert summed(3, 4) == 7, f"Incorrect result, should give 7, gave {summed(3, 4)}"

@Test
def test_thats_not_directly_related_to_anything():
    assert 3 == 2 + 1, "Not equal"


print(test(all_tests))