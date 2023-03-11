import json
import unittest

from prsmsp.panels import MeliPayamak
from prsmsp.models import Response


class TestMeliPayamakPanel(unittest.TestCase):

    def test_send_sms(self):
        with open('./config.json') as file:
            melipayamak_configs = json.load(file)["melipayamak"]
            fake_success_response = Response(200, dict())
            panel = MeliPayamak()
            panel_resp = panel.send_sms('09393535526', 'some', melipayamak_configs["originator"], melipayamak_configs["username"], melipayamak_configs["password"])
            self.assertEqual(fake_success_response, panel_resp)


if __name__ == "__main__":
    unittest.main()
