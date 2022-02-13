from distutils.command.upload import upload
import os
from unittest import result
from definitions import ROOT_DIR
from natsort import natsorted

class NewsModel:
    class NewsEntry:
        def __init__(self, url, title):
            self.url = url
            self.title = title

    def __init__(self):
        # подготовка данных
        # считаем, что pdf-файлы новостей содержатся в папке "/upload/news" проекта
        news_directory = os.path.join(ROOT_DIR, 'upload', 'news')
        news_files = os.listdir(news_directory)

        # считаем, что сервер рендерит pdf-файлы новостей по url "/upload/news"
        news_url = "/upload/news"

        # пока что имена - это и есть названия файла
        self.entries = [
            self.NewsEntry(url=f"{news_url}/{filename}", title=os.path.splitext(filename)[0]) \
            for filename in sorted(news_files,
            key = lambda s: int("".join(filter(str.isdigit, s))),
            reverse=True) ]

    def getTop(self, n_entries):
        return self.entries[:n_entries]