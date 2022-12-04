from flask import Blueprint, request
floatingMusic_bp = Blueprint('floatingMusic', __name__)
from functools import wraps

def before(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        something = None

        return f(something, *args, **kwargs)
    return decorator

def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        something = None
        # print(args, kwargs)
        token = request.headers.get('Authorization', None)
        # print(token)
        return f(something, *args, **kwargs)
    return decorator

from utils._database import DBInstance

dbInstance = DBInstance('postgres')


from floatingMusic.info import *
from floatingMusic.op import *