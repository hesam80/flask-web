from flask import Blueprint

views = Blueprint('viwes', __name__)
@views.route('/')
def home():
    return "<p>home</p>"