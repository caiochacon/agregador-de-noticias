from flask import render_template, redirect, url_for, request, flash
from apscheduler.schedulers.background import BackgroundScheduler
from importlib.machinery import SourceFileLoader
from passlib.hash import sha256_crypt
from models import User
from flask import Flask
from gerador import *

usuario = User()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

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
    return redirect(url_for('profile'))


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

@app.route('/profile')
def profile():
    return render_template('profile.html', name=usuario.name, email=usuario.email)

@app.route('/logout')
def logout():
    usuario.logout()
    return redirect(url_for('home'))

def atualiza_bd():

    webscrap_dataset()
    gera_principais_e_recomendados()

    print("Banco de dados foi atualizado com sucesso.")

def webscrap_dataset():
    webscrap = SourceFileLoader("tabelas", "/home/vinicius_olzon/Documents/ENG_SOFTWARE/backend/flask_app/web_scrapping/src/scrapy_runner.py").load_module()
    input()
    scrapper = webscrap.ScrapyRunner()
    print("TA VARRENO")
    scrapper.run()

def gera_principais_e_recomendados():
    recomendacao = SourceFileLoader("tabelas", "/home/vinicius_olzon/Documents/ENG_SOFTWARE/backend/flask_app/agregador_de_noticias_recommendation_system/notebooks/recommendation.py").load_module()
    # Retorna X notícias mais recentes de cada portal 
    dataset_top_news, df_to_recomendations = recomendacao.catcher.catch_top_news('/home/vinicius_olzon/Documents/ENG_SOFTWARE/backend/flask_app/agregador_de_noticias_recommendation_system/dataset/noticiasGeradas.csv')
    # Retorna as x notícias principais e 3 notícias relacionadas a cada uma delas
    dataset_topnews, dataset_recomendations = recomendacao.recomendation_system.run(dataset_top_news, df_to_recomendations)

    # Armazena as informações das X notícias mais recentes e as guarda no banco de dados
    tupla_principal = [tuple(x) for x in dataset_topnews.to_numpy()]
    # Armazena as informações das 3 notícias mais relacionadas dessas X notícias no banco de dados
    tupla_relacionada = [tuple(x) for x in dataset_recomendations.to_numpy()]

    # Insere a notícia principal
    for i in range(len(tupla_principal)):
        titulo = tupla_principal[i][1]
        data_publicacao = '2024-05-03'
        categoria = tupla_principal[i][6]
        texto = tupla_principal[i][3]
        fonte = tupla_principal[i][7]
        link = tupla_principal[i][4]
        imagem = tupla_principal[i][5]
        tabelas['noticia'].insert(titulo = titulo, data_publicacao = data_publicacao, categoria = categoria, texto = texto, fonte = fonte, link = link, imagem = imagem)
        # Insere 3 notícias relacionadas a anterior
        for j in range(i+(i*2), (i*2)+i+3):
            tabelas['noticia'].insert(titulo = tupla_relacionada[j][1], data_publicacao =  '2024-05-03', categoria = tupla_relacionada[j][6], texto = tupla_relacionada[j][3], fonte = tupla_relacionada[j][7], link = tupla_relacionada[j][4], imagem = tupla_relacionada[j][5])

# Fica executando a tarefa 'atualiza_bd' a cada 'x' tempo
sched = BackgroundScheduler(daemon=True)
sched.add_job(atualiza_bd,'interval',seconds=1)
sched.start()

if __name__ == '__main__':
    app.run(debug=False)
