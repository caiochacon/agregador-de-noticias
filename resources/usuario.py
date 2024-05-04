from flask import Blueprint, request
from models import db
from models.usuario import Usuario
from web_scrapping.src.scrapy_runner import ScrapyRunner

usuario = Blueprint('usuario', __name__, url_prefix='/usuario')

@usuario.route('/', methods=["POST"])
def criarUsuario():
    data = request.get_json()
    nome = data.get('nome')
    email = data.get('email')
    senha = data.get('senha')
    usuario_ja_cadastrado =  db.session.query(Usuario).filter(Usuario.email == email).first()
    if usuario_ja_cadastrado is not None:
        return {"error": "Usuário já cadastrado com este email"}, 409

    novo_usuario = Usuario(nome=nome, email=email, senha=senha, assinante=False)
    db.session.add(novo_usuario)
    db.session.commit()
    db.session.refresh(novo_usuario)
    return novo_usuario.__dict__

@usuario.route('/<int:id_usuario>', methods=["GET"])
def getBy(id_usuario):
    print(f'Usuario id: {id_usuario}')
    ScrapyRunner.run()
    return []