import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os
load_dotenv() 
api_key=os.getenv("api_key")
OWEndpoint = os.getenv("OWEndpoint")
account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")
weatherparams={
    "lat":10.358965,
    "lon":77.980271,
    "appid":api_key,
    "exclude":"current,minutely,daily",
}
response = requests.get(OWEndpoint,params=weatherparams)
data=response.json()
slicee=data["hourly"][:12]
is_rain = False
for i in slicee:
    c=i["weather"][0]["id"]
    if int(c) < 700:
        is_rain=True
if is_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It is going to rain today. Please bring your Umbrella",
        from_='+12015811673',
        to='+917904471528'
    )
    print(message.status)
