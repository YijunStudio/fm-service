from flask import current_app, request
import jwt
from wxService import get_access_token, get_openid, get_user_by_openid, wxService_bp

from utils._resp import resp, response_body
from utils._error import err_resp, LOGIN_FAILED, DATABASE_ERROR

import requests

import datetime

import os
env = os.environ


@wxService_bp.route('/Login', methods=["GET", "POST"])
@get_access_token
def login(*args, **kwargs):
    # print(*args)
    reqArgs = request.args
    # reqJson = request.get_json(silent=False)
    # print(request.path, request.full_path, env.get('APPID'), env.get('APPSECRET'), request.args)
    res = get_openid(reqArgs.get('js_code'))
    # print(res)
    openid = res.get('openid', None)
    unionid = res.get('unionid', None)
    session_key = res.get('session_key', None)
    if not openid:
        err_resp(LOGIN_FAILED, request.path)
    (status, res) = get_user_by_openid(openid, unionid)
    if not status:
        err_resp(DATABASE_ERROR)
    tokenData = res.copy()
    tokenData['current_timestamp'] = datetime.datetime.now().timestamp()
    tokenData['session_key'] = session_key
    token = jwt.encode(tokenData, current_app.config['SECRET_KEY'], 'HS256')
    resp(response_body(200, request.path, {'userInfo': res, 'token': token, 'current_timestamp': datetime.datetime.now().timestamp()}))
