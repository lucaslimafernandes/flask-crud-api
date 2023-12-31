import sqlite3
from faker import Faker
from datetime import datetime


fake = Faker()


def insert_fake_user():

    sql = """
        INSERT INTO user (nome, email, sexo, data_nascimento, profissao, endereco)
        VALUES (?, ?, ?, ?, ?, ?);
    """

    profile = fake.profile()

    nome = profile['name']
    email = profile['mail']
    sexo = profile['sex']
    dt_nasc = profile['birthdate']
    dt_nasc = dt_nasc.strftime('%Y-%m-%d')
    profissao = profile['job']
    endereco = profile['residence']

    db_path = 'database.db'
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute(
        sql, (
            nome,
            email,
            sexo,
            dt_nasc,
            profissao,
            endereco
        )
    )
    conn.commit()
    last_id = cur.lastrowid

    response = {
        'response': {
            'status': 'successful' ,
            'user': {
                'id': last_id ,
                'name': nome
            }
        }
    }
    conn.close()

    return response


if __name__ == '__main__':

    # para executar, deve estar na pasta src
    # e chamar a execução python
    # python3 models/fake_data.py

    response = insert_fake_user()
    print(response)
    
