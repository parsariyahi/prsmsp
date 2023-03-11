import json

import requests

from prsmsp.abctracts.abcpanel import ABCSmsPanel
from prsmsp.models import Response


class MeliPayamak(ABCSmsPanel):

    def _response_parser(self, resp):
        status_code = int(resp.status_code)
        real_response = json.loads(resp.text)

        return Response(status_code, real_response)

    def send_sms(self, receptor: str, message: str, originator: str, username: str, password: str):
        """send sms with melipayamak sms panel

        Args:
            receptor (str): the reciver of your sms,
                            if there is many seperate them with comma (,)
                            like: 09xxx,09xxx,09xxx.
            message (str): your message.
            originator (str): your number that want to send the sms
            from_ (str): your line number or (originator)
            username, password (str): this is the way that melipayamak authenticate you,
                           they will give you this when you bought your service.

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
                "username": username,
                "password": password,
            }

        resp = requests.post(url, json=data)

        return self._response_parser(resp)
