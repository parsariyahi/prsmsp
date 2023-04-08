import json

import requests

from prsmsp.abstracts.abcpanel import ABCSmsPanel
from prsmsp.factories import AuthFactory
from prsmsp.models import Response


class GhasedakSms(ABCSmsPanel):
    def __init__(self, api_key: str) -> None:
        """Take the auth info

        :param api_key: your ghasedak sms api key auth
        :type api_key: str

        :rtype None
        :return: None
        """
        self.auth = AuthFactory.get("api_key")(api_key)

    def _response_parser(self, resp):
        status_code = int(resp.status_code)
        real_response = json.loads(resp.text)

        return Response(status_code, real_response)

    def send_sms(self, receptor: str, message: str, originator: str) -> Response:
        """send sms with ghasedak sms panel

        :param receptor: reciver of your message
        :type receptor: str

        :param message: the message you want to send
        :type message: str

        :param originator: the originator that you want to send your message
        :type originator: str

        :rtype Response
        :return: The requests response
        """

        url = "https://api.ghasedak.me/v2/sms/send/simple"

        data = {
            "receptor": receptor,
            "message": message,
            "originator": originator,
        }

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded",
            "charset": "utf-8",
            "apikey": self.auth.api_key,
        }

        resp = requests.post(url, data=data, headers=headers)

        return self._response_parser(resp)
