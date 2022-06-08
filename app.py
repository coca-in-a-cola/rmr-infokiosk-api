from flask import Flask
from api.route.news import news_api
from api.route.maps import maps_api
from api.route.menus import menus_api
from route import spa
from upload.serve import upload
from waitress import serve

def create_app():
    app = Flask(__name__)

    app.url_map.strict_slashes = False

    app.register_blueprint(news_api)
    app.register_blueprint(maps_api)
    app.register_blueprint(menus_api)
    app.register_blueprint(upload)
    
    # Держите его последним
    app.register_blueprint(spa)
    return app

if __name__ == '__main__':
    from argparse import BooleanOptionalAction, ArgumentParser

    # app.py -p 3000 запустит приложение с портом 3000
    parser = ArgumentParser()
    parser.add_argument('-t', '--host', default='0.0.0.0', type=str, help='Видимость сервера. 0.0.0.0 откроет его для всех публичных адресов, 127.0.0.1 - только на локальном')
    parser.add_argument('-p', '--port', default=5000, type=int, help='Порт, на котором будет работать приложение')
    parser.add_argument('-b', '--production', default=False, action='store_true', help='Отметьте, если сервер работает в боевом режиме')
    parser.add_argument('-l', '--light', default=False, action='store_true', help='Запуск киоска в облегчённой версии. Без услуг')
    args = parser.parse_args()
    port = args.port
    host = args.host

    app = create_app()
    app.config['NO_SERVICES'] = args.light
    # host='0.0.0.0' означает, что приложение будет работать на всех публичных адресах
    if (args.production):
        serve(app, host=host, port=port)
    else:
        app.run(host=host, port=port)
