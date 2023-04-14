import json
import unittest

from prsmsp.panels import MeliPayamak
from prsmsp.models import Response


class TestNikSmsPanel(unittest.TestCase):

    def test_send_sms(self):
        with open('./config.json') as file:
            melipayamak_configs = json.load(file)["niksms"]
            fake_success_response = Response(200, dict())
            panel = MeliPayamak(melipayamak_configs["username"], melipayamak_configs["password"])
            panel_resp = panel.send_sms('09909090900', 'some', melipayamak_configs["originator"])
            self.assertEqual(fake_success_response, panel_resp)


if __name__ == "__main__":
    unittest.main()
