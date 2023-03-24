import json
import unittest

from prsmsp.panels import Kavenegar
from prsmsp.models import Response


class TestKaveNegarPanel(unittest.TestCase):

    def test_send_sms(self):
        with open('./config.json') as file:
            kavenegar_configs = json.load(file)["kavenegar"]
            fake_success_response = Response(200, dict())
            panel = Kavenegar(kavenegar_configs["api_key"])
            panel_resp = panel.send_sms('09909090900', 'some')
            self.assertEqual(fake_success_response, panel_resp)


if __name__ == "__main__":
    unittest.main()
