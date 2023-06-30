from prsmsp.panels import *

class PanelFactory:

    @staticmethod
    def get(panel_name: str):

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

        if p:
            return p

        raise KeyError("Panel Not Found")

