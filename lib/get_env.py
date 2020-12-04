from os import environ

MINIM_FLASK_APP_SECRET_KEY = "MINIM_FLASK_APP_SECRET_KEY"
MINIM_AUTH_KEY = "MINIM_AUTH_KEY"
MINIM_GITLAB_TOKEN = "MINIM_GITLAB_TOKEN"
PORT = "PORT"

def get_env(value):
    return environ[value] if value in environ else None