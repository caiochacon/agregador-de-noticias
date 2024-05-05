from tabelas.config import Connection

# Herda de Connection pq vai utilizar os métodos de Connection
class UsuarioTable(Connection):
    # CREATE
    def __init__(self):
        Connection.__init__(self)
        sql = """
        CREATE TABLE IF NOT EXISTS usuario(
            id_usuario SERIAL PRIMARY KEY NOT NULL,
            email VARCHAR(255) NOT NULL,
            nome VARCHAR(255) NOT NULL,
            senha VARCHAR(255) NOT NULL,
            assinante BOOLEAN NOT NULL
        )
        """
        self.execute(sql)
        self.commit()

    # READ/Search
    def read(self, select = '*', id_usuario = 0, nome = '', email = '', senha = '', assinante = False, search_type = 'nome'):
        try:
            sql = f"SELECT {select} FROM usuario WHERE nome = '{nome}'"

            if search_type == "id_usuario":
                sql = f"SELECT {select} FROM usuario WHERE id_usuario = {id_usuario}"
            elif search_type ==  "email":
                sql = f"SELECT {select} FROM usuario WHERE email = '{email}'"
            elif search_type ==  "senha":
                sql = f"SELECT {select} FROM usuario WHERE senha = '{senha}'"
            elif search_type ==  "assinante":
                sql = f"SELECT {select} FROM usuario WHERE assinante = '{assinante}'"

            data = self.query(sql)
            if data:
                return data
            
            return False
        except Exception as error:
            print("Record not found in UsuarioTable", error)

    def read_all(self, select = '*'):
        try:
            sql = f"SELECT {select} FROM usuario"

            data = self.query(sql)
            if data:
                return data
            
            return False
        except Exception as error:
            print("Record not found in UsuarioTable", error)

    # UPDATE
    def update(self, id_usuario = 0, nome = '', email = '', senha = '', assinante = False, update_type="nome"):
        try:
            sql = f"UPDATE usuario SET nome = '{nome}' WHERE id_usuario = {id_usuario}"
            
            if update_type == "usuario":
                sql = f"UPDATE usuario SET nome = '{nome}' WHERE id_usuario = {id_usuario}"
            elif update_type == "email":
                sql = f"UPDATE usuario SET email = '{email}' WHERE id_usuario = {id_usuario}"
            elif update_type == "senha":
                sql = f"UPDATE usuario SET senha = '{senha}' WHERE id_usuario = {id_usuario}"
            elif update_type == "assinante":
                sql = f"UPDATE usuario SET assinante = '{assinante}' WHERE id_usuario = {id_usuario}"

            self.execute(sql)
            self.commit()
            # print("Record updated")
        except Exception as error:
            print("Error updating usuario", error)

    # INSERT
    def insert(self, nome, email, senha, assinante):
        try:
            sql = f"INSERT INTO usuario (nome, email, senha, assinante) VALUES ('{nome}', '{email}', '{senha}', {assinante})"

            self.execute(sql)
            self.commit()
        except Exception as error:
            print("Error inserting record", error)

    # DELETE
    def delete(self, id_usuario = 0):
        try:
            sql_search = f"SELECT * FROM usuario WHERE id_usuario = {id_usuario}"

            if not self.query(sql_search):
                return False
            
            sql_delete = f"DELETE FROM usuario WHERE id_usuario = {id_usuario}"

            self.execute(sql_delete)
            self.commit()
            return False
        except Exception as error:
            print("Error deleting record", error)

# Testando
# tables = {}
# tables['usuarios'] = UsuarioTable()
# tables['usuario'].insert("Vinicius Freitas", "viniciusolzon", "1234", "vinicius@fake.com")

# print(tables['usuarios'].read('nome', email = 'vinicius123.com', search_type='email'))
# print(tables['usuarios'].read('email', usuario = 'viniciusolzon', search_type='usuario'))
# print(tables['usuarios'].read('usuario', nome = 'Vinicius Freitas Schiavinato Olzon', search_type='nome'))

# tables['usuarios'].update(id_usuario = 1, nome = 'Vinicius Freitas', update_type='nome')
# tables['usuarios'].update(id_usuario = 1, usuario = 'viniciusolzon', update_type='usuario')
# tables['usuarios'].update(id_usuario = 1, email = 'vinicius@fake.com', update_type='email')
# tables['usuarios'].update(id_usuario = 1, senha = '1234', update_type='senha')

# tables['usuarios'].insert("Victor Mororo", "mororo", 'mororo@fake.com', '1234')

# tables['usuarios'].delete(id_usuario = 1)