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