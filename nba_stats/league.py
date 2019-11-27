"""League-wide stats"""

from nba_stats.nba_api import NbaAPI
from nba_stats import constants


class Lineups:
    """Stats for various lineups throughout the league"""
    _endpoint = 'leaguedashlineups'

    def __init__(
            self,
            group_quantity=constants.GroupQuantity.Default,
            season_type=constants.SeasonType.Default,
            measure_type=constants.MeasureType.Default,
            per_mode=constants.PerMode.Default,
            plus_minus=constants.PlusMinus.Default,
            pace_adjust=constants.PaceAdjust.Default,
            rank=constants.Rank.Default,
            season=constants.CURRENT_SEASON,
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
            last_n_games=constants.LastNGames.Default,
    ):
        self._params = {
            'GroupQuantity': group_quantity,
            'SeasonType': season_type,
            'MeasureType': measure_type,
            'PerMode': per_mode,
            'PlusMinus': plus_minus,
            'PaceAdjust': pace_adjust,
            'Rank': rank,
            'Season': season,
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

    def results(self):
        return self.api.get_result()


class TeamStats:
    """League-wide team stats."""
    _endpoint = 'leaguedashteamstats'

    def __init__(
            self,
            conference=constants.Conference.Default,
            date_from=constants.DateFrom.Default,
            date_to=constants.DateTo.Default,
            division=constants.Division.Default,
            game_scope=constants.Game_Scope.Default,
            game_segment=constants.GameSegment.Default,
            last_n_games=constants.LastNGames.Default,
            league_id=constants.League.Default,
            location=constants.Location.Default,
            measure_type=constants.MeasureType.Default,
            month=constants.Month.Default,
            opponent_team_id=constants.OpponentTeamID.Default,
            outcome=constants.Outcome.Default,
            playoff_round=constants.PlayoffRound.Default,
            pace_adjust=constants.PaceAdjust.Default,
            per_mode=constants.PerMode.Default,
            period=constants.Period.Default,
            player_experience=constants.PlayerExperience.Default,
            player_position=constants.PlayerPosition.Default,
            plus_minus=constants.PlusMinus.Default,
            rank=constants.Rank.Default,
            season=constants.CURRENT_SEASON,
            season_segment=constants.SeasonSegment.Default,
            season_type=constants.SeasonType.Default,
            shot_clock_range=constants.ShotClockRange.Default,
            starter_bench=constants.StarterBench.Default,
            team_id=constants.TeamID.Default,
            vs_conference=constants.VsConference.Default,
            vs_division=constants.VsDivision.Default,
    ):
        self._params = {
            'LeagueID': league_id,
            'SeasonType': season_type,
            'MeasureType': measure_type,
            'PerMode': per_mode,
            'PlusMinus': plus_minus,
            'PaceAdjust': pace_adjust,
            'Rank': rank,
            'Season': season,
            'PORound': playoff_round,
            'Outcome': outcome,
            'Location': location,
            'Month': month,
            'SeasonSegment': season_segment,
            'DateFrom': date_from,
            'DateTo': date_to,
            'OpponentTeamID': opponent_team_id,
            'VsConference': vs_conference,
            'VsDivision': vs_division,
            'TeamID': team_id,
            'Conference': conference,
            'Division': division,
            'GameSegment': game_segment,
            'Period': period,
            'ShotClockRange': shot_clock_range,
            'LastNGames': last_n_games,
            'GameScope': game_scope,
            'PlayerExperience': player_experience,
            'PlayerPosition': player_position,
            'StarterBench': starter_bench,
        }
        self.api = NbaAPI(self._endpoint, self._params)

    def results(self):
        return self.api.get_result()


class PlayerStats:
    """League-wide (all) player stats"""
    _endpoint = 'leaguedashplayerstats'

    def __init__(
            self,
            season_type=constants.SeasonType.Default,
            measure_type=constants.MeasureType.Default,
            per_mode=constants.PerMode.Default,
            plus_minus=constants.PlusMinus.Default,
            pace_adjust=constants.PaceAdjust.Default,
            rank=constants.Rank.Default,
            season=constants.CURRENT_SEASON,
            playoff_round=constants.PlayoffRound.Default,
            outcome=constants.Outcome.Default,
            location=constants.Location.Default,
            month=constants.Month.Default,
            season_segment=constants.SeasonSegment.Default,
            date_from=constants.DateFrom.Default,
            date_to=constants.DateTo.Default,
            opponent_team_id=constants.OpponentTeamID.Default,
            vs_conference=constants.VsConference.Default,
            vs_division=constants.VsDivision.Default,
            team_id=constants.TeamID.Default,
            conference=constants.Conference.Default,
            division=constants.Division.Default,
            game_segment=constants.GameSegment.Default,
            period=constants.Period.Default,
            shot_clock_range=constants.ShotClockRange.Default,
            last_n_games=constants.LastNGames.Default,
            game_scope=constants.Game_Scope.Default,
            player_experience=constants.PlayerExperience.Default,
            player_position=constants.PlayerPosition.Default,
            starter_bench=constants.StarterBench.Default,
            draft_year=constants.DraftYear.Default,
            draft_pick=constants.DraftPick.Default,
            college=constants.College.Default,
            country=constants.Country.Default,
            height=constants.Height.Default,
            weight=constants.Weight.Default,
    ):
        self._params = {
            'SeasonType': season_type,
            'MeasureType': measure_type,
            'PerMode': per_mode,
            'PlusMinus': plus_minus,
            'PaceAdjust': pace_adjust,
            'Rank': rank,
            'Season': season,
            'PORound': playoff_round,
            'Outcome': outcome,
            'Location': location,
            'Month': month,
            'SeasonSegment': season_segment,
            'DateFrom': date_from,
            'DateTo': date_to,
            'OpponentTeamID': opponent_team_id,
            'VsConference': vs_conference,
            'VsDivision': vs_division,
            'TeamID': team_id,
            'Conference': conference,
            'Division': division,
            'GameSegment': game_segment,
            'Period': period,
            'ShotClockRange': shot_clock_range,
            'LastNGames': last_n_games,
            'GameScope': game_scope,
            'PlayerExperience': player_experience,
            'PlayerPosition': player_position,
            'StarterBench': starter_bench,
            'DraftYear': draft_year,
            'DraftPick': draft_pick,
            'College': college,
            'Country': country,
            'Height': height,
            'Weight': weight,
        }
        self.api = NbaAPI(self._endpoint, self._params)

    def results(self):
        return self.api.get_result()


class PlayerTrackingStats:
    """Various player tracking stats such as catch and shoot tracking,
       speed and distance, post-ups, touches, etc.
    """
    _endpoint = 'leaguedashptstats'

    def __init__(
            self,
            league_id=constants.League.Default,
            season_type=constants.SeasonType.Default,
            player_or_team=constants.PlayerOrTeam.Default,
            per_mode=constants.PerMode.Default,
            season=constants.CURRENT_SEASON,
            playoff_round=constants.PlayoffRound.Default,
            outcome=constants.Outcome.Default,
            location=constants.Location.Default,
            month=constants.Month.Default,
            season_segment=constants.SeasonSegment.Default,
            date_from=constants.DateFrom.Default,
            date_to=constants.DateTo.Default,
            opponent_team_id=constants.OpponentTeamID.Default,
            vs_conference=constants.VsConference.Default,
            vs_division=constants.VsDivision.Default,
            team_id=constants.TeamID.Default,
            conference=constants.Conference.Default,
            division=constants.Division.Default,
            last_n_games=constants.LastNGames.Default,
            game_scope=constants.Game_Scope.Default,
            player_experience=constants.PlayerExperience.Default,
            player_position=constants.PlayerPosition.Default,
            pt_measure_type=constants.PtMeasureType.Default,
            starter_bench=constants.StarterBench.Default,
            draft_year=constants.DraftYear.Default,
            draft_pick=constants.DraftPick.Default,
            college=constants.College.Default,
            country=constants.Country.Default,
            height=constants.Height.Default,
            weight=constants.Weight.Default,
    ):

        self._params = {
            'LeagueID': league_id,
            'PtMeasureType': pt_measure_type,
            'SeasonType': season_type,
            'PlayerOrTeam': player_or_team,
            'PerMode': per_mode,
            'Season': season,
            'PORound': playoff_round,
            'Outcome': outcome,
            'Location': location,
            'Month': month,
            'SeasonSegment': season_segment,
            'DateFrom': date_from,
            'DateTo': date_to,
            'OpponentTeamID': opponent_team_id,
            'VsConference': vs_conference,
            'VsDivision': vs_division,
            'TeamID': team_id,
            'Conference': conference,
            'Division': division,
            'LastNGames': last_n_games,
            'GameScope': game_scope,
            'PlayerExperience': player_experience,
            'PlayerPosition': player_position,
            'StarterBench': starter_bench,
            'DraftYear': draft_year,
            'DraftPick': draft_pick,
            'College': college,
            'Country': country,
            'Height': height,
            'Weight': weight,
        }
        self.api = NbaAPI(self._endpoint, self._params)

    def results(self):
        return self.api.get_result()


class PlayerLeaders:
    """Season league leaders in various stats"""
    _endpoint = 'leagueleaders'

    def __init__(
            self,
            league_id=constants.League.Default,
            per_mode=constants.PerMode.Default,
            stat_category=constants.StatCategory.Default,
            season=constants.CURRENT_SEASON,
            season_type=constants.SeasonType.Default,
            scope=constants.Scope.Default,
    ):
        self._params = {
            'LeagueID': league_id,
            'PerMode': per_mode,
            'StatCategory': stat_category,
            'Season': season,
            'SeasonType': season_type,
            'Scope': scope,
        }
        self.api = NbaAPI(self._endpoint, self._params)

    def results(self):
        return self.api.get_result()
