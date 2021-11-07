from src import db, ma
from datetime import datetime


class Clients(db.Model):
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


class ClientSchema(ma.Schema):
    class Meta:
        fields = ('_id', 'name', 'cpf', 'age', 'creatd_at')


client_schema = ClientSchema()
clients_schema = ClientSchema(many=True)


class Imagens(db.Model):
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


class ImagenSchema(ma.Schema):
    class Meta:
        fields = ('_id', 'name', 'rendered_data', 'creatd_at', 'client_id')


image_schema = ImagenSchema()
images_schema = ImagenSchema(many=True)

