"""Test shot_chart module and included endpoints.

We won't mock any api calls just to make sure they haven't changed on us.
"""
from nbapy import shot_chart

player_id = "1628369"  # Jayson Tatum


class TestShotChart:
    @staticmethod
    def test_shot_chart():
        stats = shot_chart.ShotChart(player_id).shot_chart()
        assert stats is not None

    @staticmethod
    def test_league_average():
        stats = shot_chart.ShotChart(player_id).league_average()
        assert stats is not None
