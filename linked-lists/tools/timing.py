from time import time as perf_counter
import random

# Timing wrapper
def method_timer(method):
    def wrapper_method(*arg, **kw):
        t = perf_counter()
        ret = method(*arg, **kw)
        print('Method ' + method.__name__ + ' took : ' +
              "{:2.5f}".format(perf_counter()-t) + ' sec')
        return ret
    return wrapper_method

if __name__ == "__main__":
    @method_timer
    def test_method():
        print("Test")
    test_method()