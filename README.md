# <div align="center"> <img src="https://date.nager.at/images/logo.webp" width="200" style="vertical-align:middle;" /> nager_date.py </div>

> Web-API for [Nager.Date](https://date.nager.at) — a public holiday API covering 100+ countries with support for long weekends, upcoming holidays, and worldwide data.
</div>

## Quick Start
```python
from nager_date import NagerDate

nager = NagerDate()

# Get public holidays in Germany for 2025
print(nager.get_public_holidays(year=2025, country_code="DE"))

# Check if today is a public holiday in the US
status = nager.is_today_public_holiday("US")
print(status)  # 200 = yes, 204 = no, 400 = error

# Get upcoming holidays worldwide
print(nager.get_worldwide_upcoming_public_holidays())
```

---

## Countries

| Method | Description |
|--------|-------------|
| `get_available_countries()` | List all supported countries |
| `get_country_info(country_code)` | Get details for a specific country |

---

## Public Holidays

| Method | Description |
|--------|-------------|
| `get_public_holidays(year, country_code)` | Get public holidays for a country and year |
| `get_long_weekends(year, country_code)` | Get long weekends for a country and year |
| `is_today_public_holiday(country_code)` | Check if today is a public holiday |
| `get_upcoming_public_holidays(country_code)` | Next public holidays for a country |
| `get_worldwide_upcoming_public_holidays()` | Next public holidays across all countries |

---

## `is_today_public_holiday` Response Codes

| Code | Meaning |
|------|---------|
| `200` | Today is a public holiday |
| `204` | Today is not a public holiday |
| `400` | Invalid country code |
