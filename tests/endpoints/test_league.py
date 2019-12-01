"""
Test league module and included endpoints.

We won't mock any api calls just to make sure they haven't changed on us.
"""
from nbapy import league


class TestLineups:
    @staticmethod
    def test_results():
        lineups = league.Lineups().lineups()
        assert lineups is not None


class TestTeamStats:
    @staticmethod
    def test_stats():
        stats = league.TeamStats().stats()
        assert stats is not None


class TestPlayerStats:
    @staticmethod
    def test_stats():
        stats = league.PlayerStats().stats()
        assert stats is not None


class TestPlayerTrackingStats:
    @staticmethod
    def test_stats():
        stats = league.PlayerTrackingStats().stats()
        assert stats is not None


class TestLeagueLeaders:
    @staticmethod
    def test_players():
        players = league.LeagueLeaders().players()
        assert players is not None
