import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import StandardScaler
import urllib.parse

# Load the dataset
data = pd.read_csv("your_dataset.csv")

# Separate features and target variable
X = data.drop(columns=['index', 'Target'])
y = data['Target']

# Initialize Gradient Boosting Classifier
clf = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)

# Fit the classifier
clf.fit(X, y)

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Function to extract features from the URL
def extract_features(url):
    parsed_url = urllib.parse.urlparse(url)
    features = [
        len(parsed_url.netloc),  # Length of the network location part of the URL
        len(parsed_url.path),    # Length of the path part of the URL
        "-" in parsed_url.netloc,  # Presence of '-' in the network location
        "." in parsed_url.path,    # Presence of '.' in the path
    ]
    return features

# Function to predict phishing using a trained model
def predict_phishing(url):
    # Extract features from the URL
    features = extract_features(url)
    # Reshape features to match the shape expected by the model (1, num_features)
    features = scaler.transform([features])
    # Make prediction
    prediction = clf.predict(features)
    return prediction[0]

# Function to get user input URL
def get_user_input():
    url = input("Enter the URL you want to predict: ")
    return url

# Example usage
def main():
    url = get_user_input()
    prediction = predict_phishing(url)
    if prediction == 1:
        print(f"{url} is predicted to be a phishing URL.")
    else:
        print(f"{url} is predicted to be a legitimate URL.")

if __name__ == "__main__":
    main()
