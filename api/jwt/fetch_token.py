from flask import current_app, request, jsonify
from functools import wraps
import jwt
from datetime import datetime
from db.ORMs.models import User
from datetime import datetime

# Декторатор проверяет наличие токена, и возвращает декодированное его содержимое
def fetch_token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        # or request body as authToken
        if not token:
            try:
                token = request.get_json()['authToken']
            except:
                return jsonify({'error' : 'Токен не найден!'}), 401
  
        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms="HS256")
        except:
            return jsonify({
                'error' : 'Неверный токен!'
            }), 401

        if current_app.config['DEBUG']:
            print(f"""
            Decoded token:
            {str(data)}
            ---
            """)
        if (datetime.utcnow() > datetime.fromisoformat(data['expires'])):
            return jsonify({
                'error' : 'Время сессии истекло! Войдите в систему снова'
            }), 401

        current_user = User.query\
        .filter_by(card_code = data['card_code'])\
        .first()
        if current_app.config['DEBUG']:
            print(f"""
            Found user:
            {str(current_user)}
            ---
            """)

        # returns the current logged in users contex to the routes
        return  f(current_user, *args, **kwargs)
    
    return decorated