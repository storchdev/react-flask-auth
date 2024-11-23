"""
This module provides functions to interact with an SQLite database.
"""

import sqlite3
from typing import List, Tuple, Any


# Helper function to interact with the database
def query_db(query: str, args: Tuple[Any] = (), *, one: bool | None = False) \
        -> sqlite3.Row | List[sqlite3.Row] | None:

    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(query, args)

    if one:
        rv = cur.fetchone()
    else:
        rv = cur.fetchall()

    conn.commit()
    conn.close()
    return rv


# Create tables
def init_db():
    query = '''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password_hash TEXT NOT NULL
        )
    '''
    query_db(query)
