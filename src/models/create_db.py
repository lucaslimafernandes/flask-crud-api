import sqlite3



def create_db():
    """
        Função para criar a tabela, deve ser executada
        uma vez, para iniciar o aplicativo corretamente
    """

    db_path = 'database.db'

    sql = """
        CREATE TABLE user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            sexo TEXT NOT NULL,
            data_nascimento TEXT NOT NULL,
            profissao TEXT NOT NULL,
            endereco TEXT NOT NULL
        );
    """

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute(sql)
    conn.commit()
    conn.close()





if __name__ == '__main__':
    
    # para executar, deve estar na pasta src
    # e chamar a execução python
    # python3 models/create_db.py

    create_db()

