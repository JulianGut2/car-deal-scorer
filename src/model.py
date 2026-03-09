from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error
import xgboost as xgb
import pandas as pd
import numpy as np
import joblib

def train_model(df):
    le = LabelEncoder()
    cat_columns = ["manufacturer", "model", "condition", "fuel", "transmission", "drive", "type"]
    for col in cat_columns:
        df[col] = le.fit_transform(df[col])

    X = df.drop(columns = ["price"])
    y = df["price"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

    model = xgb.XGBRegressor(n_estimators = 100, random_state = 42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    print(f"RMSE: ${rmse:,.2f}")

    joblib.dump(model, "model.pkl")

    return model