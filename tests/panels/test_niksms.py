import json
import unittest

from prsmsp.panels import NikSms
from prsmsp.models import Response


class TestNikSmsPanel(unittest.TestCase):

    def test_send_sms(self):
        with open('./config.json') as file:
            niksms_configs = json.load(file)["niksms"]
            fake_success_response = Response(200, dict())
            panel = NikSms(niksms_configs["username"], niksms_configs["password"])
            panel_resp = panel.send_sms('09909090900', 'some', niksms_configs["originator"])
            self.assertEqual(fake_success_response, panel_resp)


if __name__ == "__main__":
    unittest.main()
