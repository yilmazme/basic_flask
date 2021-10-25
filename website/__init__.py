from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager, login_manager

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    ENV = "dev"

    if ENV == "dev":
        app.debug = True
        app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:<password>@localhost/flaskapp'

    else:
        app.debug = False
        app.config["SQLALCHEMY_DATABASE_URI"] = ''

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
  
    app.config["SECRET_KEY"] = "KKKJ7878bhjbnbh8787"
    db.init_app(app)



    from .views import views
    from .auth import auth

    #prefix will be adde before what comes from imports
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")


    from .models import User, Note

    create_database(app)


    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


    return app

def create_database(app):
    if not path.exists("website/" + "initalDb"):
        db.create_all(app=app)
        print("Database created!")

