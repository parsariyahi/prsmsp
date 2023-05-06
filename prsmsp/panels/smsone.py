import json

import requests

from prsmsp.abstracts.abcpanel import ABCSmsPanel
from prsmsp.factories import AuthFactory
from prsmsp.models import Response


class SmsOne(ABCSmsPanel):
    def __init__(self, api_key: str) -> None:
        """Take the auth info

        :param api_key: your smsone token auth
        :type api_key: str

        :rtype None
        :return: None
        """
        self.auth = AuthFactory.get("api_key")(api_key)

    def _response_parser(self, resp: requests.Response) -> Response:
        status_code = int(resp.status_code)
        real_response = json.loads(resp.text)

        return Response(status_code, real_response)

    def send_sms(
        self, receptor: str, message: str
    ) -> Response:  # NoQA
        """send sms with smsone sms panel

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
            "Authorization": f"Bearer {self.auth.api_key}"
        }

        url = "https://app.sms1.ir:7001/api/service/send"

        data = {
            "message": message,
            "recipient": receptor,
        }

        resp = requests.post(url, headers=headers, json=data)

        return self._response_parser(resp)