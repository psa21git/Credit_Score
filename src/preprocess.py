import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder


# -----------------------------
# CONFIG
# -----------------------------
DROP_COLS = ["Customer_ID", "ID", "Name", "SSN"]

CATEGORICAL_COLS = [
    "Occupation",
    "Type_of_Loan",
    "Credit_Mix",
    "Payment_of_Min_Amount",
    "Payment_Behaviour",
    "Credit_Score"
]


# -----------------------------
# UTIL FUNCTIONS
# -----------------------------
def parse_month(col):
    """
    Convert Month column to numeric (1–12).
    Handles: 'September', '9', 9, '01'
    """
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
    """
    mode:
        - 'train'   → used inside notebook
        - 'predict' → used inside Flask / inference
    """

    df = df.copy()

    # -----------------------------
    # Drop ID / non-feature columns
    # -----------------------------
    df.drop(columns=DROP_COLS, errors="ignore", inplace=True)

    # -----------------------------
    # Month handling
    # -----------------------------
    if "Month" in df.columns:
        df["Month"] = parse_month(df["Month"])

        if df["Month"].isna().all():
            df["Month"] = 1
        else:
            df["Month"] = df["Month"].fillna(
                df["Month"].dropna().mode().iloc[0]
            )

    # -----------------------------
    # Categorical Encoding
    # -----------------------------
    encoders = pickle.load(open("models/encoders.pkl", "rb"))

    for col in CATEGORICAL_COLS:
        if col in df.columns:
            le = encoders[col]

            # handle unseen labels safely
            df[col] = df[col].map(
                lambda x: x if x in le.classes_ else le.classes_[0]
            )
            df[col] = le.transform(df[col])

    # -----------------------------
    # Numeric coercion
    # -----------------------------
    for col in df.columns:
        if col not in CATEGORICAL_COLS:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    df.fillna(0, inplace=True)

    # -----------------------------
    # Feature order enforcement
    # -----------------------------
    FEATURES = pickle.load(open("models/features.pkl", "rb"))
    df = df.reindex(columns=FEATURES, fill_value=0)

    return df
