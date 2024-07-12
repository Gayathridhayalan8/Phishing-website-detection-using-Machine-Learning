from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load the model
with open('phishing_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/predict', methods=['POST'])
def predict():
    url = request.json['url']
    # Extract features from the URL
    features = extract_features(url)
    # Make prediction using the model
    prediction = model.predict([features])[0]
    return jsonify({'prediction': prediction})

def extract_features(url):
    # Code to extract features from the URL
    return features

if __name__ == '__main__':
    app.run(debug=True)
