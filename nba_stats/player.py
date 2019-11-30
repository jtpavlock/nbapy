import pandas as pd

from nba_stats.nba_api import NbaAPI
from nba_stats import constants


class PlayerNotFoundException(Exception):
    pass


def get_id(
        name,
        season=constants.CURRENT_SEASON,
        active_only=1,
):
    """Get a player_id for any specified player.

    Calls PlayerList, then matches name to return the id. Player id is needed
    for most of our player functions.

    Args:
        name: name of the player to lookup. This must match the name
            as presented on nba.com (case insensitive)
        season: season to lookup
        active_only: only match active players

    Returns:
        Nba.com player_id

    Raises:
        PlayerNotFoundException
    """
    name = name.lower()

    players = pd.DataFrame(
        PlayerList(season=season, active_only=active_only).players())

    player = players.loc[players['DISPLAY_FIRST_LAST'].str.lower() == name,
                         'PERSON_ID']
    try:
        player_id = player.iat[0]
    except IndexError:
        raise PlayerNotFoundException(
            f'The player "{name}" could not be found. Please double check the '
            'name against nba.com')

    return player_id


class PlayerList:
    """Contains a list of players and their teams.

    Args:
        league_id: ID for the league to look in
        season: Season given to look up. This affects whether or not the player
            is active and on what team.
        active_only: (1 or 0 for true or false respectively).
            Only return active players for the given season.
            If season is set prior to the current season, and active_only is 1,
            then only players who's career ended in the specified season will
            be listed.
    """
    _endpoint = 'commonallplayers'

    def __init__(
            self,
            league_id=constants.League.NBA,
            season=constants.CURRENT_SEASON,
            active_only=1,
    ):
        self._params = {
            'LeagueID': league_id,
            'Season': season,
            'IsOnlyCurrentSeason': active_only,
        }
        self.api = NbaAPI(self._endpoint, self._params)

    def players(self):
        return self.api.get_result()


class Summary:
    """
    Contains common player information like headline stats, weight, etc.

    Args:
        player_id: ID of the player to look up
    """
    _endpoint = 'commonplayerinfo'

    def __init__(self, player_id: str):
        self._params = {'PlayerID': player_id}

        self.api = NbaAPI(self._endpoint, self._params)

    def info(self):
        return self.api.get_result('CommonPlayerInfo')

    def headline_stats(self):
        return self.api.get_result('PlayerHeadlineStats')


