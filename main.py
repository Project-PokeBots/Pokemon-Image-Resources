import requests
from pokemonnames import pokemon_names

for pokemon in range(898):
    with open(f"FILEPATH/{pokemon}.png", "wb+") as f:
        f.write(requests.get(f"https://pokemonimageurl{pokemon}.png").content)
        # or {pokemon_names[pokemon].lower()} for name conversion
        f.close()
        print(pokemon)

print("DONE")