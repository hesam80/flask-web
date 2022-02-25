from flask import Blueprint, Flask, flash, redirect, render_template, request, url_for
from datetime import date
views = Blueprint('views', __name__)
@views.route('/')
def view():

    today = str(date.today()) 
    message = "simpleapps redeployedd Wow how it's Very Nice!"
    congramessage="Congratulations, you successfully deployed  container image to Cloud Run at: "

    return render_template('index.html' ,congmsg=congramessage,message=message ,today=today)
