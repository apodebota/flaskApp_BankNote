from flask import Flask, request
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)
with open('RFClassifier_model.pkl','rb') as model_file:
    classifier = pickle.load(model_file)

@app.route("/")
def welcome():
    return "Welcome Everyone"

@app.route("/predict")
def predict_note_authenticity():
    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    return "The predicted value is " + str(prediction)

@app.route("/predict_file", methods=["POST"])
def predict_note_authenticity_file():
    df_test = pd.read_pickle(request.files.get("file"))
    #variance = request.args.get('variance')
    #skewness = request.args.get('skewness')
    #curtosis = request.args.get('curtosis')
    #entropy = request.args.get('entropy')
    predictions = classifier.predict(df_test)
    predictions = [prediction.item() for prediction in predictions]
    return "The predicted values for the csv are " + str(list(predictions))

if __name__=='__main__':
    app.run()