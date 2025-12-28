# 📊 Credit Score Prediction System  
**End-to-End Machine Learning Project with Flask**

---

## 📌 Project Overview

This project is an **end-to-end Machine Learning application** that predicts a customer’s **creditworthiness** based on financial and behavioral attributes.

The system includes:
- Data preprocessing & model training (Jupyter Notebook)
- Model serialization
- A Flask backend for inference
- A user-friendly web interface (HTML + CSS)
- Production-safe preprocessing to ensure **training–inference consistency**

---

## 🎯 Objective

To classify a customer’s **Credit Status** (`Good` / `Bad`) and estimate the **probability of default** using historical credit data.

---

## 🧠 Machine Learning Details

- **Problem Type:** Supervised Classification  
- **Algorithm Used:** (as trained in notebook, e.g., Random Forest / Logistic Regression)  
- **Target Variable:** `Credit_Score`  
- **Evaluation Metrics:**  
  - Precision  
  - Recall  
  - F1-Score  
  - ROC-AUC  

---

## 🗂️ Project Structure

```bash
credit-score-project/
│
├── app/
│ ├── app.py # Flask app factory
│ ├── routes.py # Routes for UI & prediction
│ └── model_loader.py # Loads model & scaler
│
├── src/
│ └── preprocess.py # Centralized preprocessing logic
│
├── data/
│ ├── train.csv
│ └── test.csv
│
├── models/
│ ├── credit_model.pkl # Trained ML model
│ ├── scaler.pkl # Feature scaler
│ ├── encoders.pkl # Label encoders for categorical features
│ └── features.pkl # Feature order used during training
│
├── template/
│ └── index.html # Frontend HTML form
│
├── static/
│ ├── style.css # Styling
│ └── script.js # (Optional) JS for async requests
│
├── notebook/
│ └── CreditScoreClassifier.ipynb
│
├── requirements.txt
├── run.py
└── README.md
```

---

## 🔄 End-to-End Workflow

```bash 
Raw Data
↓
Data Cleaning & Feature Engineering (Notebook)
↓
Model Training & Evaluation
↓
Save Model, Scaler, Encoders & Feature Schema
↓
Flask Backend Loads Artifacts
↓
User Input (Web Form)
↓
Consistent Preprocessing
↓
Prediction & Risk Probability
```


---

## 🧪 Preprocessing Strategy (Key Highlight)

To avoid common production issues, **all preprocessing is centralized** in:
``` bash
src/preprocess.py
```


This ensures:
- Same categorical encoding as training
- Same numerical cleaning logic
- Safe handling of unseen categories
- Consistent `Month` parsing (handles `"September"`, `"9"`, `9`)
- Exact feature **order matching training**
- No data leakage

---

## 🌐 Web Application

### Features:
- Fully functional credit prediction form
- Accepts all model input features
- Clean UI using CSS
- Can work **with or without JavaScript**
- Backend-driven inference using Flask

### Routes:
| Route | Method | Description |
|------|--------|------------|
| `/` | GET | Render prediction form |
| `/predict` | POST | Perform credit prediction |

---

## ▶️ How to Run the Project

### 1️⃣ Clone the repository
```bash
git clone <repo-url>
cd credit-score-project
```

### 2️⃣ Install dependencies 
```bash
pip install -r requirements.txt 
```
### 3️⃣ Run the Flask app 
```bash
python run.py
``` 
### 4️⃣ Open in browser 
```bash
http://127.0.0.1:5000/
``` 
### 🧾 Sample Prediction Output 
```bash
Credit Status: Good 
Default Risk: 0.137
```

## 🧑‍💻 Tech Stack

- **Python**
- **Pandas, NumPy**
- **Scikit-learn**
- **Flask**
- **HTML & CSS**

---

## 💡 Key Learnings & Highlights

- Built a **production-safe ML pipeline**
- Handled real-world data issues (missing values, mixed formats)
- Solved feature schema & ordering problems
- Designed clean Flask architecture using app factory
- Separated concerns: training vs inference vs UI

---

## 📈 Future Improvements

- Convert preprocessing into an sklearn `Pipeline`
- Add SHAP-based model explainability
- Add server-side input validation
- Dockerize the application
- Deploy to cloud (Render / Railway / AWS)

---

## 👤 Author

**P Sreyanshu Anupam**  
Machine Learning & Data Science Enthusiast

---

## 📄 License

This project is for **educational and demonstration purposes**.

