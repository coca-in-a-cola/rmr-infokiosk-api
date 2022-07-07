from http import HTTPStatus
from flask import Blueprint, send_from_directory, abort, request, jsonify
from api.middleware.check_admin import check_admin
from api.model.upload import check_extension, save_file, delete_file
from werkzeug.utils import secure_filename
import os

upload = Blueprint('upload', __name__)

@upload.route('/upload/<path:filename>', methods=['GET'])
def serve_file(filename):
    """
     Подключает все файлы из папки "upload"
    ---
    """
    try:
        return send_from_directory('upload', filename, as_attachment=True)
    except:
        return jsonify({
                    'error' : 'Файл не найден'
            }), 404


@upload.route('/upload/<path:filename>', methods=['POST'])
@check_admin
def upload_file(filename):
    if 'file' not in request.files:
        return jsonify({
                    'error' : 'Файл не прикреплён. Используйте параметр "file" в запросе'
            }), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({
                    'error' : 'Файл не выбран'
            }), 400 

    if not(file and check_extension(filename)):
        return jsonify({
                        'error' : f'Файл {filename} имеет неверный формат или расширение'
                }), 400 

    try:
        save_file(file, filename, 'upload')
    except Exception as save_file_error:
        return jsonify({
                    'error' : f'Невозможно сохранить файл как {filename}: {save_file_error}'
            }), 400 

    return jsonify({
                    'success' : 'true'
            }), 200 


@upload.route('/upload/<path:filename>', methods=['DELETE'])
@check_admin
def remove_file(filename):
    if not(check_extension(filename)):
        return jsonify({
                    'error' : 'Недопустимый файл или расширение'
            }), 400 
    try:
        delete_file(filename, 'upload')
    except Exception as delete_file_error:
        return jsonify({
                    'error' : f'Невозможно удалить файл {filename}: {delete_file_error}'
            }), 400 

    return jsonify({
                    'success' : 'true'
            }), 200 