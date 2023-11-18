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

