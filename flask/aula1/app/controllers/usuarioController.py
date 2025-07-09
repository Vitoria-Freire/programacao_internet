from flask import render_template, flash
from app import db
import sqlalchemy as sa


from app.models import Usuario

class UsuarioController:
    
    def cadastrar_usuario(form):
        usuario = Usuario()
        form.populate_obj(usuario)
        
        db.session.add(usuario)
        db.session.commit()
        flash(f"O usuario {usuario.username} foi cadastrado com sucesso!")
        return render_template("index.html", usuario = usuario)
    
    
    def listar_usuarios():
        query = sa.select(Usuario)
        usuarios = db.session.scalars(query)
        return usuarios
    
    
    def buscar_por_username(username):
        query = sa.select(Usuario).where(Usuario.username == username)
        usuario = db.session.scalars(query).first()
        return usuario
    
    
    def atualizar_usuario(id, form):
        usuario = db.session.get(Usuario, id)
        if usuario:
            usuario.username = form.username
            db.session.commit()
            print('Usuário atualizado com sucesso!')
        else:
            print('Usuário não encontrado.')
            
            
    def remover_usuario(id):
        usuario = db.session.get(Usuario, id)
        if usuario:
            db.session.delete(usuario)
            db.session.commit()
            print('Usuário removido com sucesso!')
        else:
            print('Usuário não encontrado.')