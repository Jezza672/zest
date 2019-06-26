from .test import Test


class Tests(Test):
    '''A decorator that takes a function to test, registers it, and sets up the test.
    
    function_to_test - The function that will be passed to the testing function when the test is run.'''
    def __init__(self, function_to_test):
        super().__init__(None)
        self.func = function_to_test
    
    def __str__(self):
        return f"Test for '{self.func.__module__}.{self.func.__name__}'"

    def __call__(self, test_func):
        self.test_function = test_func
        return self.run

    def run(self):
        return super().run(self.func)
