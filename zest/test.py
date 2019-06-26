from time import time

from . import test_list
from .result import Result


class Test:
    def __init__(self, test_function):
        test_list.append(self)
        self.test_function = test_function

    def __call__(self, *args, **kwargs):
        return self.run(*args, **kwargs)

    def __str__(self):
        if self.test_function is not None:
            if self.test_function.__doc__ is not None:
                return self.test_function.__doc__
            else:
                return self.test_function.__name__
        else:
            return "Test"

    def run(self, *args, **kwargs):
        try:
            t_start = time()
            self.test_function(*args, **kwargs)
            time_taken = time() - t_start
            self.result = Result(self, True, time=time_taken)
        except Exception as e:
            self.result = Result(self, False, e)
        return self.result