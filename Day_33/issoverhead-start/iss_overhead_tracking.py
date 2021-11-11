import requests
from datetime import datetime
import smtplib,ssl
import time

def iss_position:
    MY_LAT = 28.535517  # Your latitude
    MY_LONG = 77.391029  # Your longitude

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])


    # Your position is within +5 or -5 degrees of the ISS position.

    if (MY_LAT-5 <= iss_latitude <= MY_LAT+5) and (MY_LONG-5 <= iss_longitude <= MY_LONG+5):
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if sunset <= time_now <= sunrise:
        return True


# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
    time.sleep(60)

    if iss_position and is_night():
        port = 587
        sender_email = "timmyturtle460@gmail.com"
        password = 'qwerty9876()'

        context = ssl.create_default_context()
        connection = smtplib.SMTP("smtp.gmail.com",port)
        connection.starttls(context=context)
        connection.login(user=sender_email, password=password)
        connection.sendmail(
            from_addr=sender_email,
            to_addrs=sender_email,
            msg="Subject:Look up\n\n Hey look up the iss is passing")
        connection.close()

