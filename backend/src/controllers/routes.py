from src import app, db
from flask import request
from src.models.tables import Clients, Imagens
from base64 import b64encode


def rendered_img(data):
    render = b64encode(data).decode('ascii')
    return render


@app.route('/')
def index():
    return {"msg": 'Hello'}


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        fields = request.form
        print(fields)
        name = fields["name"]
        cpf = fields["cpf"]
        age = fields["age"]
        print(name, cpf, age)

        file = request.files["file"]

        file_name = file.filename
        data_binary = file.read()
        img_base64 = rendered_img(data_binary)
        print(file_name)

        new_Client = Clients(name, cpf, age)
        db.session.add(new_Client)
        db.session.commit()


        new_Image = Imagens(file_name, data_binary, img_base64, new_Client._id)
        db.session.add(new_Image)
        db.session.commit()

        return {"client_id": new_Client._id, "img_id":new_Image._id} 

    return {"Method": 'Get'}
