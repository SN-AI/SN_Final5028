import sqlite3
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_dir, '../userdata.db')

def init_usersdb():
    with sqlite3.connect(db_path) as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS users (userid INTEGER PRIMARY KEY, user_name TEXT)')
    conn.commit()
    conn.close()

def init_usercompaniesdb():
    with sqlite3.connect(db_path) as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS usercompanies (id INTEGER PRIMARY KEY AUTOINCREMENT, userid INTEGER, company_name TEXT, FOREIGN KEY (userid) REFERENCES users(userid))''')
    conn.commit()
    conn.close()


if __name__ == '__main__':
    init_usersdb()
    init_usercompaniesdb()