import joblib
import os

def load_model(model_path='models/fraud_model.joblib'):
    return joblib.load(model_path)

def predict_transaction(model, features):
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]
    return {
        'prediction': int(prediction),
        'fraud_score': round(probability, 4)
    }
