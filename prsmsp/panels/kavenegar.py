import requests

from prsmsp.abctracts.abcpanel import ABCSmsPanel


class KaveNegar(ABCSmsPanel):

    #api_key = None
    #receptor = None
    #message = None

    def test_panel(self):
        """test the sms panel (connection, url, etc.)
        in this case we used the getdate api from {kavenegar} smspanel.
        """

        url = "https://api.kavenegar.com/v1/0/utils/getdate.json"
        resp = requests.get(url)

        return resp

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
            _type_: _description_
        """

        url = f"https://api.kavenegar.com/v1/{api_key}/sms/send.json"

        params = {
                "receptor": receptor,
                "message": message,
            }

        resp = requests.get(url, params=params)

        return resp
