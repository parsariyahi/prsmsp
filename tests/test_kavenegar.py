import json
import unittest

from prsmsp.panels.kavenegar import KaveNegar
from prsmsp.models.response import Response


class TestRespnoseModel(unittest.TestCase):

    def test_send_sms(self):
        with open('./config.json') as file:
            kavenegar_configs = json.load(file)["kavenegar"]
            fake_success_response = Response(200, dict())
            panel = KaveNegar()
            panel_resp = panel.send_sms('09393535526', 'some', kavenegar_configs["api_key"])
            self.assertEqual(fake_success_response, panel_resp)


if __name__ == "__main__":
    unittest.main()
