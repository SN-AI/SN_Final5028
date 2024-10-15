# src/userdata/users.py

import os
from flask import Flask, request, jsonify
import sqlite3
from ..config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('Config')

db = SQLAlchemy(app)

# models
class User(db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(80), unique=True, nullable=False)

class UserCompanies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('user.userid'), nullable=False)
    company_name = db.Column(db.String(80), nullable=False)

# DB Table Creation
with app.app_context():
    db.create_all()

@app.route('/add_company', methods=['POST'])
def add_company():
    data = request.get_json()
    company_name = data['company_name']
    user_id = data['userid']
    new_company = UserCompanies(userid=user_id, company_name=company_name)
    db.session.add(new_company)
    db.session.commit()
    return '', 201

@app.route('/get_companies', methods=['GET'])
def get_companies():
    user_id = request.args.get('userid')
    companies = UserCompanies.query.filter_by(userid=user_id).all()
    companies_list = [{'company_name': company.company_name} for company in companies]
    return jsonify(companies_list)

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    user_name = data['user_name']
    new_user = User(user_name=user_name)
    db.session.add(new_user)
    db.session.commit()
    return '', 201

@app.route('/get_users', methods=['GET'])
def get_users():
    users = User.query.all()
    users_list = [{'user_name': user.user_name} for user in users]
    return jsonify(users_list)

@app.route('/get_user', methods=['GET'])
def get_user():
    user_name = request.args.get('user_name')
    user = User.query.filter_by(user_name=user_name).first()
    if user:
        return jsonify({'userid': user.userid})
    else:
        return jsonify({'error': 'User not found'}), 404
    

