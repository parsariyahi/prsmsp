Introduction
============
This package is a middle-ware between you and your sms provider.
We just call the apis that your sms provider has and send the data that you gave us.

Motivation
**********
I needed to use several sms panels in a project and i had to implement each of them, so i thought i can write a package that do this for me, i just import the panel that i want to use and use it.
In this way, i didn't need to implement each at the time, just use the needed panel and send the data to this package.

Examples
********
Example for Kavenegar sms panel, authentication is done by api key

.. code-block:: python
   :caption: send sms with Kavenegar
   
   from prsmsp.panels import Kavenegar
   
   api_key = "your api key"
   panel = Kavenegar(api_key)

   receptor = "sms reciver"
   message = "sms message"
   resp = panel.send_sms(receptor, message)

   print(resp.status_code)


Example for Webonesms sms panel, authentication is done by username password

.. code-block:: python
   :caption: send sms with Webonesms
   
   from prsmsp.panels import WebOneSms
   
   username = "your username"
   password = "your password"
   panel = WebOneSms(username, password)

   receptor = "sms reciver"
   message = "sms message"
   originator = "sms panel originator"
   resp = panel.send_sms(receptor, message, originator)

   print(resp.status_code)

