from flask import Flask
from flask import jsonify

from models.users import User

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    response = {"response": "Hello, World!"}
    return jsonify(response)


@app.route('/user/all', methods=['GET'])
def all_users():

    user = User()

    response = user.get_all()
    return jsonify(response)



if __name__ == '__main__':
    app.run(debug=True, port=5001)