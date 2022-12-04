from flask import current_app, request
from floatingMusic import floatingMusic_bp, token_required, dbInstance

from utils._resp import resp, response_body
from utils._error import err_resp, DATABASE_ERROR, REQUEST_INVAILD, NOITEM_ERROR

import os
env = os.environ

@floatingMusic_bp.route('/updateSubmission', methods=["GET", "POST"])
@token_required
def update_submission(*args, **kwargs):
    # print(args, kwargs)
    reqParams = request.args
    reqJson = request.get_json(silent=True)
    # print(reqParams)
    print(reqJson)
    u_id, p_id, t_id, k_ids = reqJson.values()
    print(u_id, p_id, t_id, k_ids, type(k_ids))
    if not (u_id and p_id and t_id and k_ids):
        err_resp(REQUEST_INVAILD, "updateSubmission")
    values = []
    for k_id in k_ids:
        values.append('(%d, %d, %d, \'%s\')' % (u_id, p_id, t_id, k_id))
    (status, res) = dbInstance.mutate('insert into floatingmusic.submission(user_id, project_id, topic_id, key_id) values%s;' % (','.join(values)))
    # (status, res) = dbInstance.query(['_id', 'name', 'status', 'max_selection_count'], 'topic', ['_id=%d' % t_id], ['_id asc'])
    print(status, res)
    if not status:
        err_resp(DATABASE_ERROR, "updateSubmission")
    # if len(res) != 1:
    #     err_resp(NOITEM_ERROR, "updateSubmission")
    resp(response_body(200, "updateSubmission", {}))