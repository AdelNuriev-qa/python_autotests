import requests

import pytest


def test_status_code ():

    response = requests.get ('https://api.pokemonbattle.me:9104/trainers')

    assert response.status_code == 200

