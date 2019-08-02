from flask import Flask,request, send_from_directory
from ModelView import prediction_app
from flask_sqlalchemy import SQLAlchemy
from database import DatabaseManager
from sqlalchemy import create_engine
import os
from flask_cors import CORS
def create_app():
    URI = os.environ['URI']
    server = Flask('titanic_prediction', static_url_path='/static')
    server.config['SQLALCHEMY_DATABASE_URI'] = URI
    CORS(server)
    DatabaseManager.db = SQLAlchemy(server)
    DatabaseManager.engine = create_engine(URI)
    server.register_blueprint(prediction_app)
    return server
