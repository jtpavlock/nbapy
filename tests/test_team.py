"""
Test team module and included endpoints.

We won't mock any api calls just to make sure they haven't changed on us.
"""
from nba_stats import team


class TestList:
    @staticmethod
    def test_teams():
        assert team.TeamList().teams() is not None


class TestSummary:
    @staticmethod
    def test_info():
        assert team.TeamSummary(1610612738).info() is not None

    @staticmethod
    def test_season_ranks():
        assert team.TeamSummary(1610612738).season_ranks() is not None


class TestDetails:
    @staticmethod
    def test_background():
        assert team.Details(1610612738).background() is not None

    @staticmethod
    def test_history():
        assert team.Details(1610612738).history() is not None

    @staticmethod
    def test_social_sites():
        assert team.Details(1610612738).social_sites() is not None

    @staticmethod
    def test_awards_championships():
        assert team.Details(1610612738).awards_championships() is not None

    @staticmethod
    def test_awards_conf():
        assert team.Details(1610612738).awards_conf() is not None

    @staticmethod
    def test_awards_div():
        assert team.Details(1610612738).awards_div() is not None

    @staticmethod
    def test_hof():
        assert team.Details(1610612738).hof() is not None

    @staticmethod
    def test_retired():
        assert team.Details(1610612738).retired() is not None


class TestCommonRoster():
    @staticmethod
    def test_roster():
        assert team.CommonRoster(1610612738).roster() is not None

    @staticmethod
    def test_coaches():
        assert team.CommonRoster(1610612738).coaches() is not None


class TestSplits():
    @staticmethod
    def test_overall():
        assert team.Splits(1610612738).overall() is not None


class TestGeneralSplits():
    @staticmethod
    def test_location():
        assert team.GeneralSplits(1610612738).location() is not None

    @staticmethod
    def test_wins_losses():
        assert team.GeneralSplits(1610612738).wins_losses() is not None

    @staticmethod
    def test_month():
        assert team.GeneralSplits(1610612738).month() is not None

    @staticmethod
    def test_pre_post_all_star():
        assert team.GeneralSplits(1610612738).pre_post_all_star() is not None

    @staticmethod
    def test_days_rest():
        assert team.GeneralSplits(1610612738).days_rest() is not None


class TestLineupSplits():
    @staticmethod
    def test_lineups():
        assert team.LineupSplits(1610612738).lineups() is not None


class TestOpponentSplits():
    @staticmethod
    def test_by_conference():
        assert team.OpponentSplits(1610612738).by_conference() is not None

    @staticmethod
    def test_by_division():
        assert team.OpponentSplits(1610612738).by_division() is not None

    @staticmethod
    def test_by_team():
        assert team.OpponentSplits(1610612738).by_team() is not None


class TestLastNGamesSplits():
    @staticmethod
    def test_last_5():
        assert team.LastNGamesSplits(1610612738).last_5() is not None

    @staticmethod
    def test_last_10():
        assert team.LastNGamesSplits(1610612738).last_10() is not None

    @staticmethod
    def test_last_15():
        assert team.LastNGamesSplits(1610612738).last_15() is not None

    @staticmethod
    def test_last_20():
        assert team.LastNGamesSplits(1610612738).last_20() is not None

    @staticmethod
    def test_game_num():
        assert team.LastNGamesSplits(1610612738).game_num() is not None


class TestInGameSplits():
    @staticmethod
    def test_by_half():
        assert team.InGameSplits(1610612738).by_half() is not None

    @staticmethod
    def test_by_period():
        assert team.InGameSplits(1610612738).by_period() is not None

    @staticmethod
    def test_by_score_margin():
        assert team.InGameSplits(1610612738).by_score_margin() is not None

    @staticmethod
    def test_by_actual_margin():
        assert team.InGameSplits(1610612738).by_actual_margin() is not None


class TestClutchSplits():
    @staticmethod
    def test_last_5m_lte_5pts():
        assert team.ClutchSplits(2554).last_5m_lte_5pts() is not None

    @staticmethod
    def test_last_3m_lte_5pts():
        assert team.ClutchSplits(2554).last_3m_lte_5pts() is not None

    @staticmethod
    def test_last_1m_lte_5pts():
        assert team.ClutchSplits(2554).last_1m_lte_5pts() is not None

    @staticmethod
    def test_last_30s_lte_3pts():
        assert team.ClutchSplits(2554).last_30s_lte_3pts() is not None

    @staticmethod
    def test_last_10s_lte_3pts():
        assert team.ClutchSplits(2554).last_10s_lte_3pts() is not None

    @staticmethod
    def test_last_5m_pm_5pts():
        assert team.ClutchSplits(2554).last_5m_pm_5pts() is not None

    @staticmethod
    def test_last_3m_pm_5pts():
        assert team.ClutchSplits(2554).last_3m_pm_5pts() is not None

    @staticmethod
    def test_last_1m_pm_5pts():
        assert team.ClutchSplits(2554).last_1m_pm_5pts() is not None


