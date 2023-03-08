import unittest

from prsmsp.panels.kavenegar import KaveNegar
from prsmsp.models.response import Response


class TestRespnoseModel(unittest.TestCase):

    def test_send_sms(self):
        fake_success_response = Response(200, dict())
        panel = KaveNegar()
        panel_resp = panel.send_sms('09393535526', 'some', '4E3638544854644634596B315A6975556849413430307864764E4A50374B6C557572416B4C6531324841453D')
        self.assertEqual(fake_success_response, panel_resp)


if __name__ == "__main__":
    unittest.main()
