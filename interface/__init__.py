from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e4fd2314b7d8e52744874483bb147046'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database_prod.db' 
db = SQLAlchemy(app)

from interface import routes