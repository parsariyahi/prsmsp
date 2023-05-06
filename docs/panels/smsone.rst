Sms1
====
Sms1 is a unknown sms panel, but has good documentation and great features.
`Their Site <https://sms1.ir/>`_

Send Sms
********
sending sms with sms1

.. code-block:: python
   :caption: send sms with sms1
   
   from prsmsp.panels import SmsOne
   
   token = "your token"
   panel = SmsOne(token)

   receptor = "sms reciver"
   message = "sms message"
   resp = panel.send_sms(receptor, message)

   print(resp.status_code)

