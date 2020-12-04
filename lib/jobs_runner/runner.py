import json
import os
import threading
from os import path

from db.jobs import create_job, update_job_status, update_job_step
from lib.gitlab import gitlab_download_artifact
from lib.jobs import KIND_ARTIFACT, KIND_DOCKER_BUILD
from .docker_job import build_docker_image
from .download_artifact_job import download_artifact


def run(project):
    pipeline_steps = json.loads(project['pipeline_steps'])
    pipeline_env = json.loads(project['pipeline_envs'])
    build_branch = project['build_branch']
    id_project = project['id']
    job = create_job(id_project)
    for step in pipeline_steps:
        if (step['type']) == KIND_ARTIFACT:
            info = json.loads(step['value'])
            print(info)
            if info:
                gitlab_job = info['job']
                if gitlab_job is not None:
                    print("gitlab_download_artifact in job %s for branch %s on project %s" % (
                        job, build_branch, str(id_project)))
                    status = download_artifact(job, KIND_ARTIFACT, gitlab_download_artifact(id_project, build_branch, gitlab_job))
                    update_job_step(job['uuid'], step, status)
        if (step['type']) == KIND_DOCKER_BUILD:
            # think about git here
            build_docker_image(path.join(os.getcwd(), 'Dockerfile'))


class JobsRunner(object):
    def __init__(self, interval=1):
        self.interval = interval

    def run(self, project):
        print('Running on >>> ' + str(project['id']))
        thread = threading.Thread(target=run, args=(project,))
        thread.daemon = True
        thread.start()
