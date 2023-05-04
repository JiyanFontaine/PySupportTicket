from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import *
from app import createApp

app = createApp()
app.config["SQLALCHEMY_DATABASE_URI"] = Config.SQLALCHEMY_DATABASE_URI

if __name__ == "__main__":
    app.run()
