from nba_stats.nba_api import NbaAPI
from nba_stats import constants


class TeamList:
    _endpoint = 'commonteamyears'

    def __init__(self,
                 league_id=constants.League.NBA):
        self._params = {
            'LeagueID': league_id
        }

        self.api = NbaAPI(self._endpoint, self._params)

    def teams(self):
        return self.api.get_result()


class TeamSummary:
    _endpoint = 'teaminfocommon'

    def __init__(self,
                 team_id,
                 season=constants.CURRENT_SEASON,
                 league_id=constants.League.NBA,
                 season_type=constants.SeasonType.Default):
        self._params = {
            'TeamID': team_id,
            'Season': season,
            'LeagueID': league_id,
            'SeasonType': season_type,
        }
        self.api = NbaAPI(self._endpoint, self._params)

    def info(self):
        return self.api.get_result('TeamInfoCommon')

    def season_ranks(self):
        return self.api.get_result('TeamSeasonRanks')


class Details:
    """Various team details."""
    _endpoint = 'teamdetails'

    def __init__(self, team_id):
        self._params = {
            'TeamID': team_id
        }

        self.api = NbaAPI(self._endpoint, self._params)

    def background(self):
        """Background info such as coach, city, arena, owner, etc. """
        return self.api.get_result('TeamBackground')

    def history(self):
        """History info such as nickname, year founded, etc."""
        return self.api.get_result('TeamHistory')

    def social_sites(self):
        """Team social media sites."""
        return self.api.get_result('TeamSocialSites')

    def awards_championships(self):
        """Champtionship title victories and opponents"""
        return self.api.get_result('TeamAwardsChampionships')

    def awards_conf(self):
        """Conference title victories and opponents"""
        return self.api.get_result('TeamAwardsConf')

    def awards_div(self):
        """Division title victories and opponents"""
        return self.api.get_result('TeamAwardsDiv')

    def hof_players(self):
        """All team hall of fame players."""
        return self.api.get_result('TeamHof')

    def retired_players(self):
        """Retired numbers and associated info"""
        return self.api.get_result('TeamRetired')


class CommonRoster:
    _endpoint = 'commonteamroster'

    def __init__(self,
                 team_id,
                 season=constants.CURRENT_SEASON):
        self._params = {
            'TeamID': team_id,
            'Season': season,
        }
        self.api = NbaAPI(self._endpoint, self._params)

    def roster(self):
        return self.api.get_result('CommonTeamRoster')

    def coaches(self):
        return self.api.get_result('Coaches')


class Splits:
    """Team stats splits.

    Also a base class containing common arguments for different split type
    child classes.

    Args:
        team_id: ID of the team to look up
        measure_type: Specifies type of measure to use (Base, Advanced, etc.)
        per_mode: Mode to measure statistics (Totals, PerGame, Per36, etc.)
        plus_minus: Whether or not to consider plus minus (Y or N)
        pace_adjust: Whether or not to pace adjust stats (Y or N)
        rank: Whether or not to consider rank (Y or N)
        league_id: ID for the league to look in (Default is 00)
        season: Season given to look up
        season_type: Season type to consider (Regular / Playoffs)
        po_round: Playoff round
        outcome: Filter out by wins or losses
        location: Filter out by home or away
        month: Specify month to filter by
        season_segment: Filter by pre/post all star break
        date_from: Filter out games before a specific date
        date_to: Filter out games after a specific date
        opponent_team_id: Opponent team ID to look up
        vs_conference: Filter by conference
        vs_division: Filter by division
        game_segment: Filter by half / overtime
        period: Filter by quarter / specific overtime
        shot_clock_range: Filter statistics by range in shot clock
        last_n_games: Filter by number of games specified in N
    """
    _endpoint = 'teamdashboardbygeneralsplits'

    def __init__(
            self,
            team_id,
            measure_type=constants.MeasureType.Default,
            per_mode=constants.PerMode.Default,
            plus_minus=constants.PlusMinus.Default,
            pace_adjust=constants.PaceAdjust.Default,
            rank=constants.Rank.Default,
            league_id=constants.League.Default,
            season=constants.CURRENT_SEASON,
            season_type=constants.SeasonType.Default,
            po_round=constants.PlayoffRound.Default,
            outcome=constants.Outcome.Default,
            location=constants.Location.Default,
            month=constants.Month.Default,
            season_segment=constants.SeasonSegment.Default,
            date_from=constants.DateFrom.Default,
            date_to=constants.DateTo.Default,
            opponent_team_id=constants.OpponentTeamID.Default,
            vs_conference=constants.VsConference.Default,
            vs_division=constants.VsDivision.Default,
            game_segment=constants.GameSegment.Default,
            period=constants.Period.Default,
            shot_clock_range=constants.ShotClockRange.Default,
            last_n_games=constants.LastNGames.Default,
    ):
        self._params = {
            'TeamID': team_id,
            'MeasureType': measure_type,
            'PerMode': per_mode,
            'PlusMinus': plus_minus,
            'PaceAdjust': pace_adjust,
            'Rank': rank,
            'LeagueID': league_id,
            'Season': season,
            'SeasonType': season_type,
            'PORound': po_round,
            'Outcome': outcome,
            'Location': location,
            'Month': month,
            'SeasonSegment': season_segment,
            'DateFrom': date_from,
            'DateTo': date_to,
            'OpponentTeamID': opponent_team_id,
            'VsConference': vs_conference,
            'VsDivision': vs_division,
            'GameSegment': game_segment,
            'Period': period,
            'ShotClockRange': shot_clock_range,
            'LastNGames': last_n_games
        }
        self.api = NbaAPI(self._endpoint, self._params)

    def overall(self):
        return self.api.get_result('OverallTeamDashboard')


