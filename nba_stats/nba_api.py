import datetime

from requests import get
import pandas as pd


class NbaAPI():
    TODAY = datetime.datetime.today()
    BASE_URL = 'http://stats.nba.com/stats/'
    HEADERS = {
        'Host': 'stats.nba.com',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/78.0.3904.97 Safari/537.36',
        'Referer': 'https://stats.nba.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
    }

    def __init__(self, endpoint, params):
        """
        Args:
            endpoint: endpoint for our api call
        """
        self.endpoint = endpoint
        self.params = params
        self.json = self._get_json()

    def get_result(self, result_set_name: str=None):
        """Return a specific set of results from our request for those that
        support it.

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
            try:
                result_set = next(
                    (res for res in self.json['resultSets']
                     if res['name'] == result_set_name), None)
            except KeyError:
                # maybe it's under 'resultSet'
                result_set = next(
                    (res for res in self.json['resultSet']
                     if res['name'] == result_set_name), None)
        else:
            # there should only be one resultSet to lookup
            try:
                result_set = self.json['resultSet']
            except KeyError:
                # maybe it's under 'resultSets'
                result_set = self.json['resultSets'][0]

        headers = result_set['headers']
        values = result_set['rowSet']

        return pd.DataFrame(values, columns=headers)

    def _get_json(self):
        """
        Internal method to streamline our requests / json getting

        Args:
            params (dict): parameters to be passed to the API

        Raises:
            HTTPError: if requests hits a status code != 200

        Returns:
            json (json): json object for selected API call
        """
        _get = get(
            self.BASE_URL + self.endpoint,
            params=self.params,
            headers=self.HEADERS)
        _get.raise_for_status()

        return _get.json()
