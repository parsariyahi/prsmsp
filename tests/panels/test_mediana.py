import json
import unittest

from prsmsp.panels import Mediana
from prsmsp.models import Response


class TestSmsDotIrPanel(unittest.TestCase):

    def test_send_sms(self):
        with open('./config.json') as file:
            smsir_configs = json.load(file)["smsir"]
            fake_success_response = Response(200, dict())
            panel = Mediana(smsir_configs["api_key"])
            panel_resp = panel.send_sms('09909090900', 'some', smsir_configs["originator"])
            self.assertEqual(fake_success_response, panel_resp)


if __name__ == "__main__":
    unittest.main()
