from flask import Blueprint, Flask, flash, redirect, render_template, request, url_for
from datetime import date
views = Blueprint('views', __name__)
@views.route('/')
def view():
    today = str(date.today()) 
    my_location=find_location()
   

    
    message = "simpleapps redeployedd Wow how it's Very Nice!"
    congramessage="Congratulations, you successfully deployed  container image to Cloud Run at: "

    return render_template('index.html' ,congmsg=congramessage,message=message ,today=today,city=my_location[2])
def find_location():
    try:
        response = requests.get('https://ipinfo.io')
        data = response.json()
        loc = data['loc'].split(',')
        lat, long = float(loc[0]), float(loc[1])
        city = data.get('city', 'Unknown')
        state = data.get('region', 'Unknown')
        return lat, long, city, state
        #return lat, long
    except:
        #Displaying ther error message
        print("Internet Not avialable")
        #closing the program 
        exit()
        return False