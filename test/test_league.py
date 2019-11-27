"""
Test league module and included endpoints.

We won't mock any api calls just to make sure they haven't changed on us.
"""
from nba_stats import league


class TestLineups:
    @staticmethod
    def test_default():
        lineups = league.Lineups()
        assert lineups.results() is not None


class TestStats:
    @staticmethod
    def test_default():
        team_stats = league.TeamStats()
        assert team_stats.results() is not None


class TestPlayerStats:
    @staticmethod
    def test_default():
        player_stats = league.PlayerStats()
        assert player_stats.results() is not None


class TestTrackingStats:
    @staticmethod
    def test_default():
        pt_stats = league.PlayerTrackingStats()
        assert pt_stats.results() is not None


class TestLeagueLeaders:
    @staticmethod
    def test_default():
        leaders = league.PlayerLeaders()
        assert leaders.results() is not None
