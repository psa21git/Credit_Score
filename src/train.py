import os
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from src.preprocess import preprocess_input

def train_and_save():
    os.makedirs("models", exist_ok=True)

    df = pd.read_csv("data/train.csv")

    X = df.drop("Credit_Score", axis=1)
    y = df["Credit_Score"]

    # 🔥 TRAIN MODE
    X = preprocess_input(X, mode="train")

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )
    model.fit(X_scaled, y)

    pickle.dump(model, open("models/credit_model.pkl", "wb"))
    pickle.dump(scaler, open("models/scaler.pkl", "wb"))
    pickle.dump(X.columns.tolist(), open("models/features.pkl", "wb"))

if __name__ == "__main__":
    train_and_save()
