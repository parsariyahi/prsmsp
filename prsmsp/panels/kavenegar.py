import json

import requests

from prsmsp.abstracts.abcpanel import ABCSmsPanel
from prsmsp.factories import AuthFactory
from prsmsp.models import Response


class Kavenegar(ABCSmsPanel):
    def __init__(self, api_key: str) -> None:
        """Take the auth info

        :param api_key: your kavenegar api key auth
        :type api_key: str

        :rtype None
        :return: None
        """
        self.auth = AuthFactory.get("api_key")(api_key)

    def _response_parser(self, resp):
        status_code = int(resp.status_code)
        real_response = json.loads(resp.text)

        return Response(status_code, real_response)

    def send_sms(self, receptor: str, message: str) -> Response:
        """send sms with kavenegar sms panel

        :param receptor: reciver of your message
        :type receptor: str

        :param message: the message you want to send
        :type message: str

        :rtype Response
        :return: The requests response
        """

        url = f"https://api.kavenegar.com/v1/{self.auth.api_key}/sms/send.json"

        params = {
            "receptor": receptor,
            "message": message,
        }

        resp = requests.get(url, params=params)

        return self._response_parser(resp)
