import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import StandardScaler
import urllib.parse

# Load the dataset
data = pd.read_csv("C:\\Users\\danus\\Desktop\\da1\\crdataset.csv")

# Separate features and target variable
X = data.drop(columns=['index', 'Target'])
y = data['Target']
# Initialize Gradient Boosting Classifier
clf = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)

# Fit the classifier
clf.fit(X, y)
# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)  # Fit scaler only on training features

# Example of feature extraction from a URL in a phishing website detection project

def extract_features(url):
    # Placeholder for feature extraction logic
    features = ...  # Extract features from the URL
    return features

# Example usage:
url = "https://example.com/phishing_page"
features = extract_features(url)
print("Extracted features:", features)

 # Apply transformation using the same scaler fitted on training data
    features = scaler.transform([features])
    features_df = pd.DataFrame(features, columns=X.columns)  # Convert back to DataFrame with column names
    # Make prediction
    prediction = clf.predict(features_df)
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
