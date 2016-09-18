from flask import Flask
# from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config.from_object("config")
# db = SQLAlchemy(app)

app.secret_key = 'you-will-never-guess'

from uber import views
