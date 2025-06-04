from app import app
from flask import render_template


@app.route('/')
def hello():
    #user = 'Vitória'
    return render_template('index.html')

@app.route('/sobre')
def sob():
    #user = 'Vitória'
    return render_template('sobre.html')

# @app.route('/')
# def home():
#     usuario = { 
#         'nome' : 'Vitória',
#         'produtos' : ['Banana', 'Abacaxi', 'Melancia']
#     }
#     logado = True
#     return render_template('index.html', usuario = usuario, logado = logado)

@app.route('/contato')
def hola():
    return render_template('contato.html')

@app.route('/preferidos')
def ola():
    return 'Gosto de ler livros, assistir séries, viajar e sair com meus amigos'