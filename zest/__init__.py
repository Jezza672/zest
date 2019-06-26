from zest.base import *
from zest.result import *
from zest.testable import *
from zest.tests import *

def raises(error, function, *args, **kwargs):
    try:
        function(*args, **kwargs)
    except error:
        return True
    return False