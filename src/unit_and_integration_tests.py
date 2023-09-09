import unittest
from app import app, db, Teamstats
from sqlalchemy import inspect


class TestApp(unittest.TestCase):
    def setUp(self):
        # Set up a test client for making requests to the app
        app.config['TESTING'] = True
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_main_page(self):
        # Send a GET request to the root URL ("/")
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Enter a team number 1-40", response.data)

    def test_database_creation(self):
        with app.app_context():
            inspector = inspect(db.engine)  # Create an inspector for the database
            # Check if the "teamstats" table exists
            self.assertTrue(inspector.has_table("teamstats"))

    def test_integration_api_output(self):
        # Send a POST request to the "/api_output" endpoint with user input
        response = self.app.post('/api_output', data={'user_input': '1'})
        self.assertEqual(response.status_code, 200)
        
        # Check if the response contains a specific HTML element
        self.assertIn(b'<h1 class="title"> Team </h1>', response.data)

if __name__ == '__main__':
    unittest.main()