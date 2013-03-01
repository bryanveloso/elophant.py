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
        return get(uri, params={'key': self.key}).json()

    def get_summoner(self, summoner_name):
        return self._http_get('summoner', summoner_name)

    def get_mastery_pages(self, summoner_id):
        return self._http_get('mastery_pages', summoner_id)

    def get_rune_pages(self, summoner_id):
        return self._http_get('rune_pages', summoner_id)

    def get_recent_games(self, account_id):
        return self._http_get('recent_games', account_id)

    def get_summoner_names(self, summoner_ids):
        if isinstance(summoner_ids, list):
            summoner_ids = ','.join(str(x) for x in summoner_ids)
        return self._http_get('summoner_names', summoner_ids)

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

    def find_team(self, team_name):
        return self._http_get('find_team', team_name)

    def get_team_end_of_game_stats(self, team_id, game_id):
        return self._http_get('team', team_id, 'end_of_game_stats', game_id)

    def get_team_ranked_stats(self, team_id):
        return self._http_get('team_ranked_stats', team_id)
