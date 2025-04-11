from flask import Flask, request, jsonify
from ml_service.predictor import load_model, predict_transaction
from ml_service.preprocessing import preprocess_input

app = Flask(__name__)
model = load_model()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    processed = preprocess_input(data)
    result = predict_transaction(model, processed)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
