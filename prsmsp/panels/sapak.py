import json

import requests

from prsmsp.abstracts.abcpanel import ABCSmsPanel
from prsmsp.factories import AuthFactory
from prsmsp.models import Response


class Sapak(ABCSmsPanel):
    def __init__(self, api_key: str) -> None:
        """Take the auth info

        :param api_key: your sapak api key auth
        :type api_key: str

        :rtype None
        :return: None
        """
        self.auth = AuthFactory.get("api_key")(api_key)

    def _response_parser(self, resp: requests.Response) -> Response:
        status_code = int(resp.status_code)
        if resp.text:
            real_response = json.loads(resp.text)
        else:
            real_response = resp.text

        return Response(status_code, real_response)

    def send_sms(
        self, receptor: str, message: str, originator: str
    ) -> Response:  # NoQA
        """send sms with sapak sms panel

        :param receptor: reciver of your message
        :type receptor: str

        :param message: the message you want to send
        :type message: str

        :param originator: the originator that you want to send your message
        :type originator: str

        :rtype Response
        :return: The requests response
        """

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "X-API-KEY": self.auth.api_key,
        }

        url = "https://api.sapak.me/v1/messages"

        data = {
            "text": message,
            "from": originator,
            "to": receptor,
        }

        resp = requests.post(url, headers=headers, json=data)

        return self._response_parser(resp)
