import os
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


gestor = LoginManager()
app = Flask(__name__)
directorio= os.path.abspath(os.path.dirname(__file__))

app.config['SECRET_KEY'] ='201099luck'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///' + os.path.join(directorio,'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False


db=SQLAlchemy(app)

Migrate(app,db)

gestor.init_app(app)
gestor.login_view='login'