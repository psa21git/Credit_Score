from flask import Flask
from app.routes import predict_bp
import os

def create_app():
    app = Flask(__name__,
                template_folder=os.path.join(os.getcwd(), "template"),
                static_folder=os.path.join(os.getcwd(), "static"),
                static_url_path="/static"
        )
    app.register_blueprint(predict_bp)
    return app
