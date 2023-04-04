## Supported panels

* [Kavenegar](http://kavenegar.com)
* [Sms.ir](http://sms.ir)
* [Web one](http://webone-sms.ir)
* [Meli Payamak](https://www.melipayamak.com)
* [Mediana](https://mediana.ir)
* [Ghasedak Sms](https://ghasedak.me)

## Why use this package?

1.  You have all the famous and well designed sms panels ready to go.
2.  When you have to work with several sms panels.
3.  Don't need to build the wheel of your bicycle each time ☺.

## How to use

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
### Read [Docs](https://prsmsp.readthedocs.io/)


## How to support this project
for this project to be better and bigger than what it is now.
we need to support more panels and even test a real send sms which needs a subscription for each sms provider 
if you have subs for any sms panel or docs of any sms panel and you think it would be good for this pacakge to have support that sms panel please open an issue or contact me
My email is pany.parsariyahi@gmail.com
