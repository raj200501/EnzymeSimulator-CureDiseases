import unittest
from sklearn.linear_model import LinearRegression
import joblib

class ModelTrainingTestCase(unittest.TestCase):
    def test_model_training(self):
        model = joblib.load('genomic_model.pkl')
        self.assertIsInstance(model, LinearRegression)

if __name__ == '__main__':
    unittest.main()
