FarazSms
========
FarazSms is a modern sms provider with stable services. they have good documentation and nice admin panel
`Their Site <https://farazsms.com/>`_

Send Sms
********
sending sms with FarazSms

.. code-block:: python
   :caption: send sms with FarazSms
   
   from prsmsp.panels import FarazSms
   
   api_key = "your api key"
   panel = FarazSms(api_key)

   receptor = "sms reciver"
   message = "sms message"
   originator = "sms panel originator"
   resp = panel.send_sms(receptor, message, originator)

   print(resp.status_code)
