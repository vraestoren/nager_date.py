from requests import Session, Response

class NagerDate:
	def __init__(self) -> None:
		self.api = "https://date.nager.at/api/v3"
		self.session = Session()
		self.session.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
		}

	def _get(self, endpoint: str) -> Response:
		return self.session.get(f"{self.api}{endpoint}")

	def get_country_info(self, county_code: str) -> dict:
		return self._get(f"/CountryInfo/{country_code}").json()
	
	def get_available_countries(self) -> dict:
		return self._get("/AvailableCountries").json()
	
	def get_long_weekends(
			self,
			year: int,
			country_code: str) -> dict:
		return self._get(f"/LongWeekend/{year}/{country_code}").json()
	
	def get_public_holidays(
			self, year: int, country_code: str) -> dict:
		return self._get(
			f"/PublicHolidays/{year}/{country_code}").json()
	
	def is_today_public_holiday(self, country_code: str) -> int:
		return self._get(
			f"/IsTodayPublicHoliday/{country_code}").status_code
	
	def get_upcoming_public_holidays(self, country_code: str) -> dict:
		return self._get(
			f"/NextPublicHolidays/{country_code}").json()
	
	def get_worldwide_upcoming_public_holidays(self) -> dict:
		return self._get(
			f"/NextPublicHolidaysWorldWide").json()
