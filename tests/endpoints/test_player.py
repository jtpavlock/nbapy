"""Test player module and included endpoints."""
import pytest

from nbapy import player

player_id = "1628369"  # Jayson Tatum
vs_player_id = "2544"  # LeBron James


class TestGetId:
    @staticmethod
    def test_valid_player():
        player.get_id("Jayson tatum", active_only=0) == player_id

    @staticmethod
    def test_invalid_player():
        with pytest.raises(player.PlayerNotFoundException):
            player.get_id("Jaysan Tatum")


class TestPlayerList:
    @staticmethod
    def test_players():
        players = player.PlayerList().players()
        assert players is not None


class TestSummary:
    @staticmethod
    def test_info():
        info = player.Summary(player_id).info()
        assert info is not None

    @staticmethod
    def test_headline_stats():
        headline_stats = player.Summary(player_id).headline_stats()
        assert headline_stats is not None


class TestSplits:
    @staticmethod
    def test_overall():
        overall = player.Splits(player_id).overall()
        assert overall is not None


class TestGeneralSplits:
    @staticmethod
    def test_location():
        location = player.GeneralSplits(player_id).location()
        assert location is not None

    @staticmethod
    def test_wins_losses():
        wins_losses = player.GeneralSplits(player_id).wins_losses()
        assert wins_losses is not None

    @staticmethod
    def test_month():
        month = player.GeneralSplits(player_id).month()
        assert month is not None

    @staticmethod
    def test_pre_post_all_star():
        pre_post_all_star = player.GeneralSplits(player_id).pre_post_all_star()
        assert pre_post_all_star is not None

    @staticmethod
    def test_starting_position():
        starting_position = player.GeneralSplits(player_id).starting_position()
        assert starting_position is not None

    @staticmethod
    def test_days_rest():
        days_rest = player.GeneralSplits(player_id).days_rest()
        assert days_rest is not None


class TestOpponentSplits:
    @staticmethod
    def test_by_conference():
        by_conference = player.OpponentSplits(player_id).by_conference()
        assert by_conference is not None

    @staticmethod
    def test_by_division():
        by_division = player.OpponentSplits(player_id).by_division()
        assert by_division is not None

    @staticmethod
    def test_by_team():
        by_team = player.OpponentSplits(player_id).by_team()
        assert by_team is not None


class TestLastNGamesSplits:
    @staticmethod
    def test_last_5():
        last_5 = player.LastNGamesSplits(player_id).last_5()
        assert last_5 is not None

    @staticmethod
    def test_last_10():
        last_10 = player.LastNGamesSplits(player_id).last_10()
        assert last_10 is not None

    @staticmethod
    def test_last_15():
        last_15 = player.LastNGamesSplits(player_id).last_15()
        assert last_15 is not None

    @staticmethod
    def test_last_20():
        last_20 = player.LastNGamesSplits(player_id).last_20()
        assert last_20 is not None

    @staticmethod
    def test_game_num():
        game_num = player.LastNGamesSplits(player_id).game_num()
        assert game_num is not None


class TestInGameSplits:
    @staticmethod
    def test_by_half():
        by_half = player.InGameSplits(player_id).by_half()
        assert by_half is not None

    @staticmethod
    def test_by_period():
        by_period = player.InGameSplits(player_id).by_period()
        assert by_period is not None

    @staticmethod
    def test_by_score_margin():
        by_score_margin = player.InGameSplits(player_id).by_score_margin()
        assert by_score_margin is not None

    @staticmethod
    def test_by_actual_margin():
        by_actual_margin = player.InGameSplits(player_id).by_actual_margin()
        assert by_actual_margin is not None


