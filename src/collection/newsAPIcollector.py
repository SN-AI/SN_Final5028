import asyncio
import json
import aiohttp

class NewsAPIArticle:
    def __init__(self, publisher, title, description, url, publishedAt):
        self.publisher = publisher
        self.title = title
        self.description = description
        self.url = url
        self.publishedAt = publishedAt

class NewsAPIClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.session = aiohttp.ClientSession()

    async def get_articles_json(self, company):
        url = "https://newsapi.org/v2/everything"
        params = {
            "q": company,
            "apiKey": self.api_key,
            "pageSize": 5
        }

        try:
            async with self.session.get(url, params=params) as response:
                if response.status != 200:
                    print(f"Error: Received status code {response.status}")
                    return None
                articles_json = await response.text()
                
                return articles_json
        except aiohttp.ClientError as e:
            print(f"HTTP request failed: {e}")
            return None

    async def parse_articles_json(self, json_str):
        articles_list = []

        try:
            json_data = json.loads(json_str)
            for article in json_data.get("articles", []):
                news_article = NewsAPIArticle(
                    publisher=article.get("source", {}).get("name"),
                    title=article.get("title"),
                    description=article.get("description"),
                    url=article.get("url"),
                    publishedAt=article.get("publishedAt")
                )
                articles_list.append(news_article)
        except json.JSONDecodeError as e:
            print(f"JSON decoding failed: {e}")

        return articles_list

    async def close(self):
        await self.session.close()

# Example usage
async def main():
    api_key = "1993f371257c43b6981695d55e11a47b"
    client = NewsAPIClient(api_key)
    articles_json = await client.get_articles_json("Microsoft")
    if articles_json:
        articles = await client.parse_articles_json(articles_json)
        for article in articles:
            print(article.title)
    await client.close()

# Run the example
asyncio.run(main())