from flask import current_app, request
from floatingMusic import floatingMusic_bp, token_required, before, dbInstance

from utils._resp import resp, response_body
from utils._error import err_resp, DATABASE_ERROR, REQUEST_INVAILD, NOITEM_ERROR, TOKEN_INVAILD

import os
env = os.environ

@floatingMusic_bp.route('/getProjects', methods=["GET"])
@token_required
def get_projects(*args, **kwargs):
    # print(args, kwargs)
    (current_user, *otherArgs) = args;
    if not current_user:
        err_resp(TOKEN_INVAILD, request.path)
    print(request.path, current_user)
    reqParams = request.args
    # print(reqParams)
    (status, res) = dbInstance.query(['_id', 'name', 'status', 'current_topic_id'], 'view_project', [], ['_id asc'])
    # print(status, res)
    if not status:
        err_resp(DATABASE_ERROR, request.path)
    if len(res) != 1:
        err_resp(NOITEM_ERROR, request.path)
    resp(response_body(200, request.path, res))

@floatingMusic_bp.route('/getProject', methods=["GET"])
@token_required
def get_project(*args, **kwargs):
    # print(args, kwargs)
    (current_user, *otherArgs) = args;
    if not current_user:
        err_resp(TOKEN_INVAILD, request.path)
    print(request.path, request.path, current_user)
    reqParams = request.args
    # print(reqParams)
    p_id = int(reqParams.get('p_id', None))
    if not p_id:
        err_resp(REQUEST_INVAILD, request.path)
    (status, res) = dbInstance.query(['_id', 'name', 'status', 'current_topic_id'], 'view_project', ['_id=%d' % p_id], ['_id asc'])
    # print(status, res)
    if not status:
        err_resp(DATABASE_ERROR, request.path)
    if len(res) != 1:
        err_resp(NOITEM_ERROR, request.path)
    resp(response_body(200, request.path, res[0]))


@floatingMusic_bp.route('/getProjectTopics', methods=["GET"])
@token_required
def get_project_topics(*args, **kwargs):
    # print(args, kwargs)
    (current_user, *otherArgs) = args;
    if not current_user:
        err_resp(TOKEN_INVAILD, request.path)
    print(request.path, current_user)
    reqParams = request.args
    # print(reqParams)
    p_id = int(reqParams.get('p_id', None))
    if not p_id:
        err_resp(REQUEST_INVAILD, request.path)
    (status, res) = dbInstance.query(['_id', 'name', 'status', 'sequence'], 'view_topic', ['project_id=%d' % p_id], ['sequence asc'])
    # print(status, res)
    if not status:
        err_resp(DATABASE_ERROR, request.path)
    if len(res) == 0:
        err_resp(NOITEM_ERROR, request.path)
    resp(response_body(200, request.path, res))

@floatingMusic_bp.route('/ifProjectAdmin', methods=["GET"])
@token_required
def if_project_admin(*args, **kwargs):
    # print(args, kwargs)
    (current_user, *otherArgs) = args;
    if not current_user:
        err_resp(TOKEN_INVAILD, request.path)
    print(request.path, current_user)
    reqParams = request.args
    # print(reqParams)
    p_id = int(reqParams.get('p_id', None))
    if not p_id:
        err_resp(REQUEST_INVAILD, request.path)
    (status, res) = dbInstance.query(['project_id', 'user_id'], 'project_admin', ['project_id=%d' % p_id])
    # print(status, res)
    if not status:
        err_resp(DATABASE_ERROR, request.path)
    if len(res) == 0:
        err_resp(NOITEM_ERROR, request.path)
    resp(response_body(200, request.path, res))

# @floatingMusic_bp.route('/getTopicResult', methods=["GET"])
# @token_required
# def get_topic_result(*args, **kwargs):
#     # print(args, kwargs)
#     reqParams = request.args
#     # print(reqParams)
#     p_id = int(reqParams.get('p_id', None))
#     t_id = int(reqParams.get('t_id', None))
#     if not t_id:
#         err_resp(REQUEST_INVAILD, "getTopicResult")
#     (status, res) = dbInstance.query(['key_id', 'count'], 'view_result', ['topic_id=%d' % t_id], ['key_id asc'])
#     print(status, res)
#     if not status:
#         err_resp(DATABASE_ERROR, "getTopicResult")
#     if len(res) == 0:
#         err_resp(NOITEM_ERROR, "getTopicResult")
#     resp(response_body(200, "getTopicResult", res))