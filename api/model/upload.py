from api.model.declarative_base import db
from flask import current_app
import uuid
import os



class File(db.Model):
    name = db.Column(db.Text())
    path = db.Column(db.Text(), primary_key = True)
    hashsum = db.Column(db.Text(), primary_key = True)


def check_extension(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower()\
        in current_app.config['UPLOAD_ALLOWED_EXTENSIONS']
    

def save_file(file, filename, upload_dir):
    if ('..' in filename):
        raise Exception('Ошибка безопасности!')
    
    path = filename.split('/')
    full_relative_path = f"{upload_dir}"

    for directory in path[:len(path)-1]:
        if ('.' in directory):
            raise Exception('Неверный фомрат пути!')
    
        full_relative_path = os.path.join(full_relative_path, directory)
        if not os.path.exists(full_relative_path):
            os.mkdir(full_relative_path)

    full_relative_path = os.path.join(full_relative_path, path[-1])

    file.save(full_relative_path)


def delete_file(filename, upload_dir):
    if ('..' in filename):
        raise Exception('Ошибка безопасности!')

    full_relative_path = os.path.join(upload_dir, filename)

    if not os.path.exists(full_relative_path):
            raise Exception('Файл не найден')
    
    os.remove(full_relative_path)