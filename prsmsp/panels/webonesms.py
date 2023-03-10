import json

import requests

from prsmsp.abctracts.abcpanel import ABCSmsPanel
from prsmsp.models import Response
# WSDL service


class WebOneSms(ABCSmsPanel):

    def _response_parser(self, resp):
        status_code = int(resp.status_code)
        real_response = json.loads(resp.text)

        return Response(status_code, real_response)

    def send_sms(self, receptor: str, message: str, username: str, password: str, line_number: str):
        """send sms with webone-sms.ir sms panel

        Args:
            receptor (str): the reciver of your sms.
            message (str): your message.
            username (str): your username.
            password (str): your password.
            line_number (str): your line number that webone gave it to you.

        Returns:
            _type_: _description_

        Http Request Type: GET
        """

        url = "http://webone-sms.ir/SMSInOutBox/sendsms"
        params = {
            "username": username,
            "password": password,
            "from": line_number,
            "to": receptor,
            "text": message,
        }

        resp = requests.get(url, params=params)

        return self._response_parser(resp)
