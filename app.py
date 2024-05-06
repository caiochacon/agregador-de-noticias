from flask import render_template, redirect, url_for, request, flash
from apscheduler.schedulers.background import BackgroundScheduler
from passlib.hash import sha256_crypt
from models import User
from flask import Flask
from gerador import *
import os

from web_scrapping.src.scrapy_all.scrapy_runner import ScrapyRunner
from recommendation.src.run_recommendation_system import RunRecomendationSystem
from recommendation.utils.top_news_catcher import TopNewsCatcher


usuario = User()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/assinatura')
def assinatura():
    return render_template('login.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')

    ##################################################################################################################################################
    # if this returns a user, then the email exists in database
    user = tabelas['usuario'].read('nome, email', email = email, search_type = 'email')

    # check if the user actually exists
    if not user:
        flash('Email não registrado.')
        return redirect(url_for('login')) # if the user doesn't exist or password is wrong, reload the page

    # Procura a senha (hash) desse usuário e verifica se bate com o hash da senha digitada
    senha = tabelas['usuario'].read('senha', email = email, search_type = 'email')[0][0]

    if not sha256_crypt.verify(password, senha):
        flash('Por favor cheque suas credenciais de login e tente novamente.')
        return redirect(url_for('login')) # if the user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    user_name = user[0][0]
    user_email = user[0][1]
    usuario.login_user(user_name, user_email)
    return redirect(url_for('home'))


@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    password_data = sha256_crypt.encrypt(password)

    # Procuramos o email no banco de dados, se retorna algo entende-se que existe uma conta com esse email
    user = tabelas['usuario'].read('*', email = email, search_type = 'email')

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        flash('Endereço de email já está em uso.')
        return redirect(url_for('signup'))

    # Caso ainda não exista conta com esse email, criamos uma e inserimos no banco de dados
    tabelas['usuario'].insert(name, email, password_data, 'false') # por padrão usuário não é assinante assim que registra

    return redirect(url_for('login'))

# @app.route('/profile')
# def profile():
#     return render_template('profile.html', name=usuario.name, email=usuario.email)

@app.route('/logout')
def logout():
    usuario.logout()
    return redirect(url_for('home'))


# DAQUI PRA CIMA É A PARTE QUE FALTA DE INTEGRAR COM FRONTEND ETC.
########################################################################################################
# DAQUI PRA BAIXO É O BACKEND FUNCIONANDO

def gera_principais_e_recomendados():
    current_dir = os.getcwd()
    relative_path = os.path.join('web_scrapping', 'data', 'notices.csv')
    notices_path = os.path.join(current_dir, relative_path)
    print(f'>>>>>>> {notices_path}')
    dataset_top_news, df_to_recomendations = TopNewsCatcher().catch_top_news(path_to_csv=notices_path)

    recommendation = RunRecomendationSystem(path_to_data = notices_path)
    dataset_top_news, dataset_recomendations = recommendation.run(dataset_top_news, df_to_recomendations)
    print(dataset_top_news.head(9))
    print(dataset_recomendations.head(27))
    # input()

    dataset_top_news = dataset_top_news.drop(['sentences'], axis=1)
    dataset_recomendations = dataset_recomendations.drop(['normalized_data_scores','sentences'], axis=1)
    return dataset_top_news, dataset_recomendations


