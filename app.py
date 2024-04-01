from flask import Flask, request, jsonify
import pandas as pd
import pickle

app = Flask(__name__)

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define the columns to be used for prediction
features = ['budget', 'popularity']

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json  # Assuming JSON input with correct structure

    # Extract features for prediction
    df = pd.DataFrame(data, columns=features)

    # Make predictions using the loaded model
    prediction = model.predict(df)

    # Return the prediction as JSON response
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
