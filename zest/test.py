from .base import Decorator_Base

class Test(Decorator_Base):
    def _test(self):
        return self.decorated_function()

    def __str__(self):
        return f"Test: '{self.decorated_function.__name__}'"