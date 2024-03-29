# -*- coding: utf-8 -*-
"""Assignment_5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1skjhh2gbD18OSrA2ghGT2h6MO3v6C6RA
"""

# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report

# Load the glass dataset
glass_df = pd.read_csv('/content/glass.csv')

# Separate features and target variable
X = glass_df.drop('Type', axis=1)
y = glass_df['Type']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Naïve Bayes classifier
gnb = GaussianNB()

# Train the classifier on the training set
gnb.fit(X_train, y_train)

# Predict on the testing set
y_pred = gnb.predict(X_test)

# Evaluate the model
accuracy = gnb.score(X_test, y_test)
print(f"Model Accuracy: {accuracy}")

# Generate and print classification report
report = classification_report(y_test, y_pred)
print(report)

from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report, accuracy_score

# Assuming glass_df is already loaded with the glass dataset

# Split the data into features and target variable
X = glass_df.drop('Type', axis=1)
y = glass_df['Type']

# Split the dataset into training and testing parts
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Linear SVM model
linear_svc = LinearSVC(random_state=42, max_iter=10000)
linear_svc.fit(X_train, y_train)

# Predict on the testing set
y_pred = linear_svc.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

# Print the classification report for a detailed evaluation
report = classification_report(y_test, y_pred)
print(report)