import sqlite3

DB_PASSWORD = "P@ssw0rd123"


def connect(path):
    conn = sqlite3.connect(path)
    return conn


def find_user(conn, name):
    sql = "SELECT * FROM users WHERE name = '" + name + "'"
    return conn.execute(sql).fetchall()
