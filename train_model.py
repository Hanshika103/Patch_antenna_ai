

import pandas as pd
import joblib

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

df = pd.read_csv("antenna_dataset.csv")

X = df[
    [
        "Frequency_GHz",
        "Dielectric_Constant",
        "Height_mm",
        "Loss_Tangent",
        "Copper_Thickness_mm"
    ]
]

y = df[
    [
        "Patch_Width_mm",
        "Patch_Length_mm",
        "Ground_Width_mm",
        "Ground_Length_mm"
    ]
]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

joblib.dump(model, "antenna_model.pkl")

print("Model trained successfully")