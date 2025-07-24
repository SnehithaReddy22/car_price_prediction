# app.py
import gradio as gr
import joblib
import numpy as np
import pandas as pd

# Load model
model = joblib.load("car_price_model.pkl")

def predict_price(brand, year, mileage, engine_size, fuel_type):
    input_data = {
        'brand': [brand],
        'year': [int(year)],
        'mileage': [int(mileage)],
        'engine_size': [float(engine_size)],
        'fuel_type': [fuel_type]
    }
    price = model.predict(pd.DataFrame(input_data))[0]
    return f"Estimated Car Price: ₹{int(price):,}"

# Gradio UI
iface = gr.Interface(
    fn=predict_price,
    inputs=[
        gr.Dropdown(['Toyota', 'Ford', 'BMW', 'Honda', 'Hyundai'], label="Brand"),
        gr.Slider(2000, 2024, step=1, label="Year"),
        gr.Number(label="Mileage (in km)"),
        gr.Slider(1.0, 5.0, step=0.1, label="Engine Size (L)"),
        gr.Dropdown(['Petrol', 'Diesel', 'Electric', 'Hybrid'], label="Fuel Type"),
    ],
    outputs="text",
    title="Car Price Predictor 🚗",
    description="Enter car details to estimate the price"
)

iface.launch()
