from .base import Decorator_Base


class Tests(Decorator_Base):
    '''A decorator that takes a function to test, registers it, and sets up the test.
    
    The function that is being tested will be passed to the testing function as it's
    only argument.
    
    Args:
        func (function): the function this will test.'''
    
    def _handle_function_that_tests(self, function):
        self.decorated_function = function
        self.call = super().call
        return self
        
    def handle_function(self, function):
        """Override to take in the function to test first, then the functiont that tests it."""
        self.function_to_test = function
        self.call = self._handle_function_that_tests

    def _test(self):
        return self.decorated_function(self.function_to_test)
    
    def __str__(self):
        module = self.function_to_test.__module__
        name = self.function_to_test.__name__
        self_name = self.decorated_function.__name__
        return f"Test '{self_name}' for '{module}.{name}'"
