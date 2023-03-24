Mediana
=======
Mediana is a modern and well designed sms panel, has a lots if freatures for normal users and programmers.
`Their Site <https://mediana.ir/>`_

Send Sms
********
sending sms with mediana

.. code-block:: python
   :caption: send sms with mediana
   
   from prsmsp.panels import Mediana
   
   api_key = "your api key"
   panel = Mediana(api_key)

   receptor = "sms reciver"
   message = "sms message"
   originator = "sms panel originator"
   resp = panel.send_sms(receptor, message, originator)

   print(resp.status_code)
