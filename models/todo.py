from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String(200), nullable=False)
    time = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, title, desc):
        self.title = title
        self.desc = desc

    def __repr__(self):
        return f'(id: {self.id}, title: {self.title}, desc: {self.desc})'
