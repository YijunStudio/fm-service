from flask import current_app, request
from floatingMusic import floatingMusic_bp, token_required, before, dbInstance

from utils._resp import resp, response_body
from utils._error import err_resp, DATABASE_ERROR, REQUEST_INVAILD, NOITEM_ERROR

import os
env = os.environ

@floatingMusic_bp.route('/getProjects', methods=["GET"])
@token_required
def get_projects(*args, **kwargs):
    # print(args, kwargs)
    reqParams = request.args
    # print(reqParams)
    (status, res) = dbInstance.query(['_id', 'name', 'status', 'current_topic_id'], 'view_project', [], ['_id asc'])
    # print(status, res)
    if not status:
        err_resp(DATABASE_ERROR, "getProjects")
    if len(res) != 1:
        err_resp(NOITEM_ERROR, "getProjects")
    resp(response_body(200, "getProjects", res))

@floatingMusic_bp.route('/getProject', methods=["GET"])
@token_required
def get_project(*args, **kwargs):
    # print(args, kwargs)
    reqParams = request.args
    # print(reqParams)
    p_id = int(reqParams.get('p_id', None))
    if not p_id:
        err_resp(REQUEST_INVAILD, "getProject")
    (status, res) = dbInstance.query(['_id', 'name', 'status', 'current_topic_id'], 'view_project', ['_id=%d' % p_id], ['_id asc'])
    # print(status, res)
    if not status:
        err_resp(DATABASE_ERROR, "getProject")
    if len(res) != 1:
        err_resp(NOITEM_ERROR, "getProject")
    resp(response_body(200, "getProject", res[0]))


@floatingMusic_bp.route('/getProjectTopics', methods=["GET"])
@token_required
def get_project_topics(*args, **kwargs):
    # print(args, kwargs)
    reqParams = request.args
    # print(reqParams)
    p_id = int(reqParams.get('p_id', None))
    if not p_id:
        err_resp(REQUEST_INVAILD, "getProjectTopics")
    (status, res) = dbInstance.query(['_id', 'name', 'status'], 'view_topic', ['project_id=%d' % p_id], ['_id asc'])
    # print(status, res)
    if not status:
        err_resp(DATABASE_ERROR, "getProjectTopics")
    if len(res) == 0:
        err_resp(NOITEM_ERROR, "getProjectTopics")
    resp(response_body(200, "getProjectTopics", res))


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