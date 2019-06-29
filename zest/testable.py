from .result import Results
from .base import Decorator_Base, Test_List
from .tests import Tests


class Testable(Decorator_Base, Test_List):
    def __init__(self, *args, **kwargs):
        Test_List.__init__(self)
        Decorator_Base.__init__(self, *args, **kwargs)
    
    def test(self, function = None):
        def create_test(function):
            test = Tests(self, test_list=self)(function)
            return test
        
        if function:
            return create_test(function)
        else:
            return create_test

    def handle_function(self, function):
        super().handle_function(function)
        self.__name__ = function.__name__
        self.__module__ = function.__module__
        self.result_string = f"Test group for '{self.__module__}.{self.__name__}':"

    __test__ = Test_List.__test__

    def __call__(self, *args, **kwargs):
        return self.decorated_function(*args, **kwargs)

    def __repr__(self) -> str:
        return f"<Testable funcion: {repr(self.decorated_function)}>"
    
    def __str__(self) -> str:
        return f"Testable function {self.decorated_function.__name__}"
