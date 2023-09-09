#!/usr/bin/env python3

import unittest
from unittest.mock import patch
#from app import echo_input
from app import app
from flask import Flask, request
from api_request import data

class test_echo_input(unittest.TestCase):

    @patch('app.echo_input',input_text="test")

    def test_echo_input(self, patch):
        input_test_result = patch.input_text
        self.assertEqual (input_test_result, "test")

#def get_data(self, api):
#        response = requests.get(f"{api}")
#        if response.status_code == 200:
#            print("sucessfully fetched the data")
#            self.formatted_print(response.json())
#        else:
#            print(f"Hello person, there's a {response.status_code} error with your request")
#class integration_test():
#    def test_integration():
#        return

if __name__ == 'app':
    unittest.app()