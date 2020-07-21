"""Test draft_combine module and included endpoints.

We won't mock any api calls just to make sure they haven't changed on us.
"""
from nbapy import draft_combine


class TestSummary:
    @staticmethod
    def test_stats():
        stats = draft_combine.Summary().stats()
        assert stats is not None


class TestDrillResults:
    @staticmethod
    def test_stats():
        stats = draft_combine.DrillResults().stats()
        assert stats is not None


class TestSpotShooting:
    @staticmethod
    def test_stats():
        stats = draft_combine.SpotShooting().stats()
        assert stats is not None