class TestClutchSplits:
    @staticmethod
    def test_last_5m_lte_5pts():
        last_5m_lte_5pts = player.ClutchSplits(2554).last_5m_lte_5pts()
        assert last_5m_lte_5pts is not None

    @staticmethod
    def test_last_3m_lte_5pts():
        last_3m_lte_5pts = player.ClutchSplits(2554).last_3m_lte_5pts()
        assert last_3m_lte_5pts is not None

    @staticmethod
    def test_last_1m_lte_5pts():
        last_1m_lte_5pts = player.ClutchSplits(2554).last_1m_lte_5pts()
        assert last_1m_lte_5pts is not None

    @staticmethod
    def test_last_30s_lte_3pts():
        last_30s_lte_3pts = player.ClutchSplits(2554).last_30s_lte_3pts()
        assert last_30s_lte_3pts is not None

    @staticmethod
    def test_last_10s_lte_3pts():
        last_10s_lte_3pts = player.ClutchSplits(2554).last_10s_lte_3pts()
        assert last_10s_lte_3pts is not None

    @staticmethod
    def test_last_5m_pm_5pts():
        last_5m_pm_5pts = player.ClutchSplits(2554).last_5m_pm_5pts()
        assert last_5m_pm_5pts is not None

    @staticmethod
    def test_last_3m_pm_5pts():
        last_3m_pm_5pts = player.ClutchSplits(2554).last_3m_pm_5pts()
        assert last_3m_pm_5pts is not None

    @staticmethod
    def test_last_1m_pm_5pts():
        last_1m_pm_5pts = player.ClutchSplits(2554).last_1m_pm_5pts()
        assert last_1m_pm_5pts is not None


class TestTeamPerformanceSplits:
    @staticmethod
    def test_score_differential():
        score_diff = player.TeamPerformanceSplits(player_id).score_differential
        assert score_diff is not None

    @staticmethod
    def test_points_scored():
        stats = player.TeamPerformanceSplits(player_id).points_scored()
        assert stats is not None

    @staticmethod
    def test_points_against():
        stats = player.TeamPerformanceSplits(player_id).points_against()
        assert stats is not None


class TestYearOverYearSplits:
    @staticmethod
    def test_by_year():
        stats = player.YearOverYearSplits(player_id).by_year()
        assert stats is not None


class TestShootingSplits:
    @staticmethod
    def test_shot_5ft():
        shot_5ft = player.ShootingSplits(player_id).shot_5ft()
        assert shot_5ft is not None

    @staticmethod
    def test_shot_8ft():
        shot_8ft = player.ShootingSplits(player_id).shot_8ft()
        assert shot_8ft is not None

    @staticmethod
    def test_shot_areas():
        shot_areas = player.ShootingSplits(player_id).shot_areas()
        assert shot_areas is not None

    @staticmethod
    def test_assisted_shots():
        assisted_shots = player.ShootingSplits(player_id).assisted_shots()
        assert assisted_shots is not None

    @staticmethod
    def test_shot_types_summary():
        stats = player.ShootingSplits(player_id).shot_types_summary()
        assert stats is not None

    @staticmethod
    def test_shot_types_detail():
        stats = player.ShootingSplits(player_id).shot_types_detail()
        assert stats is not None

    @staticmethod
    def test_assisted_by():
        assisted_by = player.ShootingSplits(player_id).assisted_by()
        assert assisted_by is not None


class TestCareer:
    @staticmethod
    def test_reg_season_splits():
        reg_season_splits = player.Career(player_id).reg_season_splits()
        assert reg_season_splits is not None

    @staticmethod
    def test_reg_season_splits_career():
        stats = player.Career(player_id).reg_season_splits(True)
        assert stats is not None

    @staticmethod
    def test_post_season_splits():
        post_season_splits = player.Career(player_id).post_season_splits()
        assert post_season_splits is not None

    @staticmethod
    def test_post_season_splits_career():
        stats = player.Career(player_id).post_season_splits(True)
        assert stats is not None

    @staticmethod
    def test_all_star_season_splits():
        stats = player.Career(player_id).all_star_season_splits()
        assert stats is not None

    @staticmethod
    def test_all_star_season_splits_career():
        stats = player.Career(player_id).all_star_season_splits(True)
        assert stats is not None

    @staticmethod
    def test_college_season_splits():
        stats = player.Career(player_id).college_season_splits()
        assert stats is not None

    @staticmethod
    def test_college_season_splits_career():
        stats = player.Career(player_id).college_season_splits(True)
        assert stats is not None

    @staticmethod
    def test_reg_season_rankings():
        stats = player.Career(player_id).reg_season_rankings()
        assert stats is not None

    @staticmethod
    def test_post_season_rankings():
        stats = player.Career(player_id).post_season_rankings()
        assert stats is not None

    @staticmethod
    def test_season_highs():
        stats = player.Career(player_id).season_highs()
        assert stats is not None

    @staticmethod
    def test_career_highs():
        stats = player.Career(player_id).career_highs()
        assert stats is not None

    @staticmethod
    def test_next_game():
        stats = player.Career(player_id).next_game()
        assert stats is not None


