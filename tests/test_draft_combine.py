"""
Test draft_combine module and included endpoints.

We won't mock any api calls just to make sure they haven't changed on us.
"""
from nba_stats import draft_combine


class TestSummary:
    @staticmethod
    def test_stats():
        assert draft_combine.Summary().stats() is not None


class TestDrillResults:
    @staticmethod
    def test_stats():
        assert draft_combine.DrillResults().stats() is not None


class TestSpotShooting:
    @staticmethod
    def test_stats():
        assert draft_combine.SpotShooting().stats() is not None
