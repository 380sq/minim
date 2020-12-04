from flask import Blueprint, redirect

main = Blueprint('main', __name__)


@main.route('/', methods=["GET"])
def index():
    return redirect('/projects')
