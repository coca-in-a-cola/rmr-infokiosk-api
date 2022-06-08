import os
from http import HTTPStatus
from flask import Blueprint
from flask import jsonify
from api.model.menus import MenusModel
from api.schema.menus import MenuSchema
from definitions import ROOT_DIR
from flask import current_app

menus_api = Blueprint('menus', __name__)

# в целях оптимизации модель создаётся один раз
menus_model = MenusModel()

@menus_api.route('/api/menus', defaults={'link': ''})
@menus_api.route('/api/menus/<path:link>')
def menus(link):
    """
     Выдаёт соответствующее link меню
    ---
    """
    result = menus_model.get_menu_by_location(link)

    if (result):
        dump = MenuSchema().dump(result)
        if (link =='' and current_app.config['NO_SERVICES']):
            dump['buttons'][0]['link'] = None
            dump['buttons'][0]['text'] = None
            dump['buttons'][0]['icon'] = None
        return jsonify(dump)
    else:
        return 'menu not found', 404
