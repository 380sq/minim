from flask import session, request, redirect

from db.init import init_db
from lib.get_env import get_env, MINIM_FLASK_APP_SECRET_KEY
from lib.gitlab import gitlab_get_token
from routes import auth_blueprint, main_blueprint, settings_blueprint, projects_blueprint, hooks_blueprint


def config_app(app):
    app.config['SECRET_KEY'] = get_env(MINIM_FLASK_APP_SECRET_KEY)

    # init and configure
    init_db()

    @app.context_processor
    def inject_stage_and_region():
        return dict(no_gitalb_token=not gitlab_get_token())

    @app.before_request
    def check_valid_login():
        login_valid = 'user' in session  # or whatever you use to check valid login

        if (request.endpoint and
                'static' not in request.endpoint and
                not login_valid and
                not getattr(app.view_functions[request.endpoint], 'is_public', False)):
            return redirect('/login?next=' + request.path)

    # blueprint for main routes in our app
    app.register_blueprint(main_blueprint)

    # blueprint for auth routes in our app
    app.register_blueprint(auth_blueprint)

    # blueprint for settings routes in our app
    app.register_blueprint(settings_blueprint)

    # blueprint for settings routes in our app
    app.register_blueprint(projects_blueprint)

    # blueprint for settings routes in our app
    app.register_blueprint(hooks_blueprint)

    return app
