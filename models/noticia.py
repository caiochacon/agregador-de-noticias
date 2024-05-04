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