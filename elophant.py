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

    def get_summoner(self, summoner_name):
        return self._http_get('summoner', summoner_name)

    def get_mastery_pages(self, summoner_id):
        return self._http_get('mastery_pages', summoner_id)

    def get_rune_pages(self, summoner_id):
        return self._http_get('rune_pages', summoner_id)

    def get_recent_games(self, account_id):
        return self._http_get('recent_games', account_id)

    # GET summoner_names(CSV array summonerIds)
    # Returns an array of summoner names in the same order as provided in the parameter summonerIds.

    def get_leagues(self, summoner_id):
        return self._http_get('leagues', summoner_id)

    def get_ranked_stats(self, account_id, season='current'):
        return self._http_get('ranked_stats', account_id, season)

    def get_summoner_team_info(self, summoner_id):
        return self._http_get('summoner_team_info', summoner_id)

    def get_in_progress_game_info(self, summoner_name):
        return self._http_get('in_progress_game_info', summoner_name)

    def get_team(self, team_id):
        return self._http_get('team', team_id)

    # GET find_team(string tagOrName)
    # Returns a brief overview of a team, including gameType dependent Elos, the current roster, and basic match history statistics.

    # GET team_end_of_game_stats(string teamId, double gameId)
    # Returns very detailed statistics about the specified match.

    # GET team_ranked_stats(string teamId)
    # Returns each team member's statistics for the specified team. This call provides very similar results to getRankedStats.
