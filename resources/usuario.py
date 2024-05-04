from flask import Blueprint, request
from models import db
from models.usuario import Usuario


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
    return response(novo_usuario)

@usuario.route('/<int:id_usuario>', methods=["GET"])
def getById(id_usuario):
    usuario = db.session.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()
    if usuario is None:
        return {"error": f"Não existe usuário com id {id_usuario}."}, 422

    return response(usuario)


def response(usuario: Usuario):
    return {
        "id_usuario": usuario.id_usuario,
        "nome": usuario.nome,
        "email": usuario.email,
        "assinante": usuario.assinante
    }