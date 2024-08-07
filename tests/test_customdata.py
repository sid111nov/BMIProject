import unittest
from src.pipeline.CustomData import CustomData

class TestCustomData(unittest.TestCase):

    def test_get_data_as_data_frame(self):
        custom_data = CustomData(gender='Male', height=177, weight=80)
        df = custom_data.get_data_as_data_frame()
        self.assertEqual(df.shape[0], 1)
        self.assertEqual(df.iloc[0]['Gender'], 'Male')
        self.assertEqual(df.iloc[0]['Height'], 177)
        self.assertEqual(df.iloc[0]['Weight'], 80)

if __name__ == '__main__':
    unittest.main()
