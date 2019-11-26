from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os.path import join, dirname


app = Flask(__name__)
db_path = join(dirname(__file__), 'site.db')
app.config['SECRET_KEY'] = '6c681ab3e061cadc5ebbad267f4b8f37'
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"

db = SQLAlchemy(app)
from flaskapp import routes
