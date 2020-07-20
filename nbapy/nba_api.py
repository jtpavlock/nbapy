"""API wrapper for stats.nba.com."""

import time

import pandas as pd
import requests
import requests_cache

# TODO: is there a better way than a global variable?
_last_req_time = 0.0

try:
    if requests_cache.core.get_cache():
        HAS_REQUESTS_CACHE = True
except AttributeError:
    HAS_REQUESTS_CACHE = False


class NbaAPI:
    """Represents an API call for stats.nba.com ."""

    BASE_URL = "https://stats.nba.com/stats/"
    HEADERS = {
        "Host": "stats.nba.com",
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0)"
            " Gecko/20100101 Firefox/61.0"
        ),
        "Accept": "application/json",
        "Accept-Language": "en-US,en;q=0.5",
        "Referer": "https://stats.nba.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "x-nba-stats-origin": "stats",
        "x-nba-stats-token": "true",
    }

    if HAS_REQUESTS_CACHE:
        _session = requests_cache.CachedSession()
    else:
        _session = requests.Session()

    def __init__(self, endpoint: str = "", params: dict = None):
        """Make an api call to a specific endpoint with parameters.

        Args:
            endpoint: url endpoint for our api call
                stats.nba.com/stats/{endpoint}
            params: api parameters to pass
        """
        self.endpoint = endpoint
        self.params = params
        self.json = self._get_json(rate_limit=1)

        if HAS_REQUESTS_CACHE:
            print("here")

    def get_result(self, result_set_name: str = None) -> pd.DataFrame:
        """Return a specific set of results from our request for those that support it.

        Args:
            result_set_name: The name of the json 'resultSet' to return.
                This should be set whenever the nba.com api returns more than
                one 'resultSet' to specify which you want. If there is only
                one, it may be left blank.

        Returns:
            Result in a panadas dataframe

        """
        # result_set can either be under 'resultSets' or 'resultSet'
        if result_set_name:
            result_set = next(
                (
                    res
                    for res in self.json["resultSets"]
                    if res["name"] == result_set_name
                ),
                None,
            )
        else:
            # there should only be one resultSet to lookup
            try:
                result_set = self.json["resultSet"]
            except KeyError:
                # maybe it's under 'resultSets'
                result_set = self.json["resultSets"][0]

        if not result_set:
            raise KeyError

        headers = result_set["headers"]
        values = result_set["rowSet"]

        return pd.DataFrame(values, columns=headers)

    def _get_json(self, rate_limit: float):
        """Gets the request from stats.nba.com .

        Will also update _last_req_time if the request was not from a cache.
        Args:
            rate_limit: how long to wait in seconds in between api calls
                is ignored if the requests are cached

        Raises:
            requests.exceptions.HTTPError: if requests hits a status code != 200
            requests.exceptions.Timeout: if requests.get takes longer than `timeout`

        Returns:
            json (json): json object for selected API call
        """
        global _last_req_time
        current = time.time()
        time_passed = current - _last_req_time

        while time_passed < rate_limit:
            time.sleep(1)
            time_passed += 1

        response = self._session.get(
            self.BASE_URL + self.endpoint,
            params=self.params,
            headers=self.HEADERS,
            timeout=5,
        )
        response.raise_for_status()

        if not (HAS_REQUESTS_CACHE and response.from_cache):
            _last_req_time = time.time()

        return response.json()
