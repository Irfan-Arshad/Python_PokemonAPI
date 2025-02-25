import requests
import sqlite3

# Function to fetch Pokémon data from PokéAPI
def fetch_pokemon(pokemon_name_or_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name_or_id}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise error if request fails
        data = response.json()

        # Extract required details
        pokemon_id = data["id"]
        name = data["name"]
        height = data["height"]
        weight = data["weight"]
        types = ", ".join(t["type"]["name"] for t in data["types"])

        return (pokemon_id, name, height, weight, types)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

# Test fetching Pokémon data
if __name__ == "__main__":
    pokemon = input("Enter Pokémon name or ID: ")
    data = fetch_pokemon(pokemon)

    if data:
        print("Fetched Pokémon Data:", data)
