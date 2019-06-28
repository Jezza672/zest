from .base import Test_Base
from .result import Result

class Results(list):
    def __init__(self, pre_text):
        super().__init__()
        self.pre_text = pre_text
        self.passed = True
        self.error = None
        self.time = 0
        self.test = Test_Base()

    def __setitem__(self, key, item):
        if isinstance(item, (Result, Results)):
            ret_val = super().__setitem__(key, item)
            
            if not item.passed:
                self.passed = False
            
            if item.error:
                self.error = item.error
            
            if item.time:
                self.time += item.time

            return ret_val
        else:
            raise TypeError("Result lists only accept test results as members.")

    def pretty(self, pre = ""):
        string = pre
        joiner = "\n" + pre
        string += self.pre_text + joiner
        pre += "\t"
        string += joiner.join(item.pretty(pre) for item in self)
        string += joiner
        string += Result.pretty(self)
        return string

    def pretty_print(self, pre = ""):
        print(self.pretty(pre))

    def __str__(self):
        return self.pretty()