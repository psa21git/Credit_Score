import os
import pickle
from src.train import train_and_save

MODEL_PATH = "models/credit_model.pkl"
SCALER_PATH = "models/scaler.pkl"
FEATURES_PATH = "models/features.pkl"
ENCODER_PATH = "models/encoders.pkl"

# 🔥 Auto-train on fresh machine
if not os.path.exists(MODEL_PATH):
    print("Model not found. Training model...")
    train_and_save()

# Load artifacts
model = pickle.load(open(MODEL_PATH, "rb"))
scaler = pickle.load(open(SCALER_PATH, "rb"))
features = pickle.load(open(FEATURES_PATH, "rb"))
encoders = pickle.load(open(ENCODER_PATH, "rb"))
