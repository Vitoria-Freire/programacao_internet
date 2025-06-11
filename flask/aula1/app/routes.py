from app import app
from flask import render_template
from app.forms.login_form import LoginForm
from app.controllers.authenticationController import AutheticationController

@app.route('/')
def hello():
    return render_template('index.html', usuario = None, usuario_logado = False)

@app.route('/sobre')
def sob():
    #user = 'Vitória'
    return render_template('sobre.html')

@app.route('/contato')
def hola():
    return render_template('contato.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    formulario = LoginForm()
    if formulario.validate_on_submit():
        return AutheticationController.login(formulario)
    return render_template('login.html', title='Login', form=formulario)
    
@app.route('/preferidos')
def ola():
    return 'Gosto de ler livros, assistir séries, viajar e sair com meus amigos'