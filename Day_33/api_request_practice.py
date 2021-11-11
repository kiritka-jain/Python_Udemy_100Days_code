import requests
from datetime import datetime

# response = requests.get("http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
#
# lattitude = data['iss_position']['latitude']
# longitude = data['iss_position']['longitude']
# iss_position = (lattitude,longitude)
#
# print(iss_position)
my_lat = 20.593683
my_long = 78.962883
formatted_int = 0

parameters = {
    'lat': my_lat,
    'long': my_long,
    'formatted': formatted_int
}
response = requests.get("https://api.sunrise-sunset.org/json",params= parameters)
response.raise_for_status()

data = response.json()
sunrise = data['results']['sunrise'].split('T')[1].split(":")[0]
sunset = data['results']['sunset'].split('T')[1].split(":")[0]
print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)