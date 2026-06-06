import functools
from datetime import datetime

def log(function):
    @functools.wraps(function)
    def pack_log(*args, **kwargs):
        date = datetime.now()
        print(f"Running {function.__name__} on {date}")
        response = function(*args, **kwargs)
        return response

    return pack_log