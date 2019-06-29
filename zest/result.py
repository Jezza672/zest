class Result:
    def __init__(self, test, passed, error = None, time = None):
        self.test = test
        self.passed = passed
        self.error = error
        self.time = time
    
    def pretty(self, pre = "", verbose = True):
        if self.passed:
            if self.time is not None:
                millis = self.time * 1000
                res = f"Passed in {millis:.4f}ms"
            else:
                res = "Passed"
        elif self.error and verbose:
            if self.error.__class__ == AssertionError:
                res = f"Failed. {self.error}"
            else:
                err_name = self.error.__class__.__name__
                err_detail = str(self.error)
                res = f"Threw unexpected {err_name}: {err_detail}"
        else:
            res = "Failed"
        return f"{pre}{self.test}: {res}"

    def pretty_print(self, pre = ""):
        print(self.pretty(pre))

    def __str__(self):
        return self.pretty()
    
    def __bool__(self):
        return self.passed
    
    def __eq__(self, other):
        return other and self.passed


class Results(list, Result):
    def __init__(self, pre_text):
        list.__init__(self)
        self.pre_text = pre_text
        self.passed = True
        self.error = None
        self.time = 0
        self.test = "Test"

    def __setitem__(self, key, item : Result):
        if isinstance(item, (Result)):
            list.__setitem__(self, key, item)
            
            if not item.passed:
                self.passed = False
            
            if item.error:
                self.error = item.error
            
            if item.time:
                self.time += item.time
        else:
            raise TypeError("Result lists only accept test results as members.")

    def pretty(self, pre = "") -> str:
        string = pre
        joiner = "\n" + pre
        string += self.pre_text + joiner
        pre += "\t"
        string += joiner.join(item.pretty(pre) for item in self)
        string += joiner
        string += Result.pretty(self)
        return string

    def pretty_print(self, pre : str  = ""):
        print(self.pretty(pre))

    def __str__(self) -> str:
        return self.pretty()