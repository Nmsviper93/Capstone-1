import unittest
from app import app  

class TestIntegration(unittest.TestCase):

    # create test client
    def setUp(self):
        self.app = app.test_client() 

    # test interaction between landing route ('/') and '/api/data' route
    def test_index_and_api_data_interaction(self):
        # simulate GET request to '/', check response status code is 200
        response = self.app.get('/')  
        self.assertEqual(response.status_code, 200)  

        # simulate GET request to '/api/data', check response status code is 200
        response = self.app.get('/api/data')  
        self.assertEqual(response.status_code, 200)  
        # check that 'data' key is present in JSON response
        self.assertIn('data', response.json())  

# run tests
if __name__ == '__main__':
    unittest.main()  