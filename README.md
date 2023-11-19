# flask-crud-api
A Simple project with Python, Flask, SQLite ...



## How to run

1. Create a Virtual Environment

    `python3 -m venv venv`

    In Linux, initialize the venv:

    `source venv/bin/activate`

    In Windows:

    `venv\Scripts\activate`

2. Install requirements

    `python3 -m pip install --upgrade pip`

    `python3 -m pip install -r requirements.txt`

3. Execute

    At first time, we need create the database, so, in the path 'src' run the script:

    `python3 models/create_db.py`

    If you need some data to test, run 'fake_data.py'

    `python3 models/fake_data.py`

    execute the main file

    `python3 main.py`



## Tests with pytest



## To test API

I prefer the software Insomnia to call API's, but, exists another solutions

[Insomnia](https://insomnia.rest/download)

[Postman](https://www.postman.com/)

[reqbin](https://reqbin.com/)


If you use Insomnia or Postman, you can import the Insomnia_APIs.json file


So, in Linux you can try cURL, to test the operations

curl --request GET \
  --url http://localhost:5001/


### Routes

    - ('/', methods=['GET']): Hello, World!

    - ('/user/insert', methods=['POST']): Insert user

    - ('/user/fake_insert', methods=['POST']): Insert a fake user

    - ('/user/all', methods=['GET']): Get all users

    - ('/user/<user_id>', methods=['GET']): Get a user by id

    - ('/user/<user_id>/update', methods=['PUT']): Update fields

    - ('/user/<user_id>/delete', methods=['DELETE']): Delete user


### cURL

    This cURL genereted by Insomnia

curl --request GET \
  --url http://localhost:5001/

curl --request GET \
  --url http://localhost:5001/user/all

curl --request GET \
  --url http://localhost:5001/user/1

curl --request PUT \
  --url http://localhost:5001/user/3/update \
  --header 'Content-Type: multipart/form-data' \
  --form profissao=devo \
  --form email=l@l

curl --request DELETE \
  --url http://localhost:5001/user/9/delete \
  --header 'Content-Type: multipart/form-data'

curl --request POST \
  --url http://localhost:5001/user/insert \
  --header 'Content-Type: multipart/form-data' \
  --form nome=Lucas \
  --form email=teste@email \
  --form sexo=M \
  --form data_nascimento=1993-02-07 \
  --form profissao=na \
  --form endereco=na

curl --request POST \
  --url http://localhost:5001/user/fake_insert \
  --header 'Content-Type: multipart/form-data'

