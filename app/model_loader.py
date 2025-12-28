import os
import pickle
from src.train import train_and_save

MODEL_PATH = "models/credit_model.pkl"

if not os.path.exists(MODEL_PATH):
    train_and_save()

model = pickle.load(open("models/credit_model.pkl", "rb"))
scaler = pickle.load(open("models/scaler.pkl", "rb"))
features = pickle.load(open("models/features.pkl", "rb"))

MODEL_PATH = "models/credit_model.pkl"
SCALER_PATH = "models/scaler.pkl"

# model = pickle.load(open(MODEL_PATH, "rb"))
# scaler = pickle.load(open(SCALER_PATH, "rb"))
