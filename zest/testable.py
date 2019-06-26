from .result import Results
from .test import Test
from .tests import Tests


class Testable:
    def __init__(self, func = None):
        def decorator(func):
            self.func = func
            self.__name__ = func.__name__
            self.__module__ = func.__module__
            def inner(*args, **kwargs):
                return self.func(*args, **kwargs)
            return inner

        if func is None:
            self.call = decorator
        else:
            self.call = decorator(func)
        
        self.tests = []

    def __call__(self, *args, **kwargs):
        return self.call(*args, **kwargs)
        
    def test(self, test_func):
        test_object = Tests(self.func)(test_func)
        self.tests.append(test_object)
        return test_object
    
    def run(self):
        out = Results()
        out.name = f"Tests for {self.func.__module__}.{self.func.__name__}:"
        for test in self.tests:
            out.append(test())
        return out
    
    def __repr__(self):
        return f"<Testable funcion: {repr(self.func)}>"
    
    def __str__(self):
        return f"Testable function {self.func.__name__}"
