from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

from service import PreferencesService


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


@app.route('/<user_id>/<dog_breed>')
def set_preferences_on_user(user_id, dog_breed):
    PreferencesService.save_preferences(user_id, dog_breed)
    return "OK!"


if __name__ == '__main__':
    app.run()
