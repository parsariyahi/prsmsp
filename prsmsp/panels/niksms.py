import json

import requests

from prsmsp.abstracts.abcpanel import ABCSmsPanel
from prsmsp.factories import AuthFactory
from prsmsp.models import Response


class NikSms(ABCSmsPanel):
    def __init__(self, username, password) -> None:
        """Take the auth info

        :param username: webonesms username
        :type username: str

        :param password: webonesms password
        :type password: str

        :rtype None
        :return: None
        """
        self.auth = AuthFactory.get("username_pass")(username, password)

    def _response_parser(self, resp: requests.Response) -> Response:
        status_code = int(resp.status_code)
        real_response = json.loads(resp.text)

        return Response(status_code, real_response)

    def send_sms(self, receptor: str, message: str, originator: str = "") -> Response:
        """send sms with niksms sms panel

        :param receptor: reciver of your message
        :type receptor: str

        :param message: the message you want to send
        :type message: str

        :param originator: the originator that you want to send your message (optional)
        :type originator: str

        :rtype Response
        :return: The requests response
        """

        url = "https://niksms.com/fa/PublicApi/PtpSms"

        data = {
            "numbers": [receptor],
            "message": message,
            "username": self.auth.username,
            "password": self.auth.password,
        }

        if originator :
            data["senderNumber"] = originator

        resp = requests.post(url, json=data)

        return self._response_parser(resp)
