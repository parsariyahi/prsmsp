import requests

from prsmsp.abctracts.abcpanel import ABCSmsPanel

# WSDL service


class WebOneSms(ABCSmsPanel):

    def test_panel(self, username, password, from_, to, text):
        """test the sms panel (connection, url, etc.)
        in this case we used the sendsms api from {webone-sms.ir} smspanel.
        """

        url = "http://webone-sms.ir/SMSInOutBox/sendsms"
        params = {
            "username": username,
            "password": password,
            "from": from_,
            "to": to,
            "text": text,
        }

        resp = requests.get(url, params=params)

        return resp

    def send_sms(self, receptor: str, message: str, username: str, password: str, line_number: str):
        """send sms with webone-sms.ir sms panel

        Args:
            receptor (str): the reciver of your sms.
            message (str): your message.
            username (str): your username.
            password (str): your password.
            line_number (str): your line number that webone gave it to you.

        Returns:
            _type_: _description_

        Http Request Type: GET
        """

        url = "http://webone-sms.ir/SMSInOutBox/sendsms"
        params = {
            "username": username,
            "password": password,
            "from": line_number,
            "to": receptor,
            "text": message,
        }

        resp = requests.get(url, params=params)

        return resp
