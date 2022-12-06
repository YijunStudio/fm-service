from flask import current_app, request
from floatingMusic import floatingMusic_bp, token_required, dbInstance

from utils._resp import resp, response_body
from utils._error import err_resp, DATABASE_ERROR, REQUEST_INVAILD, NOITEM_ERROR, TOKEN_INVAILD

import os
env = os.environ

@floatingMusic_bp.route('/updateUser', methods=["GET", "POST"])
@token_required
def update_user(*args, **kwargs):
    # print(args, kwargs)
    (current_user, *otherArgs) = args;
    if not current_user:
        err_resp(TOKEN_INVAILD, request.path)
    print(request.path, current_user)
    u_id = current_user.get('_id', None)
    reqParams = request.args
    reqJson = request.get_json(silent=True)
    # print(reqParams)
    # print(reqJson)
    # wx_nickname = reqJson.values()
    wx_nickname = reqJson.get('wx_nickname')
    # print(p_id, t_id, k_ids, type(k_ids))
    if not (u_id and wx_nickname):
        err_resp(REQUEST_INVAILD, request.path)
    (status, res) = dbInstance.mutate('update floatingmusic.user set wx_nickname=\'%s\' where _id=%d' % (wx_nickname, u_id))
    # (status, res) = dbInstance.query(['_id', 'name', 'status', 'max_selection_count'], 'topic', ['_id=%d' % t_id], ['_id asc'])
    print(status, res)
    if not status:
        err_resp(DATABASE_ERROR, request.path)
    resp(response_body(200, request.path, {}))