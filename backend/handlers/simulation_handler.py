from models.simulation import EnzymeSimulation

def run_simulation(enzyme, dna_sequence):
    simulation = EnzymeSimulation(enzyme, dna_sequence)
    result = simulation.run()
    return result
