from app import app
from flask import render_template


@app.route('/')
def hello():
    user = 'Vitória'
    return render_template('index.html', nome1 = user)

@app.route('/')
def home():
    usuario = { 
        'nome' : 'Vitória',
        'produtos' : ['Banana', 'Abacaxi', 'Melancia']
    }
    logado = True
    return render_template('index.html', usuario = usuario, logado = logado)

@app.route('/endereco')
def hola():
    return 'Moro em Ceará-Mirim/RN'

@app.route('/preferidos')
def ola():
    return 'Gosto de ler livros, assistir séries, viajar e sair com meus amigos'