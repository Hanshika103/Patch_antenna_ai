import pandas as pd
import joblib

from xgboost import XGBRegressor
from sklearn.multioutput import MultiOutputRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# Load dataset
df = pd.read_csv("antenna_dataset.csv")

# Input features
X = df[
    [
        "Frequency_GHz",
        "Dielectric_Constant",
        "Height_mm",
        "Loss_Tangent",
        "Copper_Thickness_mm"
    ]
]

# Target outputs
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

# Base XGBoost Model
xgb = XGBRegressor(
    n_estimators=200,
    max_depth=5,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    objective="reg:squarederror",
    random_state=42,
    n_jobs=1
)

# Multi-output wrapper
model = MultiOutputRegressor(xgb)

# Train model
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred) ** 0.5

print("=" * 50)
print("Model : XGBoost Regressor")
print(f"R² Score : {r2:.4f}")
print(f"MAE      : {mae:.4f}")
print(f"RMSE     : {rmse:.4f}")
print("=" * 50)

# Save trained model
joblib.dump(model, "antenna_model.pkl")

print("✅ XGBoost model trained and saved successfully!")