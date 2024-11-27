import unittest
from app.app import app

class FlaskTestCase(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Set up the Flask test client before running tests
        cls.client = app.test_client()

    def test_hello(self):
        # Simulate a GET request to the root URL
        response = self.client.get('/')
        
        # Assert the response status code is 200 OK
        self.assertEqual(response.status_code, 200)
        
        # Assert the response data matches the expected output
        self.assertEqual(response.data.decode('utf-8'), "Hello, Docker!")
    
    def test_not_found(self):
        # Simulate a GET request to a non-existing URL
        response = self.client.get('/nonexistent')
        
        # Assert the response status code is 404 Not Found
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()

