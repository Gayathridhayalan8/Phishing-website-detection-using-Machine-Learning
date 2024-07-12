import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
data = pd.read_csv(r"C:\\Users\\danus\\Desktop\\da1\\dataset.csv")
# Print column names to verify
print("Column Names:", data.columns)

# Check if 'Target' column exists in the dataset
if 'Target' in data.columns:
    # Drop 'Target' column to create feature matrix X
    X = data.drop(columns=['Target'])
    y = data['Target']  
    print("X shape:", X.shape)
else:
    print("'Target' column not found in the dataset.")

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate the model
accuracy = model.score(X_test, y_test)
print("Model Accuracy:", accuracy)

# Save the model
with open('phishing_model.pkl', 'wb') as file:
    pickle.dump(model, file)
