import os
import pickle
import gdown

MODEL_PATH = "models/credit_model.pkl"
SCALER_PATH = "models/scaler.pkl"
FEATURES_PATH = "models/features.pkl"
ENCODER_PATH = "models/encoders.pkl"

def download_models_if_missing():
    os.makedirs("models", exist_ok=True)
    
    files_to_download = {
        MODEL_PATH: "19LG5gbtMZuvpxtpfhUAHEyOfm6HmA-kz",
        SCALER_PATH: "141bw4eosyYcq1RsWhRCr7lvbWULVnYQQ", 
        FEATURES_PATH: "1zbnCpRSec281iFvpQqyx9gUngS9y5gco",
        ENCODER_PATH: "1jQLfYJvzj8yEQhS6C2hlT8emwl29XNBz" 
    }

    for path, file_id in files_to_download.items():
        if not os.path.exists(path):
            if file_id == "YOUR_ENCODERS_GDRIVE_ID_HERE":
                print(f"⚠️ Warning: Please add the gdrive link for {path} in app/model_loader.py")
                continue
            print(f"Downloading {path} from Google Drive...")
            gdown.download(id=file_id, output=path, quiet=False)

# Auto-download models
download_models_if_missing()

# Load artifacts
try:
    model = pickle.load(open(MODEL_PATH, "rb"))
    scaler = pickle.load(open(SCALER_PATH, "rb"))
    features = pickle.load(open(FEATURES_PATH, "rb"))
    encoders = pickle.load(open(ENCODER_PATH, "rb"))
except FileNotFoundError as e:
    print(f"Missing models! Please provide correct GDrive links or add them locally. {e}")
    model = None
    scaler = None
    features = None
    encoders = None
