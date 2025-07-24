# generate_car_data.py
import pandas as pd
import numpy as np
import random

brands = ['Toyota', 'Ford', 'BMW', 'Honda', 'Hyundai']
fuel_types = ['Petrol', 'Diesel', 'Electric', 'Hybrid']

def generate_car_data(n=1000):
    data = {
        'brand': np.random.choice(brands, n),
        'year': np.random.randint(2000, 2024, n),
        'mileage': np.random.randint(5000, 200000, n),
        'engine_size': np.round(np.random.uniform(1.0, 5.0, n), 1),
        'fuel_type': np.random.choice(fuel_types, n),
    }

    df = pd.DataFrame(data)
    
    # Create a simple price generation logic
    df['price'] = (
        20000
        - (2024 - df['year']) * 500
        - df['mileage'] * 0.05
        + df['engine_size'] * 1000
        + df['brand'].map({'BMW': 5000, 'Toyota': 2000, 'Ford': 1500, 'Honda': 1800, 'Hyundai': 1000})
        + df['fuel_type'].map({'Petrol': -500, 'Diesel': -700, 'Electric': 2000, 'Hybrid': 1000})
    ).astype(int)

    df.to_csv("car_data.csv", index=False)
    print("✅ Data generated and saved to 'car_data.csv'")

generate_car_data()
