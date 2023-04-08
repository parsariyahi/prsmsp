import sys
import json

import requests

from prsmsp.abstracts.abcpanel import ABCSmsPanel
from prsmsp.factories import AuthFactory
from prsmsp.models import Response


class Mediana(ABCSmsPanel):
    # this is the client version for mediana package
    # this is not relevant to our package version,
    # its just the version that mediana package uses.
    __client_version = "1.0.1"
    __user_agent = (
        f"MedianaSMS/ApiClient/{__client_version} Python/{str(sys.hexversion)}"
    )

    def __init__(self, api_key: str) -> None:
        """Take the auth info

        :param api_key: your mediana api key auth
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
        """send sms with mediana sms panel

        :param receptor: reciver of your message
        :type receptor: str

        :param message: the message you want to send
        :type message: str

        :rtype Response
        :return: The requests response
        """

        url = "http://rest.medianasms.com/v1/messages"  # the url for send sms

        params = {
            "originator": originator,
            "recipients": [receptor],
            "message": message,
        }

        headers = requests.utils.default_headers()
        # this is just a simple defualt header.
        # mediana require this, also they implement it in this way.
        auth_header = f"AccessKey {self.auth.api_key}"
        headers.update(
            {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "Authorization": auth_header,
                "User-Agent": self.__user_agent,
            }
        )

        resp = requests.get(url, headers=headers, params=params)

        return self._response_parser(resp)
