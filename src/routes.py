import aiohttp
import json
import asyncio
from flask import Flask, request, jsonify
from collection.newsAPIcollector import NewsAPIClient
from analysis.sentimentAnalysis import sentiment_analysis

app = Flask(__name__)

api_key = "1993f371257c43b6981695d55e11a47b"
news_client = NewsAPIClient(api_key)


@app.route("/get_sentiment", methods=["POST"])
async def get_sentiment():
    company_name = request.form.get("company_name")
    if not company_name:
        return jsonify({"error": "Please provide a company name"}), 400

    async with aiohttp.ClientSession() as session:
        url = "https://newsapi.org/v2/everything"
        params = {
            "q": company_name,
            "apiKey": api_key,
            "pageSize": 5
        }
        async with session.get(url, params=params) as response:
            if response.status != 200:
                return jsonify({"error": f"Failed to get articles from NewsAPI! Status code: {response.status}"}), response.status
            try:
                articles_json = await response.json()
                articles = await news_client.parse_articles_json(articles_json)
            except aiohttp.ContentTypeError:
                return jsonify({"error": "Invalid JSON response!"}), 500
    
    if isinstance(articles_json, dict) and 'articles' in articles_json:
        articles = articles_json['articles']
    else:
        return jsonify({"error": "Failed to parse articles from NewsAPI response!"}), 500
    
    titles = [article["title"] for article in articles]
    sentiments = [{"title": title, "sentiment": sentiment_analysis(title)} for title in titles]
    return jsonify({"results": sentiments})

@app.route("/get_articles", methods=["POST"])
async def get_articles():
    company_name = request.form.get("company_name")

    async with aiohttp.ClientSession() as session:
        url = "https://newsapi.org/v2/everything"
        params = {
            "q": company_name,
            "apiKey": api_key,
            "pageSize": 5
        }
        async with session.get(url, params=params) as response:
            if response.status != 200:
                return "Failed to get articles from NewsAPI!"
            articles_json = await response.json()
            articles = await news_client.parse_articles_json(articles_json)
            
            if isinstance(articles_json, dict) and 'articles' in articles_json:
                articles = articles_json['articles']
            else:
                return jsonify({"error": "Failed to parse articles from NewsAPI response!"}), 500
            
            titles = [article["title"] for article in articles]
            return jsonify(titles)
        
@app.route("/")
def home():
    return "The server is running!"