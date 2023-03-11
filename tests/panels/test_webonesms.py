import json
import unittest

from prsmsp.panels import WebOneSms
from prsmsp.models import Response


class TestWebOneSmsPanel(unittest.TestCase):

    def test_send_sms(self):
        with open('./config.json') as file:
            webonesms_configs = json.load(file)["webonesms"]
            fake_success_response = Response(200, dict())
            panel = WebOneSms()
            panel_resp = panel.send_sms('09393535526', 'some', webonesms_configs["username"], webonesms_configs["password"], webonesms_configs["originator"])
            self.assertEqual(fake_success_response, panel_resp)


if __name__ == "__main__":
    unittest.main()
