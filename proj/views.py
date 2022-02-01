from flask import Blueprint, Flask, flash, redirect, render_template, request, url_for
from datetime import date
views = Blueprint('views', __name__)
@views.route('/')
def view():

    today = str(date.today()) 
    """Return a friendly HTTP greeting."""
    message = "simpleapps redeployedd Wow how it's Nice!!"
    congramessage="Congratulations, you successfully deployed  container image to Cloud Run at:", today
    """Get Cloud Run environment variables."""
    return render_template('index.html' ,congmsg=congramessage,message=message)
