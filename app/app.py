from flask import Flask
from app.routes import predict_bp
import os
import pickle
import gdown

def create_app():
    app = Flask(__name__,
                template_folder=os.path.join(os.getcwd(), "template"),
                static_folder=os.path.join(os.getcwd(), "static"),
                static_url_path="/static"
        )

    # Download models from Google Drive if they don't exist
    # Note: The link for scaler.pkl is the same as credit_model.pkl based on your input
    # update the scaler.pkl link if it was a copy-paste error
    base_dir = os.getcwd()
    models_dir = os.path.join(base_dir, "models")
    os.makedirs(models_dir, exist_ok=True)
    
    files_to_download = {
        os.path.join(models_dir, "credit_model.pkl"): "19LG5gbtMZuvpxtpfhUAHEyOfm6HmA-kz",
        os.path.join(models_dir, "scaler.pkl"): "141bw4eosyYcq1RsWhRCr7lvbWULVnYQQ", 
        os.path.join(models_dir, "features.pkl"): "1zbnCpRSec281iFvpQqyx9gUngS9y5gco"
    }

    for path, file_id in files_to_download.items():
        if not os.path.exists(path):
            print(f"Downloading {path} from Google Drive...")
            gdown.download(id=file_id, output=path, quiet=False)

    # ✅ LOAD MODEL HERE (inside create_app)
    model = pickle.load(open(os.path.join(models_dir, "credit_model.pkl"), "rb"))
    scaler = pickle.load(open(os.path.join(models_dir, "scaler.pkl"), "rb"))
    features = pickle.load(open(os.path.join(models_dir, "features.pkl"), "rb"))

    # store in app (so routes can access)
    app.model = model
    app.scaler = scaler
    app.features = features

    app.register_blueprint(predict_bp)
    return app