def guarda_noticias_no_bd(dataset_top_news, dataset_recomendations):
    # Armazena as informações das X notícias mais recentes e as guarda no banco de dados
    tupla_principal = [tuple(x) for x in dataset_top_news.to_numpy()]
    # Armazena as informações das 3 notícias mais relacionadas dessas X notícias no banco de dados
    tupla_relacionada = [tuple(x) for x in dataset_recomendations.to_numpy()]

    # Insere a notícia principal
    for i in range(len(tupla_principal)):
        # print(i)

        titulo = tupla_principal[i][0]
        data_publicacao = '2024-05-03'
        categoria = tupla_principal[i][5]
        texto = tupla_principal[i][2]
        fonte = tupla_principal[i][6]
        link = tupla_principal[i][3]
        imagem = tupla_principal[i][4]
        tabelas['noticia'].insert(titulo = titulo, data_publicacao = data_publicacao, categoria = categoria, texto = texto, fonte = fonte, link = link, imagem = imagem)
        # input()

        # Insere 3 notícias relacionadas a anterior
        for j in range(i+(i*2), (i*2)+i+3):
            # print(j)
            data_publicacao = '2024-05-03'

            tabelas['noticia'].insert(titulo = tupla_relacionada[j][0], data_publicacao = data_publicacao, categoria = tupla_relacionada[j][5], texto = tupla_relacionada[j][2], fonte = tupla_relacionada[j][6], link = tupla_relacionada[j][3], imagem = tupla_relacionada[j][4])
        # print()


def atualiza_bd():
    # Executa o webscrap e salva o csv resultante em 'web_scrapping/data/notices.csv'
    ScrapyRunner.run()

    # Executa o sistema de recomendação a partir do csv gerado, devolvendo dois dataframes:
    # o primeiro com as 9 notícias principais e o segundo dataframe com as 27 notícias relacionadas a essas 9 (3 de cada) 
    df_principais, df_recomendados = gera_principais_e_recomendados()
    guarda_noticias_no_bd(df_principais, df_recomendados)
    print("Banco de dados atualizado com sucesso.")

# clicou_salvar_noticia()
# if not usuario.is_authenticated():
#   flash("Para salvar notícias, logue em sua conta.")
# else:
#   pega o id_noticia da notícia em questão (a notícia na tela vai ter uma tupla com todas as suas informações, incluindo o id_usuario)
#   id_noticia = tupla_da_noticia_selecionada[0] (é pra ser algo assim, primeiro item da tupa é o id)
#   salva_noticia(id_noticia)
# Ao clicar em salvar notícia, se estiver logado:
def salva_noticia(identificador_noticia):
    id_usuario = tabelas['usuario'].read('id_usuario', email = usuario.email, search_type = 'email')[0][0]
    # id_usuario = tabelas['usuario'].read('id_usuario', email = 'test@fake1.com', search_type = 'email')[0][0]
    tabelas['noticia_favorita'].insert(id_usuario = id_usuario, id_noticia = identificador_noticia)


# clicou em 'para você'
# if not usuario.is_authenticated():
#   flash("Para ver suas recomendações, logue em sua conta.")
# else:
#   render_template('para você')
#   lá vai ter duas 'colunas', uma com o histórico de acessos e outra com as notícias salvas
#   historico_noticias()
#   noticias_salvas()
def noticias_salvas():
    # verifica qual é o usuário logado
    id_usuario = tabelas['usuario'].read('id_usuario', email = usuario.email, search_type = 'email')[0][0]
    # id_usuario = tabelas['usuario'].read('id_usuario', email = 'test@fake1.com', search_type = 'email')[0][0]

    # pega o id de todas as notícias q ele já salvo
    id_noticias_salvas = tabelas['noticia_favorita'].read(select = 'id_noticia', id_usuario = id_usuario, search_type = 'id_usuario')
    # print(id_noticias_salvas)
    # input()
    
    # com esse id, se coleta todas as informações dessas notícias
    noticias_fav = []
    for i in range(0, len(id_noticias_salvas)):
        noticia_fav = tabelas['noticia'].read(id_noticia = id_noticias_salvas[i][0], search_type = 'id_noticia')
        # print(noticia_fav)
        # input()
        noticias_fav.append(noticia_fav)
    # retorna uma lista de tuplas com todas as informações das notícias salvas pelo usuário logado
    # print("TERMINOU")
    # input()
    return noticias_fav


