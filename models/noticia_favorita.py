from models import db

class NoticiaFavorita(db.Model):
    id_noticia_favorita = db.Column(db.Integer, primary_key=True, nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=False)
    id_noticia = db.Column(db.Integer, db.ForeignKey('noticia.id_noticia'), nullable=False)

    usuario = db.relationship('Usuario', backref=db.backref('noticias_favoritas', lazy=True))
    noticia = db.relationship('Noticia', backref=db.backref('usuarios_favoritos', lazy=True))