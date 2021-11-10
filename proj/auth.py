from flask import Blueprint, Flask, flash, redirect, render_template, request, url_for
auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<p>login</p>"

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/signup')
def signup():
    return render_template('register.html')


