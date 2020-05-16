from flask import abort, request
from functools import wraps

def json_request(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if not request.is_json:
            abort(415)

        return fn(*args, **kwargs)

    return wrapper
