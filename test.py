import unittest
from unittest.mock import patch, mock_open
import json
from io import StringIO
from lessonOrganizer2A import Login, SignUp, initialize_user_data  # Replace `your_script` with your script's filename

class TestLoginSystem(unittest.TestCase):

    @patch("builtins.input", side_effect=["test_user", "test_pass"])
    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps([{"username": "test_user", "password": "test_pass"}]))
    @patch("sys.stdout", new_callable=StringIO)
    def test_login_successful(self, mock_stdout, mock_open, mock_input):
        Login()
        self.assertIn("Login successful!", mock_stdout.getvalue())

    @patch("builtins.input", side_effect=["wrong_user", "wrong_pass", "n"])
    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps([{"username": "test_user", "password": "test_pass"}]))
    @patch("sys.stdout", new_callable=StringIO)
    def test_login_unsuccessful(self, mock_stdout, mock_open, mock_input):
        Login()
        self.assertIn("Invalid username or password.", mock_stdout.getvalue())
        self.assertIn("Please try logging in again.", mock_stdout.getvalue())

    @patch("builtins.input", side_effect=["test_user", "test_pass", "y", "new_user", "new_pass"])
    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps([{"username": "test_user", "password": "test_pass"}]))
    @patch("sys.stdout", new_callable=StringIO)
    def test_login_with_signup(self, mock_stdout, mock_open, mock_input):
        Login()
        self.assertIn("Invalid username or password.", mock_stdout.getvalue())
        self.assertIn("Sign-up successful!", mock_stdout.getvalue())

    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps({}))
    @patch("json.dump")
    def test_initialize_user_data(self, mock_json_dump, mock_open):
        initialize_user_data("new_user")
        mock_json_dump.assert_called_once()

if __name__ == "__main__":
    unittest.main()
#hi Sir