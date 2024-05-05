import psycopg2 as db

class Connection():
    def __init__(self):
        self.config = {
            "postgres": {
                "user": "postgres",
                "password": "1234",
                "host": "localhost",
                "port": "5432",
                "database": "CI_NOTICIARIO"
            }
        }
        
        try:
            self.conn = db.connect(**self.config["postgres"])
            self.cur = self.conn.cursor()
        except Exception as error:
            print("Error connecting to postgres database", error)
            exit(1)

    def __enter__(self):
        return self
    
    def __exit__(self):
        self.conn.commit()
        self.cur.close()
        self.conn.close()

    def commit(self):
        return self.conn.commit()
    
    def fetchall(self):
        return self.cur.fetchall()

    # executa o comando SQL
    def execute(self, sql, params=None):
        self.cur.execute(sql, params or ())

    # executa o comando SQL e dá o fetchall pra pegar os resultados desse comando
    def query(self, sql, params=None):
        self.cur.execute(str(sql), params or ())
        return self.fetchall()