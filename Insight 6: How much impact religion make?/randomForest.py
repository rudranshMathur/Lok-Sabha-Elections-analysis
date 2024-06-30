from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder

# One-hot encode the 'Winning Party' column
one_hot_encoder = OneHotEncoder()
winning_party_encoded = one_hot_encoder.fit_transform(data[['Winning Party']]).toarray()

# Prepare the feature matrix and target vector
X = data[['Hindus (%)', 'Muslims (%)', 'Christians (%)', 'Other (%)', 'Total Population (millions)']]
y = winning_party_encoded

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Get feature importances
importances = clf.feature_importances_
feature_names = X.columns

# Create a DataFrame to display feature importances
feature_importances = pd.DataFrame({'Feature': feature_names, 'Importance': importances})
feature_importances = feature_importances.sort_values(by='Importance', ascending=False)

print(feature_importances)

y_pred = clf.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
