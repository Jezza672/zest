class Result:
    def __init__(self, test, passed, error = None, time = None):
        self.test = test
        self.passed = passed
        self.error = error
        self.time = time
    
    def pretty(self, pre : str = "", verbose = True):
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

    def pretty_print(self, pre : str = ""):
        print(self.pretty(pre))

    def __str__(self) -> str:
        return self.pretty()
    
    def __bool__(self) -> bool:
        return self.passed
    
    def __eq__(self, other) -> bool:
        return other and self.passed


class Results(list, Result):
    def __init__(self, pre_text):
        list.__init__(self)
        self.pre_text = pre_text
        self.failed = 0
        self.passed = True
        self.time = 0

    def append(self, item):
        if isinstance(item, Result):
            list.append(self, item)

            if not item.passed:
                self.passed = False
                self.failed += 1
            
            if item.time:
                self.time += item.time
        else:
            raise TypeError("Result lists only accept test results as members.")

    def pretty(self, pre : str = "") -> str:
        string = pre
        joiner = "\n" + pre
        if not self.passed:
            self.error = AssertionError(f"{len(self) - self.failed}/{len(self)} passed.")
        self.test = f"{self.pre_text} - {len(self)} tests" 
        string += Result.pretty(self) + joiner
        pre += "\t"
        string += joiner.join(item.pretty(pre) for item in self)
        return string

    def __str__(self) -> str:
        return self.pretty()