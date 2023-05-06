import json
import unittest

from prsmsp.panels import SmsOne
from prsmsp.models import Response


class TestSmsOnePanel(unittest.TestCase):

    def test_send_sms(self):
        with open('./config.json') as file:
            smsone_configs = json.load(file)["smsone"]
            fake_success_response = Response(200, dict())
            panel = SmsDotIr(smsone_configs["api_key"])
            panel_resp = panel.send_sms('09909090900', 'some')
            self.assertEqual(fake_success_response, panel_resp)


if __name__ == "__main__":
    unittest.main()

