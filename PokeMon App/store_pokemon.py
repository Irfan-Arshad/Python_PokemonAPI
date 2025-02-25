import sqlite3
from fetch_pokemon import fetch_pokemon

# Function to insert Pokémon data into SQLite database
def store_pokemon(pokemon_name_or_id):
    # Fetch data from PokéAPI
    pokemon_data = fetch_pokemon(pokemon_name_or_id)
    
    if not pokemon_data:
        print("No data found. Cannot store in database.")
        return
    
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect("pokemon.db")
        cursor = conn.cursor()

        # Insert Pokémon data (ignore if already exists)
        cursor.execute('''
            INSERT OR IGNORE INTO pokemon (id, name, height, weight, type) 
            VALUES (?, ?, ?, ?, ?)
        ''', pokemon_data)

        # Commit changes and close the connection
        conn.commit()
        conn.close()

        print(f"Pokémon {pokemon_data[1]} (ID: {pokemon_data[0]}) stored successfully.")

    except sqlite3.Error as e:
        print(f"Database error: {e}")

# Test storing Pokémon
if __name__ == "__main__":
    pokemon = input("Enter Pokémon name or ID to store: ")
    store_pokemon(pokemon)
