import json

import requests

from prsmsp.abctracts.abcpanel import ABCSmsPanel
from prsmsp.factories import AuthFactory
from prsmsp.models import Response


class WebOneSms(ABCSmsPanel):

    def __init__(self, username, password):
        self.auth = AuthFactory.get('username_pass')(username, password)

    def _response_parser(self, resp):
        status_code = int(resp.status_code)
        try:
            real_response = json.loads(resp.text)
        except json.JSONDecodeError:
            # if the json coder couldn't decode,
            # we just put it like what is is
            real_response = {'resp': resp.text}

        return Response(status_code, real_response)

    def send_sms(self, receptor: str, message: str, line_number: str):
        """send sms with webone-sms.ir sms panel

        Args:
            receptor (str): the reciver of your sms.
            message (str): your message.
            line_number (str): your line number that webone gave it to you.

        Returns:
            _type_: _description_

        Http Request Type: GET
        """

        url = "http://webone-sms.ir/SMSInOutBox/sendsms"
        params = {
            "username": self.auth.username,
            "password": self.auth.password,
            "from": line_number,
            "to": receptor,
            "text": message,
        }

        resp = requests.get(url, params=params)

        return self._response_parser(resp)