class Splits:
    """Player stats splits.

    Also a base class containing common arguments for different split type
    child classes.

    Args:
        player_id: ID of the player to look up
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
    _endpoint = 'playerdashboardbygeneralsplits'  # this could be any split

    def __init__(
            self,
            player_id: str,
            team_id: str = 0,
            measure_type=constants.MeasureType.Default,
            per_mode=constants.PerMode.Default,
            plus_minus=constants.PlusMinus.Default,
            pace_adjust=constants.PaceAdjust.Default,
            rank=constants.PaceAdjust.Default,
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
            'PlayerID': player_id,
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
            'LastNGames': last_n_games,
        }
        self.api = NbaAPI(self._endpoint, self._params)

    def overall(self):
        return self.api.get_result('OverallPlayerDashboard')


class GeneralSplits(Splits):
    """Contains stats pertaining to location, wins and losses, pre/post all star
    break, starting position, and numbers of days rest

    Args:
        see Splits
    """
    _endpoint = 'playerdashboardbygeneralsplits'

    def location(self):
        return self.api.get_result('LocationPlayerDashboard')

    def wins_losses(self):
        return self.api.get_result('WinsLossesPlayerDashboard')

    def month(self):
        return self.api.get_result('MonthPlayerDashboard')

    def pre_post_all_star(self):
        return self.api.get_result('PrePostAllStarPlayerDashboard')

    def starting_position(self):
        return self.api.get_result('StartingPosition')

    def days_rest(self):
        return self.api.get_result('DaysRestPlayerDashboard')


class OpponentSplits(Splits):
    """Contains stats pertaining to player stats vs certain opponents by
    division, conference, and by specific team opponent

    Args:
        see Splits
    """
    _endpoint = 'playerdashboardbyopponent'

    def by_conference(self):
        return self.api.get_result('ConferencePlayerDashboard')

    def by_division(self):
        return self.api.get_result('DivisionPlayerDashboard')

    def by_team(self):
        return self.api.get_result('OpponentPlayerDashboard')


class LastNGamesSplits(Splits):
    """Contains players stats per last 5, 10, 15, and 20 games, or
    specified number of games.

    Args:
        see Splits
    """
    _endpoint = 'playerdashboardbylastngames'

    def last_5(self):
        return self.api.get_result('Last5PlayerDashboard')

    def last_10(self):
        return self.api.get_result('Last10PlayerDashboard')

    def last_15(self):
        return self.api.get_result('Last15PlayerDashboard')

    def last_20(self):
        return self.api.get_result('Last20PlayerDashboard')

    def game_num(self):
        """Stats for sets of 10 games"""
        return self.api.get_result('GameNumberPlayerDashboard')


class InGameSplits(Splits):
    """Contains player stats by half, by quarter, by score margin,
    and by actual margins.

    Args:
        see Splits
    """
    _endpoint = 'playerdashboardbygamesplits'

    def by_half(self):
        return self.api.get_result('ByHalfPlayerDashboard')

    def by_period(self):
        return self.api.get_result('ByPeriodPlayerDashboard')

    def by_score_margin(self):
        return self.api.get_result('ByScoreMarginPlayerDashboard')

    def by_actual_margin(self):
        return self.api.get_result('ByActualMarginPlayerDashboard')


class ClutchSplits(Splits):
    """Contains a lot of methods for last n minutes with a deficit of
    x points.

    Args:
        see Splits
    """
    _endpoint = 'playerdashboardbyclutch'

    def last_5m_lte_5pts(self):
        """Splits in last 5 minutes <= 5 points"""
        return self.api.get_result('Last5Min5PointPlayerDashboard')

    def last_3m_lte_5pts(self):
        """Splits in last 3 minutes <= 5 points"""
        return self.api.get_result('Last3Min5PointPlayerDashboard')

    def last_1m_lte_5pts(self):
        """Splits in last minute <= 5 points"""
        return self.api.get_result('Last1Min5PointPlayerDashboard')

    def last_30s_lte_3pts(self):
        """Splits in last 30 seconds <= 3 points"""
        return self.api.get_result('Last30Sec3PointPlayerDashboard')

    def last_10s_lte_3pts(self):
        """Splits in last 10 seconds <= 3 points"""
        return self.api.get_result('Last10Sec3PointPlayerDashboard')

    def last_5m_pm_5pts(self):
        """Splits in last 5 minutes +/- 5 points"""
        return self.api.get_result('Last5MinPlusMinus5PointPlayerDashboard')

    def last_3m_pm_5pts(self):
        """Splits in last 3 minutes +/- 5 points"""
        return self.api.get_result('Last3MinPlusMinus5PointPlayerDashboard')

    def last_1m_pm_5pts(self):
        """Splits in last minute +/- 5 points"""
        return self.api.get_result('Last1MinPlusMinus5PointPlayerDashboard')


class TeamPerformanceSplits(Splits):
    """Player stats by different team performance metrics such as score
    differential, points scored, and points scored against.

    Args:
        see Splits
    """
    _endpoint = 'playerdashboardbyteamperformance'

    def score_differential(self):
        return self.api.get_result('ScoreDifferentialPlayerDashboard')

    def points_scored(self):
        return self.api.get_result('PointsScoredPlayerDashboard')

    def points_against(self):
        return self.api.get_result('PontsAgainstPlayerDashboard')


class YearOverYearSplits(Splits):
    """Displays player stats over the given season and over all seasons in
    the given league.

    Args:
        see Splits
    """
    _endpoint = 'playerdashboardbyyearoveryear'

    def by_year(self):
        return self.api.get_result('ByYearPlayerDashboard')


class ShootingSplits(Splits):
    """Stats based on shot distance, area, assisted to, shot types, and
    assisted by.

    Args:
        see Splits
    """
    _endpoint = 'playerdashboardbyshootingsplits'

    def shot_5ft(self):
        return self.api.get_result('Shot5FTPlayerDashboard')

    def shot_8ft(self):
        return self.api.get_result('Shot8FTPlayerDashboard')

    def shot_areas(self):
        return self.api.get_result('ShotAreaPlayerDashboard')

    def assisted_shots(self):
        return self.api.get_result('AssitedShotPlayerDashboard')

    def shot_types_summary(self):
        return self.api.get_result('ShotTypeSummaryPlayerDashboard')

    def shot_types_detail(self):
        return self.api.get_result('ShotTypePlayerDashboard')

    def assisted_by(self):
        return self.api.get_result('AssistedBy')


class Career:
    """
    Contains stats based on several parameters such as career regular season
    totals, post season career totals, all star season careers totals, college
    season career totals, season/career highs and next game info.

    Args:
        player_id: Player ID to look up
        per_mode: Mode to measure statistics (Totals, PerGame, Per36, etc.)
        league_id: ID for the league to look in (Default is 00)
    """
    _endpoint = 'playerprofilev2'

    def __init__(
            self,
            player_id: str,
            per_mode=constants.PerMode.PerGame,
            league_id=constants.League.NBA,
    ):
        self._params = {
            'PlayerID': player_id,
            'LeagueID': league_id,
            'PerMode': per_mode,
        }
        self.api = NbaAPI(self._endpoint, self._params)

    def reg_season_splits(self, career=False):
        """Regular-season splits

        Args:
            career:
                True: Career totals
                False: Per-season (per_mode) stats
        """
        if career:
            return self.api.get_result('CareerTotalsRegularSeason')
        return self.api.get_result('SeasonTotalsRegularSeason')

    def post_season_splits(self, career=False):
        """Post-season splits

        Args:
            career:
                True: Career totals
                False: Per-season (per_mode) stats
        """
        if career:
            return self.api.get_result('CareerTotalsPostSeason')
        return self.api.get_result('SeasonTotalsPostSeason')

    def all_star_season_splits(self, career=False):
        """Splits for all seasons the player was an all-star

        Args:
            career:
                True: Career totals
                False: Per-season (per_mode) stats
        """
        if career:
            return self.api.get_result('CareerTotalsAllStarSeason')
        return self.api.get_result('SeasonTotalsAllStarSeason')

    def college_season_splits(self, career=False):
        """College splits

        Args:
            career:
                True: Career totals
                False: Per-season (per_mode) stats
        """
        if career:
            return self.api.get_result('CareerTotalsCollegeSeason')
        return self.api.get_result('SeasonTotalsCollegeSeason')

    def reg_season_rankings(self):
        """Regular season split rankings"""
        return self.api.get_result('SeasonRankingsRegularSeason')

    def post_season_rankings(self):
        """Post season split rankings"""
        return self.api.get_result('SeasonRankingsPostSeason')

    def season_highs(self):
        """Season highs in basic stats"""
        return self.api.get_result('SeasonHighs')

    def career_highs(self):
        """Career highs in basic stats"""
        return self.api.get_result('CareerHighs')

    def next_game(self):
        """Info on the player's next game"""
        return self.api.get_result('NextGame')


