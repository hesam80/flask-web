from flask import Blueprint

views = Blueprint('viwes', __name__)
@auth.route('/')
def home():
    return "<p>home</p>"