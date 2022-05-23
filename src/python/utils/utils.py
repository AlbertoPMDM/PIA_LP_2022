from functools import wraps
from time import time

def timing(f:object)-> None:
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print(f'func {f} took {te-ts}')
        return result
    return wrap

def timingTime(f:object)-> None:
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print(f'func {f} took {te-ts}')
        return te-ts
    return wrap