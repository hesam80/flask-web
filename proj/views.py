from flask import Blueprint, Flask, flash, redirect, render_template, request, url_for

views = Blueprint('viwes', __name__)
@views.route('/')
def home():
    return "<p>home hello</p>"