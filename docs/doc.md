# Prsmsp Document

## Instalation
```shell
pip install prsmsp
```
* * *
## how to use ?

### how to import your panel

#### you can import the class
```python
from prsmsp.panels import {YOUR_SMS_PANEL_CLASS}
```
where the ```YOUR_SMS_PANEL_CLASS``` is the class of that panel

#### or you can import the module
```python
from prsmsp.panels import {YOUR_SMS_PANEL_NAME}
```
where the ```YOUR_SMS_PANEL_NAME``` is the name of that panel

#### Example

Import The Class
```python
from prsmsp.panels import KaveNegar

auth = 'Your auth info'
panel = KaveNegar(auth)
```

Import The Module
```python
from prsmsp.panels import kavenegar

auth = 'Your auth info'
panel = kavenegar.KaveNegar(auth)
```