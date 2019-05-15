import os
from flask import Flask
from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_moment import Moment

app = Flask(__name__)
app.config.from_object(Config)

#initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
mail = Mail(app)
moment = Moment(app)
# Flask-Login needs to know what is the view function that handles logins
login.login_view = 'login'

from app import routes, models,errors,log_func

if not app.debug:
    log_func.setup_logger('logs/microblog.log')