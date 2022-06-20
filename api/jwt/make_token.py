from datetime import datetime, timedelta
from flask import current_app
import jwt

def make_token(card_code):
    return jwt.encode({
        'card_code': card_code,
        'expires' : datetime.isoformat(datetime.utcnow() \
            + timedelta(seconds = current_app.config['SESSION_TIME_IN_SECONDS'])),
    }, current_app.config['SECRET_KEY'], algorithm="HS256")