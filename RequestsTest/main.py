import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '0922c1ebd542fe37ef7309b7c86c7e97'
HEADER ={'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
body_registration ={
    "trainer_token": TOKEN,
    "email": "klimenkodenis439@gmail.com",
    "password": "1234QWERTY"
}

body_new = {
    "name": "Бульбазавр",
    "photo_id": 261
}

body_name ={
    "pokemon_id": "281108",
    "name": "ПРЯНИК",
    "photo_id": 263
}

body_pokeball={
    "pokemon_id": "290569"
}
'''response=requests.post(url=f'{URL}/trainers/reg', headers=HEADER, json = body_registration)
print(response.text)'''



'''response=requests.post(url=f'{URL}/pokemons', headers=HEADER, json = body_new)
print(response.text)'''

'''response=requests.put(url=f'{URL}/pokemons', headers=HEADER, json = body_name)
print(response.text)'''


response=requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json = body_pokeball)
print(response.text)