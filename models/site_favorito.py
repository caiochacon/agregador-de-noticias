from models import db

class SiteFavorito(db.Model):
    id_site_favorito = db.Column(db.Integer, primary_key=True, nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=False)
    site = db.Column(db.String(255), nullable=False)

    usuario = db.relationship('Usuario', backref=db.backref('sites_favoritos', lazy=True))