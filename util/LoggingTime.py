import time

def logging_time(fn):
    def wrapper_fn(*args, **kwargs):
        start_time = time.time()
        result = fn(*args, **kwargs)
        print("Working Time[{}]: {} sec".format(fn.__name__, time.time()-start_time))
        return result
    return wrapper_fn