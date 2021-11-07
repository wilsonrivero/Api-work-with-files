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
   
    for i in range(len(clients)):
        images_list = []
        client = clients[i]
        client_id = client._id
    
        Imgs = Imagens.query.filter_by(client_id=client_id).all()
        imgs_serializer = images_schema.dump(Imgs)
        images_list.append(imgs_serializer)
        # result_client["Images"] = images_list


    # print(images_list)
   
    return json.dumps(result_client)


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        fields = request.form
        name = fields["name"]
        cpf = fields["cpf"]
        age = fields["age"]

        file = request.files["file"]

        if file:
            file_name = file.filename
            data_binary = file.read()
            img_base64 = rendered_img(data_binary)

            new_Client = Clients(name, cpf, age)
            db.session.add(new_Client)
            db.session.commit()


            new_Image = Imagens(file_name, data_binary, img_base64, new_Client._id)
            db.session.add(new_Image)
            db.session.commit()

        return {"client_id": new_Client._id, "img_id":new_Image._id} 

    return {"Method": 'Get'}
