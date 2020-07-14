from abc import ABC, abstractmethod

from nbapy.nba_api import NbaAPI
from nbapy import constants


class Info:
    _endpoint = "boxscoresummaryv2"

    def __init__(
        self,
        game_id: str,
        season=constants.CURRENT_SEASON,
        season_type=constants.SeasonType.Default,
        range_type=constants.RangeType.Default,
        start_period=constants.StartPeriod.Default,
        end_period=constants.EndPeriod.Default,
        start_range=constants.StartRange.Default,
        end_range=constants.EndRange.Default,
    ):
        self._params = {
            "GameID": game_id,
            "Season": season,
            "SeasonType": season_type,
            "RangeType": range_type,
            "StartPeriod": start_period,
            "EndPeriod": end_period,
            "StartRange": start_range,
            "EndRange": end_range,
        }
        self.api = NbaAPI(self._endpoint, self._params)

    def game_summary(self):
        return self.api.get_result("GameSummary")

    def other_stats(self):
        return self.api.get_result("OtherStats")

    def officials(self):
        return self.api.get_result("Officials")

    def inactive_players(self):
        return self.api.get_result("InactivePlayers")

    def game_info(self):
        return self.api.get_result("GameInfo")

    def line_score(self):
        return self.api.get_result("LineScore")

    def last_meeting(self):
        return self.api.get_result("LastMeeting")

    def season_series(self):
        return self.api.get_result("SeasonSeries")

    def available_video(self):
        return self.api.get_result("AvailableVideo")


class _BoxScore(ABC):
    @property
    @classmethod
    @abstractmethod
    def _endpoint(cls):
        return NotImplementedError

    def __init__(
        self,
        game_id: str,
        season=constants.CURRENT_SEASON,
        season_type=constants.SeasonType.Default,
        range_type=constants.RangeType.Default,
        start_period=constants.StartPeriod.Default,
        end_period=constants.EndPeriod.Default,
        start_range=constants.StartRange.Default,
        end_range=constants.EndRange.Default,
    ):
        self._params = {
            "GameID": game_id,
            "Season": season,
            "SeasonType": season_type,
            "RangeType": range_type,
            "StartPeriod": start_period,
            "EndPeriod": end_period,
            "StartRange": start_range,
            "EndRange": end_range,
        }
        self.api = NbaAPI(self._endpoint, self._params)


class BoxScore(_BoxScore):
    _endpoint = "boxscoretraditionalv2"

    def players_stats(self):
        return self.api.get_result("PlayerStats")

    def team_stats(self):
        return self.api.get_result("TeamStats")

    def team_starter_bench_stats(self):
        return self.api.get_result("TeamStarterBenchStats")


class BoxScoreScoring(_BoxScore):
    _endpoint = "boxscorescoringv2"

    def players_stats(self):
        return self.api.get_result("sqlPlayersScoring")

    def team_stats(self):
        return self.api.get_result("sqlTeamsScoring")


class BoxScoreUsage(_BoxScore):
    _endpoint = "boxscoreusagev2"

    def players_stats(self):
        return self.api.get_result("sqlPlayersUsage")

    def team_stats(self):
        return self.api.get_result("sqlTeamsUsage")


class BoxScoreMisc(_BoxScore):
    _endpoint = "boxscoremiscv2"

    def players_stats(self):
        return self.api.get_result("sqlPlayersMisc")

    def team_stats(self):
        return self.api.get_result("sqlTeamsMisc")


class BoxScoreAdvanced(_BoxScore):
    _endpoint = "boxscoreadvancedv2"

    def players_stats(self):
        return self.api.get_result("PlayerStats")

    def team_stats(self):
        return self.api.get_result("TeamStats")


class BoxScoreFourFactors(_BoxScore):
    _endpoint = "boxscorefourfactorsv2"

    def players_stats(self):
        return self.api.get_result("sqlPlayersFourFactors")

    def team_stats(self):
        return self.api.get_result("sqlTeamsFourFactors")


class BoxScorePlayerTracking:
    _endpoint = "boxscoreplayertrackv2"

    def __init__(self, game_id):
        self._params = {"GameID": game_id}
        self.api = NbaAPI(self._endpoint, self._params)

    def stats(self):
        return self.api.get_result()


class PlayByPlay:
    _endpoint = "playbyplay"

    def __init__(
        self,
        game_id,
        start_period=constants.StartPeriod.Default,
        end_period=constants.EndPeriod.Default,
    ):
        self._params = {
            "GameID": game_id,
            "StartPeriod": start_period,
            "EndPeriod": end_period,
        }
        self.api = NbaAPI(self._endpoint, self._params)

    def stats(self):
        return self.api.get_result("PlayByPlay")

    def available_video(self):
        return self.api.get_result("AvailableVideo")


class BoxScoreHustle:
    _endpoint = "hustlestatsboxscore"

    def __init__(self, game_id):
        self._params = {"GameID": game_id}
        self.api = NbaAPI(self._endpoint, self._params)

    def players_stats(self):
        return self.api.get_result("PlayerStats")

    def team_stats(self):
        return self.api.get_result("TeamStats")
