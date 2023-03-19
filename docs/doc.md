# Prsmsp Document

## Instalation
```shell
pip install prsmsp
```
* * *
## Import

### Import Panels

>#### you can import the class
>```python
>from prsmsp.panels import {YOUR_SMS_PANEL_CLASS}
>```
>where the ```YOUR_SMS_PANEL_CLASS``` is the class of that panel

>#### or you can import the module
>```python
>from prsmsp.panels import {YOUR_SMS_PANEL_NAME}
>```
>where the ```YOUR_SMS_PANEL_NAME``` is the name of that panel

#### **Example**

>Import The Class
>```python
>from prsmsp.panels import KaveNegar
>```

>Import The Module
>```python
>from prsmsp.panels import kavenegar
>```

## Authentication
Just pass your Auth data into your panel class when you initiate the class

>```python
>from prsmsp.panels import {YOUR_SMS_PANEL_CLASS} as YourPanel
>
>panel = YourPanel(auth)
>```

### __api key__
>```python
>from prsmsp.panels import {YOUR_SMS_PANEL_CLASS} as YourPanel
>
>api_key = 'your api key'
>panel = YourPanel(api_key)
>```

### __Username Password__ 
>```python
>from prsmsp.panels import {YOUR_SMS_PANEL_CLASS} as YourPanel
>
>username, password = 'your username', 'your password'
>panel = YourPanel(username, password)
>```

## Sending Sms 

### **```send_sms()```** method

>```python
>from prsmsp.panels import {YOUR_SMS_PANEL_CLASS} as YourPanel
>
>panel = YourPanel(auth)
>panel.send_sms(data)
>```
the **```data```** depends on your sms panel, for more info read the docs of your panels


## Response

>```python
>from prsmsp.panels import {YOUR_SMS_PANEL_CLASS} as YourPanel
>
>panel = YourPanel(auth)
>resp = panel.send_sms(data)
>print(rsep.status_code) # returns http status code of your request
>print(resp.real_resp) # returns the exact response that your sms panel sent
>```
the **```resp.status_code```** is HTTP status code for your request.

the **```resp.real_resp```** is the response that your sms panel sent to us.