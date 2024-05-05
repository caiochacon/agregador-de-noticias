# from importlib.machinery import SourceFileLoader
# # Aqui importamos as tabelas do banco de dados para o sistema (criam elas se já não foram criadas)
# importado = SourceFileLoader("tabelas", "/home/vinicius_olzon/Documents/ENG_SOFTWARE/backend/flask_auth_app/project/tabelas/gerador.py").load_module()

from tabelas.usuario import UsuarioTable
from tabelas.noticia import NoticiaTable
from tabelas.sites_fav import SiteFavoritoTable
from tabelas.noticias_fav import NoticiaFavoritaTable

tabelas = {}

tabelas['usuario'] = UsuarioTable()
tabelas['noticia'] = NoticiaTable()
tabelas['site_favorito'] = SiteFavoritoTable()
tabelas['noticia_favorita'] = NoticiaFavoritaTable()

# print()
# print("TESTE")
# print()

# preenchendo a tabela de notícias com o csv de notícias
# tabelas['noticia'].insert('_titulo', '2022-02-12', '_categoria', '_texto', '_fonte', '_link', '_imagem')
