from flask import Blueprint, request, session, render_template, redirect

from lib import public_endpoint
from lib.get_env import get_env, MINIM_AUTH_KEY

auth = Blueprint('auth', __name__)


@public_endpoint
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        if request.form.get('token') == get_env(MINIM_AUTH_KEY):
            session['user'] = 'ok'
            next_url = request.form.get('next_url')
            return redirect(next_url or '/')

    return render_template('login.html', next=request.args.get('next'))


@auth.route('/logout')
def logout():
    if 'user' in session:
        del session['user']
    return redirect('/')
