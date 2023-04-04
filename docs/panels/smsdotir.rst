Sms.ir
======
Sms.ir is a well designed sms provider with good and stable services. 
`Their Site <https://sms.ir/>`_

Send Sms
********
sending sms with sms.ir

.. code-block:: python
   :caption: send sms with Sms.ir
   
   from prsmsp.panels import SmsDotIr
   
   api_key = "your api key"
   panel = SmsDotIr(api_key)

   receptor = "sms reciver"
   message = "sms message"
   originator = "sms panel originator"
   resp = panel.send_sms(receptor, message, originator)

   print(resp.status_code)
