from api.model.declarative_base import db
from flask import current_app
from datetime import datetime
import uuid as _uuid


class News(db.Model):
    uuid = db.Column(db.String(32), primary_key = True)
    url = db.Column(db.Text())
    title = db.Column(db.Text())
    created = db.Column(db.DateTime())

    def __init__(self, uuid = str(_uuid.uuid4().hex), created = datetime.utcnow(), **kwargs):
        super().__init__(uuid = uuid, created = created, **kwargs)