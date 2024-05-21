import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN =  '6a012dd463c01f331265c080674268fc'
HEADER = {'Content-Type' :'application/json', 'trainer_token': TOKEN}
body_pokemon ={
    "pokemon_id": "27942",
    "name": "Филини2",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

body_pokebol = {
    "pokemon_id": "28008"
}   

response_create = requests.post(url=f'{URL}/pokemons',headers = HEADER, json = body_pokemon)
print(response_create.text)


response_new=requests.put(url =f'{URL}/pokemons',headers= HEADER, json= body_pokemon)
print(response_new.text)

respons_pokebol = requests.post(url =f'{URL}/trainers/add_pokeball',headers=HEADER,json=body_pokebol)
print(respons_pokebol.text)









