class User():
    def __init__(self):
        self.logged = False
        self.name = "Usuário desconhecido"
        self.email = "Email desconhecido"

    def login_user(self, name, email):
        self.logged = True
        self.name = name
        self.email = email
        
    def logout(self):
        self.logged = False
        self.name = "Usuário desconhecido"
        self.email = "Email desconhecido"

    def is_authenticated(self):
        return self.logged
