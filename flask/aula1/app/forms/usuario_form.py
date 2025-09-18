from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email

class UsuarioForm(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired(message="Por favor, preencha o seu nome de usuário.")])
    email = EmailField('Email', validators=[DataRequired(message="Por favor, preencha o email."), Email(message='Email inválido.')])
    # password = StringField('Senha', validators=[DataRequired(message="Por favor, preencha a senha.")])
    botao_salvar = SubmitField('Salvar')