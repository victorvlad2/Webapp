import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        # Set up a test client for making requests to the app
        self.app = app.test_client()

    def test_main_page(self):
        # Send a GET request to the root URL ("/")
        response = self.app.get('/')
        
        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        
        # Optionally, you can check the content of the response
        self.assertIn(b"Enter a team number 1-40", response.data)

    def test_api_output(self):
        # Send a POST request to the "/api_output" endpoint with user input
        response = self.app.post('/api_output', data={'user_input': '1'})
        
        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        
        # Optionally, you can check the content of the response
        self.assertIn(b"Team Stats:", response.data)

if __name__ == '__main__':
    unittest.main()