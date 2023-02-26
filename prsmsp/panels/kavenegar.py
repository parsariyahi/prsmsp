import requests

from prsmsp.abctract.abcpanel import ABCSmsPanel


class KaveNegar(ABCSmsPanel):

    #api_key = None
    #receptor = None
    #message = None

    def send_sms(self, receptor: str, message: str, api_key: str):
        url = f"https://api.kavenegar.com/v1/{api_key}/sms/send.json"

        params = {
                "receptor": receptor,
                "message": message,
            }

        resp = requests.get(url, params=params)

        return resp
