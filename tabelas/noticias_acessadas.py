from tabelas.config import Connection

# Herda de Connection pq vai utilizar os métodos de Connection
class NoticiaAcessadaTable(Connection):
    # CREATE
    def __init__(self):
        Connection.__init__(self)
        sql = """
        CREATE TABLE IF NOT EXISTS noticia_acessada(
            id_noticia_acessada SERIAL PRIMARY KEY NOT NULL,
            id_usuario INT NOT NULL,
            id_noticia INT NOT NULL,
            FOREIGN KEY (id_usuario) REFERENCES usuario (id_usuario),
            FOREIGN KEY (id_noticia) REFERENCES noticia (id_noticia)
        )
        """
        self.execute(sql)
        self.commit()

    # READ/Search
    def read(self, select = '*', id_noticia_acessada = 0, id_usuario = 0, id_noticia = 0, search_type = 'id_noticia_acessada'):
        try:
            sql = f"SELECT {select} FROM noticia_acessada WHERE id_noticia_acessada = '{id_noticia_acessada}'"

            if search_type == "id_usuario":
                sql = f"SELECT {select} FROM noticia_acessada WHERE id_usuario = {id_usuario}"
            elif search_type ==  "id_noticia":
                sql = f"SELECT {select} FROM noticia_acessada WHERE id_noticia = '{id_noticia}'"

            data = self.query(sql)
            if data:
                return data

            return False
        except Exception as error:
            print("Record not found in NoticiaAcessadaTable", error)

    def read_all(self, select = '*'):
        try:
            sql = f"SELECT {select} FROM noticia_acessada"

            data = self.query(sql)
            if data:
                return data
            
            return False
        except Exception as error:
            print("Record not found in NoticiaAcessadaTable", error)

    # INSERT
    def insert(self, id_usuario = 0, id_noticia = 0):
        try:
            sql = f"INSERT INTO noticia_acessada (id_usuario, id_noticia) VALUES ('{id_usuario}', '{id_noticia}')"

            self.execute(sql)
            self.commit()
        except Exception as error:
            print("Error inserting record", error)

    # DELETE
    def delete(self, id_noticia_acessada = 0):
        try:
            sql_search = f"SELECT * FROM noticia_acessada WHERE id_noticia_acessada = {id_noticia_acessada}"

            if not self.query(sql_search):
                return False
            
            sql_delete = f"DELETE FROM noticia_acessada WHERE id_noticia_acessada = {id_noticia_acessada}"

            self.execute(sql_delete)
            self.commit()
            return False
        except Exception as error:
            print("Error deleting record", error)
