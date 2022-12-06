from flask import current_app, request
from floatingMusic import floatingMusic_bp, token_required, before, dbInstance

from utils._resp import resp, response_body
from utils._error import err_resp, DATABASE_ERROR, REQUEST_INVAILD, NOITEM_ERROR, TOKEN_INVAILD

import os
env = os.environ

@floatingMusic_bp.route('/YourUrl', methods=["GET", "POST"])
@before
def your_url(*args, **kwargs):
    print(*args)
    resp(response_body(200, "YourUrl", {}))

@floatingMusic_bp.route('/getTopic', methods=["GET"])
@token_required
def get_topic(*args, **kwargs):
    # print(args, kwargs)
    (current_user, *otherArgs) = args;
    if not current_user:
        err_resp(TOKEN_INVAILD, request.path)
    print(request.path, current_user)
    reqParams = request.args
    # print(reqParams)
    t_id = int(reqParams.get('t_id', None))
    if not t_id:
        err_resp(REQUEST_INVAILD, request.path)
    (status, res) = dbInstance.query(['_id', 'name', 'status', 'max_selection_count'], 'topic', ['_id=%d' % t_id], ['_id asc'])
    # print(status, res)
    if not status:
        err_resp(DATABASE_ERROR, request.path)
    if len(res) != 1:
        err_resp(NOITEM_ERROR, request.path)
    resp(response_body(200, request.path, res[0]))


@floatingMusic_bp.route('/getTopicKeys', methods=["GET"])
@token_required
def get_topic_keys(*args, **kwargs):
    # print(args, kwargs)
    (current_user, *otherArgs) = args;
    if not current_user:
        err_resp(TOKEN_INVAILD, request.path)
    print(request.path, current_user)
    reqParams = request.args
    # print(reqParams)
    t_id = int(reqParams.get('t_id', None))
    if not t_id:
        err_resp(REQUEST_INVAILD, request.path)
    (status, res) = dbInstance.query(['_id', 'name'], 'key', ['topic_id=%d' % t_id], ['_id asc'])
    # print(status, res)
    if not status:
        err_resp(DATABASE_ERROR, request.path)
    if len(res) == 0:
        err_resp(NOITEM_ERROR, request.path)
    resp(response_body(200, request.path, res))


@floatingMusic_bp.route('/getTopicResult', methods=["GET"])
@token_required
def get_topic_result(*args, **kwargs):
    # print(args, kwargs)
    (current_user, *otherArgs) = args;
    if not current_user:
        err_resp(TOKEN_INVAILD, request.path)
    print(request.path, current_user)
    reqParams = request.args
    # print(reqParams)
    p_id = int(reqParams.get('p_id', None))
    t_id = int(reqParams.get('t_id', None))
    if not t_id:
        err_resp(REQUEST_INVAILD, request.path)
    (status, res) = dbInstance.query(['key_id', 'count'], 'view_result', ['topic_id=%d' % t_id], ['key_id asc'])
    print(status, res)
    if not status:
        err_resp(DATABASE_ERROR, request.path)
    if len(res) == 0:
        err_resp(NOITEM_ERROR, request.path)
    resp(response_body(200, request.path, res))

# checkTopicSubmission
@floatingMusic_bp.route('/checkTopicSubmission', methods=["GET"])
@token_required
def check_topic_submission(*args, **kwargs):
    # print(args, kwargs)
    (current_user, *otherArgs) = args;
    if not current_user:
        err_resp(TOKEN_INVAILD, request.path)
    print(request.path, current_user)
    u_id = current_user.get('_id', None)
    reqParams = request.args
    # print(reqParams)
    p_id = int(reqParams.get('p_id', None))
    t_id = int(reqParams.get('t_id', None))
    if not t_id:
        err_resp(REQUEST_INVAILD, request.path)
    (status, res) = dbInstance.query(['_id', 'key_id', 'project_id', 'topic_id'], 'submission', ['topic_id=%d' % t_id, 'user_id=%d' % u_id], ['key_id asc'])
    print(status, res)
    if not status:
        err_resp(DATABASE_ERROR, request.path)
    # if len(res) == 0:
    #     err_resp(NOITEM_ERROR, request.path)
    if len(res):
        checkStatus = True
    else:
        checkStatus = False
    resp(response_body(200, request.path, { 'status': checkStatus, 'submissions': res }))