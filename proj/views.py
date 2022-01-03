from flask import Blueprint, Flask, flash, redirect, render_template, request, url_for

views = Blueprint('views', __name__)
@views.route('/')
def view():
    """Return a friendly HTTP greeting."""
    message = "simpleapps redeployedd Wow how it's Nice!2022"
    congramessage="Congratulations, you successfully deployed a container image to Cloud Run!"
    """Get Cloud Run environment variables."""
    return render_template('index.html' ,congmsg=congramessage,message=message)
