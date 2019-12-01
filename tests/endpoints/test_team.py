"""Test team module and included endpoints.

We won't mock any api calls just to make sure they haven't changed on us.
"""
from nbapy import team

team_id = '1610612738'  # Celtics
player_id = '2544'  # LeBron James


class TestList:
    @staticmethod
    def test_teams():
        team_list = team.TeamList().teams()
        assert team_list is not None


class TestSummary:
    @staticmethod
    def test_info():
        team_info = team.TeamSummary(team_id).info()
        assert team_info is not None

    @staticmethod
    def test_season_ranks():
        team_season_ranks = team.TeamSummary(team_id).season_ranks()
        assert team_season_ranks is not None


class TestDetails:
    @staticmethod
    def test_background():
        team_background = team.Details(team_id).background()
        assert team_background is not None

    @staticmethod
    def test_history():
        team_history = team.Details(team_id).history()
        assert team_history is not None

    @staticmethod
    def test_social_sites():
        team_sites = team.Details(team_id).social_sites()
        assert team_sites is not None

    @staticmethod
    def test_awards_championships():
        team_chips = team.Details(team_id).awards_championships()
        assert team_chips is not None

    @staticmethod
    def test_awards_conf():
        team_conf_awards = team.Details(team_id).awards_conf()
        assert team_conf_awards is not None

    @staticmethod
    def test_awards_div():
        team_div_awards = team.Details(team_id).awards_div()
        assert team_div_awards is not None

    @staticmethod
    def test_hof_players():
        team_hof_players = team.Details(team_id).hof_players()
        assert team_hof_players is not None

    @staticmethod
    def test_retired_players():
        team_retired_players = team.Details(team_id).retired_players()
        assert team_retired_players is not None


class TestCommonRoster():
    @staticmethod
    def test_roster():
        team_roster = team.CommonRoster(team_id).roster()
        assert team_roster is not None

    @staticmethod
    def test_coaches():
        team_coaches = team.CommonRoster(team_id).coaches()
        assert team_coaches is not None


class TestSplits():
    @staticmethod
    def test_overall():
        team_overall = team.Splits(team_id).overall()
        assert team_overall is not None


class TestGeneralSplits():
    @staticmethod
    def test_location():
        team_location = team.GeneralSplits(team_id).location()
        assert team_location is not None

    @staticmethod
    def test_wins_losses():
        team_wins_losses = team.GeneralSplits(team_id).wins_losses()
        assert team_wins_losses is not None

    @staticmethod
    def test_month():
        team_month = team.GeneralSplits(team_id).month()
        assert team_month is not None

    @staticmethod
    def test_pre_post_all_star():
        team_all_star = team.GeneralSplits(team_id).pre_post_all_star()
        assert team_all_star is not None

    @staticmethod
    def test_days_rest():
        team_days_rest = team.GeneralSplits(team_id).days_rest()
        assert team_days_rest is not None


class TestLineupSplits():
    @staticmethod
    def test_lineups():
        team_lineups = team.LineupSplits(team_id).lineups()
        assert team_lineups is not None


class TestOpponentSplits():
    @staticmethod
    def test_by_conference():
        team_by_conference = team.OpponentSplits(team_id).by_conference()
        assert team_by_conference is not None

    @staticmethod
    def test_by_division():
        team_by_division = team.OpponentSplits(team_id).by_division()
        assert team_by_division is not None

    @staticmethod
    def test_by_team():
        team_by_team = team.OpponentSplits(team_id).by_team()
        assert team_by_team is not None


class TestLastNGamesSplits():
    @staticmethod
    def test_last_5():
        team_last_5 = team.LastNGamesSplits(team_id).last_5()
        assert team_last_5 is not None

    @staticmethod
    def test_last_10():
        team_last_10 = team.LastNGamesSplits(team_id).last_10()
        assert team_last_10 is not None

    @staticmethod
    def test_last_15():
        team_last_15 = team.LastNGamesSplits(team_id).last_15()
        assert team_last_15 is not None

    @staticmethod
    def test_last_20():
        team_last_20 = team.LastNGamesSplits(team_id).last_20()
        assert team_last_20 is not None

    @staticmethod
    def test_game_num():
        team_game_num = team.LastNGamesSplits(team_id).game_num()
        assert team_game_num is not None


