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


## Tests


### Tests with pytest

After main script are running

1. run the online_route test

    `pytest tests/online_route.py`

2. run the test about API

    `pytest tests/user_api.py`



### To test API

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


Other way to visualize the routes, after the main is running,

access the 'http://localhost:5001/swagger/' 

or 'http://localhost:5001/swagger-ui/'

You can test the API's with the Swagger UI too.



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
  --form data_nascimento=2000-01-01 \
  --form profissao=na \
  --form endereco=na

curl --request POST \
  --url http://localhost:5001/user/fake_insert \
  --header 'Content-Type: multipart/form-data'



## Running in a Cloud (GCP, AWS, Azure, OCI, Others)



## Github actions

Dentro do server /home/flask/.ssh
ssh-keygen -m PEM -t rsa -b 4096 -C "lucaslimafernandes@github"

salvei como github-actions

cat github-actions.pub >> authorized_keys




