from flask import Blueprint, request, jsonify
#from model.prediction import make_prediction
from model.run_pipeline import make_prediction,read_train
import pandas as pd
from database import DatabaseManager
prediction_app=Blueprint('prediction_route',__name__)

@prediction_app.route('/prediction',methods=['POST'])
def predict():
    message = ""
    if request.method == 'POST':
        try:
            json_data=request.get_json()
            df = pd.DataFrame.from_dict(json_data)
        except:
            message = "No data provided"
        try:
            f = request.files['file']
            df = pd.read_csv(f,index_col = "PassengerId")
        except:
            message = "No data provided"
        try:
            df["Survived"]=make_prediction(df)
        except:
            message = "Wrong format"
        return jsonify({'success':True,"predictions":df[["Survived","Name"]].to_json(orient='values')})
    return jsonify({'success':False,"message":message})
@prediction_app.route('/health', methods = ['GET'])
def health():
    return "hello"
@prediction_app.route('/state', methods = ['GET'])
def state():
    return "Running"
@prediction_app.route('/passengers', methods = ['POST','GET'])
def passengers():
    if request.method == 'POST':
        f = request.files['file']
        df = pd.read_csv(f,index_col = "PassengerId")
        df.to_sql("Passengers",con = DatabaseManager.engine,if_exists = "replace")
        return 'Passengers created'
@prediction_app.route('/train', methods = ['GET'])
def train():
    read_train()
    return "Model trained"
    
