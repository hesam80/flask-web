from flask import Flask

def create_app():
    app=Flask(__name__)
    app.config['secret_key'] = 'hesam'
    from .auth import auth
    from .views import views
    app.register_blueprint(auth , '/')
    app.register_blueprint(views,'/')
    return app
