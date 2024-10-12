import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get("DB_URI", f"sqlite:///app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
