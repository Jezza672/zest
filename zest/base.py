from time import time
from typing import Callable

from .result import Result
from zest.all_tests import all_tests, test



class Test_Base:
    """Virtual class that defines the pre-requisites that a test must fulfil"""
    def __init__(self):
        all_tests.append(self)
        print(len(all_tests))

    def __test__(self, *args, **kwargs):
        print(self)
        try:
            t_start = time()
            self._test(*args, **kwargs)
            time_taken = time() - t_start
            self.result = Result(self, True, time=time_taken)
        except Exception as e:
            self.result = Result(self, False, e)
        return self.result

    def _test(self) -> bool:
        raise NotImplementedError("Test function not implemented")

    def call(self, *args, **kwargs) -> Result:
        return test(self)

    def __call__(self, *args, **kwargs):
        return self.call(*args, **kwargs)

    def __str__(self):
        return "Test"

class Decorator_Base(Test_Base):
    """Virtual class that defines a test created using a decorator"""

    def _function_in(self, function):
        self.call = super().call
        self.handle_function(function)
        return self
    def __init__(self, func = None, **kwargs):
        
        # If the decorator was applied without brackets after,
        # the function it decorates will be passed as the only
        # argument to the constructor
        if func:
            self._function_in(func)
        
        # If the decorator was called with brackets after,
        # the decorator will still need to take in a function
        # the first time it is called
        else: 
            self.call = self._function_in

            # If the decorator was called with keyword arguments for
            # initialisation, run the initialisation with those
            if len(kwargs) > 0:
                self.initialise(**kwargs)

    def initialise(self, **kwargs):
        """Virtual method to be overridden.
        Takes keywords in in the case that the decorator is called
        like so:
        
        @decorator(**kwargs)

        def decorated_function(...):
            ...
        """
        pass

    def handle_function(self, function : Callable):
        """Default function handler"""
        self.decorated_function = function
        
        
        