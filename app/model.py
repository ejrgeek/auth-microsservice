from .extensions import db

class User(db.Model):
    __tablename__ = "users"
    __table_args__ = {'schema': 'auth_schema'}
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)