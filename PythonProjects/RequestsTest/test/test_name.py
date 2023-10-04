import requests

import pytest

@pytest.mark.parametrize ('key, value', [("trainer_name", "Автотест"), ("id", "2451")])
def test_response_json (key, value):

    response = requests.get ('https://api.pokemonbattle.me:9104/trainers', params = {'trainer_id' : 2451})

    assert response.json()[key] == value