from api.model.declarative_base import db
from api.integrations.rmrail_1c import get_user_by_card_code_1C
from flask import current_app

class User(db.Model):
    card_code = db.Column(db.Integer, primary_key = True)
    fullname = db.Column(db.String(100))
    personnel_number = db.Column(db.Integer)
    subdivision = db.Column(db.Text())
    position = db.Column(db.Text())
    phone_number = db.Column(db.String(30))


def get_user_by_card_code(code):
    user_info = User.query\
                .filter_by(card_code = code)\
                .first()

    # если не нашли, вытягиваем данные с 1С
    if not user_info:
        user_info = get_user_by_card_code_1C(code)
        if (user_info):
            user = User(**user_info)
            current_app.db.session.add(user)
            current_app.db.session.commit()
        else:
            return None

    return user_info