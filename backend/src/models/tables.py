from src import db
from datetime import datetime
from sqlalchemy_serializer import SerializerMixin


class Clients(db.Model, SerializerMixin):

    serialize_only = ('_id', 'name', 'cpf', 'age', 'creatd_at', 'images_id')
    serialize_rules = ()

    __tablename__ = 'clients'
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    cpf = db.Column(db.String)
    age = db.Column(db.Integer)
    creatd_at = db.Column(db.DateTime, default=datetime.now)
    images_id = db.relationship('Imagens', backref='Clients', lazy=True)

    def __init__(self, name, cpf, age):
        self.name = name
        self.cpf = cpf
        self.age = age


class Imagens(db.Model, SerializerMixin):
    serialize_only = ('_id', 'name', 'name', 'data','rendered_data', 'creatd_at', 'client_id')
    serialize_rules = ()

    __tablename__ = 'images'
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    data = db.Column(db.LargeBinary)
    rendered_data = db.Column(db.Text)
    create_at = db.Column(db.DateTime, default=datetime.now)
    client_id = db.Column(db.Integer, db.ForeignKey('clients._id'))

    def __init__(self, name, data, rendered_data, client_id):
        self.name = name
        self.data = data
        self.rendered_data = rendered_data
        self.client_id = client_id
