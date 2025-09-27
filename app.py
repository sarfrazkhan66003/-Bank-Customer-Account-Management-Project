import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load model, scaler, and feature list
model = joblib.load("churn_model.pkl")
scaler = joblib.load("scaler.pkl")
features = joblib.load("features.pkl")

st.title("🚀 Bank Customer Churn Prediction")

st.markdown("Enter customer details below to check if the customer will churn:")

# --- User Inputs ---
age = st.number_input("Customer Age", min_value=18, max_value=100, value=32)
gender = st.selectbox("Gender", ["M", "F"])
dependents = st.number_input("Dependent Count", min_value=0, value=2)
education = st.selectbox("Education Level", ["Uneducated","High School","College","Graduate","Post-Graduate","Doctorate"])
marital = st.selectbox("Marital Status", ["Single","Married","Divorced"])
income = st.selectbox("Income Category", ["Less than $40K","$40K - $60K","$60K - $80K","$80K - $120K","$120K +"])
card = st.selectbox("Card Category", ["Blue","Silver","Gold","Platinum"])
months_on_book = st.number_input("Months on Book", min_value=1, value=39)
total_relationship = st.number_input("Total Relationship Count", min_value=0, value=2)
months_inactive = st.number_input("Months Inactive (12 mon)", min_value=0, value=1)
contacts_count = st.number_input("Contacts Count (12 mon)", min_value=0, value=2)
credit_limit = st.number_input("Credit Limit", min_value=100.0, value=5000.0)
revolving_balance = st.number_input("Total Revolving Balance", min_value=0.0, value=1000.0)
avg_open_to_buy = st.number_input("Avg Open To Buy", min_value=0.0, value=4000.0)

# --- Encoding categorical variables ---
gender_map = {"M":0, "F":1}
edu_map = {"Uneducated":0,"High School":1,"College":2,"Graduate":3,"Post-Graduate":4,"Doctorate":5}
marital_map = {"Single":0,"Married":1,"Divorced":2}
income_map = {"Less than $40K":0,"$40K - $60K":1,"$60K - $80K":2,"$80K - $120K":3,"$120K +":4}
card_map = {"Blue":0,"Silver":1,"Gold":2,"Platinum":3}

# Create dictionary of all inputs
input_dict = {
    "Customer_Age": age,
    "Gender": gender_map[gender],
    "Dependent_count": dependents,
    "Education_Level": edu_map[education],
    "Marital_Status": marital_map[marital],
    "Income_Category": income_map[income],
    "Card_Category": card_map[card],
    "Months_on_book": months_on_book,
    "Total_Relationship_Count": total_relationship,
    "Months_Inactive_12_mon": months_inactive,
    "Contacts_Count_12_mon": contacts_count,
    "Credit_Limit": credit_limit,
    "Total_Revolving_Bal": revolving_balance,
    "Avg_Open_To_Buy": avg_open_to_buy,
}

# Make DataFrame with same columns as training
input_df = pd.DataFrame([input_dict])
# Align columns exactly with training features
input_df = input_df.reindex(columns=features, fill_value=0)

# Scale input
input_scaled = scaler.transform(input_df)

if st.button("Predict Churn"):
    prediction = model.predict(input_scaled)[0]
    prob = model.predict_proba(input_scaled)[0][1] * 100

    if prediction == 1:
        st.error(f"⚠️ Customer is likely to CHURN (Probability: {prob:.2f}%)")
    else:
        st.success(f"✅ Customer will stay with the bank (Churn Probability: {prob:.2f}%)")



#output terminal :- streamlit run "d:/PW Data Science/Project/Bank Customer Churn Prediction Project/app.py"
