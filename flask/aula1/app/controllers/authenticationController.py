from flask import redirect, render_template, flash

class AutheticationController:

    def login(form):
        flash(f'O usuario {form.username.data} fez o login, lembrar={form.remember_me.data}')
        usuario = {
            'nome': form.username.data
        }
        return render_template('index.html', usuario = usuario, usuario_logado = True)
