from flask import current_app, request, jsonify
from functools import wraps
import jwt
from datetime import datetime

# Декторатор проверяет наличие токена, и возвращает декодированное его содержимое
def fetch_token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        # return 401 if token is not passed
        if not token:
            return jsonify({'error' : 'Токен не найден!'}), 401
  
        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, current_app.config['SECRET_KEY'])
            print(data)
        except:
            return jsonify({
                'error' : 'Неверный токен!'
            }), 401
        # returns the current logged in users contex to the routes
        return  f(data, *args, **kwargs)
  
    return decorated