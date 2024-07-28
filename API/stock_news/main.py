import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os


# Constants
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

load_dotenv()  # Load environment variables from .env file

STOCK_API_KEY = os.getenv('STOCK_API_KEY')
NEWS_API_KEY = os.getenv('NEWS_API_KEY')
ACCOUNT_SID = os.getenv('ACCOUNT_SID')
AUTH_TOKEN = os.getenv('AUTH_TOKEN')
WHATSAPP_FROM = os.getenv('WHATSAPP_FROM')
WHATSAPP_TO = os.getenv('WHATSAPP_TO')


def fetch_stock_data():
    """Fetches the daily stock prices."""
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": STOCK_API_KEY
    }
    
    response = requests.get(STOCK_ENDPOINT, params=params, verify=False)
    response.raise_for_status()
    return response.json().get("Time Series (Daily)", {})

def calculate_stock_change(stock_data):
    """Calculates the percentage change between the closing prices of the last two days."""
    dates = list(stock_data.items())[:2]
    if len(dates) < 2:
        return 0

    closing_price_yesterday = float(dates[0][1]["4. close"])
    closing_price_day_before = float(dates[1][1]["4. close"])
    change_percentage = abs((closing_price_yesterday - closing_price_day_before) / closing_price_yesterday) * 100
    return change_percentage

def fetch_news():
    """Fetches the latest news articles for the company."""
    params = {
        "q": COMPANY_NAME,
        "language": "en",
        "apiKey": NEWS_API_KEY
    }
    
    response = requests.get(NEWS_ENDPOINT, params=params)
    response.raise_for_status()
    return response.json().get("articles", [])[:3]  # Get the first 3 articles



def send_whatsapp_message(articles):
    """Sends news articles via WhatsApp using the Twilio API."""
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    
    for article in articles:
        title = article['title']
        description = article['description'].replace('\n', ' ').strip()
        url = article['url']
        message_body = f"Headline: {title}\nBrief: {description}\nURL: {url}"
        message = client.messages.create(
            from_=WHATSAPP_FROM,
            body=message_body,
            to=WHATSAPP_TO
        )
        print(f"Message sent with status: {message.status}")
        


        
def main():
    """Main function to check stock price change and send news if applicable."""
    stock_data = fetch_stock_data()
    stock_change_percentage = calculate_stock_change(stock_data)
    
    if stock_change_percentage >5:
        articles = fetch_news()
        if articles:
            send_whatsapp_message(articles)
        else:
            print("No news articles found.")
    else:
        print("Stock price change is less than 5%. No news to fetch.")


if __name__ == "__main__":
    main()
        



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

