import urllib
import requests

API_PATH = "https://gitlab.com/api/v4"
from lib.get_env import get_env, MINIM_GITLAB_TOKEN

GITLAB_TOKEN_VALUE = "GITLAB_TOKEN_VALUE"

config = {GITLAB_TOKEN_VALUE: get_env(MINIM_GITLAB_TOKEN)}


def gitlab_set_token(value):
    config[GITLAB_TOKEN_VALUE] = value


def gitlab_get_token():
    return config[GITLAB_TOKEN_VALUE]


def get_headers():
    return {'PRIVATE-TOKEN': gitlab_get_token()}


def get_gitlab_projects(username):
    res = requests.get(API_PATH + "/users/%s/projects" % username, headers=get_headers())
    if res.status_code == 200:
        return None, res.json()
    return res.json(), None


def gitlab_get_project(project_path_with_namespace):
    url_path = urllib.parse.quote(project_path_with_namespace, safe='')
    print(">>> url : ")
    print(url_path)
    res = requests.get(API_PATH + "/projects/" + url_path,
                       headers=get_headers())
    if res.status_code == 200:
        return None, res.json()
    return res.json(), None


def gitlab_get_project_branches(id):
    print(">>> url : ")
    print(API_PATH + "/projects/%s/repository/branches/" % id)
    res = requests.get(API_PATH + "/projects/%s/repository/branches/" % id,
                       headers=get_headers())
    if res.status_code == 200:
        return None, res.json()
    return res.json(), None


def gitlab_download_artifact(id, ref_name, job):
    print(">>> url : ")
    print(API_PATH + "/projects/%s/jobs/artifacts/%s/download?job=%s" % (id, ref_name, job))
    return requests.get(API_PATH + "/projects/%s/jobs/artifacts/%s/download?job=%s" % (id, ref_name, job),
                        headers=get_headers(), stream=True)
