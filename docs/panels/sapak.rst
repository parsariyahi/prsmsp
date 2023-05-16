Sapak
=====
Sapak is a well documented sms provider with good and stable services. 
`Their Site <https://sapak.me/>`_

Send Sms
********
sending sms with Sapak sms panel

.. code-block:: python
   :caption: send sms with Sapak
   
   from prsmsp.panels import Sapak
   
   api_key = "your api key"
   panel = Sapak(api_key)

   receptor = "sms reciver"
   message = "sms message"
   originator = "sms panel originator"
   resp = panel.send_sms(receptor, message, originator)

   print(resp.status_code)

