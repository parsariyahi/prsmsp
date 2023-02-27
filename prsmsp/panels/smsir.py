import json

import requests

from prsmsp.abctracts.abcpanel import ABCSmsPanel


class SmsIr(ABCSmsPanel):

    def test_panel(self):
        """test the sms panel (connection, url, etc.)
        in this case we used the getdate api from {sms.ir} smspanel.
        """

        url = "https://api.sms.ir/v1/send/likeToLike"
        resp = requests.post(url)

        return resp

    def send_sms(self, receptor: str, message: str, api_key: str, line_number: str):
        """send sms with sms.ir sms panel

        Args:
            receptor (str): the reciver of your sms,
                            if there is many seperate them with comma (,)
                            like: 09xxx,09xxx,09xxx.
            message (str): your message.
            api_key (str): this is the way that kavenegar authenticate you,
                           they will give you this when you bought your service.

        Returns:
            _type_: _description_
        """

        headers = {
            "ACCEPT": 'application/json',
            "X-API-KEY": api_key,
        }

        url = "https://api.sms.ir/v1/send/likeToLike"

        data = {
                "LineNumber": line_number,
                "MessageText": message,
                "Mobiles": message,
            }

        resp = requests.post(url, data=json.load(data), headers=headers)

        return resp
