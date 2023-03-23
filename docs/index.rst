.. prsmsp documentation master file, created by
   sphinx-quickstart on Tue Mar 21 22:30:55 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Contents

   /intro

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Source

   /source/prsmsp

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Panels

   /panels/panels
   /panels/kavenegar
   /panels/smsdotir
   /panels/webonesms
   /panels/melipayamak


What is prsmsp ?
================
prsmsp is an open source project for working with sms providers.
this project is working as a middle-ware between you and your sms provider's panel.
prsmsp is a python library but we will add an api for it in future.
in this way you can use this lib in every programming language.

Wy i wrote this package?
========================
I needed to use several sms panels and send sms with each, so in this way i had to write each from scratch.
So i had this idea to have a package, like just import the panel that is needed and just send sms with it without any extra codes.

How to use this project
=======================
Example of how to import the panel and use it.

:doc:`Panels Doc </panels/panels>`

.. code-block:: python
   :caption: send sms with Kavenegar
   
   from prsmsp.panels import Kavenegar
   
   api_key = "your api key"
   panel = Kavenegar(api_key)

   receptor = "sms reciver"
   message = "sms message"
   resp = panel.send_sms(receptor, message)

   print(resp.status_code)

How to support this project?
============================
For getting a real test of each panel we need a subscription for each sms provider, if you have a subscription of any panel and you think its good for this project to have it, please contact me.
Another way to support this project is to contribute in any way (development, documentation, etc.).


How to contact me
=================
My email: pany.parsariyahi@gmail.com




* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
