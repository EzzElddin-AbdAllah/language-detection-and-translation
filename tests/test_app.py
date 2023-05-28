import sys
import os
# Get the path to the project's root directory
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Add the project root directory to the Python path
sys.path.insert(0, root_path)

import main
import unittest
import json

class MyTestCase(unittest.TestCase):
    """
    Test case for the Flask app endpoints.

    Attributes:
        app (Flask): The Flask test client.
    """

    def setUp(self):
        """
        Set up the test case by configuring the Flask test client.
        """
        main.app.testing = True
        self.app = main.app.test_client()

    def test_lang_detection(self):
        """
        Test the 'lang_detection' endpoint.
        """
        headers = {"Content-Type": "application/json"}
        data = {'sentence': 'It was discontinued in February 2018.'}
        response = self.app.post('/lang_detection', data=json.dumps(data), headers=headers)
        result = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result, {'language': 'English'})

    def test_translation(self):
        """
        Test the 'translation' endpoint.
        """
        headers = {"Content-Type": "application/json"}
        data = {'sentence': 'It was discontinued in February 2018.'}
        response = self.app.post('/translation', data=json.dumps(data), headers=headers)
        result = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result, {'en': 'It was discontinued in February 2018.', 'ar': 'تم إيقافه في فبراير 2018.'})


if __name__ == '__main__':
    unittest.main()