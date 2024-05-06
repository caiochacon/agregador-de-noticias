from tabelas.usuario import UsuarioTable
from tabelas.noticia import NoticiaTable
from tabelas.noticias_fav import NoticiaFavoritaTable
from tabelas.noticias_acessadas import NoticiaAcessadaTable

tabelas = {}

tabelas['usuario'] = UsuarioTable()
tabelas['noticia'] = NoticiaTable()
tabelas['noticia_favorita'] = NoticiaFavoritaTable()
tabelas['noticia_acessada'] = NoticiaAcessadaTable()