class TestGameLogs:
    @staticmethod
    def test_logs():
        stats = player.GameLogs(player_id).logs()
        assert stats is not None


class TestShotTracking:
    @staticmethod
    def test_overall():
        stats = player.ShotTracking(player_id).overall()
        assert stats is not None

    @staticmethod
    def test_general():
        stats = player.ShotTracking(player_id).general()
        assert stats is not None

    @staticmethod
    def test_shot_clock():
        stats = player.ShotTracking(player_id).shot_clock()
        assert stats is not None

    @staticmethod
    def test_dribble():
        stats = player.ShotTracking(player_id).dribbles()
        assert stats is not None

    @staticmethod
    def test_closest_defender():
        stats = player.ShotTracking(player_id).closest_defender()
        assert stats is not None

    @staticmethod
    def test_closest_defender_long():
        stats = player.ShotTracking(player_id).closest_defender_long()
        assert stats is not None

    @staticmethod
    def test_touch_time():
        stats = player.ShotTracking(player_id).touch_time()
        assert stats is not None


class TestReboundTracking:
    @staticmethod
    def test_overall():
        stats = player.ReboundTracking(player_id).overall()
        assert stats is not None

    @staticmethod
    def test_shot_type():
        stats = player.ReboundTracking(player_id).shot_type()
        assert stats is not None

    @staticmethod
    def test_num_contested():
        stats = player.ReboundTracking(player_id).num_contested()
        assert stats is not None

    @staticmethod
    def test_shot_distance():
        stats = player.ReboundTracking(player_id).shot_distance()
        assert stats is not None

    @staticmethod
    def test_rebound_distance():
        stats = player.ReboundTracking(player_id).rebound_distance()
        assert stats is not None


class TestPassTracking:
    @staticmethod
    def test_made():
        stats = player.PassTracking(player_id).made()
        assert stats is not None

    @staticmethod
    def test_received():
        stats = player.PassTracking(player_id).received()
        assert stats is not None


class TestDefenseTracking:
    @staticmethod
    def test_shot_types():
        stats = player.DefenseTracking(player_id).shot_types()
        assert stats is not None


class TestVsPlayer:
    @staticmethod
    def test_overall():
        stats = player.VsPlayer(player_id, vs_player_id).overall()
        assert stats is not None

    @staticmethod
    def test_on_off_court():
        stats = player.VsPlayer(player_id, vs_player_id).on_off_court()
        assert stats is not None

    @staticmethod
    def test_shot_dist_overall():
        stats = player.VsPlayer(player_id, vs_player_id).shot_dist_overall()
        assert stats is not None

    @staticmethod
    def test_shot_dist_on_court():
        stats = player.VsPlayer(player_id, vs_player_id).shot_dist_on_court()
        assert stats is not None

    @staticmethod
    def test_shot_dist_off_court():
        stats = player.VsPlayer(player_id, vs_player_id).shot_dist_off_court()
        assert stats is not None

    @staticmethod
    def test_shot_area_overall():
        stats = player.VsPlayer(player_id, vs_player_id).shot_area_overall()
        assert stats is not None

    @staticmethod
    def test_shot_area_on_court():
        stats = player.VsPlayer(player_id, vs_player_id).shot_area_on_court()
        assert stats is not None

    @staticmethod
    def test_shot_area_off_court():
        stats = player.VsPlayer(player_id, vs_player_id).shot_area_off_court()
        assert stats is not None

    @staticmethod
    def test_player_info():
        stats = player.VsPlayer(player_id, vs_player_id).player_info()
        assert stats is not None

    @staticmethod
    def test_vs_player_info():
        stats = player.VsPlayer(player_id, vs_player_id).vs_player_info()
        assert stats is not None
