import unittest
import pandas as pd
from src.pipeline.prediction_pipeline import PredictionPipeline

class TestPredictionPipeline(unittest.TestCase):

    def test_predict(self):
        data = pd.DataFrame({
            'Gender': ['Male'],
            'Height': [177],
            'Weight': [80]
        })
        pipeline = PredictionPipeline(data)
        result = pipeline.predict()
        
        self.assertTrue(0 <= result[0] <=5)

if __name__ == '__main__':
    unittest.main()
