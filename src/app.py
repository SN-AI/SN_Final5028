#!/usr/bin/env python3


from flask import Flask, request, jsonify
from routes import home, get_articles, get_sentiment
from userdata.users import add_company, get_companies, add_user, get_users, get_user
from config import Config
from flask_sqlalchemy import SQLAlchemy

# Create Flask app instance
app = Flask(__name__)
app.config.from_object(Config)

# initialize db
db = SQLAlchemy(app)

# Register routes
    
app.add_url_rule('/', 'home', home)
app.add_url_rule('/articles', 'get_articles', get_articles, methods=['POST'])
app.add_url_rule('/articles/sentiment', 'get_sentiment', get_sentiment, methods=['POST'])
app.add_url_rule('/add_company', 'add_company', add_company, methods=['POST'])
app.add_url_rule('/get_companies', 'get_companies', get_companies, methods=['GET'])
app.add_url_rule('/add_user', 'add_user', add_user, methods=['POST'])
app.add_url_rule('/get_users', 'get_users', get_users, methods=['GET'])
app.add_url_rule('/get_user', 'get_user', get_user, methods=['GET'])


# Run the app
if __name__ == "__main__":
    app.run()