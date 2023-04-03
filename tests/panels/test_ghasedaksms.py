import json
import unittest

from prsmsp.panels import GhasedakSms
from prsmsp.models import Response


class TestGhasedakSms(unittest.TestCase):

    def test_send_sms(self):
        with open('./config.json') as file:
            ghasedaksms_config = json.load(file)["ghasedaksms"]
            fake_success_response = Response(200, dict())
            panel = GhasedakSms(ghasedaksms_config["api_key"])
            panel_resp = panel.send_sms('09909090900', 'some', ghasedaksms_config["originator"])
            self.assertEqual(fake_success_response, panel_resp)


if __name__ == "__main__":
    unittest.main()
