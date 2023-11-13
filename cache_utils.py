from functools import wraps
from pymemcache.client import base

client = base.Client(('localhost', 11211))


def cache(func):
    @wraps(func)
    def wrapper(n):
        result = client.get(str(n))
        if result is None:
            print('cache miss')
            result = func(n)
            client.set(str(n), str(result))
        else:
            print('cache hit')
        return int(result)
    return wrapper
