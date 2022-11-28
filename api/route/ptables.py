import os
from http import HTTPStatus
from flask import Blueprint
from flask import jsonify, current_app
from api.middleware.jwt_auth import check_user_confirmed
from api.model.ptables import PTable
from api.schema.ptables import PTableSchema
from api.middleware.fetch_json import fetch_json
from api.middleware.check_admin import check_admin
from api.middleware.json_api import JSON_API
from api.middleware.jwt_auth import fetch_token
from api.integrations.rmrail_1c import send_form_task
from api.middleware.du_task_number import du_task_number

ptables_api = Blueprint('ptables', __name__)
json_api = JSON_API(PTable, PTableSchema)


@ptables_api.route('/api/ptables', methods=['GET'])
def forms():
    result = PTable.query.all()
    if (result):
        dump = PTableSchema().dump(result, many=True)
        return jsonify(dump)
    else:
        return jsonify({
                    'error' : 'Нет таблиц'
            }), 404
    

@ptables_api.route('/api/ptables', methods=['POST'])
@check_admin
@fetch_json
@json_api.post
@json_api.return_model
def post_forms(model):
    pass


@ptables_api.route('/api/ptables/<uuid>', methods=['GET'])
def get_forms_by_uuid(*args, uuid, **kwargs):
    result = PTable.query.get(uuid)
    if (result):
        dump = PTableSchema().dump(result, many=False)
        return jsonify(dump)
    else:
        return jsonify({
                    'error' : 'Форма не найдена'
            }), 404


@ptables_api.route('/api/ptables/<uuid>', methods=['POST'])
@check_admin
@fetch_json
@json_api.post_by_uuid
@json_api.return_model
def post_forms_by_uuid(*args, **kwargs):
    pass


@ptables_api.route('/api/ptables/<uuid>', methods=['DELETE'])
@check_admin
@json_api.delete_by_uuid
@json_api.return_model
def delete_forms_by_uuid(*args, **kwargs):
    pass


@ptables_api.route('/api/ptables/<uuid>', methods=['PUT'])
@check_admin
@fetch_json
@json_api.put_by_uuid
@json_api.return_model
def put_forms_by_uuid(*args, **kwargs):
    pass