class TestInGameSplits():
    @staticmethod
    def test_by_half():
        team_by_half = team.InGameSplits(team_id).by_half()
        assert team_by_half is not None

    @staticmethod
    def test_by_period():
        team_by_period = team.InGameSplits(team_id).by_period()
        assert team_by_period is not None

    @staticmethod
    def test_by_score_margin():
        team_by_score_margin = team.InGameSplits(team_id).by_score_margin()
        assert team_by_score_margin is not None

    @staticmethod
    def test_by_actual_margin():
        team_by_actual_margin = team.InGameSplits(team_id).by_actual_margin()
        assert team_by_actual_margin is not None


class TestClutchSplits():
    @staticmethod
    def test_last_5m_lte_5pts():
        team_last_5m_lte_5pts = team.ClutchSplits(2554).last_5m_lte_5pts()
        assert team_last_5m_lte_5pts is not None

    @staticmethod
    def test_last_3m_lte_5pts():
        team_last_3m_lte_5pts = team.ClutchSplits(2554).last_3m_lte_5pts()
        assert team_last_3m_lte_5pts is not None

    @staticmethod
    def test_last_1m_lte_5pts():
        team_last_1m_lte_5pts = team.ClutchSplits(2554).last_1m_lte_5pts()
        assert team_last_1m_lte_5pts is not None

    @staticmethod
    def test_last_30s_lte_3pts():
        team_last_30s_lte_3pts = team.ClutchSplits(2554).last_30s_lte_3pts()
        assert team_last_30s_lte_3pts is not None

    @staticmethod
    def test_last_10s_lte_3pts():
        team_last_10s_lte_3pts = team.ClutchSplits(2554).last_10s_lte_3pts()
        assert team_last_10s_lte_3pts is not None

    @staticmethod
    def test_last_5m_pm_5pts():
        team_last_5m_pm_5pts = team.ClutchSplits(2554).last_5m_pm_5pts()
        assert team_last_5m_pm_5pts is not None

    @staticmethod
    def test_last_3m_pm_5pts():
        team_last_3m_pm_5pts = team.ClutchSplits(2554).last_3m_pm_5pts()
        assert team_last_3m_pm_5pts is not None

    @staticmethod
    def test_last_1m_pm_5pts():
        team_last_1m_pm_5pts = team.ClutchSplits(2554).last_1m_pm_5pts()
        assert team_last_1m_pm_5pts is not None


class TestShootingSplits():
    @staticmethod
    def test_shot_5ft():
        team_shot_5ft = team.ShootingSplits(team_id).shot_5ft()
        assert team_shot_5ft is not None

    @staticmethod
    def test_shot_8ft():
        team_shot_8ft = team.ShootingSplits(team_id).shot_8ft()
        assert team_shot_8ft is not None

    @staticmethod
    def test_shot_areas():
        team_shot_areas = team.ShootingSplits(team_id).shot_areas()
        assert team_shot_areas is not None

    @staticmethod
    def test_assisted_shots():
        team_assisted_shots = team.ShootingSplits(team_id).assisted_shots()
        assert team_assisted_shots is not None

    @staticmethod
    def test_shot_types():
        team_shot_types = team.ShootingSplits(team_id).shot_types()
        assert team_shot_types is not None

    @staticmethod
    def test_assisted_by():
        team_assisted_by = team.ShootingSplits(team_id).assisted_by()
        assert team_assisted_by is not None


class TestPerformanceSplits():
    @staticmethod
    def test_score_differential():
        team_score_diff = team.PerformanceSplits(team_id).score_differential()
        assert team_score_diff is not None

    @staticmethod
    def test_points_scored():
        team_points_scored = team.PerformanceSplits(team_id).points_scored()
        assert team_points_scored is not None

    @staticmethod
    def test_points_against():
        team_points_against = team.PerformanceSplits(team_id).points_against()
        assert team_points_against is not None


class TestPlayerSplits():
    @staticmethod
    def test_players():
        team_players = team.PlayerSplits(team_id).players()
        assert team_players is not None


class TestPlayerOnOffSplits():
    @staticmethod
    def test_on_court():
        team_on_court = team.PlayerOnOffSplits(team_id).on_court()
        assert team_on_court is not None

    @staticmethod
    def test_off_court():
        team_off_court = team.PlayerOnOffSplits(team_id).off_court()
        assert team_off_court is not None


