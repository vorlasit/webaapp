from database import db
from .user import user_group

class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    users = db.relationship('User', secondary=user_group, back_populates='groups')
