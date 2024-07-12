from backend.app import db

class DNASequence(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sequence = db.Column(db.String(500), nullable=False)
    source = db.Column(db.String(100), nullable=False)
