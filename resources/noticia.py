from flask import Blueprint, jsonify
from models import db
from models.noticia import Noticia

noticia = Blueprint('noticia', __name__, url_prefix='/noticia')

@noticia.route('/', methods=["GET"])
def getAll():
  noticias = db.session.query(Noticia).slice(0, 30).all()
  return noticias

@noticia.route('/<int:id_noticia>', methods=["GET"])
def getById(id_noticia):
  noticia = db.session.query(Noticia).filter(Noticia.id_noticia == id_noticia).first()
  if noticia is None:
    return {"error": f"Não existe notícia com id {id_noticia}."}, 422
  return jsonify(noticia)