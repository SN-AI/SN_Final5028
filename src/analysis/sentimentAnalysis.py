from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

def sentiment_analysis(text):
    endpoint = "https://sentiment-algo-string.cognitiveservices.azure.com/"
    key = "b851ce0e48c44315b1455ed920d60a7e"  # valid until October 20 2024

    text_analytics_client = TextAnalyticsClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(key)
    )

    try:
        response = text_analytics_client.analyze_sentiment(documents=[text])[0]
        sentiment = response.sentiment
        return sentiment
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
