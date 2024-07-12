import unittest
from backend.handlers.simulation_handler import run_simulation

class SimulationHandlerTestCase(unittest.TestCase):
    def test_run_simulation(self):
        enzyme = "enzyme1"
        dna_sequence = "ATCG"
        result = run_simulation(enzyme, dna_sequence)
        self.assertIn("interaction_result", result)

if __name__ == '__main__':
    unittest.main()
