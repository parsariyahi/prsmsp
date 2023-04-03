Ghasedak
========
ghasedak sms is a well designed sms provider, has greate documentation and stable services. 
`Their Site <https://ghasedak.me/>`_

Send Sms
********
sending sms with ghasedak sms

.. code-block:: python
   :caption: send sms with Kavenegar
   
   from prsmsp.panels import GasedakSms
   
   api_key = "your api key"
   panel = GasedakSms(api_key)

   receptor = "sms reciver"
   message = "sms message"
   originator = "sms panel originator"
   resp = panel.send_sms(receptor, message, originator)

   print(resp.status_code)