class GeneralSplits(Splits):
    """Contains stats pertaining to location, wins and losses, pre/post all star
    break and numbers of days rest

    Args:
        see Splits
    """
    _endpoint = 'teamdashboardbygeneralsplits'

    def location(self):
        return self.api.get_result('LocationTeamDashboard')

    def wins_losses(self):
        return self.api.get_result('WinsLossesTeamDashboard')

    def month(self):
        return self.api.get_result('MonthTeamDashboard')

    def pre_post_all_star(self):
        return self.api.get_result('PrePostAllStarTeamDashboard')

    def days_rest(self):
        return self.api.get_result('DaysRestTeamDashboard')


class LineupSplits:
    """Splits for all team lineup combinations"""
    _endpoint = 'teamdashlineups'

    def __init__(
            self,
            team_id,
            game_id='',
            group_quantity=constants.GroupQuantity.Default,
            season=constants.CURRENT_SEASON,
            season_type=constants.SeasonType.Default,
            measure_type=constants.MeasureType.Default,
            per_mode=constants.PerMode.Default,
            plus_minus=constants.PlusMinus.Default,
            pace_adjust=constants.PaceAdjust.Default,
            rank=constants.Rank.Default,
            outcome=constants.Outcome.Default,
            location=constants.Location.Default,
            month=constants.Month.Default,
            season_segment=constants.SeasonSegment.Default,
            date_from=constants.DateFrom.Default,
            date_to=constants.DateTo.Default,
            opponent_team_id=constants.OpponentTeamID.Default,
            vs_conference=constants.VsConference.Default,
            vs_division=constants.VsDivision.Default,
            game_segment=constants.GameSegment.Default,
            period=constants.Period.Default,
            last_n_games=constants.LastNGames.Default
    ):
        self._params = {
            'GroupQuantity': group_quantity,
            'GameID': game_id,
            'TeamID': team_id,
            'Season': season,
            'SeasonType': season_type,
            'MeasureType': measure_type,
            'PerMode': per_mode,
            'PlusMinus': plus_minus,
            'PaceAdjust': pace_adjust,
            'Rank': rank,
            'Outcome': outcome,
            'Location': location,
            'Month': month,
            'SeasonSegment': season_segment,
            'DateFrom': date_from,
            'DateTo': date_to,
            'OpponentTeamID': opponent_team_id,
            'VsConference': vs_conference,
            'VsDivision': vs_division,
            'GameSegment': game_segment,
            'Period': period,
            'LastNGames': last_n_games
        }
        self.api = NbaAPI(self._endpoint, self._params)

    def lineups(self):
        return self.api.get_result('Lineups')


