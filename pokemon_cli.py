import sqlite3
import requests

DB_NAME = "pokemon.db"

# Function to initialize the database (run once)
def initialise_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pokemon (
            id INTEGER PRIMARY KEY, 
            name TEXT UNIQUE, 
            height INTEGER, 
            weight INTEGER, 
            type TEXT
        )
    """)
    conn.commit()
    conn.close()

# Function to fetch Pokémon data from PokéAPI
def fetch_pokemon_from_api(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        pokemon_id = data["id"]
        name = data["name"]
        height = data["height"]
        weight = data["weight"]
        types = ", ".join([t["type"]["name"] for t in data["types"]])

        return (pokemon_id, name, height, weight, types)
    else:
        print("❌ Pokémon not found!")
        return None

# Function to add Pokémon to the database
def add_pokemon(pokemon_data):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO pokemon VALUES (?, ?, ?, ?, ?)", pokemon_data)
        conn.commit()
        print(f"✅ {pokemon_data[1].capitalize()} added to database!")
    except sqlite3.IntegrityError:
        print("⚠️ This Pokémon is already in the database.")
    conn.close()

# Function to view all Pokémon
def view_all_pokemon():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pokemon")
    records = cursor.fetchall()
    conn.close()

    if records:
        print("\n📜 Stored Pokémon:")
        for row in records:
            print(f"ID: {row[0]}, Name: {row[1]}, Height: {row[2]}, Weight: {row[3]}, Type: {row[4]}")
    else:
        print("⚠️ No Pokémon found in the database.")

# Function to search for a Pokémon by ID or name
def search_pokemon(identifier):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    if identifier.isdigit():
        cursor.execute("SELECT * FROM pokemon WHERE id = ?", (int(identifier),))
    else:
        cursor.execute("SELECT * FROM pokemon WHERE name LIKE ?", (identifier.lower(),))

    record = cursor.fetchone()
    conn.close()

    if record:
        print(f"\n🔍 Found Pokémon: ID: {record[0]}, Name: {record[1]}, Height: {record[2]}, Weight: {record[3]}, Type: {record[4]}")
    else:
        print("❌ Pokémon not found.")

# Function to update Pokémon details
def update_pokemon(pokemon_id, new_height, new_weight, new_type):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE pokemon 
        SET height = ?, weight = ?, type = ? 
        WHERE id = ?
    """, (new_height, new_weight, new_type, pokemon_id))

    if cursor.rowcount > 0:
        print(f"✅ Pokémon with ID {pokemon_id} updated successfully!")
    else:
        print("❌ No Pokémon found with that ID.")

    conn.commit()
    conn.close()

# Function to delete a Pokémon by ID
def delete_pokemon(pokemon_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM pokemon WHERE id = ?", (pokemon_id,))

    if cursor.rowcount > 0:
        print(f"🗑️ Pokémon with ID {pokemon_id} deleted successfully!")
    else:
        print("❌ No Pokémon found with that ID.")

    conn.commit()
    conn.close()

# Main CLI Menu
def main_menu():
    initialise_database()

    while True:
        print("\n📌 Pokémon Database CLI")
        print("1️⃣ View all Pokémon")
        print("2️⃣ Search Pokémon by Name or ID")
        print("3️⃣ Add Pokémon from PokéAPI")
        print("4️⃣ Manually Add Pokémon")
        print("5️⃣ Update Pokémon")
        print("6️⃣ Delete Pokémon")
        print("7️⃣ Exit")

        choice = input("Select an option (1-7): ")

        if choice == "1":
            view_all_pokemon()
        elif choice == "2":
            identifier = input("Enter Pokémon Name or ID: ")
            search_pokemon(identifier)
        elif choice == "3":
            pokemon_name = input("Enter Pokémon name: ")
            data = fetch_pokemon_from_api(pokemon_name)
            if data:
                add_pokemon(data)
        elif choice == "4":
            pokemon_id = int(input("Enter Pokémon ID: "))
            name = input("Enter Pokémon name: ").lower()
            height = int(input("Enter Pokémon height: "))
            weight = int(input("Enter Pokémon weight: "))
            type_ = input("Enter Pokémon type(s) (comma-separated): ")
            add_pokemon((pokemon_id, name, height, weight, type_))
        elif choice == "5":
            pokemon_id = input("Enter Pokémon ID to update: ")
            new_height = input("Enter new height: ")
            new_weight = input("Enter new weight: ")
            new_type = input("Enter new type(s) (comma-separated): ")
            update_pokemon(int(pokemon_id), int(new_height), int(new_weight), new_type)
        elif choice == "6":
            pokemon_id = input("Enter Pokémon ID to delete: ")
            confirm = input(f"Are you sure you want to delete Pokémon ID {pokemon_id}? (yes/no): ")
            if confirm.lower() == "yes":
                delete_pokemon(int(pokemon_id))
        elif choice == "7":
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("⚠️ Invalid option. Please choose between 1-7.")

if __name__ == "__main__":
    main_menu()
