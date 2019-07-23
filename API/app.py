from flask import Flask
from ModelView import prediction_app
from flask_sqlalchemy import SQLAlchemy
from database import DatabaseManager
from sqlalchemy import create_engine
def create_app():
    server = Flask('titanic_prediction')
    server.config['SQLALCHEMY_DATABASE_URI'] = "postgres://kfxiospxmgkzoz:d99897afdbe0e12fa88f777a6dee3580b111f8af92c25fa2f04f4a89bc94886e@ec2-54-217-219-235.eu-west-1.compute.amazonaws.com:5432/d6m1suvh09ctsk"
    DatabaseManager.db = SQLAlchemy(server)
    DatabaseManager.engine = create_engine("postgres://kfxiospxmgkzoz:d99897afdbe0e12fa88f777a6dee3580b111f8af92c25fa2f04f4a89bc94886e@ec2-54-217-219-235.eu-west-1.compute.amazonaws.com:5432/d6m1suvh09ctsk")
    server.register_blueprint(prediction_app)
    return server