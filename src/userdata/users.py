import os
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)



@app.route('/add_company', methods=['POST'])
def add_company():
    data = request.get_json()
    company_name = data['company_name']
    user_id = data['userid']
    with sqlite3.connect('./src/userdata.db') as conn:
        conn.execute('INSERT INTO usercompanies (userid, company_name) VALUES (?, ?)', (user_id, company_name))
    conn.close()
    return '', 201

@app.route('/get_companies', methods=['GET'])
def get_companies():
    user_id = request.args.get('userid')
    with sqlite3.connect('./src/userdata.db') as conn:
        cursor = conn.execute('SELECT company_name FROM usercompanies WHERE userid = ?', (user_id,))
        companies = [{'company_name': row[0]} for row in cursor.fetchall()]
    conn.close()
    return jsonify(companies)

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    user_name = data['user_name']   
    with sqlite3.connect('./src/userdata.db') as conn:
        conn.execute('INSERT INTO users (user_name) VALUES (?)', (user_name,))
    conn.close()
    return '', 201

@app.route('/get_users', methods=['GET'])
def get_users():
    with sqlite3.connect('./src/userdata.db') as conn:
        cursor = conn.execute('SELECT user_name FROM users')
        users = [{'user_name': row[0]} for row in cursor.fetchall()]
    conn.close()
    return jsonify(users)

@app.route('/get_user', methods=['GET'])
def get_user():
    user_name = request.args.get('user_name')
    with sqlite3.connect('./src/userdata.db') as conn:
        cursor = conn.execute('SELECT userid FROM users WHERE user_name = ?', (user_name,))
        user = [{'userid': row[0]} for row in cursor.fetchall()]
    conn.close()
    return jsonify(user)
    

