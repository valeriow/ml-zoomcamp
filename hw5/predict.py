import pickle

from flask import Flask
from flask import request
from flask import jsonify


with open("model2.bin", 'rb') as file:
  model = pickle.load(file)
  dv = pickle
with open("dv.bin", 'rb') as file:
  dv = pickle.load(file)

app = Flask('Credit Aproval')

@app.route('/predict', methods=['POST'])
def predict():
    client = request.get_json()

    X = dv.transform([client])
    y_pred = model.predict_proba(X)[0, 1]
    credit_aproval = y_pred >= 0.5

    result = {
        'probability': float(y_pred),
        'credit_aproval': bool(credit_aproval)
    }

    return jsonify(result)

@app.route('/ping', methods=['GET'])
def ping():
   return "pong"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)