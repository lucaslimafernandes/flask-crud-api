from flask import Flask
from flask import jsonify, request

from models.users import User
from models.fake_data import insert_fake_user

app = Flask(__name__)



## Create
@app.route('/user/insert', methods=['POST'])
def insert_user():

    user = User()
    try:
        response = user.insert_user(
            nome=request.form['nome'] ,
            email=request.form['email'] ,
            sexo=request.form['sexo'] ,
            data_nascimento=request.form['data_nascimento'] ,
            profissao=request.form['profissao'] ,
            endereco=request.form['endereco'] ,
        )
        return jsonify(response)

    except:
        response = {
            'response': 'Algum campo foi mal preenchido, por favor, tentar novamente!'
        }
        return jsonify(response)


@app.route('/user/fake_insert', methods=['POST'])
def insert_fake():

    response = insert_fake_user()
    return jsonify(response)


## Read
@app.route('/', methods=['GET'])
def index():
    response = {"response": "Hello, World!"}
    return jsonify(response)


@app.route('/user/all', methods=['GET'])
def all_users():

    user = User()

    response = user.get_all()
    return jsonify(response)


## Update


## Delete



if __name__ == '__main__':
    app.run(debug=True, port=5001)