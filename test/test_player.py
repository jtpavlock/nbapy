"""
Test player module and included endpoints.

We won't mock any api calls just to make sure they haven't changed on us.
"""
import pandas as pd
import pytest

from nba_stats import player


class TestGetId:
    @staticmethod
    def test_valid_player():
        player.get_id('Lebron James') == 2544

    @staticmethod
    def test_invalid_player():
        with pytest.raises(player.PlayerNotFoundException):
            player.get_id('Lebran James')


class TestPlayerList:
    @staticmethod
    def test_results():
        assert player.PlayerList().results() is not None


class TestSummary:
    @staticmethod
    def test_info():
        assert player.Summary(2544).info() is not None

    @staticmethod
    def test_headline_stats():
        assert player.Summary(2544).headline_stats() is not None


class TestSplits():
    @staticmethod
    def test_overall():
        assert player.Splits(2544).overall() is not None


class TestGeneralSplits():

    @staticmethod
    def test_location():
        assert player.GeneralSplits(2544).location() is not None

    @staticmethod
    def test_wins_losses():
        assert player.GeneralSplits(2544).wins_losses() is not None

    @staticmethod
    def test_month():
        assert player.GeneralSplits(2544).month() is not None

    @staticmethod
    def test_pre_post_all_star():
        assert player.GeneralSplits(2544).pre_post_all_star() is not None

    @staticmethod
    def test_starting_position():
        assert player.GeneralSplits(2544).starting_position() is not None

    @staticmethod
    def test_days_rest():
        assert player.GeneralSplits(2544).overall() is not None


class TestOpponentSplits():
    @staticmethod
    def test_by_conference():
        assert player.OpponentSplits(2544).by_conference() is not None

    @staticmethod
    def test_by_division():
        assert player.OpponentSplits(2544).by_division() is not None

    @staticmethod
    def test_by_team():
        assert player.OpponentSplits(2544).by_team() is not None


class TestLastNGamesSplits():
    @staticmethod
    def test_last_5():
        assert player.LastNGamesSplits(2544).last_5() is not None

    @staticmethod
    def test_last_10():
        assert player.LastNGamesSplits(2544).last_10() is not None

    @staticmethod
    def test_last_15():
        assert player.LastNGamesSplits(2544).last_15() is not None

    @staticmethod
    def test_last_20():
        assert player.LastNGamesSplits(2544).last_20() is not None

    @staticmethod
    def test_last_5():
        assert player.LastNGamesSplits(2544).last_5() is not None


class TestInGameSplits():
    @staticmethod
    def test_by_half():
        assert player.InGameSplits(2544).by_half() is not None

    @staticmethod
    def test_by_period():
        assert player.InGameSplits(2544).by_period() is not None

    @staticmethod
    def test_by_score_margin():
        assert player.InGameSplits(2544).by_score_margin() is not None

    @staticmethod
    def test_by_actual_margin():
        assert player.InGameSplits(2544).by_actual_margin() is not None


class TestClutchSplits():
    @staticmethod
    def test_last_5m_lte_5pts():
        assert player.ClutchSplits(2554).last_5m_lte_5pts() is not None

    @staticmethod
    def test_last_3m_lte_5pts():
        assert player.ClutchSplits(2554).last_3m_lte_5pts() is not None

    @staticmethod
    def test_last_1m_lte_5pts():
        assert player.ClutchSplits(2554).last_1m_lte_5pts() is not None

    @staticmethod
    def test_last_30s_lte_3pts():
        assert player.ClutchSplits(2554).last_30s_lte_3pts() is not None

    @staticmethod
    def test_last_10s_lte_3pts():
        assert player.ClutchSplits(2554).last_10s_lte_3pts() is not None

    @staticmethod
    def test_last_5m_pm_5pts():
        assert player.ClutchSplits(2554).last_5m_pm_5pts() is not None

    @staticmethod
    def test_last_3m_pm_5pts():
        assert player.ClutchSplits(2554).last_3m_pm_5pts() is not None

    @staticmethod
    def test_last_1m_pm_5pts():
        assert player.ClutchSplits(2554).last_1m_pm_5pts() is not None


class TestTeamPerformanceSplits():
    @staticmethod
    def test_score_differential():
        assert (player.TeamPerformanceSplits(2544).score_differential()
                is not None)

    @staticmethod
    def test_points_scored():
        assert player.TeamPerformanceSplits(2544).points_scored() is not None

    @staticmethod
    def test_points_against():
        assert player.TeamPerformanceSplits(2544).points_against() is not None


class TestYearOverYearSplits():
    @staticmethod
    def test_by_year():
        assert player.YearOverYearSplits(2544).by_year() is not None


