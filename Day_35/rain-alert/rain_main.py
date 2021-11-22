import os

import requests
from twilio.rest import Client


api_key = os.environ.get("api_key")
my_lat = 10.222670
my_long = 93.243011
maximum_hr = 12
# account_sid = 'bfrwufqwjdgye546ASEDF'
# auth_token = os.environ.get("auth_token")
parameters = {
    'lat': my_lat,
    'lon': my_long,
    'appid': api_key,
    'exclude':'minutely,daily,currently'
}
response = requests.get('https://api.openweathermap.org/data/2.5/onecall', params=parameters)
response.raise_for_status()

data = response.json()
will_rain = False
for hr in range(maximum_hr):
    weather_id = (data['hourly'][hr]['weather'][0]['id'])
    if weather_id <=700:
        will_rain = True

if will_rain:
     print("Bring an umbrella.")
## Get rain alert message
    # client = Client(account_sid,auth_token)
    # message = client.messages\
    #         .create(
    #     body='Bring an Umbrella, it will ☔️',
    #     from= '+123456789',
    #     to = '+987654321'
    # )
    # print(message.status)