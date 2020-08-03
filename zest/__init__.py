from .base import *
from .result import *
from .testable import *
from .tests import *
from .test import *

def raises(error, function, *args, **kwargs):
    try:
        function(*args, **kwargs)
    except error:
        return True
    return False

def test(test_object : Test_Base) -> Result:
    return test_object.__test__()