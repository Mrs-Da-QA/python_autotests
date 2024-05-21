import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN =  '6a012dd463c01f331265c080674268fc'
HEADER = {'Content-Type' :'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '2363'
body_pokemon ={
    "pokemon_id": "27942",
    "name": "Филини2",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

def test_status_code():
    response = requests.get(url =f'{URL}/pokemons',params={'trainer_id':TRAINER_ID})
    assert response.status_code==200

def test_part_of_pespons():
    response_get = requests.get(url =f'{URL}/pokemons',params={'trainer_id':TRAINER_ID})
    assert response_get.json()["data"][0]["name"] == 'Филини2'

@pytest.mark.parametrize('key,value',[('name','Филини2'),('trainer_id',TRAINER_ID),('id','28010')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url =f'{URL}/pokemons',params={'trainer_id':TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value

def test_trainers():
    response_get = requests.get(url=f'{URL}/trainers', params={'trainer_id':TRAINER_ID})
    assert response_get.status_code==200
    assert response_get.json()["data"][0]["trainer_name"]=='Филя'