class GameLogs:
    """Contains a full log of all the games for a player for a given season

    Args:
        player_id: ID of the player to look up
        league_id: ID for the league to look in
        season: Season given to look up
        season_type: Season type to consider (Regular / Playoffs)
    """
    _endpoint = 'playergamelog'

    def __init__(
            self,
            player_id: str,
            league_id=constants.League.NBA,
            season=constants.CURRENT_SEASON,
            season_type=constants.SeasonType.Regular,
    ):
        self._params = {
            'PlayerID': player_id,
            'LeagueID': league_id,
            'Season': season,
            'SeasonType': season_type,
        }
        self.api = NbaAPI(self._endpoint, self._params)

    def logs(self):
        return self.api.get_result('PlayerGameLog')


class ShotTracking(Splits):
    """Tracking data for shooting for a given player

    Args:
        see Splits
    """
    _endpoint = 'playerdashptshots'

    def overall(self):
        return self.api.get_result('Overall')

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
    _endpoint = 'playerdashptreb'

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
    _endpoint = 'playerdashptpass'

    def made(self):
        return self.api.get_result('PassesMade')

    def received(self):
        return self.api.get_result('PassesReceived')


class DefenseTracking(Splits):
    """
    Tracking data for defense for a given player

    Args:
        see Splits
    """
    _endpoint = 'playerdashptshotdefend'

    def shot_types(self):
        return self.api.get_result('DefendingShots')


