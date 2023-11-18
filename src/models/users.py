import sqlite3

db_path = './database.db'

conn = sqlite3.connect(db_path, check_same_thread=False)
cur = conn.cursor()



class User:

    def __init__(self) -> None:
        pass


    def get_all(self):

        sql = """
            select * from user;
        """
        cur.execute(sql)

        return cur.fetchall()


    def insert_user(self, **kwargs):

        sql = """
            INSERT INTO user (nome, email, sexo, data_nascimento, profissao, endereco) 
            VALUES (?, ?, ?, ?, ?, ?)
            ;
        """

        kw_accepted = ['nome', 'email', 'sexo', 'data_nascimento', 'profissao', 'endereco']

        # Validação de dados
        try:
            for k, v in kwargs.items():
                if not isinstance(v, str):
                    response = {
                        'response': f'key: {k} not string!'
                    }
                    raise Exception(response)
                    # return f'key: {k} not string!'

                if k not in kw_accepted:
                    response = {
                        'response': f'key: {k} not accepted!'
                    }
                    raise Exception(response)
                    # return f'key: {k} not accepted!'
        except Exception as e:
            return str(e)
        
        cur.execute(sql, (
            kwargs['nome'],
            kwargs['email'],
            kwargs['sexo'],
            kwargs['data_nascimento'],
            kwargs['profissao'],
            kwargs['endereco'],
        ))

        conn.commit()
        last_id = cur.lastrowid

        response = {
            'response': {
                'status': 'successful' ,
                'response': {
                'id': last_id ,
                'name': kwargs['nome']
                }
            }
        }
        return response


        


