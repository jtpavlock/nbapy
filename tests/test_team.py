"""
Test team module and included endpoints.

We won't mock any api calls just to make sure they haven't changed on us.
"""
from nba_stats import team


class TestList:
    @staticmethod
    def test_default():
        team_list = team.List()
        assert team_list.results() is not None
