import pandas as pd
from pathlib import Path
import os
import preprocessing as pp
from pipeline import prediction_pipeline
from sklearn.model_selection import train_test_split
from database import DatabaseManager
import pickle
TRAINING_DATA_FILE = os.path.dirname(os.path.realpath(__file__)) + '/datasets/train.csv'
TEST_DATA_FILE = os.path.dirname(os.path.realpath(__file__)) + '/datasets/test.csv'
MODELS_PATH = os.path.dirname(os.path.realpath(__file__)) + '/exported_models/final_model.csv'
def _save_model(model):
    pickle.dump(model, open(MODELS_PATH, 'wb'))
def _load_model():
    return pickle.load(open(MODELS_PATH, 'rb'))
def read_train():
    #df = pd.read_csv(TRAINING_DATA_FILE, index_col="PassengerId")
    df = pd.read_sql("Passengers",DatabaseManager.engine,index_col="PassengerId")
    X = df.drop("Survived",axis=1)
    y = df["Survived"]
    X_train,X_test,y_train,y_test = train_test_split(X,y)
    pipeline = prediction_pipeline
    pipeline.fit(X_train,y_train)
    print(pipeline.score(X_test,y_test))
    _save_model(pipeline)
def read_test():
    df = pd.read_csv(TEST_DATA_FILE, index_col="PassengerId")
    pipeline = _load_model()
    predictions = pipeline.predict(df)
    print(predictions)
    predictions = pd.DataFrame(predictions,columns=["Survived"],index = df.index)
    predictions.to_csv("predictionsKaggle.csv")
def make_prediction(df):
    pipeline = _load_model()
    predictions = pipeline.predict(df)
    return predictions
def show_path():
    print("real", os.path.realpath(__file__))
if __name__ == '__main__':      #This part will only run when running this file directly
    read_train()