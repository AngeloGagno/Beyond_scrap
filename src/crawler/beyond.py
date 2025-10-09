from requests import HTTPError
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from datetime import datetime, timedelta
import requests


class BeyondCrawler:
    def __init__(
        self,
        cookies: dict,
        headers: dict,
        *,
        max_retries: int = 5,
        backoff_factor: float = 1.5,
        status_forcelist: tuple[int, ...] = (429, 500, 502, 503, 504),
        allowed_methods: set[str] = {"GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS"},
    ):
        self.cookies = cookies
        self.headers = headers
        self.session = self._session_with_retry(
            max_retries=max_retries,
            backoff_factor=backoff_factor,
            status_forcelist=status_forcelist,
            allowed_methods=allowed_methods,
        )

    def _session_with_retry(
        self,
        *,
        max_retries: int,
        backoff_factor: float,
        status_forcelist: tuple[int, ...],
        allowed_methods: set[str],
    ) -> requests.Session:
        retry = Retry(
            total=max_retries,
            connect=max_retries,
            read=max_retries,
            status=max_retries,
            backoff_factor=backoff_factor,
            status_forcelist=status_forcelist,
            allowed_methods=allowed_methods,
            respect_retry_after_header=True,
        )
        adapter = HTTPAdapter(max_retries=retry)
        s = requests.Session()
        s.mount("https://", adapter)
        s.mount("http://", adapter)
        return s

    def get_endpoint_status_page(self) -> int:
        resp = self.session.get(
            "https://api.beyondpricing.com/api/pricing/listings",
            cookies=self.cookies,
            headers=self.headers,
            timeout=15,
        )
        return resp.status_code

    def get_endpoint_webpage(self):
        status = self.get_endpoint_status_page()
        if status == 200:
            resp = self.session.get(
                "https://api.beyondpricing.com/api/pricing/listings",
                cookies=self.cookies,
                headers=self.headers,
                timeout=15,
            )
            return resp.json()
        else:
            raise HTTPError(f"Status: {status}")


class BeyondPost(BeyondCrawler):
    def __init__(
        self,
        cookies:dict,
        headers:dict,
        start_date: datetime,
        end_date: datetime,
        percentual: float,
        accommodation_id: str,
        *,
        max_retries: int = 5,
        backoff_factor: float = 1.5,
        status_forcelist: tuple[int, ...] = (429, 500, 502, 503, 504),
        allowed_methods: set[str] = {"GET", "POST"},
        timeout: int = 15,
    ):
        super().__init__(
            cookies,
            headers,
            max_retries=max_retries,
            backoff_factor=backoff_factor,
            status_forcelist=status_forcelist,
            allowed_methods=allowed_methods,
        )
        self.start_date = start_date
        self.end_date = end_date
        self.percentual = percentual
        self.timeout = timeout

        self.url = self.url_generator(accommodation_id)
        self.weeklist = self.week_list()
        self.calendar_creator = self.calendar_overrides_creator()
        self.payload = self.post_json()

    def url_generator(self, accommodation_id) -> str:
        return f"https://api.beyondpricing.com/api/pricing/listings/{accommodation_id}/edit-overrides"

    def week_list(self) -> list[str]:
        days_name = []
        d = self.start_date
        while d <= self.end_date:
            days_name.append(d.strftime("%A").lower())
            d += timedelta(days=1)
        return list(dict.fromkeys(days_name)) 

    def calendar_overrides_creator(self) -> list[dict]:
        calendar_overrides = []
        d = self.start_date
        while d <= self.end_date:
            calendar_overrides.append(
                {
                    "date": d.strftime("%Y-%m-%d"),
                    "manual_overrides": {"price_dynamic_override": self.percentual / 100.0},
                }
            )
            d += timedelta(days=1)
        return calendar_overrides

    def post_json(self) -> dict:
        return {
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "end_date": self.end_date.strftime("%Y-%m-%d"),
            "days_of_week": self.weeklist,
            "price_percentage_override": 100 + self.percentual,
            "calendar_overrides": self.calendar_creator,
        }

    def post_beyond_pipeline(self) -> requests.Response:
        resp = self.session.post(
            url=self.url,
            cookies=self.cookies,
            headers=self.headers,
            json=self.payload,
            timeout=self.timeout,
        )
        return resp
