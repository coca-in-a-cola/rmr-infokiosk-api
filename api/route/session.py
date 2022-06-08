from crypt import methods
import jwt
from http import HTTPStatus
from flask import Blueprint, jsonify, request, current_app
from api.schema.user import UserSchema
from api.requests.rmrail_1c import get_user_by_card_code
from api.jwt.fetch_token import fetch_token
from definitions import ROOT_DIR
from datetime import datetime, timedelta

session_api = Blueprint('api', __name__)

#TODO: дописать!!!
#POST - создаёт новую сессию, PUT - продлевает, DELETE - завершает

@session_api.route('/api/session', methods=['POST'])
def auth_user():
    """
    """
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        data = request.json
        if (data.ssid):
            user_info = get_user_by_card_code(data.ssid)
            lifeTime = datetime.utcnow() + timedelta(minutes = 30)
            if (user_info):
                token = jwt.encode({
                    'user_id': data.ssid,
                    'lifeTime' : lifeTime,
                    'user': user_info,
                }, current_app.config['SECRET_KEY'])
                return jsonify({
                    'authToken' : token,
                    'lifeTime': lifeTime,
                    'userName': user_info['fullname'] if 'fullname' in user_info else 'ОШИБКА НЕТ ФИО'
                }), 200
            else:
                return jsonify({
                    'error' : 'код пропуска не найден в базе сотрудников РМР!'
                }), 404
        else:
            return jsonify({
                'error' : 'должен содержать поле ssid с кодом пропуска сотрудника'
            }), 400
    else:
        return jsonify({
                'error' : 'Ошибка! Отправляйте данные только через json'
        }), 400

@session_api.route('/api/session', methods=['PUT'])
@fetch_token
def prolong(session):
    pass