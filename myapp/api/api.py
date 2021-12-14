import os, pytz, requests, math,time
from flask import Flask

app = Flask(__name__, static_folder='../build', static_url_path='/')
app.config.from_envvar('./setting.cfg')


@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/api/weather')
def get_current_weather(city='tehran'):
    API_KEY = '92ef7fe4196f1fe341c896bb105291b3'
    API_URL = 'http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&appid={}'
    weather = requests.get(API_URL.format(city, API_KEY)).json()
    return weather


