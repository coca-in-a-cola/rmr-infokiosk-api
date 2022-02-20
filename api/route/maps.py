import os
from http import HTTPStatus
from flask import Blueprint
from flask import jsonify
from api.model.maps import MapsModel
from api.schema.news import NewsEntrySchema
from definitions import ROOT_DIR

maps_api = Blueprint('maps', __name__)

# в целях оптимизации модель создаётся один раз
# считаем, что карты содержатся в папке "/upload/maps" проекта
maps_model = MapsModel(os.path.join(ROOT_DIR, 'upload', 'maps'), '/upload/maps')

@maps_api.route('/api/maps/<category>')
def maps(category):
    """
     Выдаёт картинки карт по категориям
    ---
    """
    result = maps_model.getByCategory(category)

    if (result):
        return jsonify({"imageList": NewsEntrySchema().dump(result, many=True)})
    else:
        return HTTPStatus.NOT_FOUND, 404
