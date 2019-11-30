"""
Test league module and included endpoints.

We won't mock any api calls just to make sure they haven't changed on us.
"""
from nba_stats import league


class TestLineups:
    @staticmethod
    def test_results():
        assert league.Lineups().lineups() is not None


class TestTeamStats:
    @staticmethod
    def test_results():
        assert league.TeamStats().stats() is not None


class TestPlayerStats:
    @staticmethod
    def test_results():
        assert league.PlayerStats().stats() is not None


class TestPlayerTrackingStats:
    @staticmethod
    def test_results():
        assert league.PlayerTrackingStats().stats() is not None


class TestLeagueLeaders:
    @staticmethod
    def test_results():
        assert league.LeagueLeaders().players() is not None
