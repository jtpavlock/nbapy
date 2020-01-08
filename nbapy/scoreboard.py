"""Displays game info for all games in a given day"""

from datetime import datetime

from nbapy.nba_api import NbaAPI
from nbapy import constants


class Scoreboard:
    """A scoreboard for all games for a given day.

    Displays current games plus info for a given day

    Args:
        month: Specified month (1-12)
        day: Specified day (1-31)
        year: Specified year (YYYY)
        league_id: ID for the league to look in (Default is 00)
        offset: Day offset from which to operate
    """
    _endpoint = 'scoreboard'
    TODAY = datetime.today()

    def __init__(
            self,
            month=TODAY.month,
            day=TODAY.day,
            year=TODAY.year,
            league_id=constants.League.Default,
            offset=0
    ):
        self._game_date = '{month:02d}/{day:02d}/{year}'.format(month=month,
                                                                day=day,
                                                                year=year)
        self._params = {
            'LeagueID': league_id,
            'GameDate': self._game_date,
            'DayOffset': offset
        }
        self.api = NbaAPI(self._endpoint, self._params)

    def game_header(self):
        return self.api.get_result('GameHeader')

    def line_score(self):
        return self.api.get_result('LineScore')

    def series_standings(self):
        return self.api.get_result('SeriesStandings')

    def last_meeting(self):
        return self.api.get_result('LastMeeting')

    def east_conf_standings_by_day(self):
        return self.api.get_result('EastConfStandingsByDay')

    def west_conf_standings_by_day(self):
        return self.api.get_result('WestConfStandingsByDay')

    def available(self):
        return self.api.get_result('Available')
