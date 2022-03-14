import requests
import smtplib

MY_EMAIL = "thehimraj18@gmail.com"
MY_PASSWORD = "GOD KRI$NA"
api_key = "b729447282318471486e81ba5fe6a6d7"

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

parameters = {
    "lat": 	26.148043,
    "lon": 	91.731377,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

will_rain = False

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
sliced_weather_data = weather_data["hourly"][:12]
for hour_data in sliced_weather_data:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
        connection.ehlo()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="himraj.webuse001@gmail.com",
            msg="Subject:Rain alert\n\nTime to take your umbrella."
        )