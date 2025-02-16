import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
import joblib

# 1. Load or Create a Sample Dataset
data = {
    "temperature": [25, 30, 22, 28, 26, 32, 27],
    "humidity": [60, 55, 65, 70, 68, 50, 62],
    "rainfall": [200, 180, 220, 250, 230, 150, 190],
    "yield": [6.0, 7.5, 5.2, 8.0, 6.8, 7.2, 6.5]
}

df = pd.DataFrame(data)

# 2. Split Features and Target
X = df[["temperature", "humidity", "rainfall"]]  # Features
y = df["yield"]  # Target variable (Crop Yield)

# 3. Train DecisionTreeRegressor
model = DecisionTreeRegressor()
model.fit(X, y)

# 4. Save the Model
joblib.dump(model, "models/crop_yield_model.pkl")

print("Model trained and saved successfully!")
