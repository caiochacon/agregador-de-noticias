from tabelas.config import Connection

# Herda de Connection pq vai utilizar os métodos de Connection
class NoticiaTable(Connection):
    # CREATE
    def __init__(self):
        Connection.__init__(self)
        sql = """
        CREATE TABLE IF NOT EXISTS noticia(
            id_noticia SERIAL PRIMARY KEY NOT NULL,
            titulo VARCHAR(255) NOT NULL,
            data_publicacao TIMESTAMP NOT NULL,
            categoria VARCHAR(255) NOT NULL,
            texto TEXT NOT NULL,
            fonte VARCHAR(255) NOT NULL,
            link TEXT NOT NULL,
            imagem TEXT NOT NULL
        )
        """
        self.execute(sql)
        self.commit()

    def like(self, select = '*', frase = ''):
        try:
            sql = f"SELECT {select} FROM noticia WHERE titulo LIKE '%{frase}%' OR titulo LIKE INITCAP('%{frase}%') OR texto LIKE '%{frase}%' OR texto LIKE  INITCAP('%{frase}%')"
            data = self.query(sql)

            if data:
                return data
            
            return False
        except Exception as error:
            print("Record not found in NoticiaTable", error)

    # READ/Search
    def read(self, select = '*', id_noticia = 0, titulo = '', data_publicacao = 0, categoria = '',
            texto = '', fonte = '', link = '', imagem = '', search_type = 'titulo'):
        try:
            sql = f"SELECT {select} FROM noticia WHERE titulo = '{titulo}'"

            if search_type == "id_noticia":
                sql = f"SELECT {select} FROM noticia WHERE id_noticia = {id_noticia}"
            elif search_type == "data_publicacao":
                sql = f"SELECT {select} FROM noticia WHERE data_publicacao = '{data_publicacao}'"
            elif search_type == "categoria":
                sql = f"SELECT {select} FROM noticia WHERE categoria = '{categoria}'"
            elif search_type == "texto":
                sql = f"SELECT {select} FROM noticia WHERE texto = '{texto}'"
            elif search_type == "fonte":
                sql = f"SELECT {select} FROM noticia WHERE fonte = '{fonte}'"
            elif search_type == "link":
                sql = f"SELECT {select} FROM noticia WHERE link = '{link}'"
            elif search_type == "imagem":
                sql = f"SELECT {select} FROM noticia WHERE imagem = '{imagem}'"

            data = self.query(sql)

            if data:
                return data
            
            return False
        except Exception as error:
            print("Record not found in NoticiaTable", error)
            

    def read_all(self, select = '*'):
        try:
            sql = f"SELECT {select} FROM noticia"

            data = self.query(sql)
            if data:
                return data
            
            return False
        except Exception as error:
            print("Erro ao buscar notícias:", error)

    # UPDATE
    def update(self, id_noticia = 0, titulo = '', data_publicacao = 0, categoria = '',
            texto = '', fonte = '', link = '', imagem = '', update_type = 'titulo'):
        try:
            sql = f"UPDATE noticia SET titulo = {titulo} WHERE id_noticia = {id_noticia}"

            if update_type == "data_publicacao":
                sql = f"UPDATE noticia SET data_publicacao = {data_publicacao} WHERE id_noticia = {id_noticia}"
            elif update_type == "categoria":
                sql = f"UPDATE noticia SET categoria = '{categoria}' WHERE id_noticia = {id_noticia}"
            elif update_type == "texto":
                sql = f"UPDATE noticia SET texto = '{texto}' WHERE id_noticia = {id_noticia}"
            elif update_type == "fonte":
                sql = f"UPDATE noticia SET fonte = '{fonte}' WHERE id_noticia = {id_noticia}"
            elif update_type == "link":
                sql = f"UPDATE noticia SET link = '{link}' WHERE id_noticia = {id_noticia}"
            elif update_type == "imagem":
                sql = f"UPDATE noticia SET imagem = '{imagem}' WHERE id_noticia = {id_noticia}"
                
            self.execute(sql)
            self.commit()
            # print("Record updated")
        except Exception as error:
            print("Error updating noticia", error)

    # INSERT
    def insert(self, titulo = '', data_publicacao = 0, categoria = '',
            texto = '', fonte = '', link = '', imagem = ''):
        try:
            sql = f"INSERT INTO noticia (titulo, data_publicacao, categoria, texto, fonte, link, imagem) VALUES ('{titulo}', '{data_publicacao}', '{categoria}', '{texto}', '{fonte}', '{link}', '{imagem}')"
            # print(sql)

            self.execute(sql)
            self.commit()
        except Exception as error:
            print("Error inserting record", error)
            return False

    # DELETE
    def delete(self, id_noticia = 0):
        try:
            sql_search = f"SELECT * FROM noticia WHERE id_noticia = {id_noticia}"

            if not self.query(sql_search):
                return "Record not found on database"
            sql_delete = f"DELETE FROM noticia WHERE id_noticia = {id_noticia}"

            self.execute(sql_delete)
            self.commit()

            return True
        except Exception as error:
            print("Error deleting record", error)
