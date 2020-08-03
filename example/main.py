from zest import Testable

def squared(x):
    return x*x

@Testable
def summed(x, y):
    return x + y

if __name__ == "__main__":
    print(squared(5))
    print(summed(5, 7))