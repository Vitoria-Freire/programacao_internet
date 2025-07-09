from app.models.usuario import Usuario
from app import app, db

class UsuarioController:

    def salvar(formulario):
        try:
            usuario = Usuario()
            formulario.populate_obj(usuario)
            db.session.add(usuario)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return False