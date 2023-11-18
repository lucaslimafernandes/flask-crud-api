import sqlite3

db_path = './database.db'

conn = sqlite3.connect(db_path, check_same_thread=False)
# conn.row_factory = sqlite3.Row
cur = conn.cursor()



class User:

    def __init__(self) -> None:
        pass


    def get_all(self):

        sql = """
            select 
                u.id ,
                u.nome ,
                u.email ,
                u.sexo ,
                u.data_nascimento ,
                u.profissao , 
                u.endereco
            from user u
            ;
        """
        cur.execute(sql)
        
        res = []
        for i in cur.fetchall():
            res.append(
                {
                    'id':               i[0] ,
                    'nome':             i[1] ,
                    'email':            i[2] ,
                    'sexo':             i[3] ,
                    'data_nascimento':  i[4] ,
                    'profissao':        i[5] ,
                    'endereco':         i[6] ,
                }
            )

        return res
    

    def get_by_id(self, _id):

        sql = """
            select 
                u.id ,
                u.nome ,
                u.email ,
                u.sexo ,
                u.data_nascimento ,
                u.profissao , 
                u.endereco
            from
                user u
            where
                u.id = ?
            ;
        """
        cur.execute(sql, (_id,))
        
        res = []
        for i in cur.fetchall():
            res.append(
                {
                    'id':               i[0] ,
                    'nome':             i[1] ,
                    'email':            i[2] ,
                    'sexo':             i[3] ,
                    'data_nascimento':  i[4] ,
                    'profissao':        i[5] ,
                    'endereco':         i[6] ,
                }
            )

        return res


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
                'user': {
                    'id': last_id ,
                    'name': kwargs['nome']
                }
            }
        }
        return response


        


