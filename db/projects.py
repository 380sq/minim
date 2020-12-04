from db.db import get_cursor, commit_db
from uuid import uuid4
from json import dumps

CREATE_TABLE_PROJECTS_SQL = """
CREATE TABLE IF NOT EXISTS projects (
 uuid GUID PRIMARY KEY ,
 id INTEGER unique,
 name TEXT unique,
 build_branch varchar,
 pipeline_steps json, 
 pipeline_envs json, 
 info json )"""

SELECT_PROJECTS_SQL = """ SELECT * from projects LIMIT ? OFFSET ? """

INSERT_PROJECT_SQL = """ INSERT INTO projects(uuid, id, 'name', info) VALUES(?,?,?,?) """


def get_projects(**kwargs):
    page = kwargs['page'] if 'page' in kwargs else 10
    page_size = kwargs['page_size'] if 'page_size' in kwargs else 0
    print(page)
    print(page_size)
    return get_cursor().execute(SELECT_PROJECTS_SQL, (page, page_size * page)).fetchall()


def add_project(project):
    # https://docs.gitlab.com/ee/api/projects.html#get-single-project
    print("add_project")
    print(project)
    uuid = uuid4()
    name = project['path_with_namespace']
    id = project['id']
    get_cursor().execute(INSERT_PROJECT_SQL, (str(uuid), int(id), name, dumps(project)))
    commit_db()


def get_project_by_id(id):
    return get_cursor().execute("Select * from projects where id= ? ;", (str(id),)).fetchone()


def get_project_by_uuid(uuid):
    return get_cursor().execute("Select * from projects where uuid=? ;", uuid)


def update_project_pipeline(id, branch, steps, env):
    # steps & env already stringified
    get_cursor().execute(" UPDATE projects set build_branch= ?, pipeline_steps= ?, pipeline_envs= ? where id=? ",
                         (branch, steps, env, id))
    commit_db()
