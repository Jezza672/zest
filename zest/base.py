from time import time
from typing import Callable

from .result import Result, Results

all_tests = None

class Test_Base:
    """Virtual class that defines the pre-requisites that a test must fulfil"""
    def __init__(self, test_list = all_tests):
        test_list.register(self)

    def __test__(self, *args, **kwargs) -> Result:
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
        return self.__test__()

    def __call__(self, *args, **kwargs):
        return self.call(*args, **kwargs)

    def __str__(self):
        return "Test"

class Test_List(list):
    result_string = "Test Group:"
    def __setitem__(self, key, item):
        if isinstance(item, (Test_List, Test_Base)):
            super().__setitem__(key, item)
        else:
            raise TypeError("Test lists only accept tests as members.")
    
    def __str__(self) -> str:
        return f"[{', '.join(str(t) for t in self)}]"

    def register(self, test):
        if test not in self:
            self.append(test)

    def unregister(self, test):
        try:
            self.remove(test)
        except ValueError:
            pass

    def __call__(self) -> Results:
        return self.__test__()

    def __test__(self) -> Results:
        out = Results(self.result_string)
        for test in self:
            out.append(test.__test__())
        return out

all_tests = Test_List()

class Decorator_Base(Test_Base):
    """Virtual class that defines a test created using a decorator"""

    def _function_in(self, function):
        self.call = super().call
        self.handle_function(function)
        return self

    def __init__(self, func = None, test_list = all_tests, **kwargs):
        super().__init__(test_list = test_list)
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
        
        
        