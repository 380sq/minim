import json

from flask import Blueprint, render_template, request, redirect

from db import add_project, get_projects, get_project_by_id, update_project_pipeline
from lib.gitlab import gitlab_get_project, gitlab_get_project_branches

projects = Blueprint('projects', __name__)


@projects.route('/projects', methods=["POST", "GET"])
def index():
    error = None
    if request.method == "POST":
        project_path_with_namespace = request.form.get('path_with_namespace')
        if project_path_with_namespace is not None:
            err, project = gitlab_get_project(project_path_with_namespace)
            if err:
                error = json.dumps(err)
            else:
                add_project(project)
        else:
            error = "no project selected"

    projects = get_projects()

    return render_template('index.html', projects=projects, error=error)


@projects.route('/projects/<id>')
def project(id):
    from lib.jobs import TYPES
    project = get_project_by_id(id)
    err, branches = gitlab_get_project_branches(id)
    if not branches:
        branches = []
    return render_template('project.html', project=project, branches=branches, types=json.dumps(TYPES), error=err)


@projects.route('/projects/<id>/pipeline', methods=["POST"])
def pipeline(id):
    steps = request.form.get('steps')
    env = request.form.get('envs')
    branch = request.form.get('branch')
    if steps is not None and env is not None:
        update_project_pipeline(id, branch, steps, env)

    return redirect('/projects/' + id)


@projects.route('/projects/<id>/run-pipeline', methods=["POST"])
def run_pipeline(id):
    from lib.socket import send_io_message
    send_io_message('test')
    from lib.jobs_runner import JobsRunner
    project = get_project_by_id(id)
    r = JobsRunner()
    r.run(project)
    return redirect('/projects/' + id)
