import json

import requests

from prsmsp.abctracts.abcpanel import ABCSmsPanel


class KaveNegar(ABCSmsPanel):

    def send_sms(self, receptor: str, message: str, api_key: str):
        """send sms with kavenegar sms panel

        Args:
            receptor (str): the reciver of your sms,
                            if there is many seperate them with comma (,)
                            like: 09xxx,09xxx,09xxx.
            message (str): your message.
            api_key (str): this is the way that kavenegar authenticate you,
                           they will give you this when you bought your service.

        Returns:
            dict: the response that kavenegar will return.

        Http Request Type: GET
        """

        url = f"https://api.kavenegar.com/v1/{api_key}/sms/send.json"

        params = {
                "receptor": receptor,
                "message": message,
            }

        resp = requests.get(url, params=params)

        #jsonify the real response of your kavenegar resp,
        #for more info read the docs https://kavenegar.com/rest.html
        return json.loads(resp.text)
