import unittest
from unittest.mock import patch
from gimmethat import app, check_auth
from base64 import b64encode
from io import StringIO
from random import shuffle, sample, randint
from string import ascii_letters, digits

TEST_TRUE_CREDENTIALS = [{"username": "new_user",
                          "password": "new_user_password"}]

TEST_FALSE_CREDENTIALS = [{"username": "admin",
                           "password": "admin"}]


def produce_random_text():
    charset = ascii_letters + digits
    s = list(charset)
    shuffle(s)
    s = sample(s, randint(1, len(s)))
    return ''.join(s)


class LoginTests(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_page_open_no_creds(self):
        response = self.client.get('/')
        assert response.status_code == 401

    @patch('gimmethat.users.load_creds', return_value=TEST_TRUE_CREDENTIALS)
    def test_page_open_wrong_creds(self, load_creds_function):
        user = TEST_FALSE_CREDENTIALS[0]
        auth = b64encode(
            bytes(user['username'] + ':' + user['password'], 'utf8')).decode()
        response = self.client.get(
            '/', headers={'Authorization': 'Basic {}'.format(auth)})
        assert response.status_code == 401

    @patch('gimmethat.users.load_creds', return_value=TEST_TRUE_CREDENTIALS)
    def test_page_open_correct_creds(self, load_creds_function):
        user = TEST_TRUE_CREDENTIALS[0]
        auth = b64encode(
            bytes(user['username'] + ':' + user['password'], 'utf8')).decode()
        response = self.client.get(
            '/', headers={'Authorization': 'Basic {}'.format(auth)})
        assert response.status_code == 200

    @patch('os.listdir', return_value=[])
    @patch('gimmethat.users.load_creds', return_value=TEST_TRUE_CREDENTIALS)
    def test_upload_file_wrong_creds(self, load_creds_function, listdir_function):
        user = TEST_FALSE_CREDENTIALS[0]
        auth = b64encode(
            bytes(user['username'] + ':' + user['password'], 'utf8')).decode()
        files = []
        num_of_files = randint(1, 100)
        response = self.client.post(
            '/',
            data={'file': []},
            headers={'Authorization': 'Basic {}'.format(auth)})

        print(response.status_code)
        assert response.status_code == 401

    @patch('os.listdir', return_value=[])
    @patch('gimmethat.users.load_creds', return_value=TEST_TRUE_CREDENTIALS)
    def test_upload_file_correct_creds(
        self, load_creds_function, listdir_function):
        user = TEST_TRUE_CREDENTIALS[0]
        auth = b64encode(
            bytes(user['username'] + ':' + user['password'], 'utf8')).decode()
        response = self.client.post(
            '/',
            data={'file': []},
            headers={'Authorization': 'Basic {}'.format(auth)})

        print(response.status_code)
        assert response.status_code == 302

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()