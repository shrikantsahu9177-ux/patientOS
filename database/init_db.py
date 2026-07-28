import os
import sys

# Add parent directory to path so we can import models
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask
from models.models import db

def create_app():
    app = Flask(__name__, template_folder='../ui', static_folder='../assets')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database/patientos.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
        print("Database tables created successfully.")
