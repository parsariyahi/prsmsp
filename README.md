<div align="center">
    <h1> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/IMessage_logo.svg/2048px-IMessage_logo.svg.png" width="80px"><br/>prsmsp</h1>
</div>
<p align="center"> <a href="https://prsmsp.readthedocs.io" target="_blank"><img alt="" src="https://img.shields.io/badge/Website-EA4C89?style=normal&logo=dribbble&logoColor=white" style="vertical-align:center" /></a>
    
   
# Description
Python Library for sending SMS with supported SMS service providers, This project works as an API between you and your SMS provider, read more about this project at [Read The Docs](https://prsmsp.readthedocs.io/).

<br>

# Features
When you use a SMS panel from a provider, you implement it from zero, and if you want to change the panel, you need to refactor all of your code.
and for implementing a panel from zero you need time to read their document and try to use it and implement it.
this project save you time for implementing panels and for refactoring your code.

## Why use this project?
- You have all the famous and well designed SMS panels ready to go.
- You can have several SMS panels at the same time.
- Don't need to build the wheel of your bicycle each time ☺.
- Fast and Small
- Easy to implement and use

<br>

# Supported panels

* [Kavenegar](http://kavenegar.com)
* [Sms.ir](http://sms.ir)
* [Web one](http://webone-sms.ir)
* [Meli Payamak](https://www.melipayamak.com)
* [Mediana](https://mediana.ir)
* [Ghasedak Sms](https://ghasedak.me)
* [Faraz Sms](https://farazsms.com/)
* [Nik Sms](https://niksms.com/)
* [Sms1](https://sms1.ir/)

<br>

# How to use?
First lets install the package
```shell
pip install prsmsp
```

This block of code is for **kavenegar** sms panel.

Each of sms panels has its own parameters. Please read their docs first.

```python
from prsmsp.panels import Kavenegar

api_key = "your api key"
panel = Kavenegar(api_key)  # auth

receptor = "your receptor"
msg = "your message"
panel.send_sms(receptor, msg)
```

#### [Docs](https://prsmsp.readthedocs.io/en/latest/panels/panels.html)

<br>

# How to support this project?
for this project to be better and bigger than what it is now.
we need to support more panels and even test a real send sms which needs a subscription for each sms provider 
if you have subs for any sms panel or docs of any sms panel and you think it would be good for this pacakge to have support that sms panel please open an issue or contact me
My email is pany.parsariyahi@gmail.com

