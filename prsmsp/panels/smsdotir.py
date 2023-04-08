import json

import requests

from prsmsp.abstracts.abcpanel import ABCSmsPanel
from prsmsp.factories import AuthFactory
from prsmsp.models import Response


class SmsDotIr(ABCSmsPanel):
    def __init__(self, api_key: str):
        """Take the auth info

        :param api_key: your smsir api key auth
        :type api_key: str

        :rtype None
        :return: None
        """
        self.auth = AuthFactory.get("api_key")(api_key)

    def _response_parser(self, resp):
        status_code = int(resp.status_code)
        real_response = json.loads(resp.text)

        return Response(status_code, real_response)

    def send_sms(
        self, receptor: str, message: str, originator: str
    ) -> Response:  # NoQA
        """send sms with smsir sms panel

        :param receptor: reciver of your message
        :type receptor: str

        :param message: the message you want to send
        :type message: str

        :param originator: the originator that you want to send your message
        :type originator: str

        :rtype Response
        :return: The requests response
        """
        receptors = []
        messages = []

        headers = {
            "X-API-KEY": self.auth.api_key,
            "ACCEPT": "application/json",
            "Content-Type": "application/json",
        }

        url = "https://api.sms.ir/v1/send/likeToLike"

        receptors.append(receptor)
        messages.append(message)

        data = {
            "LineNumber": originator,
            "MessageTexts": messages,
            "Mobiles": receptors,
        }

        resp = requests.post(url, headers=headers, json=data)

        return self._response_parser(resp)
