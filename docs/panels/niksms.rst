NikSms
======

NikSms is a well designed sms provider, They have great support team, and good documantation.
`Their Site <https://niksms.com/>`_.

Send Sms
********
sending sms with NikSms

.. code-block:: python
   :caption: send sms with NikSms

   from prsmsp.panels import NikSms
   
   username = "your username"
   password = "your password"
   panel = NikSms(username, password)

   receptor = "sms reciver"
   message = "sms message"
   originator = "sms panel originator" # Optional
   resp = panel.send_sms(receptor, message, originator)

   print(resp.status_code)
