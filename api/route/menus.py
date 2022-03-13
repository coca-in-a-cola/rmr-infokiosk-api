import os
from http import HTTPStatus
from flask import Blueprint
from flask import jsonify
from api.model.menus import MenusModel
from api.schema.menus import MenuSchema
from definitions import ROOT_DIR

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
        return jsonify(MenuSchema().dump(result))
    else:
        return 'menu not found', 404
