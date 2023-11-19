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


@app.route('/user/<user_id>', methods=['GET'])
def user_by_id(user_id):

    user = User()
    response = user.get_by_id(user_id)
    return jsonify(response)


## Update
@app.route('/user/<user_id>/update', methods=['PUT'])
def update_user(user_id):

    kw_accepted = ['nome', 'email', 'sexo', 'data_nascimento', 'profissao', 'endereco']
    f = request.form
    keys_list = [x for x in f.keys()]

    for k in keys_list:
        if k not in kw_accepted:

            response =  {
                'response': 'some key is not accepted!'
            }
            return jsonify(response)

    user = User()
    response = user.update_user(user_id, data=f)

    return jsonify(response)


## Delete
@app.route('/user/<user_id>/delete', methods=['DELETE'])
def delete_user(user_id):

    user = User()
    response = user.delete_user(user_id)

    return jsonify(response)



if __name__ == '__main__':
    app.run(debug=True, port=5001)



#       from flask import Flask
#   from flask_apispec import FlaskApiSpec

#   app = Flask(__name__)
#   docs = FlaskApiSpec(app)

#   @app.route('/hello')
#   def hello():
#       """Hello World"""
#       return {'hello': 'world'}

#   docs.register(hello)

#   if __name__ == '__main__':
#       app.run(debug=True)
