from http import HTTPStatus
from flask import Blueprint, send_file, send_from_directory, safe_join, abort

upload = Blueprint('upload', __name__)

@upload.route('/upload/<path:filename>')
def serve_file(filename):
    """
     Подключает все файлы из папки "upload"
    ---
    """
    try:
        return send_from_directory('upload', filename, as_attachment=True)
    except FileNotFoundError:
        abort(404)