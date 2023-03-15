import json

import requests

from prsmsp.abctracts.abcpanel import ABCSmsPanel
from prsmsp.factories import AuthFactory
from prsmsp.models import Response


class MeliPayamak(ABCSmsPanel):

    def __init__(self, username, password):
        self.auth = AuthFactory.get('username_pass')(username, password)

    def _response_parser(self, resp):
        status_code = int(resp.status_code)
        real_response = json.loads(resp.text)

        return Response(status_code, real_response)

    def send_sms(self, receptor: str, message: str, originator: str):
        """send sms with melipayamak sms panel

        Args:
            receptor (str): the reciver of your sms,
                            if there is many seperate them with comma (,)
                            like: 09xxx,09xxx,09xxx.
            message (str): your message.
            originator (str): your number that want to send the sms
            from_ (str): your line number or (originator)

        Returns:
            dict: the response that melipayamak will return.

        Http Request Type: POST
        """

        url = "https://rest.payamak-panel.com/api/SendSMS/SendSMS"

        data = {
                "to": receptor,
                "from": originator,
                "text": message,
                "isFlash": False,
                "username": self.auth.username,
                "password": self.auth.password,
            }

        resp = requests.post(url, json=data)

        return self._response_parser(resp)
