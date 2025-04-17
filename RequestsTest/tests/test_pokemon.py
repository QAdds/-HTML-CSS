import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '0922c1ebd542fe37ef7309b7c86c7e97'
HEADER ={'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TREAINER_ID = 32884

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons',params = {'treainer_id' : TREAINER_ID})
    assert response.status_code == 200

def test_status_code_n():
    response = requests.get(url = f'{URL}/trainers',params = {'treainer_id' : TREAINER_ID})
    assert response.status_code == 200 #проверочный

def test_trainer_name():
    response_get = requests.get(url = f'{URL}/me', headers=HEADER)
    assert response_get.json()["data"][0]["trainer_name"] == "Popkorn"




