import requests
from twilio.rest import Client

Stock_api_key = 'HYMSAA95KIYESMOD'
News_api = '83f59bfcd80d442b8ba99970ae463a3d'
Twilio_sid = '********************'
Twilio_auth_token = '*********************'

STOCK_NAME = 'TSLA'
COMPANY_NAME = 'Tesla Inc'

Stock_endpoint = 'https://www.alphavantage.co/query'
News_endpoint = 'https://newsapi.org/v2/everything'

stock_parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK_NAME,
    'apikey': Stock_api_key
}

news_parameters = {
    'qInTitle':STOCK_NAME,
    'apikey':News_api
}

# fetch the stock
response = requests.get(Stock_endpoint, params=stock_parameters)
data = response.json()['Time Series (Daily)']
data_list = [value for (key,value) in data.items()]

yesterday_data = data_list[0]
day_before_yesterday_data = data_list[1]

yesterday_closing_rate = float(yesterday_data['4. close'])
day_before_yesterday_closing_rate = float(day_before_yesterday_data['4. close'])

difference = abs(yesterday_closing_rate-day_before_yesterday_closing_rate)
percentage_change = (difference/yesterday_closing_rate)*100
if percentage_change > 4:
    news_response = requests.get(News_endpoint,news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()
    articles = news_data['articles']
    three_articles = articles[:3]
    formatted_articles_list = [f"Headline:{article['title']}.\n Brief:{article['description']}" for article in three_articles]
    print(formatted_articles_list)

# sms sending using twilio
# client = Client(Twilio_sid,Twilio_auth_token)
# for each_article in formatted_articles_list:
#     message = client.messages \
#         .create(
#         body= each_article,
#         from = '123456789',
#         to = '987654321'
#     )
#



