from models import db

class Noticia(db.Model):
    id_noticia = db.Column(db.Integer, primary_key=True, nullable=False)
    titulo = db.Column(db.String(255), nullable=False)
    data_publicacao = db.Column(db.Date, nullable=False)
    categoria = db.Column(db.String(255), nullable=False)
    texto = db.Column(db.Text, nullable=False)
    fonte = db.Column(db.String(255), nullable=False)
    link = db.Column(db.Text, nullable=False)
    imagem = db.Column(db.Text, nullable=False)

    def __json__(self):
        return {
            "id_noticia": self.id_noticia,
            "titulo": self.titulo,
            "data_publicacao": self.data_publicacao.strftime("%Y-%m-%d"),
            "categoria": self.categoria,
            "texto": self.texto,
            "fonte": self.fonte,
            "link": self.link,
            "imagem": self.imagem
        }