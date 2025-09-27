# -Bank-Customer-Account-Management-Project

A combined project featuring two powerful Streamlit apps:
1️⃣ Bank Customer Churn Prediction – Predict whether a bank customer is likely to leave.
2️⃣ Bank Management System – Create and manage customer bank accounts securely.

🚀 Features
1. Bank Customer Churn Prediction App
Predicts customer churn using a pre-trained ML model.
Accepts multiple customer details (age, gender, education, credit limit, etc.).
Provides churn probability with intuitive feedback (✅ Stay / ⚠️ Likely to Churn).

2. Bank Management System App
Create new bank accounts with secure PINs.
View account details with authentication.
Deposit and withdraw money safely.
SQLite database for storing accounts.

🧠 Algorithm & Key Concepts
🔹 Churn Prediction
Input Preprocessing: Encodes categorical data (gender, education, card type).
Scaling: Uses a fitted scaler to normalize features.
Prediction: Logistic Regression / ML model predicts churn probability.

🔹 Bank Management
Database (SQLite3): Stores account number, name, PIN, and balance.
OOP (BankAccount Class): Handles deposit/withdrawal with real-time balance updates.
Authentication: Validates PIN before showing details or allowing transactions.

📝 Why It’s Necessary

Banks lose millions annually due to customer churn – this app predicts it early.
A simple and transparent bank management system builds customer trust.
Demonstrates how data science + software engineering can solve real-world problems.

📊 Technologies Used

Python
Streamlit
SQLite3
NumPy / Pandas
Joblib (Model & Scaler)

