import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from src.preprocess import preprocess_input

def train_and_save():
    # load data
    df = pd.read_csv("data/train.csv")

    X = df.drop("Credit_Score", axis=1)
    y = df["Credit_Score"]

    # preprocess training data
    X = preprocess_input(X, mode="train")

    # train-test split
    X_train, X_val, y_train, y_val = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # scale
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)

    # train model
    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=10,
        random_state=42
    )
    model.fit(X_train_scaled, y_train)

    # save artifacts locally (NOT in GitHub)
    pickle.dump(model, open("models/credit_model.pkl", "wb"))
    pickle.dump(scaler, open("models/scaler.pkl", "wb"))
    pickle.dump(X_train.columns.tolist(), open("models/features.pkl", "wb"))

if __name__ == "__main__":
    train_and_save()
