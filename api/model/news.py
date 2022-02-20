import os

class NewsModel:
    class NewsEntry:
        def __init__(self, url, title):
            self.url = url
            self.title = title

    def __init__(self, upload_dir, render_url):
        # подготовка данных
        news_files = os.listdir(upload_dir)

        # пока что имена - это и есть названия файла
        self.__entries = [
            self.NewsEntry(url=f"{render_url}/{filename}", title=os.path.splitext(filename)[0]) \
            for filename in sorted(news_files,
            key = lambda s: int("".join(filter(str.isdigit, s))
                                if "".join(filter(str.isdigit, s)) != ''
                                else 0),
            reverse=True) ]

    def get_top(self, n_entries):
        return self.__entries[:n_entries]
    
    def get_all(self):
        return self.__entries[:]