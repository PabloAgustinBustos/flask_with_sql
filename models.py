from flask_login import UserMixin
from app import db

class User(db.Model, UserMixin):
    __tablename__ = "users"

    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False)
    password = db.Column(db.Text, nullable=False)
    role = db.Column(db.String(10))
    description = db.Column(db.String(10))

    def __repr__(self):
        return f"<User: {self.username}, Role: {self.role}>"
    
    get_id = lambda self: self.uid