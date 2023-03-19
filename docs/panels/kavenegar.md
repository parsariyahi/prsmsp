kavenegar sms panel

usage
```python
from prsmsp.panels.kavenegar import KaveNegar

panel = KaveNegar()

"""
receptor -> is the reciver of your message, recpetor: str
msg      -> is your message that you want to send, msg: str
api_key  -> is your authentication info that kavenegar gave to you, api_key: str
"""

receptor = "Your Recivers"
msg = "Your Message"
api_key = "Your Auth Key"

resp = panel.send_sms(receptor, msg, api_key)

print(resp)
```

