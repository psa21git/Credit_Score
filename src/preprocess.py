import pandas as pd
import os
import pickle
from sklearn.preprocessing import LabelEncoder

# -----------------------------
# PATHS
# -----------------------------
ENCODER_PATH = "models/encoders.pkl"
FEATURES_PATH = "models/features.pkl"

# -----------------------------
# CONFIG
# -----------------------------
DROP_COLS = ["Customer_ID", "ID", "Name", "SSN"]

CATEGORICAL_COLS = [
    "Occupation",
    "Type_of_Loan",
    "Credit_Mix",
    "Payment_of_Min_Amount",
    "Payment_Behaviour"
]

# -----------------------------
# UTIL FUNCTIONS
# -----------------------------
def parse_month(col):
    if pd.api.types.is_numeric_dtype(col):
        return col

    return pd.to_datetime(
        col,
        format="mixed",
        errors="coerce"
    ).dt.month

# -----------------------------
# MAIN PREPROCESS FUNCTION
# -----------------------------
def preprocess_input(df, mode="predict"):
    df = df.copy()
    os.makedirs("models", exist_ok=True)

    # Drop non-feature columns
    df.drop(columns=DROP_COLS, errors="ignore", inplace=True)

    # Month handling
    if "Month" in df.columns:
        df["Month"] = parse_month(df["Month"])
        df["Month"] = df["Month"].fillna(
            df["Month"].mode().iloc[0] if not df["Month"].mode().empty else 1
        )

    # -----------------------------
    # TRAIN MODE → FIT ENCODERS
    # -----------------------------
    if mode == "train":
        encoders = {}

        for col in CATEGORICAL_COLS:
            if col in df.columns:
                le = LabelEncoder()
                df[col] = le.fit_transform(df[col].astype(str))
                encoders[col] = le

        pickle.dump(encoders, open(ENCODER_PATH, "wb"))

    # -----------------------------
    # PREDICT MODE → LOAD ENCODERS
    # -----------------------------
    else:
        if not os.path.exists(ENCODER_PATH):
            raise RuntimeError("Encoders not found. Train the model first.")

        encoders = pickle.load(open(ENCODER_PATH, "rb"))

        for col in CATEGORICAL_COLS:
            if col in df.columns:
                le = encoders[col]
                df[col] = df[col].astype(str).map(
                    lambda x: x if x in le.classes_ else le.classes_[0]
                )
                df[col] = le.transform(df[col])

    # Numeric coercion
    for col in df.columns:
        if col not in CATEGORICAL_COLS:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    df.fillna(0, inplace=True)

    # Feature order enforcement (prediction only)
    if mode == "predict":
        features = pickle.load(open(FEATURES_PATH, "rb"))
        df = df.reindex(columns=features, fill_value=0)

    return df
