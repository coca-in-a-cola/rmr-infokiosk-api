import os

from api.model.news import NewsModel

class MapsModel:


    def __init__(self, upload_dir, render_url):
        # подготовка данных
        dirs = os.listdir(upload_dir)

        models = [NewsModel(os.path.join(upload_dir, dir), \
                    f'{render_url}/{dir}') for dir in dirs] 

        self.__entries = dict(zip(dirs, models))


    def getByCategory(self, category):
        if (category in self.__entries):
            return self.__entries[category].get_all()