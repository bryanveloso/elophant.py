# -*- coding: utf-8 -*-
import py, pytest


@pytest.fixture(scope='module')
def api():
    from elophant import Elophant
    api = Elophant(key='KhsmDi7vcb5QM7Sh6BQY', region='na')
    return api

@pytest.fixture(scope='module')
def data():
    return {
        'account_id': 32736337,
        'summoner_name': 'Crs Rhux',
        'summoner_id': 19959767,
        'team_id': 'TEAM-7362d288-7d5c-45be-a3d6-4e39bd925679',
        'team_name': 'Crs'
    }

@pytest.mark.usefixtures('api', 'data')
class TestClass:
    def test_get_summoner(self, api, data):
        call = api.get_summoner(data['summoner_name'])
        assert call['success']
        assert call['data']['name'] == data['summoner_name']

    def test_get_mastery_pages(self, api, data):
        call = api.get_mastery_pages(data['summoner_id'])
        assert call['success']

    def test_get_rune_pages(self, api, data):
        call = api.get_rune_pages(data['summoner_id'])
        assert call['success']

    def test_get_recent_games(self, api, data):
        call = api.get_recent_games(data['account_id'])
        assert call['success']

    def test_get_summoner_names(self, api):
        call = api.get_summoner_names([19959767, 34292665])
        assert call['success']
        assert call['data'][0] == 'Crs Rhux'
        assert call['data'][1] == 'Bischu'

    def test_get_leagues(self, api, data):
        call = api.get_leagues(data['summoner_id'])
        assert call['success']

    def test_get_ranked_stats(self, api, data):
        call = api.get_ranked_stats(data['account_id'])
        assert call['success']

    def test_get_summoner_team_info(self, api, data):
        call = api.get_summoner_team_info(data['summoner_id'])
        assert call['success']

    def test_get_team(self, api, data):
        call = api.get_team(data['team_id'])
        assert call['success']

    def test_find_team(self, api, data):
        call = api.find_team(data['team_name'])
        assert call['success']

    def test_get_team_ranked_stats(self, api, data):
        call = api.get_team_ranked_stats(data['team_id'])
        assert call['success']
