# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, BooleanField, SubmitField
# from wtforms.validators import DataRequired

# class UsuarioForm(FlaskForm):
#     username = StringField('Usuário', validators=[DataRequired()])
#     email = StringField('Email', validators=[DataRequired()])
#     password_hash = PasswordField('Senha', validators=[DataRequired()])
#     submit = SubmitField('Cadastrar')

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email

class UsuarioForm(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired(message="Por favor, preencha o seu nome de usuário.")])
    email = EmailField('Email', validators=[DataRequired(message="Por favor, preencha o email."), Email(message='Email inválido.')])
    botao_salvar = SubmitField('Salvar')