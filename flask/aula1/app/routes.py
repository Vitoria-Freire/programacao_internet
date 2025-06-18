from app import app
from flask import render_template, redirect
from app.forms.login_form import LoginForm, UserForm
from app.controllers.authenticationController import AutheticationController
from app.models import Usuario
from app import db

@app.route('/')
def hello():
    return render_template('index.html', usuario = None, usuario_logado = False)

@app.route('/sobre')
def sob():
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
    
@app.route('/inserir', methods=['GET', 'POST'])
def inserindo():
    formulario = UserForm()
    if formulario.validate_on_submit():
        usuario = Usuario (
            username = formulario.username.data,
            email = formulario.email.data,
            password_hash =formulario.password.data
        )
        db.session.add(usuario)
        db.session.commit()
        return redirect('/')
    return render_template('login.html', title='Cadastro', form=formulario)


