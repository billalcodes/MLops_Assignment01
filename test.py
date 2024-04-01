import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_prediction_endpoint(self):
        data = {'budget': 1000000, 'popularity': 8.5}
        response = self.app.post('/predict', json=data)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'prediction', response.data)
        prediction = response.json['prediction']
        self.assertTrue(0 <= prediction <= 1)

if __name__ == '__main__':
    unittest.main()