class OpponentSplits(Splits):
    """Contains stats pertaining to a team vs certain opponents by
    division, conference, and by specific team opponent

    Args:
        see Splits
    """
    _endpoint = 'teamdashboardbyopponent'

    def by_conference(self):
        return self.api.get_result('ConferenceTeamDashboard')

    def by_division(self):
        return self.api.get_result('DivisionTeamDashboard')

    def by_team(self):
        return self.api.get_result('OpponentTeamDashboard')


class LastNGamesSplits(Splits):
    """Contains team stats per last 5, 10, 15, and 20 games, or
    specified number of games.

    Args:
        see Splits
    """
    _endpoint = 'teamdashboardbylastngames'

    def last_5(self):
        return self.api.get_result('Last5TeamDashboard')

    def last_10(self):
        return self.api.get_result('Last10TeamDashboard')

    def last_15(self):
        return self.api.get_result('Last15TeamDashboard')

    def last_20(self):
        return self.api.get_result('Last20TeamDashboard')

    def game_num(self):
        """Stats for sets of 10 games"""
        return self.api.get_result('GameNumberTeamDashboard')


class InGameSplits(Splits):
    """Contains team stats by half, by quarter, by score margin,
    and by actual margins.

    Args:
        see Splits
    """
    _endpoint = 'teamdashboardbygamesplits'

    def by_half(self):
        return self.api.get_result('ByHalfTeamDashboard')

    def by_period(self):
        return self.api.get_result('ByPeriodTeamDashboard')

    def by_score_margin(self):
        return self.api.get_result('ByScoreMarginTeamDashboard')

    def by_actual_margin(self):
        return self.api.get_result('ByActualMarginTeamDashboard')


class ClutchSplits(Splits):
    """Contains a lot of methods for last n minutes with a deficit of
    x points.

    Args:
        see Splits
    """
    _endpoint = 'teamdashboardbyclutch'

    def last_5m_lte_5pts(self):
        """Splits in last 5 minutes <= 5 points"""
        return self.api.get_result('Last5Min5PointTeamDashboard')

    def last_3m_lte_5pts(self):
        """Splits in last 3 minutes <= 5 points"""
        return self.api.get_result('Last3Min5PointTeamDashboard')

    def last_1m_lte_5pts(self):
        """Splits in last minute <= 5 points"""
        return self.api.get_result('Last1Min5PointTeamDashboard')

    def last_30s_lte_3pts(self):
        """Splits in last 30 seconds <= 3 points"""
        return self.api.get_result('Last30Sec3PointTeamDashboard')

    def last_10s_lte_3pts(self):
        """Splits in last 10 seconds <= 3 points"""
        return self.api.get_result('Last10Sec3PointTeamDashboard')

    def last_5m_pm_5pts(self):
        """Splits in last 5 minutes +/- 5 points"""
        return self.api.get_result('Last5MinPlusMinus5PointTeamDashboard')

    def last_3m_pm_5pts(self):
        """Splits in last 3 minutes +/- 5 points"""
        return self.api.get_result('Last3MinPlusMinus5PointTeamDashboard')

    def last_1m_pm_5pts(self):
        """Splits in last minute +/- 5 points"""
        return self.api.get_result('Last1MinPlusMinus5PointTeamDashboard')


class ShootingSplits(Splits):
    """Stats based on shot distance, area, assisted to, shot types, and
    assisted by.

    Args:
        see Splits
    """
    _endpoint = 'teamdashboardbyshootingsplits'

    def shot_5ft(self):
        return self.api.get_result('Shot5FTTeamDashboard')

    def shot_8ft(self):
        return self.api.get_result('Shot8FTTeamDashboard')

    def shot_areas(self):
        return self.api.get_result('ShotAreaTeamDashboard')

    def assisted_shots(self):
        return self.api.get_result('AssitedShotTeamDashboard')

    def shot_types(self):
        return self.api.get_result('ShotTypeTeamDashboard')

    def assisted_by(self):
        return self.api.get_result('AssistedBy')


class PerformanceSplits(Splits):
    """Team stats by different performance metrics such as score
    differential, points scored, and points scored against.

    Args:
        see Splits
    """
    _endpoint = 'teamdashboardbyteamperformance'

    def score_differential(self):
        return self.api.get_result('ScoreDifferentialTeamDashboard')

    def points_scored(self):
        return self.api.get_result('PointsScoredTeamDashboard')

    def points_against(self):
        return self.api.get_result('PontsAgainstTeamDashboard')


