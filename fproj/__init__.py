from flask import Flask

def create_app():
    app=Flask(__name__)
    app.config['secret_key'] = 'hesam'
    return app
