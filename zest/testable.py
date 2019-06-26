from .result import Results
from .base import Decorator_Base
from .tests import Tests


class Testable(Decorator_Base):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tests = []
    
    def test(self, function = None):
        def create_test(function):
            test = Tests(self)(function)
            self.tests.append(test)
            return test
        
        if function:
            return create_test(function)
        else:
            return create_test

    def handle_function(self, function):
        super().handle_function(function)
        self.__name__ = function.__name__
        self.__module__ = function.__module__

    def __call__(self, *args, **kwargs):
        return self.decorated_function(*args, **kwargs)
 
    def __test__(self):
        out = Results()
        for test in self.tests:
            out.append(test())
        return out

    def __repr__(self):
        return f"<Testable funcion: {repr(self.decorated_function)}>"
    
    def __str__(self):
        return f"Testable function {self.decorated_function.__name__}"
