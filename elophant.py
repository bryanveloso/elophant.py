# -*- coding: utf-8 -*-

from requests import get

DEFAULT_ELOPHANT_URL = 'http://api.elophant.com/v2'


class Elophant(object):
    """
    The API wrapper for Elophant(.com).

    """
    ELOPHANT_URL = DEFAULT_ELOPHANT_URL

    def __init__(self, key=None, region=None):
        self.key = key
        self.region = region

    def _http_get(self, *parts):
        uriparts = [self.ELOPHANT_URL, self.region]
        for uripart in parts:
            uriparts.append(str(uripart))
        uri = '/'.join(uriparts)
        print uri
        return get(uri, params={'key': self.key}).json()

    def summoner(self, summoner_name):
        return self._http_get('summoner', summoner_name)

    # GET mastery_pages(int summonerId)
    # Returns an array with each mastery book page and subsequent talent point entries for a specific summoner.

    # GET rune_pages(int summonerId)
    # Returns an array with each rune page and subsequent runes for a specific summoner.

    # GET recent_games(int accountId)
    # Returns the statistics for a summoner's 10 most recent games.

    # GET summoner_names(CSV array summonerIds)
    # Returns an array of summoner names in the same order as provided in the parameter summonerIds.

    # GET leagues(int summonerId)
    # Returns the current League for the requested summonerId, including all players within the League.

    # GET ranked_stats(int accountId, string season)
    # Returns every statistic for every champion accumulated from all ranked game types for a specified summoner and season.

    # GET summoner_team_info(int summonerId)
    # Returns all team info regarding the specified summoner, including team overviews and all of the teams the summoner has created.

    # GET in_progress_game_info(string summonerName)
    # Returns the player information for both teams, bans (if draft or ranked), and observer information.

    # GET team(string teamId)
    # Returns a brief overview of a team, including gameType dependent Elos, the current roster, and basic match history statistics.

    # GET find_team(string tagOrName)
    # Returns a brief overview of a team, including gameType dependent Elos, the current roster, and basic match history statistics.

    # GET team_end_of_game_stats(string teamId, double gameId)
    # Returns very detailed statistics about the specified match.

    # GET team_ranked_stats(string teamId)
    # Returns each team member's statistics for the specified team. This call provides very similar results to getRankedStats.
