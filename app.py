from flask import Flask
from api.route.news import news_api
from api.route.maps import maps_api
from upload.serve import upload

def create_app():
    app = Flask(__name__)

    app.register_blueprint(news_api)
    app.register_blueprint(maps_api)
    app.register_blueprint(upload)
    
    return app

if __name__ == '__main__':
    from argparse import ArgumentParser

    # app.py -p 3000 запустит приложение с портом 3000
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app = create_app()
    
    # host='0.0.0.0' означает, что приложение будет работать на всех публичных адресах
    app.run(host='0.0.0.0', port=port)