class VsPlayer:
    """Contains general stats that pertain to players against other players

    Args:
        :player_id: ID of the player to look up
        :vs_player_id: ID of the vs player to look up
        :team_id: ID of the team to look up
        :measure_type: Specifies type of measure to use (Base, Advanced, etc.)
        :per_mode: Mode to measure statistics (Totals, PerGame, Per36, etc.)
        :plus_minus: Whether or not to consider plus minus (Y or N)
        :pace_adjust: Whether or not to pace adjust stats (Y or N)
        :rank: Whether or not to consider rank (Y or N)
        :league_id: ID for the league to look in (Default is 00)
        :season: Season given to look up
        :season_type: Season type to consider (Regular / Playoffs)
        :po_round: Playoff round
        :outcome: Filter out by wins or losses
        :location: Filter out by home or away
        :month: Specify month to filter by
        :season_segment: Filter by pre/post all star break
        :date_from: Filter out games before a specific date
        :date_to: Filter out games after a specific date
        :opponent_team_id: Opponent team ID to look up
        :vs_conference: Filter by conference
        :vs_division: Filter by division
        :game_segment: Filter by half / overtime
        :period: Filter by quarter / specific overtime
        :shot_clock_range: Filter statistics by range in shot clock
        :last_n_games: Filter by number of games specified in N

    Attributes:
        json: Contains the full json dump to play around with
    """
    _endpoint = 'playervsplayer'

    def __init__(
            self,
            player_id: str,
            vs_player_id: str,
            team_id: str = 0,
            measure_type=constants.MeasureType.Default,
            per_mode=constants.PerMode.Default,
            plus_minus=constants.PlusMinus.Default,
            pace_adjust=constants.PaceAdjust.Default,
            rank=constants.PaceAdjust.Default,
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
            'PlayerID': player_id,
            'VsPlayerID': vs_player_id,
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
            'LastNGames': last_n_games,
        }
        self.api = NbaAPI(self._endpoint, self._params)

    def overall(self):
        """Splits comparison"""
        return self.api.get_result('Overall')

    def on_off_court(self):
        """Player1's splits with Player2 on and off the court"""
        return self.api.get_result('OnOffCourt')

    def shot_dist_overall(self):
        """Player1's shooting distance splits regardless of Player2"""
        return self.api.get_result('ShotDistanceOverall')

    def shot_dist_on_court(self):
        """Player1's shooting distance splits with Player2 on the court"""
        return self.api.get_result('ShotDistanceOnCourt')

    def shot_dist_off_court(self):
        """Player1's shooting distance splits with Player2 off the court"""
        return self.api.get_result('ShotDistanceOffCourt')

    def shot_area_overall(self):
        """Player1's shooting by area splits regardless of Player2"""
        return self.api.get_result('ShotAreaOverall')

    def shot_area_on_court(self):
        """Player1's shooting by area splits with Player2 on the court"""
        return self.api.get_result('ShotAreaOnCourt')

    def shot_area_off_court(self):
        """Player1's shooting by area splits with Player2 off the court"""
        return self.api.get_result('ShotAreaOffCourt')

    def player_info(self):
        return self.api.get_result('PlayerInfo')

    def vs_player_info(self):
        return self.api.get_result('VsPlayerInfo')
