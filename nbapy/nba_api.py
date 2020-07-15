"""API wrapper for stats.nba.com."""

import datetime

from requests import get
import pandas as pd


class NbaAPI:
    """Represents an API call for stats.nba.com."""

    TODAY = datetime.datetime.today()
    BASE_URL = "http://stats.nba.com/stats/"
    HEADERS = {
        "Host": "stats.nba.com",
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0)"
            " Gecko/20100101 Firefox/61.0"
        ),
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        "Referer": "https://stats.nba.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "x-nba-stats-origin": "stats",
        "x-nba-stats-token": "true",
    }

    def __init__(self, endpoint: str, params):
        """Make an api call to a specific endpoint with parameters.

        Args:
            endpoint: url endpoint for our api call
                stats.nba.com/stats/{endpoint}
            params: api parameters to pass
        """
        self.endpoint = endpoint
        self.params = params
        self.json = self._get_json()

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

    def _get_json(self):
        """Internal method to streamline our requests / json getting.

        Raises:
            HTTPError: if requests hits a status code != 200

        Returns:
            json (json): json object for selected API call
        """
        _get = get(
            self.BASE_URL + self.endpoint, params=self.params, headers=self.HEADERS
        )
        _get.raise_for_status()

        return _get.json()
