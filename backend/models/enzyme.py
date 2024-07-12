from backend.app import db

class Enzyme(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    sequence = db.Column(db.String(500), nullable=False)
