from flask import Blueprint, render_template, request, redirect

from lib.gitlab import gitlab_set_token, gitlab_get_token

settings = Blueprint('settings', __name__)


@settings.route('/settings', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        gitlab_token = request.form.get('gitlab_token')
        if gitlab_token is not None:
            gitlab_set_token(gitlab_token)
            return redirect('/')

    return render_template('settings.html', token=gitlab_get_token())
