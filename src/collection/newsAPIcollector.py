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
        
    async def init_session(self):
        self.session = aiohttp.ClientSession()
    
    async def close_session(self):
        await self.session.close()

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
        if isinstance(json_str, dict):
            return json_str
        return json.loads(json_str)

    async def close(self):
        await self.session.close()

# Example usage
async def main():
    api_key = "1993f371257c43b6981695d55e11a47b"
    news_client = NewsAPIClient(api_key)
    await news_client.init_session()
    articles_json = await news_client.get_articles_json("Microsoft")
    if articles_json:
        articles = await news_client.parse_articles_json(articles_json)
        for article in articles:
            print(article.title)
    await news_client.close()

# Run the example
if __name__ == "__main__":
    asyncio.run(main())