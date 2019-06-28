from .base import *
from .result import *
from .testable import *
from .tests import *
from .all_tests import *

def raises(error, function, *args, **kwargs):
    try:
        function(*args, **kwargs)
    except error:
        return True
    return False