import warnings
import functools
import time

def logging_time(fn):
    def wrapper_fn(*args, **kwargs):
        start_time = time.time()
        result = fn(*args, **kwargs)
        print("Working Time [{}]: {} sec".format(fn.__name__, time.time()-start_time))
        return result
    return wrapper_fn

def deprecated(fn):
    @functools.wraps(fn)
    def wrapper_fn(*args, **kwargs):
        warnings.simplefilter('always', DeprecationWarning)  # turn off filter
        warnings.warn("Call to deprecated function {}.".format(fn.__name__),
                      category=DeprecationWarning,
                      stacklevel=2)
        warnings.simplefilter('default', DeprecationWarning)  # reset filter
        return fn(*args, **kwargs)
    return wrapper_fn