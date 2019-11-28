"""
Test league module and included endpoints.

We won't mock any api calls just to make sure they haven't changed on us.
"""
from nba_stats import league


class TestLineups:
    @staticmethod
    def test_results():
        assert league.Lineups().results() is not None


class TestStats:
    @staticmethod
    def test_results():
        assert league.TeamStats().results() is not None


class TestPlayerStats:
    @staticmethod
    def test_results():
        assert league.PlayerStats().results() is not None


class TestTrackingStats:
    @staticmethod
    def test_results():
        assert league.PlayerTrackingStats().results() is not None


class TestLeagueLeaders:
    @staticmethod
    def test_results():
        assert league.LeagueLeaders().results() is not None
