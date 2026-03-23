from flask import Flask
from app.routes import predict_bp
import os
import pickle

def create_app():
    app = Flask(__name__,
                template_folder=os.path.join(os.getcwd(), "template"),
                static_folder=os.path.join(os.getcwd(), "static"),
                static_url_path="/static"
        )

    # ✅ LOAD MODEL HERE (inside create_app)
    model = pickle.load(open("models/credit_model.pkl", "rb"))
    scaler = pickle.load(open("models/scaler.pkl", "rb"))
    features = pickle.load(open("models/features.pkl", "rb"))

    # store in app (so routes can access)
    app.model = model
    app.scaler = scaler
    app.features = features

    app.register_blueprint(predict_bp)
    return app
