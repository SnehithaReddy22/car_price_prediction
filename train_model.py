# train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import make_pipeline
from sklearn.compose import ColumnTransformer
import joblib

# Load data
df = pd.read_csv("car_data.csv")

# Features and target
X = df.drop("price", axis=1)
y = df["price"]

# Preprocessing
categorical = ['brand', 'fuel_type']
numerical = ['year', 'mileage', 'engine_size']

preprocessor = ColumnTransformer([
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical)
], remainder='passthrough')

# Model pipeline
model = make_pipeline(preprocessor, RandomForestRegressor(n_estimators=100, random_state=42))

# Train/test split and training
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, "car_price_model.pkl")
print("✅ Model trained and saved as 'car_price_model.pkl'")