class PlayerSplits(Splits):
    """Splits for all the players on a team."""
    _endpoint = 'teamplayerdashboard'

    def players(self):
        return self.api.get_result('PlayersSeasonTotals')


class PlayerOnOffSplits(Splits):
    """Team splits when a specific player is on or off the court."""
    _endpoint = 'teamplayeronoffdetails'

    def on_court(self):
        return self.api.get_result('PlayersOnCourtTeamPlayerOnOffDetails')

    def off_court(self):
        return self.api.get_result('PlayersOffCourtTeamPlayerOnOffDetails')


class PlayerOnOffSummary(Splits):
    """Team stats on offensive/defensive/net rating with players
       on or off the court.
    """
    _endpoint = 'teamplayeronoffsummary'

    def on_court(self):
        return self.api.get_result('PlayersOnCourtTeamPlayerOnOffSummary')

    def off_court(self):
        return self.api.get_result('PlayersOffCourtTeamPlayerOnOffSummary')


class YearOverYearSplits(Splits):
    """Displays team stats over the given season and over all seasons in
    the given league.

    Args:
        see Splits
    """
    _endpoint = 'teamdashboardbyyearoveryear'

    def by_year(self):
        return self.api.get_result('ByYearTeamDashboard')


class ShotTracking(Splits):
    """Shooting tracking data for a given team

    Args:
        see Splits
    """
    _endpoint = 'teamdashptshots'

    def general(self):
        return self.api.get_result('GeneralShooting')

    def shot_clock(self):
        return self.api.get_result('ShotClockShooting')

    def dribbles(self):
        return self.api.get_result('DribbleShooting')

    def closest_defender(self):
        return self.api.get_result('ClosestDefenderShooting')

    def closest_defender_long(self):
        return self.api.get_result('ClosestDefender10ftPlusShooting')

    def touch_time(self):
        return self.api.get_result('TouchTimeShooting')


class ReboundTracking(Splits):
    """Tracking data for rebounding for a given team

    Args:
        see Splits
    """
    _endpoint = 'teamdashptreb'

    def overall(self):
        return self.api.get_result('OverallRebounding')

    def shot_type(self):
        return self.api.get_result('ShotTypeRebounding')

    def num_contested(self):
        return self.api.get_result('NumContestedRebounding')

    def shot_distance(self):
        return self.api.get_result('ShotDistanceRebounding')

    def rebound_distance(self):
        return self.api.get_result('RebDistanceRebounding')


class PassTracking(Splits):
    """Tracking data for passing for a given team

    Args:
        see Splits
    """
    _endpoint = 'teamdashptpass'

    def made(self):
        return self.api.get_result('PassesMade')

    def received(self):
        return self.api.get_result('PassesReceived')


class GameLogs:
    _endpoint = 'teamgamelogs'

    def __init__(
            self,
            team_id,
            date_from=constants.DateFrom.Default,
            date_to=constants.DateTo.Default,
            game_segment=constants.GameSegment.Default,
            last_n_games=constants.LastNGames.Default,
            league_id=constants.League.Default,
            location=constants.Location.Default,
            measure_type=constants.MeasureType.Default,
            month=constants.Month.Default,
            opponent_team_id=constants.OpponentTeamID.Default,
            outcome=constants.Outcome.Default,
            po_round=constants.PlayoffRound.Default,
            pace_adjust=constants.PaceAdjust.Default,
            per_mode=constants.PerMode.Default,
            period=constants.Period.Default,
            plus_minus=constants.PlusMinus.Default,
            rank=constants.Rank.Default,
            season=constants.CURRENT_SEASON,
            season_segment=constants.SeasonSegment.Default,
            season_type=constants.SeasonType.Default,
            shot_clock_range=constants.ShotClockRange.Default,
            vs_conference=constants.VsConference.Default,
            vs_division=constants.VsDivision.Default,
    ):
        self._params = {
            'TeamID': team_id,
            'DateFrom': date_from,
            'DateTo': date_to,
            'GameSegment': game_segment,
            'LastNGames': last_n_games,
            'LeagueID': league_id,
            'Location': location,
            'MeasureType': measure_type,
            'Month': month,
            'OpponentTeamID': opponent_team_id,
            'Outcome': outcome,
            'PORound': po_round,
            'PaceAdjust': pace_adjust,
            'PerMode': per_mode,
            'Period': period,
            'PlusMinus': plus_minus,
            'Rank': rank,
            'Season': season,
            'SeasonSegment': season_segment,
            'SeasonType': season_type,
            'ShotClockRange': shot_clock_range,
            'VsConference': vs_conference,
            'VsDivision': vs_division,
        }
        self.api = NbaAPI(self._endpoint, self._params)

    def logs(self):
        return self.api.get_result('TeamGameLogs')


