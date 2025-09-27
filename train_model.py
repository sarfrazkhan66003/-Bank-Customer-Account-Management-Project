import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load dataset
df = pd.read_csv("D:\PW Data Science\Project\Bank Customer Churn Prediction Project\BankChurners.csv")

# 🎯 Target column ko rename kar do
df["Churn"] = df["Attrition_Flag"].apply(lambda x: 1 if x == "Attrited Customer" else 0)

# Drop unnecessary columns (Kaggle dataset mein extra info hoti hai)
df = df.drop(columns=["CLIENTNUM", "Attrition_Flag"])

# Encode categorical columns
categorical_cols = ["Gender", "Education_Level", "Marital_Status", "Income_Category", "Card_Category"]
le = LabelEncoder()
for col in categorical_cols:
    df[col] = le.fit_transform(df[col])

# Features & Target
X = df.drop("Churn", axis=1)
y = df["Churn"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train Naive Bayes
model = GaussianNB()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("✅ Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Save model & scaler
joblib.dump(model, "churn_model.pkl")
joblib.dump(scaler, "scaler.pkl")
joblib.dump(list(X.columns), "features.pkl")
