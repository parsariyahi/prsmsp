import unittest

from prsmsp.models.auth import APIKeyAuth, UnamePassAuth


class TestAuthModels(unittest.TestCase):

    def test_api_key_model(self):
        api_key = 'your api key'
        model = APIKeyAuth(api_key)

        self.assertEqual(model.api_key, api_key)

    def test_username_pass_model(self):
        username = 'username'
        password = 'password'
        model = UnamePassAuth(username, password)

        self.assertEqual(model.username, username)
        self.assertEqual(model.password, password)


if __name__ == "__main__":
    unittest.main()
