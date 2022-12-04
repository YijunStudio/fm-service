from flask import current_app, request
from floatingMusic import floatingMusic_bp, token_required, before, dbInstance

from utils._resp import resp, response_body
from utils._error import err_resp, DATABASE_ERROR, REQUEST_INVAILD, NOITEM_ERROR

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
    reqParams = request.args
    # print(reqParams)
    t_id = int(reqParams.get('t_id', None))
    if not t_id:
        err_resp(REQUEST_INVAILD, "getTopic")
    (status, res) = dbInstance.query(['_id', 'name', 'status', 'max_selection_count'], 'topic', ['_id=%d' % t_id], ['_id asc'])
    # print(status, res)
    if not status:
        err_resp(DATABASE_ERROR, "getTopic")
    if len(res) != 1:
        err_resp(NOITEM_ERROR, "getTopic")
    resp(response_body(200, "getTopic", res[0]))


@floatingMusic_bp.route('/getTopicKeys', methods=["GET"])
@token_required
def get_topic_keys(*args, **kwargs):
    # print(args, kwargs)
    reqParams = request.args
    # print(reqParams)
    t_id = int(reqParams.get('t_id', None))
    if not t_id:
        err_resp(REQUEST_INVAILD, "getTopicKeys")
    (status, res) = dbInstance.query(['_id', 'name'], 'key', ['topic_id=%d' % t_id], ['_id asc'])
    # print(status, res)
    if not status:
        err_resp(DATABASE_ERROR, "getTopicKeys")
    if len(res) == 0:
        err_resp(NOITEM_ERROR, "getTopicKeys")
    resp(response_body(200, "getTopicKeys", res))


@floatingMusic_bp.route('/getTopicResult', methods=["GET"])
@token_required
def get_topic_result(*args, **kwargs):
    # print(args, kwargs)
    reqParams = request.args
    # print(reqParams)
    p_id = int(reqParams.get('p_id', None))
    t_id = int(reqParams.get('t_id', None))
    if not t_id:
        err_resp(REQUEST_INVAILD, "getTopicResult")
    (status, res) = dbInstance.query(['key_id', 'count'], 'view_result', ['topic_id=%d' % t_id], ['key_id asc'])
    print(status, res)
    if not status:
        err_resp(DATABASE_ERROR, "getTopicResult")
    if len(res) == 0:
        err_resp(NOITEM_ERROR, "getTopicResult")
    resp(response_body(200, "getTopicResult", res))