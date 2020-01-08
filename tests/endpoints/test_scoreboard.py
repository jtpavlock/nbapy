"""Test scoreboard module and included endpoints.

We won't mock any api calls just to make sure they haven't changed on us.
"""
from nbapy import scoreboard


class TestScoreboard:
    @staticmethod
    def test_game_header():
        stats = scoreboard.Scoreboard().game_header()
        assert stats is not None

    @staticmethod
    def test_line_score():
        stats = scoreboard.Scoreboard().line_score()
        assert stats is not None

    @staticmethod
    def test_series_standings():
        stats = scoreboard.Scoreboard().series_standings()
        assert stats is not None

    @staticmethod
    def test_last_meeting():
        stats = scoreboard.Scoreboard().last_meeting()
        assert stats is not None

    @staticmethod
    def test_east_conf_standings_by_day():
        stats = scoreboard.Scoreboard().east_conf_standings_by_day()
        assert stats is not None

    @staticmethod
    def test_west_conf_standings_by_day():
        stats = scoreboard.Scoreboard().west_conf_standings_by_day()
        assert stats is not None

    @staticmethod
    def test_available():
        stats = scoreboard.Scoreboard().available()
        assert stats is not None
