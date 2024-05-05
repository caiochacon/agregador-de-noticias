from tabelas.config import Connection

# Herda de Connection pq vai utilizar os métodos de Connection
class SiteFavoritoTable(Connection):
    # CREATE
    def __init__(self):
        Connection.__init__(self)
        sql = """
        CREATE TABLE IF NOT EXISTS site_favorito(
            id_site_favorito SERIAL PRIMARY KEY NOT NULL,
            id_usuario INT NOT NULL,
            site VARCHAR(255) NOT NULL,
            FOREIGN KEY (id_usuario) REFERENCES usuario (id_usuario)
        )
        """
        self.execute(sql)
        self.commit()

    # READ/Search
    def read(self, select = '*', id_site_favorito = 0, id_usuario = 0, site = '', search_type = 'site'):
        try:
            sql = f"SELECT {select} FROM site_favorito WHERE site = '{site}'"

            if search_type == "id_site_favorito":
                sql = f"SELECT {select} FROM site_favorito WHERE id_site_favorito = {id_site_favorito}"
            elif search_type ==  "id_usuario":
                sql = f"SELECT {select} FROM site_favorito WHERE id_usuario = '{id_usuario}'"

            data = self.query(sql)
            if data:
                return data

            return False
        except Exception as error:
            print("Record not found in SiteFavoritoTable", error)

    def read_all(self, select = '*'):
        try:
            sql = f"SELECT {select} FROM site_favorito"

            data = self.query(sql)
            if data:
                return data
            
            return False
        except Exception as error:
            print("Record not found in SiteFavoritoTable", error)

    # INSERT
    def insert(self, id_usuario, site):
        try:
            sql = f"INSERT INTO site_favorito (id_usuario, site) VALUES ('{id_usuario}', '{site}')"

            self.execute(sql)
            self.commit()
        except Exception as error:
            print("Error inserting record", error)

    # DELETE
    def delete(self, id_site_favorito = 0):
        try:
            sql_search = f"SELECT * FROM site_favorito WHERE id_site_favorito = {id_site_favorito}"

            if not self.query(sql_search):
                return False
            
            sql_delete = f"DELETE FROM site_favorito WHERE id_site_favorito = {id_site_favorito}"

            self.execute(sql_delete)
            self.commit()
            return False
        except Exception as error:
            print("Error deleting record", error)

