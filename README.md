# nager_date.py
Web-API for [date.nager.at](https://date.nager.at) popular project to query holidays that currently support's over 100 countries

## Example
```python
from nager_date import NagerDate

nager_date = NagerDate()
country_info = nager_date.get_country_info(country_code="US")
print(country_info)
```