# clicou em 'para você'
# if not usuario.is_authenticated():
#   flash("Para ver suas recomendações, logue em sua conta.")
# else:
#   render_template('para você')
#   lá vai ter duas 'colunas', uma com o histórico de acessos e outra com as notícias salvas
#   historico_noticias()
#   noticias_salvas()
def historico_noticias():
    # verifica qual é o usuário logado
    # id_usuario = tabelas['usuario'].read('id_usuario', email = usuario.email, search_type = 'email')[0][0]
    id_usuario = tabelas['usuario'].read('id_usuario', email = 'test@fake1.com', search_type = 'email')[0][0]

    # pega o id de todas as notícias q ele já acessou
    id_noticias_acessadas = tabelas['noticia_acessada'].read(select = 'id_noticia', id_usuario = id_usuario, search_type = 'id_usuario')
    # print(id_noticias_acessadas)
    # input()

    # com esse id, se coleta todas as informações dessas notícias
    noticias_acessadas = []
    for i in range(0, len(id_noticias_acessadas)):
        noticia_acessada = tabelas['noticia'].read(id_noticia = id_noticias_acessadas[i][0], search_type = 'id_noticia')
        # print(noticia_acessada)
        # input()
        noticias_acessadas.append(noticia_acessada)
    # retorna uma lista de tuplas com todas as informações das notícias acessadas pelo usuário logado
    # print("TERMINOU")
    # input()
    return noticias_acessadas


# Fica executando a tarefa 'atualiza_bd' a cada 'x' tempo
sched = BackgroundScheduler(daemon=True)
sched.add_job(atualiza_bd,'interval',seconds=120)
sched.start()


if __name__ == '__main__':
    atualiza_bd()
    app.static_folder = 'static'
    app.run(debug=False)

    # TESTANDO FUNCIONALIDADES
    # busca_noticia(busca = 'Lula') # vai ser utilizado na barra de pesquisa
    # salva_noticia(2066)
    # noticias_salvas()
    # historico_noticias()
    pass


# () INTEGRAR COM FRONT END
# () ARRUMAR FORMATO DA DATA NO BD NA HORA DE INSERIR AS NOTÍCIAS (só colocar horário além do ano-mês-dia)
# (ok) ARRUMAR INTERAÇÃO DO BANCO DE DADOS COM O SERVIDOR (era um bug nada a ver em config.py)
# (ok) ARRUMAR INSERÇÃO CORRETA DAS NOTÍCIAS NO BD
# (ok) INTEGRAR WEBSCRAP COM O BACKEND
# (ok) INTEGRAR SISTEMA DE RECOMENDAÇÃO COM O BACKEND
# (ok) ARRUMAR INSERÇÃO CORRETA DAS NOTÍCIAS NO BD
# (ok) AO INICIAR O SERVIDOR ATUALIZAR O BANCO DE DADOS COM AS 9 NOTICIAS PRINCIPAIS E AS 27 RELACIONADAS
# (ok) A CADA 120 SEGUNDOS ATUALIZAR O BANCO DE DADOS COM AS 9 NOTICIAS PRINCIPAIS E AS 27 RELACIONADAS
# (ok) COMPLETAR TODAS AS FUNCIONALIDADES DO SITE


# (ok)  USUARIO PODE FAZER LOGIN
# (ok)  USUARIO PODE FAZER CADASTRO
# (ok)  USUARIO 'PODE FAZER ASSINATURA' (vai pra mesma página de login)
# (ok)  USUARIO PODE BUSCAR NOTICIAS (o filtro é feito a partir de titulo e/ou texto)
# (ok)  USUARIO PODE VER ABA 'PARA VOCÊ' (SÓ SE ELE ESTIVER LOGADO, SE NÃO ESTIVER FLASHA 'FAZER LOGIN ETC.')
# (ok)    aba 'Para você' vai mostrar todas as notícias que o usuário já acessou
# (ok)    aba 'Para você' vai mostrar todas as notícias que o usuário já clicou em 'salvar'
