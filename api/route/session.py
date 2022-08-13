from crypt import methods
import jwt
from http import HTTPStatus
from flask import Blueprint, jsonify, request, current_app
from api.schema.user import UserSchema
from api.middleware.fetch_token import fetch_token
from api.middleware.make_token import make_token
from definitions import ROOT_DIR
from datetime import datetime, timedelta
from api.integrations.rmrail_1c import get_user_by_card_code

session_api = Blueprint('session', __name__)

#POST - создаёт новую сессию, PUT - продлевает

@session_api.route('/api/session', methods=['POST'])
def auth_user():
    """
    """
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        data = request.json
        if ('ssid' in data):
            # сначала смотрим пользователя в БД
            user_info = get_user_by_card_code(data['ssid'])
            if (not user_info):
                return jsonify({
                    'error' : 'Пользователь не найден'
                }), 404
                
            token = make_token(data['ssid'])
            return jsonify({
                'authToken' : token,
                'lifeTime': current_app.config['SESSION_TIME_IN_SECONDS'],
                'userName': UserSchema().dump(user_info)['fullname']
            }), 200
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
def prolong(user_info):
    if (user_info):
        token = make_token(user_info.card_code)
        return jsonify({
                        'authToken' : token,
                        'lifeTime': current_app.config['SESSION_TIME_IN_SECONDS'],
                        'userName': user_info.fullname
                    }), 200
    return jsonify({
            'error' : 'Сессия не найдена'
    }), 400