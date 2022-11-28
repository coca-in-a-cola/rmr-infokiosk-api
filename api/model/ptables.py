from api.model.declarative_base import db
import uuid as _uuid


class PTable(db.Model):
    __tablename__ = "ptable"

    uuid = db.Column(db.String(32), primary_key = True)
    
    title = db.Column(db.String(32))
    """
        Название таблицы (текст кнопки в ЛК)
    """

    columns = db.relationship("PColumn",
        backref="_ptable",
        lazy='dynamic',
        cascade = "all, delete, delete-orphan" 
    )
    """ 
        Информация о колонках таблицы
    """

    aside = db.Column(db.String(32), nullable=True)
    """
        Заголовок подтаблицы сбоку (если есть)
    """

    sort = db.Column(db.Integer)
    """
        Сортировка
    """

    def __init__(self, uuid = None, title="", sort=0, columns = [], aside = None, **kwargs):
        
        if not uuid:
            uuid = str(_uuid.uuid4().hex)

        super().__init__(uuid = uuid, title=title, sort=sort, columns=columns,\
            aside=aside, **kwargs)
        
        self.columns = [PColumn(**item, ptable_uuid = uuid) for item in columns]


class PColumn(db.Model):
    __tablename__ = "pcolumn"

    uuid = db.Column(db.String(32), primary_key = True)

    title = db.Column(db.Text())
    """
        Заголовок
    """

    size = db.Column(db.Integer)
    """
        Размер (пропорционально другим колонкам)
    """

    sortingType = db.Column(db.Text(), nullable=True)
    """
        Тип сортировки
    """

    ptable_uuid = db.Column(db.String(32), db.ForeignKey('ptable.uuid'))

    def __init__(self, uuid = None, title="", size=1, sortingType=None, **kwargs):
        if not uuid:
            uuid = str(_uuid.uuid4().hex)
        super().__init__(uuid = uuid, title=title, size=size, sortingType=sortingType, **kwargs)