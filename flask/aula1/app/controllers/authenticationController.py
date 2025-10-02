from flask import render_template, flash
from app.models.usuario import Usuario
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash

class AutheticationController:

    def login(formulario):
        username = formulario.username.data.strip()
        user = Usuario.query.filter_by(username=username).first()

        if user:
            if check_password_hash(user.password_hash,formulario.password.data):
                login_user(user, remember=formulario.remember_me.data)
                return True
            else:
                return False
            
    def logout():
        return logout_user()