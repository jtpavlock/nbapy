"""
Test player module and included endpoints.

We won't mock any api calls just to make sure they haven't changed on us.
"""
import sys, os
from nba_stats import player
sys.path = [os.path.join(os.pardir, 'python')] + sys.path


class TestLeagueLeaders:
    @staticmethod
    def test_default():
        leaders = player.Leaders()
        assert leaders.results() is not None


class TestStats:
    @staticmethod
    def test_default():
        player_stats = player.Stats()
        assert player_stats.results() is not None


class TestTrackingStats:
    @staticmethod
    def test_default():
        pt_stats = player.TrackingStats()
        assert pt_stats.results() is not None
