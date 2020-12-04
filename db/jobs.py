import json
from uuid import uuid4

from db.db import get_cursor, commit_db

CREATE_TABLE_JOBS_SQL = """
CREATE TABLE IF NOT EXISTS jobs (
 uuid GUID PRIMARY KEY,
 project_id varchar,
 branch varchar ,
 status VARCHAR ,
 steps json,
 FOREIGN KEY (project_id) REFERENCES projects (id))"""

INSERT_JOB_SQL = ''' INSERT INTO jobs(uuid, project_id, status) VALUES(?,?,'PENDING') '''


def get_jobs():
    return ""


def create_job(project_id):
    # https://docs.gitlab.com/ee/api/projects.html#get-single-project
    uuid = uuid4()
    get_cursor().execute(INSERT_JOB_SQL, (str(uuid), int(project_id)))
    commit_db()


def get_job_by_uuid(uuid):
    return get_cursor().execute("Select * from jobs where uuid= ? ;", (str(uuid),)).fetchone()


def update_job_step(uuid, step, status):
    job = get_job_by_uuid(uuid)
    info = job['info'] or []
    step['status'] = status
    info.append(step)
    # steps & env already stringified
    get_cursor().execute(" UPDATE jobs set steps = ? where uuid=? ",
                         (json.dumps(info), str(uuid)))
    commit_db()


def update_job_status(uuid, status):
    # steps & env already stringified
    get_cursor().execute(" UPDATE jobs set status= ?  where uuid=? ",
                         (status, uuid))
    commit_db()
