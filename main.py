import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 30.183950 # Your latitude
MY_LONG = -97.888400 # Your longitude

def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])


    if (MY_LAT == iss_latitude + 5 or MY_LAT == iss_latitude -5) and (MY_LONG== iss_longitude + 5 or MY_LONG==iss_longitude -5):
        return True
#Your position is within +5 or -5 degrees of the ISS position.

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

    time_now = datetime.now()
    hour=time_now.hour
    if hour > sunset and hour < sunrise:
        return True



while True:
    time.sleep(60)
    if is_night() and iss_overhead():
        connection=smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user='gmail.google.com',password='jtqe jitx jadk deui')
        connection.sendmail(from_addr='georgehuffingtons@gmail.com',to_addrs='georgehuffingtons@gmail.com',msg=f"Subject: ISS\n\n Please look up")


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



