from src import app
from flask import request


@app.route('/')
def index():
    return {"msg": 'Hello'}


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        fields = request.values
        file = request.files

        name = fields["name"]
        cpf = fields["cpf"]
        age = fields["age"]
        print(file)

        return {"Ok": ''}

    return {"Method": 'Get'}
