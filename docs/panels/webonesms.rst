Webonesms
=========
Webonesms is a sms provider that is not famous but has some nice features and good stability. 
`Their Site <https://webone-sms.ir/>`_.

Send Sms
********
sending sms with Webonesms

.. code-block:: python
   :caption: send sms with Kavenegar
   
   from prsmsp.panels import WebOneSms
   
   api_key = "your api key"
   panel = WebOneSms(api_key)

   receptor = "sms reciver"
   message = "sms message"
   originator = "sms panel originator"
   resp = panel.send_sms(receptor, message, originator)

   print(resp.status_code)

