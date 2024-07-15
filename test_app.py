import unittest
from app import app 

class TestApp(unittest.TestCase):

    # create test client
    def setUp(self):
        self.app = app.test_client()

    # test '/' route & simulate GET request, check that response status code is 200
    def test_index(self):
        response = self.app.get('/') 
        self.assertEqual(response.status_code, 200)  

# run tests
if __name__ == '__main__':
    unittest.main()  
