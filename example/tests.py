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

print(test_all())
print(test_squared())