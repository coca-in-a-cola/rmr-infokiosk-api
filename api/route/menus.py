import os
from http import HTTPStatus
from flask import Blueprint, jsonify, request, current_app
from api.schema.menus import MenuSchema
from definitions import ROOT_DIR
from api.middleware.check_admin import check_admin
from api.schema.menus import MenuSchema, ButtonSchema
from api.model.menus import get_menu_by_location, add_menu, get_menus, delete_menu_by_uuid, update_menu_by_uuid, add_menus
import uuid


menus_api = Blueprint('menus', __name__)


@menus_api.route('/api/menus-list', methods=['GET'])
def get_menus_list():
    result = get_menus()
    if (result):
        dump = MenuSchema().dump(result, many=True)
        return jsonify(dump)
    else:
        return jsonify({
                    'error' : 'Нет меню'
            }), 404


@menus_api.route('/api/menus-list', methods=['POST'])
@check_admin
def import_menus_list():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        try:
            data = request.json
            add_menus(data)
        except:
            return jsonify({
                    'error' : 'Неверный формат данных'
            }), 400
        
        return jsonify({
                'success' : True
        }), 200
    else:
        return jsonify({
                'error' : 'Ошибка! Отправляйте данные только через json'
        }), 400


@menus_api.route('/api/menus', defaults={'link': ''}, methods=['GET'])
@menus_api.route('/api/menus/<path:link>', methods=['GET'])
def get_menu(link):
    """
     Выдаёт соответствующее меню по пути
    ---
    """
    result = get_menu_by_location(link)

    if (result):
        dump = MenuSchema().dump(result, many=True)
        return jsonify(dump)
    else:
        return jsonify({
                    'error' : 'Нет меню'
            }), 404

@menus_api.route('/api/menus', defaults={'link': ''}, methods=['POST'])
@menus_api.route('/api/menus/<path:link>', methods=['POST'])
@check_admin
def place_menu(link):
    """
     Добавляет соответствующее меню по пути
    ---
    """
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        try:
            data = request.json
            data['location'] = link
            add_menu(data)
        except:
            return jsonify({
                    'error' : 'Неверный формат данных'
            }), 400
        
        return jsonify({
                'success' : True
        }), 200
    else:
        return jsonify({
                'error' : 'Ошибка! Отправляйте данные только через json'
        }), 400


@menus_api.route('/api/menus', defaults={'link': ''}, methods=['DELETE'])
@menus_api.route('/api/menus/<path:link>', methods=['DELETE'])
@check_admin
def delete_menu(link):
    """
     Удаляет меню по uuid
    ---
    """
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        try:
            data = request.json

            if not 'uuid' in data:
                return jsonify({
                        'error' : 'Не указан UUID'
                }), 400
                
            delete_menu_by_uuid(data['uuid'])
        except:
            return jsonify({
                    'error' : 'Ошибка удаления меню'
            }), 400
        
        return jsonify({
                'success' : True
        }), 200
    else:
        return jsonify({
                'error' : 'Ошибка! Отправляйте данные только через json'
        }), 400


@menus_api.route('/api/menus', defaults={'link': ''}, methods=['PUT'])
@menus_api.route('/api/menus/<path:link>', methods=['PUT'])
@check_admin
def update_menu(link):
    """
     Изменяет меню по uuid
    ---
    """
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        try:
            data = request.json
            data['location'] = link

            if not 'uuid' in data:
                return jsonify({
                        'error' : 'Не указан UUID'
                }), 400
                
            data['location'] = link
            update_menu_by_uuid(data['uuid'], data)

        except:
            return jsonify({
                    'error' : 'Ошибка редактирования меню'
            }), 400
        return jsonify({
                'success' : True
        }), 200
    else:
        return jsonify({
                'error' : 'Ошибка! Отправляйте данные только через json'
        }), 400