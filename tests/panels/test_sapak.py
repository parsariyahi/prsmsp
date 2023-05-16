import json
import unittest

from prsmsp.panels import Sapak
from prsmsp.models import Response


class TestSapakPanel(unittest.TestCase):

    def test_send_sms(self):
        with open('./config.json') as file:
            sapak_configs = json.load(file)["sapak"]
            fake_success_response = Response(200, dict())
            panel = Sapak(sapak_configs["api_key"])
            panel_resp = panel.send_sms('09909090900', 'some', sapak_configs["originator"])
            self.assertEqual(fake_success_response, panel_resp)


if __name__ == "__main__":
    unittest.main()