class TestPlayerOnOffSummary():
    @staticmethod
    def test_on_court():
        team_on_court = team.PlayerOnOffSummary(team_id).on_court()
        assert team_on_court is not None

    @staticmethod
    def test_off_court():
        team_off_court = team.PlayerOnOffSummary(team_id).off_court()
        assert team_off_court is not None


class TestYearOverYearSplits():
    @staticmethod
    def test_by_year():
        team_by_year = team.YearOverYearSplits(team_id).by_year()
        assert team_by_year is not None


class TestShotTracking():
    @staticmethod
    def test_general():
        team_general = team.ShotTracking(team_id).general()
        assert team_general is not None

    @staticmethod
    def test_shot_clock():
        team_shot_clock = team.ShotTracking(team_id).shot_clock()
        assert team_shot_clock is not None

    @staticmethod
    def test_dribble():
        team_dribble = team.ShotTracking(team_id).dribbles()
        assert team_dribble is not None

    @staticmethod
    def test_closest_defender():
        team_closest_defender = team.ShotTracking(team_id).closest_defender()
        assert team_closest_defender is not None

    @staticmethod
    def test_closest_defender_long():
        stats = team.ShotTracking(team_id).closest_defender_long()
        assert stats is not None

    @staticmethod
    def test_touch_time():
        team_touch_time = team.ShotTracking(team_id).touch_time()
        assert team_touch_time is not None


class TestReboundTracking():
    @staticmethod
    def test_overall():
        team_overall = team.ReboundTracking(team_id).overall()
        assert team_overall is not None

    @staticmethod
    def test_shot_type():
        team_shot_type = team.ReboundTracking(team_id).shot_type()
        assert team_shot_type is not None

    @staticmethod
    def test_num_contested():
        team_num_contested = team.ReboundTracking(team_id).num_contested()
        assert team_num_contested is not None

    @staticmethod
    def test_shot_distance():
        team_shot_distance = team.ReboundTracking(team_id).shot_distance()
        assert team_shot_distance is not None

    @staticmethod
    def test_rebound_distance():
        stats = team.ReboundTracking(team_id).rebound_distance()
        assert stats is not None


class TestPassTracking():
    @staticmethod
    def test_made():
        team_made = team.PassTracking(team_id).made()
        assert team_made is not None

    @staticmethod
    def test_received():
        team_received = team.PassTracking(team_id).received()
        assert team_received is not None


class TestGameLogs():
    @staticmethod
    def test_logs():
        team_logs = team.GameLogs(team_id).logs()
        assert team_logs is not None


class TestSeasonResults():
    @staticmethod
    def test_results():
        team_results = team.SeasonResults(team_id).results()
        assert team_results is not None


class TestVsPlayer():
    @staticmethod
    def test_overall():
        stats = team.VsPlayer(team_id, player_id).overall()
        assert stats is not None

    @staticmethod
    def test_vs_player_overall():
        stats = team.VsPlayer(team_id, player_id).vs_player_overall()
        assert stats is not None

    @staticmethod
    def test_on_off_court():
        stats = team.VsPlayer(team_id, player_id).on_off_court()
        assert stats is not None

    @staticmethod
    def test_shot_dist_overall():
        stats = team.VsPlayer(team_id, player_id).shot_dist_overall()
        assert stats is not None

    @staticmethod
    def test_shot_dist_on_court():
        stats = team.VsPlayer(team_id, player_id).shot_dist_on_court()
        assert stats is not None

    @staticmethod
    def test_shot_dist_off_court():
        stats = team.VsPlayer(team_id, player_id).shot_dist_off_court()
        assert stats is not None

    @staticmethod
    def test_shot_area_overall():
        stats = team.VsPlayer(team_id, player_id).shot_area_overall()
        assert stats is not None

    @staticmethod
    def test_shot_area_on_court():
        stats = team.VsPlayer(team_id, player_id).shot_area_on_court()
        assert stats is not None

    @staticmethod
    def test_shot_area_off_court():
        stats = team.VsPlayer(team_id, player_id).shot_area_off_court()
        assert stats is not None
