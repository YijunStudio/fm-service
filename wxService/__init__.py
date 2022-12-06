from flask import Blueprint
wxService_bp = Blueprint('wxService', __name__)
from functools import wraps

import os
env = os.environ

from utils._database import DBInstance

dbInstance = DBInstance('postgres')


def get_access_token(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        access_token = None

        return f(access_token, *args, **kwargs)
    return decorator


def get_openid(js_code):
    res = requests.get(
        url = 'https://api.weixin.qq.com/sns/jscode2session',
        params = {
            'appid': env.get('APPID'),
            'secret': env.get('APPSECRET'),
            'js_code': js_code,
            'grant_type': 'authorization_code',
        }
    )
    return res.json()


def get_user_by_openid(openid, unionid):
    print('get_user_by_openid')

    user = dict()
    user['wx_openid'], user['wx_unionid'] = openid, unionid
    
    (status, res) = dbInstance.query(['_id', 'wx_openid', 'wx_nickname', 'wx_phone', 'wx_unionid'], 'floatingmusic.user', ['wx_openid=\'%s\'' % openid])
    print(res)
    if not status:
        return (False, user)
    if not len(res):
        sqlphase = 'insert into floatingmusic.user(wx_openid, wx_unionid) values(\'%s\', \'%s\')' % (openid, unionid)
        (status, mutateRes) = dbInstance.mutate(sqlphase.replace("'None'", "Null"))
        print(mutateRes)
        if not status:
            return (False, user)
    elif len(res) > 1:
        return (False, user)
    (status, res) = dbInstance.query(['_id', 'wx_openid', 'wx_nickname', 'wx_phone', 'wx_unionid'], 'floatingmusic.user', ['wx_openid=\'%s\'' % openid])
    print(res)
    if not status:
        return (False, user)
    return (True, res[0])


from wxService.info import *
from wxService.op import *
