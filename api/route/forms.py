import os
from http import HTTPStatus
from flask import Blueprint
from flask import jsonify
from api.model.forms import FormTask, FormField
from api.schema.forms import FormTaskSchema
from api.middleware.fetch_json import fetch_json
from api.middleware.check_admin import check_admin
from api.middleware.json_api import JSON_API
from api.middleware.fetch_token import fetch_token
from api.integrations.rmrail_1c import send_form_task


forms_api = Blueprint('forms', __name__)
json_api = JSON_API(FormTask, FormTaskSchema)


@forms_api.route('/api/forms', methods=['GET'])
def forms():
    result = FormTask.query.all()
    if (result):
        dump = FormTaskSchema().dump(result, many=True)
        return jsonify(dump)
    else:
        return jsonify({
                    'error' : 'Нет форм'
            }), 404
    

@forms_api.route('/api/forms', methods=['POST'])
@check_admin
@fetch_json
@json_api.post
@json_api.return_model
def post_forms(model):
    pass


@forms_api.route('/api/forms/send/<uuid>', methods=['POST'])
@fetch_json
@fetch_token
def send_form(*args, uuid, data, user_info, **kwargs):
    formTask = FormTask.query.get(uuid)
    if not formTask:
        return jsonify({
                    'error' : f'Форма не найдена c uuid {uuid}'
            }), 404
    
    try:
        send_form_task(user_info, formTask, data)
    except Exception as ex:
        return jsonify({
                'error' : f'Не удалось отправить форму! Исключение: \n {ex}'
        }), 404
    
    return jsonify(data), 200


@forms_api.route('/api/forms/<uuid>', methods=['GET'])
def get_forms_by_uuid(*args, uuid, **kwargs):
    result = FormTask.query.get(uuid)
    if (result):
        dump = FormTaskSchema().dump(result, many=False)
        return jsonify(dump)
    else:
        return jsonify({
                    'error' : 'Форма не найдена'
            }), 404


@forms_api.route('/api/forms/<uuid>', methods=['POST'])
@check_admin
@fetch_json
@json_api.post_by_uuid
@json_api.return_model
def post_forms_by_uuid(*args, **kwargs):
    pass


@forms_api.route('/api/forms/<uuid>', methods=['DELETE'])
@check_admin
@json_api.delete_by_uuid
@json_api.return_model
def delete_forms_by_uuid(*args, **kwargs):
    pass


@forms_api.route('/api/forms/<uuid>', methods=['PUT'])
@check_admin
@fetch_json
@json_api.put_by_uuid
@json_api.return_model
def put_forms_by_uuid(*args, **kwargs):
    pass