class TestShootingSplits():
    @staticmethod
    def test_shot_5ft():
        assert team.ShootingSplits(1610612738).shot_5ft() is not None

    @staticmethod
    def test_shot_8ft():
        assert team.ShootingSplits(1610612738).shot_8ft() is not None

    @staticmethod
    def test_shot_areas():
        assert team.ShootingSplits(1610612738).shot_areas() is not None

    @staticmethod
    def test_assisted_shots():
        assert team.ShootingSplits(1610612738).assisted_shots() is not None

    @staticmethod
    def test_shot_types():
        assert team.ShootingSplits(1610612738).shot_types() is not None

    @staticmethod
    def test_assisted_by():
        assert team.ShootingSplits(1610612738).assisted_by() is not None


class TestPerformanceSplits():
    @staticmethod
    def test_score_differential():
        assert team.PerformanceSplits(1610612738).score_differential() is not None

    @staticmethod
    def test_points_scored():
        assert team.PerformanceSplits(1610612738).points_scored() is not None

    @staticmethod
    def test_points_against():
        assert team.PerformanceSplits(1610612738).points_against() is not None


class TestPlayerSplits():
    @staticmethod
    def test_players():
        assert team.PlayerSplits(1610612738).players() is not None


class TestPlayerOnOffSplits():
    @staticmethod
    def test_on_court():
        assert team.PlayerOnOffSplits(1610612738).on_court() is not None

    @staticmethod
    def test_off_court():
        assert team.PlayerOnOffSplits(1610612738).off_court() is not None


class TestPlayerOnOffSummary():
    @staticmethod
    def test_on_court():
        assert team.PlayerOnOffSummary(1610612738).on_court() is not None

    @staticmethod
    def test_off_court():
        assert team.PlayerOnOffSummary(1610612738).off_court() is not None


class TestYearOverYearSplits():
    @staticmethod
    def test_by_year():
        assert team.YearOverYearSplits(1610612738).by_year() is not None


class TestShotTracking():
    @staticmethod
    def test_general():
        assert team.ShotTracking(1610612738).general() is not None

    @staticmethod
    def test_shot_clock():
        assert team.ShotTracking(1610612738).shot_clock() is not None

    @staticmethod
    def test_dribble():
        assert team.ShotTracking(1610612738).dribbles() is not None

    @staticmethod
    def test_closest_defender():
        assert team.ShotTracking(1610612738).closest_defender() is not None

    @staticmethod
    def test_closest_defender_long():
        assert team.ShotTracking(1610612738).closest_defender_long() is not None

    @staticmethod
    def test_touch_time():
        assert team.ShotTracking(1610612738).touch_time() is not None


class TestReboundTracking():
    @staticmethod
    def test_overall():
        assert team.ReboundTracking(1610612738).overall() is not None

    @staticmethod
    def test_shot_type():
        assert team.ReboundTracking(1610612738).shot_type() is not None

    @staticmethod
    def test_num_contested():
        assert team.ReboundTracking(1610612738).num_contested() is not None

    @staticmethod
    def test_shot_distance():
        assert team.ReboundTracking(1610612738).shot_distance() is not None

    @staticmethod
    def test_rebound_distance():
        assert team.ReboundTracking(1610612738).rebound_distance() is not None


class TestPassTracking():
    @staticmethod
    def test_made():
        assert team.PassTracking(1610612738).made() is not None

    @staticmethod
    def test_received():
        assert team.PassTracking(1610612738).received() is not None


class TestGameLogs():
    @staticmethod
    def test_logs():
        assert team.GameLogs(1610612738).logs() is not None


class TestSeasonResults():
    @staticmethod
    def test_results():
        assert team.SeasonResults(1610612738).results() is not None


class TestVsPlayer():
    @staticmethod
    def test_overall():
        assert team.VsPlayer(1610612738, 2544).overall() is not None

    @staticmethod
    def test_vs_player_overall():
        assert team.VsPlayer(1610612738, 2544).vs_player_overall() is not None

    @staticmethod
    def test_on_off_court():
        assert team.VsPlayer(1610612738, 2544).on_off_court() is not None

    @staticmethod
    def test_shot_dist_overall():
        assert team.VsPlayer(1610612738, 2544).shot_dist_overall() is not None

    @staticmethod
    def test_shot_dist_on_court():
        assert team.VsPlayer(1610612738, 2544).shot_dist_on_court() is not None

    @staticmethod
    def test_shot_dist_off_court():
        assert (team.VsPlayer(1610612738, 2544).shot_dist_off_court()
                is not None)

    @staticmethod
    def test_shot_area_overall():
        assert team.VsPlayer(1610612738, 2544).shot_area_overall() is not None

    @staticmethod
    def test_shot_area_on_court():
        assert team.VsPlayer(1610612738, 2544).shot_area_on_court() is not None

    @staticmethod
    def test_shot_area_off_court():
        assert (team.VsPlayer(1610612738, 2544).shot_area_off_court()
                is not None)
