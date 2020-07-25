from nbapy import constants
from nbapy.nba_api import NbaAPI


class Summary:
    _endpoint = "draftcombinestats"

    def __init__(
        self, league_id=constants.League.Default, season=constants.CURRENT_SEASON
    ):
        self._params = {"LeagueID": league_id, "SeasonYear": season}
        self.api = NbaAPI(self._endpoint, self._params)

    def stats(self):
        return self.api.get_result()


class DrillResults:
    _endpoint = "draftcombinedrillresults"

    def __init__(
        self, league_id=constants.League.Default, season=constants.CURRENT_SEASON
    ):
        self._params = {"LeagueID": league_id, "SeasonYear": season}
        self.api = NbaAPI(self._endpoint, self._params)

    def stats(self):
        return self.api.get_result()


class SpotShooting:
    _endpoint = "draftcombinespotshooting"

    def __init__(
        self, league_id=constants.League.Default, season=constants.CURRENT_SEASON
    ):
        self._params = {"LeagueID": league_id, "SeasonYear": season}
        self.api = NbaAPI(self._endpoint, self._params)

    def stats(self):
        return self.api.get_result()
