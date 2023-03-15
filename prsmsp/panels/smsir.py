import json

import requests

from prsmsp.abctracts.abcpanel import ABCSmsPanel
from prsmsp.factories import AuthFactory
from prsmsp.models import Response


class SmsIr(ABCSmsPanel):

    def __init__(self, api_key):
        self.auth = AuthFactory.get('api_key')(api_key)

    def _response_parser(self, resp):
        status_code = int(resp.status_code)
        real_response = json.loads(resp.text)

        return Response(status_code, real_response)

    def send_sms(self, receptor: str, message: str, line_number: str):
        """send sms with sms.ir sms panel

        Args:
            receptor (str): the reciver of your sms,
                            if there is many seperate them with comma (,)
                            like: 09xxx,09xxx,09xxx.
            message (str): your message.

        Returns:
            _type_: _description_

        Http Request Type: POST
        """
        receptors = []
        messages = []

        headers = {
            "X-API-KEY": self.auth.api_key,
            "ACCEPT": 'application/json',
            'Content-Type': 'application/json',
        }

        url = "https://api.sms.ir/v1/send/likeToLike"

        receptors.append(receptor)
        messages.append(message)

        data = {
                "LineNumber": line_number,
                "MessageTexts": messages,
                "Mobiles": receptors,
            }

        resp = requests.post(url, headers=headers, json=data)

        return self._response_parser(resp)
