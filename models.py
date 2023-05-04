from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    role = db.Column(db.String(50))
    office = db.Column(db.String(100))


class SupportTicket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticket_topic = db.Column(db.String(100))
    description = db.Column(db.String(500))
    opened_by = db.Column(db.Integer, db.ForeignKey("user.id"))
    opened_by_user = db.relationship("User", foreign_keys=[opened_by], lazy="select")
    category = db.Column(db.String(100))
    importance = db.Column(db.String(100))
    closed_by = db.Column(db.Integer, db.ForeignKey("user.id"))
    closed_by_username = db.relationship(
        "User", foreign_keys=[closed_by], lazy="select"
    )
    created_at = db.Column(db.DateTime, default=datetime.now)
    status = db.Column(db.String(100), default="open")
