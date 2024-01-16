from prsmsp.abstracts.abcpanel import ABCSmsPanel
from prsmsp.panels import *

class PanelFactory:

    @staticmethod
    def get(panel_name: str) -> ABCSmsPanel:

        PANELS = {
            "kavenegar": Kavenegar,
            "smsdotir": SmsDotIr,
            "webonesms": WebOneSms,
            "melipayamak": MeliPayamak,
            "mediana": Mediana,
            "ghasedaksms": GhasedakSms,
            "farazsms": FarazSms,
            "niksms": NikSms,
            "smsone": SmsOne,
            "sapak": Sapak,
        }

        p = PANELS.get(panel_name, None)
        print(p)
        if p:
            return p

        raise KeyError("Panel Not Found")


class Panel:

    staticmethod
    def initiate(panel_name: str, **auth) -> ABCSmsPanel:
        if ("username" in auth and "password" in auth) \
        or ("api_key" in auth):
            p = PanelFactory.get(panel_name)

            return p(*auth.values())
        else:
            raise Exception("Authentication Info must be (username='', password='') or (api_key='')")
