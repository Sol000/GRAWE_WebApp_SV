# ------------------------------------------------------------------------
# Fileame:      server.py 
#
# Description:  Here is the entrypoint of the application. This App works 
#               as an backend for Webapp
#
# Authors:      TM, ..... 
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
#                              INCLUDES
# ------------------------------------------------------------------------
#libs
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_jwt_extended import JWTManager
#local
from config import Config

# ------------------------------------------------------------------------
#                              SETUP
# ------------------------------------------------------------------------
# Flask App
app = Flask(__name__)
app.config.from_object(Config)

# SQL-Alchemy
db = SQLAlchemy(app)

# Migrate
migrate = Migrate(app, db)

#JWT-Manager
jwt = JWTManager(app)

# login manager 
login = LoginManager(app)
login.login_view = 'login_page'

# ------------------------------------------------------------------------
#                              Import files
# ------------------------------------------------------------------------
import routes