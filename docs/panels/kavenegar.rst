Kavenegar
=========

Kavenegar is one of the most and easy to use sms providers.
`Their Site <https://kavenegar.com>`_.

Send Sms
********
sending sms with kavenegar

.. code-block:: python
   :caption: send sms with Kavenegar
   
   from prsmsp.panels import Kavenegar
   
   api_key = "your api key"
   panel = Kavenegar(api_key)

   receptor = "sms reciver"
   message = "sms message"
   resp = panel.send_sms(receptor, message)

   print(resp.status_code)
