from app import db
import sqlalchemy as sa
from app.models import Post

class PostController:
    def postar(form, usuario):
        try:
            post = Post()
            form.populate_obj(post)
            post.user_id = usuario

            db.session.add(post)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(e)
            return False