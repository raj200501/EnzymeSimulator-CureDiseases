from app import db
from models.enzyme import Enzyme
from models.dna_sequence import DNASequence

# Create tables
db.create_all()

# Insert initial genomic data
genomic_data = [
    DNASequence(sequence="ATCG", source="Database A"),
    DNASequence(sequence="GCTA", source="Database B"),
]

db.session.add_all(genomic_data)
db.session.commit()

print("Database initialized and populated with genomic data.")
