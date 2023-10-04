import requests

host = "https://api.pokemonbattle.me:9104"

token = "17811508d944ae94752bb5e64c668bea"

'''response_pokemon = requests.post (f'{host}/pokemons', json = {
    
    "name": "Крепыш",
    "photo": "https://dolnikov.ru/pokemons/albums/050.png"

}, headers = {"content_type" : "application.json", "trainer_token" : "17811508d944ae94752bb5e64c668bea"})

print (response_pokemon.text)'''

'''response_name = requests.put (f'{host}/pokemons', json = {

    "pokemon_id": "11812",
    "name": "Силач",
    "photo": "https://dolnikov.ru/pokemons/albums/088.png"

}, headers = {"content_type" : "application.json", "trainer_token" : "17811508d944ae94752bb5e64c668bea"})

print (response_name.text)'''

response_pokeball = requests.post (f'{host}/trainers/add_pokeball', json = {

    "pokemon_id": "11812"

}, headers = {"content_type" : "application.json", "trainer_token" : "17811508d944ae94752bb5e64c668bea"})

print (response_pokeball.text)