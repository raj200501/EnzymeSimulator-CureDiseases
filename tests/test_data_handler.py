import unittest
from backend.handlers.data_handler import get_genomic_data

class DataHandlerTestCase(unittest.TestCase):
    def test_get_genomic_data(self):
        data = get_genomic_data()
        self.assertTrue(len(data) > 0)

if __name__ == '__main__':
    unittest.main()
