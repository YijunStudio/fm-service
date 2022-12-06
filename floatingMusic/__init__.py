from flask import Blueprint, request, current_app
floatingMusic_bp = Blueprint('floatingMusic', __name__)
import jwt
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
        try:
            current_user = jwt.decode(token, current_app.config['SECRET_KEY'], 'HS256')
            # print(current_user)
        except Exception as err:
            print('token_required', err)
            return f(False, *args, **kwargs)
        return f(current_user, *args, **kwargs)
    return decorator

from utils._database import DBInstance

dbInstance = DBInstance('postgres')


from floatingMusic.info import *
from floatingMusic.op import *
from floatingMusic.info_project import *
from floatingMusic.op_user import *