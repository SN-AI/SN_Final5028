This app is the backend for serving a client app where the user can input a company name, receive current headlines, and have those headlines analyzed for sentiment extraction to indicate positive, negative, neutral, or mixed.

There is a collection folder that houses the python for retrieving news articles from NewsAPI.org

There is an analysis folder that houses the sentimentAnalysis engine which takes one title and returns the given sentiment.

The app.py file is the primary executable for FLASK_APP

The routes.py file contains all of the routing details and logic to support the active server

