"""Test game module and included endpoints.

We won't mock any api calls just to make sure they haven't changed on us.
"""
from nbapy import game

game_id = '0021900017'


class Info:
    @staticmethod
    def test_game_summary():
        game_summary = game.Info(game_id).game_summary()
        assert game_summary is not None

    @staticmethod
    def test_other_stats():
        other_stats = game.Info(game_id).other_stats()
        assert other_stats is not None

    @staticmethod
    def test_officials():
        officials = game.Info(game_id).officials()
        assert officials is not None

    @staticmethod
    def test_inactive_players():
        inactive_players = game.Info(game_id).inactive_players()
        assert inactive_players is not None

    @staticmethod
    def test_game_info():
        game_info = game.Info(game_id).game_info()
        assert game_info is not None

    @staticmethod
    def test_line_score():
        line_score = game.Info(game_id).line_score()
        assert line_score is not None

    @staticmethod
    def test_last_meeting():
        last_meeting = game.Info(game_id).last_meeting()
        assert last_meeting is not None

    @staticmethod
    def test_season_series():
        season_series = game.Info(game_id).season_series()
        assert season_series is not None

    @staticmethod
    def test_available_video():
        available_video = game.Info(game_id).available_video()
        assert available_video is not None


class TestBoxscore:
    @staticmethod
    def test_players_stats():
        stats = game.BoxScore(game_id).players_stats()
        assert stats is not None

    @staticmethod
    def test_team_stats():
        stats = game.BoxScore(game_id).team_stats()
        assert stats is not None

    @staticmethod
    def test_team_starter_bench_stats():
        stats = game.BoxScore(game_id).team_starter_bench_stats()
        assert stats is not None


class TestBoxScoreScoring:
    @staticmethod
    def test_players_stats():
        stats = game.BoxScoreScoring(game_id).players_stats()
        assert stats is not None

    @staticmethod
    def test_team_stats():
        stats = game.BoxScoreScoring(game_id).team_stats()
        assert stats is not None


class TestBoxScoreUsage:
    @staticmethod
    def test_players_stats():
        stats = game.BoxScoreUsage(game_id).players_stats()
        assert stats is not None

    @staticmethod
    def test_team_stats():
        stats = game.BoxScoreUsage(game_id).team_stats()
        assert stats is not None


class TestBoxScoreMisc:
    @staticmethod
    def test_players():
        stats = game.BoxScoreMisc(game_id).players_stats()
        assert stats is not None

    @staticmethod
    def test_team():
        stats = game.BoxScoreMisc(game_id).team_stats()
        assert stats is not None


class TestBoxScoreAdvanced:
    @staticmethod
    def test_players_stats():
        stats = game.BoxScoreAdvanced(game_id).players_stats()
        assert stats is not None

    @staticmethod
    def test_team_stats():
        stats = game.BoxScoreAdvanced(game_id).team_stats()
        assert stats is not None


class TestBoxScoreFourFactors:
    @staticmethod
    def test_players_stats():
        stats = game.BoxScoreFourFactors(game_id).players_stats()
        assert stats is not None

    @staticmethod
    def test_team_stats():
        stats = game.BoxScoreFourFactors(game_id).team_stats()
        assert stats is not None


class TestBoxScorePlayerTracking:
    @staticmethod
    def test_stats():
        stats = game.BoxScorePlayerTracking(game_id).stats()
        assert stats is not None


class TestPlayByPlay:
    @staticmethod
    def test_stats():
        stats = game.PlayByPlay(game_id).stats()
        assert stats is not None

    @staticmethod
    def test_available_video():
        available_video = game.PlayByPlay(game_id).available_video()
        assert available_video is not None


class TestBoxScoreHustle:
    @staticmethod
    def test_players_stats():
        stats = game.BoxScoreHustle(game_id).players_stats()
        assert stats is not None

    @staticmethod
    def test_team_stats():
        stats = game.BoxScoreHustle(game_id).team_stats()
        assert stats is not None
