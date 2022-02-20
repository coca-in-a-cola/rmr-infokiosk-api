import os
from http import HTTPStatus
from flask import Blueprint
from flask import jsonify
from api.model.news import NewsModel
from api.schema.news import NewsEntrySchema
from definitions import ROOT_DIR

news_api = Blueprint('api', __name__)

# в целях оптимизации модель создаётся один раз
# считаем, что pdf-файлы новостей содержатся в папке "/upload/news" проекта
news_model = NewsModel(os.path.join(ROOT_DIR, 'upload', 'news'), "/upload/news")

@news_api.route('/api/news')
def news():
    """
     Выдаёт 10 последних файлов новостей
    ---
    """
    result = news_model.getTop(10)

    result_obj = {"newsList": result}
    if (result):
        return jsonify({"newsList": NewsEntrySchema().dump(result, many=True)})
    else:
        return HTTPStatus.NOT_FOUND, 404
