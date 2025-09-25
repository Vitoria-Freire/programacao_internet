# from app import app
# from flask import render_template, redirect
# from app.forms.login_form import LoginForm, UserForm
# from app.controllers.authenticationController import AutheticationController
# from app.models import Usuario
# from app import db
# import sqlalchemy as sa

# @app.route('/')
# def hello():
#     return render_template('index.html', usuario = None, usuario_logado = False)

# @app.route('/sobre')
# def sob():
#     return render_template('sobre.html')

# @app.route('/contato')
# def hola():
#     return render_template('contato.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     formulario = LoginForm()
#     if formulario.validate_on_submit():
#         return AutheticationController.login(formulario)
#     return render_template('login.html', title='Login', form=formulario)
    
# @app.route('/inserir', methods=['GET', 'POST'])
# def inserindo():
#     formulario = UserForm()
#     if formulario.validate_on_submit():
#         usuario = Usuario (
#             username = formulario.username.data,
#             email = formulario.email.data,
#             password_hash =formulario.password.data
#         )
#         db.session.add(usuario)
#         db.session.commit()
#         return redirect('/')
#     return render_template('login.html', title='Cadastro', form=formulario)

from app import app
from app import db
from flask import render_template, flash, redirect, url_for
from app.forms.login_form import LoginForm
from app.forms.usuario_form import UsuarioForm
from app.forms.post_form import PostForm
from app.models import Usuario, Post
from app.controllers.authenticationController import AutheticationController
from app.controllers.usuarioController import UsuarioController
from app.controllers.postController import PostController
from app.forms.usuario_form import UsuarioForm


@app.route("/")
def home():
    return render_template("index.html", usuario = None, usuario_logado = False)


@app.route("/sobre")
def sobre():
    return "Página Sobre"


@app.route("/login", methods=['GET', 'POST'])
def login():
    formulario = LoginForm()
    if formulario.validate_on_submit():
        return UsuarioController.login(formulario)
    return render_template('login.html', title='Login', form = formulario)


@app.route("/inserir", methods=['GET', 'POST'])
def cadastrar_usuario():
    formulario = UsuarioForm()
    if formulario.validate_on_submit():
        return UsuarioController.salvar(formulario)
    return render_template('cadastro.html', title='Cadastro de Usuario', form = formulario)


@app.route('/listar', methods=['GET'])
def listar():
    usuarios = UsuarioController.listar_usuarios()
    for user in usuarios:
        print(user.id, user.username, user.email)
    return render_template("index.html")


@app.route('/listar_filtro', methods=['GET'])
def listar_com_filtro():
    username = 'leosilva'
    usuario = UsuarioController.buscar_por_username(username)
    print(usuario.id, usuario.username, usuario.email)    
    return render_template("index.html")


@app.route('/atualizar/<int:id>', methods=['GET'])
def atualizar(id):
    form = UsuarioForm()
    form.username = 'atualizei_de_novo'
    UsuarioController.atualizar_usuario(id, form)
    return render_template("index.html")


@app.route('/remover/<int:id>', methods=['GET'])
def remover(id):
    UsuarioController.remover_usuario(id)
    return render_template("index.html")

@app.route('/cadastrar', methods= ['GET', 'POST'])
def cadastrar():
    formulario = UsuarioForm()
    if formulario.validate_on_submit():
        sucesso = UsuarioController.salvar(formulario)
        if sucesso:
            flash('Usuário cadastrado com sucesso!', category='success')
            return redirect(url_for('login'))
        else: 
            flash('Erro ao cadastrar o novo usuário.', category='error')
            return render_template('cadastro.html', form = formulario)
    return render_template('cadastro.html', form = formulario)

@app.route('/post', methods=['GET', 'POST'])
def post():
    form = PostForm()
    if form.validate_on_submit():
        sucesso = PostController.postar(form, 3)
        if sucesso:
            flash('Post publicado com sucesso!', category='success')
            return render_template('index.html')
        else: 
            flash('Erro ao cadastrar o novo usuario.', category='error')
            return render_template('post.html', form = form)
    return render_template('post.html', title='Novo Post', form=form)