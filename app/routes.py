from flask import Blueprint, request, jsonify, render_template
import pandas as pd
from app.model_loader import model, scaler
import pickle
from src.preprocess import preprocess_input

predict_bp = Blueprint("predict", __name__,template_folder="../template",static_url_path="../static")

# load feature order ONCE
FEATURES = pickle.load(open("models/features.pkl", "rb"))

# ✅ HOME PAGE (GET)
@predict_bp.route("/", methods=["GET"])
def home():
    return render_template("index.html")

# ✅ PREDICTION API (POST)
@predict_bp.route("/predict", methods=["POST"])
def predict():
    data = request.json
    df = pd.DataFrame([data])

    # 🔥 single source of truth
    df = preprocess_input(df, mode="predict")

    # Scale
    df_scaled = scaler.transform(df)

    # Predict
    pred = model.predict(df_scaled)[0]
    prob = model.predict_proba(df_scaled)[0][1]

    return jsonify({
        "credit_status": "Good" if pred == 1 else "Bad",
        "default_probability": round(float(prob), 3)
    })
