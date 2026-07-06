import os
import pickle
from flask import current_app

MODEL_PATH = "models/credit_model.pkl"
SCALER_PATH = "models/scaler.pkl"

def get_model():
    """Retrieve the model lazily loaded and cached in the app context."""
    if not hasattr(current_app, "ml_model"):
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(
                f"Model file not found at '{MODEL_PATH}'. "
                "Ensure it has been uploaded/copied to the models directory."
            )
        current_app.ml_model = pickle.load(open(MODEL_PATH, "rb"))
    return current_app.ml_model

def get_scaler():
    """Retrieve the scaler lazily loaded and cached in the app context."""
    if not hasattr(current_app, "ml_scaler"):
        if not os.path.exists(SCALER_PATH):
            raise FileNotFoundError(
                f"Scaler file not found at '{SCALER_PATH}'. "
                "Ensure it has been uploaded/copied to the models directory."
            )
        current_app.ml_scaler = pickle.load(open(SCALER_PATH, "rb"))
    return current_app.ml_scaler


