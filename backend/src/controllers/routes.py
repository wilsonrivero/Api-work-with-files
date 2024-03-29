from src import app, db
from flask import request
from src.models.tables import Clients, Imagens, clients_schema, images_schema
from base64 import b64encode
import json

def rendered_img(data):
    render = b64encode(data).decode('ascii')
    return render


@app.route('/')
def index():
    clients = Clients.query.all()
    result_client = clients_schema.dump(clients)

    res_json = {
            "Clients": []
        }


    for i in range(len(clients)):
        client = clients[i]
        client_id = client._id
    
        Imgs = Imagens.query.filter_by(client_id=client_id).all()
        imgs_serializer = images_schema.dump(Imgs)
        res_json["Clients"].append({
                "Client": result_client[i],
                "Images": imgs_serializer
            })
    
    return res_json


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        fields =  request.form
        print(fields)
        name = fields["name"]
        cpf = fields["cpf"]
        age = fields["age"]

        new_Client = Clients(name, cpf, age)
        db.session.add(new_Client)
        db.session.commit()

        file = request.files["file"]
        print(file)

        if file:
            file_name = file.filename
            data_binary = file.read()
            img_base64 = rendered_img(data_binary)

            new_Image = Imagens(file_name, data_binary, img_base64, new_Client._id)
            db.session.add(new_Image)
            db.session.commit()

            return {"client_id": new_Client._id, "img_id": new_Image._id} 
        return {'cleint_id': new_Client._id}

    return {"Method": 'Get'}


@app.route('/upload/<_id>', methods=["POST"])
def upload(_id):
    if request.method == 'POST':
        file = request.files["file"]
        file_name = file.filename
        data_binary = file.read()
        img_base64 = rendered_img(data_binary)

        new_image = Imagens(file_name, data_binary, img_base64, _id)
        db.session.add(new_image)
        db.session.commit()

        return {"image_id": new_image._id, "msg": "Upload successfully!"}


@app.route('/delete/<_id>', methods=["DELETE"])
def delete(_id):
    if request.method == 'DELETE':
        client = Clients.query.filter_by(_id=_id).first()
        images = Imagens.query.filter_by(client_id=_id).first()

        if images:
            db.session.delete(images)
            db.session.commit()

        db.session.delete(client)
        db.session.commit()

        return {"msg": "Client deleted, with images"}

    return {"msg": 'This need method DELETE'}

