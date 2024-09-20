from flask import Flask, request, jsonify
import pickle
import numpy as np

# creat app
app = Flask(__name__)

# load file pkl
with open('customer_churn_random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('encoder.pkl', 'rb') as file:
    encoder = pickle.load(file)


# create api
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    # extract input
    age = int(data['age'])
    tenure = int(data['tenure'])
    usage_frequency = int(data['usage_frequency'])
    support_calls = int(data['support_calls'])
    payment_delay = int(data['payment_delay'])
    total_spend = float(data['total_spend'])
    last_interaction = int(data['last_interaction'])
    gender = data['gender']
    subscription_type = data['subscription_type']
    contract_length = data['contract_length']

    encoder_data = list(encoder.transform([[gender, subscription_type, contract_length]])[0])
    predict_array = [age, tenure, usage_frequency, support_calls, payment_delay, total_spend,
                     last_interaction] + encoder_data
    predict_array = np.array(predict_array).reshape((1, -1))

    # predict
    prediction = model.predict(predict_array)

    # Check result churn or not churn
    if prediction > 0.5:
        result = 'Churn'

    else:
        result = "Won't Churn"

    return jsonify({'prediction': result})


# run app
if __name__ == '__main__':
    app.run(debug=True)
