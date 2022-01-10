from datetime import datetime
from flask import Flask
import os
import pytz
import requests
import math

app= Flask('__name__')

API_KEY = '92ef7fe4196f1fe341c896bb105291b3'
API_URL = 'http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&appid={}'


@app.route('/')
def view():
    return query_api('tehran')

def query_api(city):
    try:
        #tst lint print(API_URL.format(city, API_KEY))
        data = requests.get(API_URL.format(city, API_KEY)).json()
    except Exception as exc:
        print(exc)
        data = None
    print (data)
    return data
#api.openweathermap.org/data/2.5/find?lat=55.5&lon=37.5&cnt=10&appid=API_KEY
#query_api('tehran')
#this change for tst
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)