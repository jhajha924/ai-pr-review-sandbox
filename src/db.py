import os
import sqlite3

DB_PASSWORD = os.environ.get("DB_PASSWORD", "")


def connect(path):
    """開啟 sqlite 連線。"""
    return sqlite3.connect(path)


def find_user(conn, name):
    """以參數化查詢取得指定名稱的使用者。"""
    sql = "SELECT * FROM users WHERE name = ?"
    return conn.execute(sql, (name,)).fetchall()