class SeasonResults:
    """Team results per season such as W/L, points, division/conference
       rank, playoff record, finals results, etc.
    """
    _endpoint = 'teamyearbyyearstats'

    def __init__(
            self,
            team_id,
            league_id=constants.League.NBA,
            season_type=constants.SeasonType.Default,
            per_mode=constants.PerMode.Default
    ):
        self._params = {
            'TeamID': team_id,
            'LeagueID': league_id,
            'SeasonType': season_type,
            'PerMode': per_mode
        }
        self.api = NbaAPI(self._endpoint, self._params)

    def results(self):
        return self.api.get_result('TeamStats')


class VsPlayer:
    _endpoint = 'teamvsplayer'

    def __init__(
            self,
            team_id,
            vs_player_id,
            measure_type=constants.MeasureType.Default,
            per_mode=constants.PerMode.Default,
            plus_minus=constants.PlusMinus.Default,
            pace_adjust=constants.PaceAdjust.Default,
            rank=constants.Rank.Default,
            league_id=constants.League.Default,
            season=constants.CURRENT_SEASON,
            season_type=constants.SeasonType.Default,
            po_round=constants.PlayoffRound.Default,
            outcome=constants.Outcome.Default,
            location=constants.Location.Default,
            month=constants.Month.Default,
            season_segment=constants.SeasonSegment.Default,
            date_from=constants.DateFrom.Default,
            date_to=constants.DateTo.Default,
            opponent_team_id=constants.OpponentTeamID.Default,
            vs_conference=constants.VsConference.Default,
            vs_division=constants.VsDivision.Default,
            game_segment=constants.GameSegment.Default,
            period=constants.Period.Default,
            shot_clock_range=constants.ShotClockRange.Default,
            last_n_games=constants.LastNGames.Default
    ):
        self._params = {
            'TeamID': team_id,
            'VsPlayerID': vs_player_id,
            'MeasureType': measure_type,
            'PerMode': per_mode,
            'PlusMinus': plus_minus,
            'PaceAdjust': pace_adjust,
            'Rank': rank,
            'LeagueID': league_id,
            'Season': season,
            'SeasonType': season_type,
            'PORound': po_round,
            'Outcome': outcome,
            'Location': location,
            'Month': month,
            'SeasonSegment': season_segment,
            'DateFrom': date_from,
            'DateTo': date_to,
            'OpponentTeamID': opponent_team_id,
            'VsConference': vs_conference,
            'VsDivision': vs_division,
            'GameSegment': game_segment,
            'Period': period,
            'ShotClockRange': shot_clock_range,
            'LastNGames': last_n_games
        }
        self.api = NbaAPI(self._endpoint, self._params)

    def overall(self):
        return self.api.get_result('Overall')

    def vs_player_overall(self):
        return self.api.get_result('vsPlayerOverall')

    def on_off_court(self):
        return self.api.get_result('OnOffCourt')

    def shot_dist_overall(self):
        return self.api.get_result('ShotDistanceOverall')

    def shot_dist_on_court(self):
        return self.api.get_result('ShotDistanceOnCourt')

    def shot_dist_off_court(self):
        return self.api.get_result('ShotDistanceOffCourt')

    def shot_area_overall(self):
        return self.api.get_result('ShotAreaOverall')

    def shot_area_on_court(self):
        return self.api.get_result('ShotAreaOnCourt')

    def shot_area_off_court(self):
        return self.api.get_result('ShotAreaOffCourt')
