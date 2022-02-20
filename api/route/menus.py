import os
from http import HTTPStatus
from flask import Blueprint
from flask import jsonify
from api.model.menus import MenusModel
from api.schema.news import NewsEntrySchema
from definitions import ROOT_DIR

menus_api = Blueprint('menus', __name__)

# в целях оптимизации модель создаётся один раз
menus_model = MenusModel('/api/menus')

@menus_api.route('/api/maps/<path:link>')
def menus(link):
    """
     Выдаёт соответствующее link меню
    ---
    """
    result = menus_model.get_menu_by_location(link)

    if (result):
        return jsonify(NewsEntrySchema().dump(result))
    else:
        return HTTPStatus.NOT_FOUND, 404
