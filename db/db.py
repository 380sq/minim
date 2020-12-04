import os
import sqlite3

from lib.helpers import create_file_if_not_exists

DEFAULT_DB_PATH = os.path.join(os.path.dirname(__file__), 'database.sqlite3')


create_file_if_not_exists(DEFAULT_DB_PATH)

con = sqlite3.connect(DEFAULT_DB_PATH, check_same_thread=False)
con.row_factory = sqlite3.Row


def commit_db():
    con.commit()


def get_cursor():
    return con.cursor()
