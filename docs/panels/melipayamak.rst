Melipayamak
=========

Melipayamak is a famous sms provider. it used in wide range of companies and has good features.
`Their Site <https://www.melipayamak.com/>`_.

Send Sms
********
sending sms with kavenegar

.. code-block:: python
   :caption: send sms with Kavenegar
   
   from prsmsp.panels import MeliPayamak
   
   username = "your username"
   password = "your password"
   panel = MeliPayamak(username, password)

   receptor = "sms reciver"
   message = "sms message"
   originator = "sms panel originator"
   resp = panel.send_sms(receptor, message, originator)

   print(resp.status_code)
