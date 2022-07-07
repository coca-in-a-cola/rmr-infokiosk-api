from api.model.declarative_base import db
from flask import current_app
import uuid


class Menu(db.Model):
    uuid = db.Column(db.String(32), primary_key = True)
    location = db.Column(db.Text())
    type = db.Column(db.String(30))
    goBack = db.Column(db.Boolean)
    goBackText = db.Column(db.Text())

    buttons = db.relationship("Button",
        backref="_menu",
        lazy='dynamic',
        cascade = "all, delete, delete-orphan" 
    )


class Button(db.Model):
    uuid = db.Column(db.String(32), primary_key = True)
    icon = db.Column(db.Text())
    link = db.Column(db.Text())
    detail = db.Column(db.Text())
    text = db.Column(db.Text())
    onClick = db.Column(db.Text())

    menu_uuid = db.Column(db.String(32), db.ForeignKey('menu.uuid'))
    #menu = db.relationship("Menu")


def get_menu_by_location(location):
    menu = Menu.query\
                .filter_by(location = location)\
                .all()
        
    return menu


def get_menus():
    return Menu.query.all()


def add_menus(data):
    current_app.db.session.add_all([__create_menu_from_data(item) for item in data])
    current_app.db.session.commit()


def __create_menu_from_data(data):
    menu_uuid = data['uuid'] if 'uuid' in data else str(uuid.uuid4().hex)
    menu = Menu(
            uuid = menu_uuid,
            goBack = data['goBack'] if 'goBack' in data else None,
            goBackText = data['goBackText'] if 'goBackText' in data else "",
            location = data['location'] if 'location' in data else None,
            type = data['type'] if 'goBack' in data else None,
            buttons = [
                Button(
                    uuid = button['uuid'] if 'uuid' in button else str(uuid.uuid4().hex),
                    icon = button['icon'] if 'icon' in button else None,
                    link = button['link'] if 'link' in button else None,
                    detail = button['detail'] if 'detail' in button else None,
                    text = button['text'] if 'text' in button else None,
                    onClick = button['onClick'] if 'onClick' in button else None,

                    menu_uuid = menu_uuid
                )
                for button in data['buttons']
            ] if 'buttons' in data else []
        )
    return menu


def add_menu(data):
    try:
        menu = __create_menu_from_data(data)
        current_app.db.session.add(menu)
    except:
        current_app.db.session.rollback()
        raise
    current_app.db.session.commit()
    return menu


def delete_menu_by_uuid(uuid):
    try:
        menu = Menu.query.get(uuid)
        current_app.db.session.delete(menu)
    except:
        current_app.db.session.rollback()
        raise

    current_app.db.session.commit()


def update_menu_by_uuid(uuid, new_data):
    new_data['uuid'] = uuid
    try:
        menu = Menu.query.get(uuid)
        current_app.db.session.delete(menu)
        menu = __create_menu_from_data(new_data)
        current_app.db.session.add(menu)
    
    except:
        current_app.db.session.rollback()
        raise

    current_app.db.session.commit()
    return menu