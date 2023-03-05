## Supporting panels

*   [x] [Kavenegar](http://kavenegar.com)
*   [x] [Web one](http://webone-sms.ir)
*   [x] [Sms ir](http://sms.ir)

## Why use this lib?

1.  You have all the famous and well designed sms panels ready to go.
2.  When you have to work with several sms panels.
3.  Don't need to build the wheel of your bicycle each time ☺.

## Usage

This block of code is for kavenegar sms panel.

Each of sms panels has its own parameters. Please read their docs first.

```python
from prsmsp.panels.kavenegar import KaveNegar

panel = Kavenegar()

panel.send_sms(receptor, msg, api_key)
```
