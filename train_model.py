import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib

# Load dataset
df = pd.read_csv("antenna_dataset.csv")

# Input
X = df[["Frequency_GHz"]]

# Outputs
y = df[
    [
        "Patch_Width_mm",
        "Patch_Length_mm",
        "Ground_Width_mm",
        "Ground_Length_mm"
    ]
]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Model
model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

# Save Model
joblib.dump(model, "antenna_model.pkl")

print("Model trained successfully!")