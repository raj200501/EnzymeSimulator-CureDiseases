from models.dna_sequence import DNASequence

def get_genomic_data():
    # Fetch genomic data from database
    sequences = DNASequence.query.all()
    data = [{"id": seq.id, "sequence": seq.sequence, "source": seq.source} for seq in sequences]
    return data