class TestShootingSplits():
    @staticmethod
    def test_shot_5ft():
        assert player.ShootingSplits(2544).shot_5ft() is not None

    @staticmethod
    def test_shot_8ft():
        assert player.ShootingSplits(2544).shot_8ft() is not None

    @staticmethod
    def test_shot_areas():
        assert player.ShootingSplits(2544).shot_areas() is not None

    @staticmethod
    def test_assisted_shots():
        assert player.ShootingSplits(2544).assisted_shots() is not None

    @staticmethod
    def test_shot_types_summary():
        assert player.ShootingSplits(2544).shot_types_summary() is not None

    @staticmethod
    def test_shot_types_detail():
        assert player.ShootingSplits(2544).shot_types_detail() is not None

    @staticmethod
    def test_assisted_by():
        assert player.ShootingSplits(2544).assisted_by() is not None


class TestCareer():
    @staticmethod
    def test_reg_season_splits():
        assert player.Career(2544).reg_season_splits() is not None

    @staticmethod
    def test_reg_season_splits_career():
        assert player.Career(2544).reg_season_splits(True) is not None

    @staticmethod
    def test_post_season_splits():
        assert player.Career(2544).post_season_splits() is not None

    @staticmethod
    def test_post_season_splits_career():
        assert player.Career(2544).post_season_splits(True) is not None

    @staticmethod
    def test_all_star_season_splits():
        assert player.Career(2544).all_star_season_splits() is not None

    @staticmethod
    def test_all_star_season_splits_career():
        assert player.Career(2544).all_star_season_splits(True) is not None

    @staticmethod
    def test_college_season_splits():
        assert player.Career(2544).college_season_splits() is not None

    @staticmethod
    def test_college_season_splits_career():
        assert player.Career(2544).college_season_splits(True) is not None

    @staticmethod
    def test_reg_season_rankings():
        assert player.Career(2544).reg_season_rankings() is not None

    @staticmethod
    def test_post_season_rankings():
        assert player.Career(2544).post_season_rankings() is not None

    @staticmethod
    def test_season_highs():
        assert player.Career(2544).season_highs() is not None

    @staticmethod
    def test_career_highs():
        assert player.Career(2544).career_highs() is not None

    @staticmethod
    def test_next_game():
        assert player.Career(2544).next_game() is not None


class TestGameLogs():
    @staticmethod
    def test_results():
        assert player.GameLogs(2544).results() is not None


class TestShotTracking():
    @staticmethod
    def test_overall():
        assert player.ShotTracking(2544).overall() is not None

    @staticmethod
    def test_general():
        assert player.ShotTracking(2544).general() is not None

    @staticmethod
    def test_shot_clock():
        assert player.ShotTracking(2544).shot_clock() is not None

    @staticmethod
    def test_dribble():
        assert player.ShotTracking(2544).dribbles() is not None

    @staticmethod
    def test_closest_defender():
        assert player.ShotTracking(2544).closest_defender() is not None

    @staticmethod
    def test_closest_defender_long():
        assert player.ShotTracking(2544).closest_defender_long() is not None

    @staticmethod
    def test_touch_time():
        assert player.ShotTracking(2544).touch_time() is not None


class TestReboundTracking():
    @staticmethod
    def test_overall():
        assert player.ReboundTracking(2544).overall() is not None

    @staticmethod
    def test_shot_type():
        assert player.ReboundTracking(2544).shot_type() is not None

    @staticmethod
    def test_num_contested():
        assert player.ReboundTracking(2544).num_contested() is not None

    @staticmethod
    def test_shot_distance():
        assert player.ReboundTracking(2544).shot_distance() is not None

    @staticmethod
    def test_rebound_distance():
        assert player.ReboundTracking(2544).rebound_distance() is not None


class TestPassTracking():
    @staticmethod
    def test_made():
        assert player.PassTracking(2544).made() is not None

    @staticmethod
    def test_received():
        assert player.PassTracking(2544).received() is not None


class TestDefenseTracking():
    @staticmethod
    def test_shot_types():
        assert player.DefenseTracking(2544).shot_types() is not None


class TestPlayerVsPlayer():
    @staticmethod
    def test_overall():
        assert player.VsPlayer(2544, 1628369).overall() is not None

    @staticmethod
    def test_on_off_court():
        assert player.VsPlayer(2544, 1628369).on_off_court() is not None

    @staticmethod
    def test_shot_dist_overall():
        assert player.VsPlayer(2544, 1628369).shot_dist_overall() is not None

    @staticmethod
    def test_shot_dist_on_court():
        assert player.VsPlayer(2544, 1628369).shot_dist_on_court() is not None

    @staticmethod
    def test_shot_dist_off_court():
        assert player.VsPlayer(2544, 1628369).shot_dist_off_court() is not None

    @staticmethod
    def test_shot_area_overall():
        assert player.VsPlayer(2544, 1628369).shot_area_overall() is not None

    @staticmethod
    def test_shot_area_on_court():
        assert player.VsPlayer(2544, 1628369).shot_area_on_court() is not None

    @staticmethod
    def test_shot_area_off_court():
        assert player.VsPlayer(2544, 1628369).shot_area_off_court() is not None

    @staticmethod
    def test_player_info():
        assert player.VsPlayer(2544, 1628369).player_info() is not None

    @staticmethod
    def test_vs_player_info():
        assert player.VsPlayer(2544, 1628369).vs_player_info() is not None
