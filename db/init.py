from db.db import get_cursor
from db.jobs import CREATE_TABLE_JOBS_SQL
from db.projects import CREATE_TABLE_PROJECTS_SQL


def init_db():
    get_cursor().execute(CREATE_TABLE_JOBS_SQL)
    get_cursor().execute(CREATE_TABLE_PROJECTS_SQL)

