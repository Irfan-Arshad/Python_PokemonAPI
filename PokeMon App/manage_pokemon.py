import sqlite3

# Function to update Pokémon details
def update_pokemon(pokemon_id, new_height, new_weight, new_type):
    conn = sqlite3.connect("pokemon.db")
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE pokemon 
        SET height = ?, weight = ?, type = ? 
        WHERE id = ?
    """, (new_height, new_weight, new_type, pokemon_id))

    if cursor.rowcount > 0:
        print(f"✅ Pokémon with ID {pokemon_id} updated successfully!")
    else:
        print(f"❌ No Pokémon found with ID {pokemon_id}.")

    conn.commit()
    conn.close()

# Function to delete a Pokémon by ID
def delete_pokemon(pokemon_id):
    conn = sqlite3.connect("pokemon.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM pokemon WHERE id = ?", (pokemon_id,))

    if cursor.rowcount > 0:
        print(f"🗑️ Pokémon with ID {pokemon_id} deleted successfully!")
    else:
        print(f"❌ No Pokémon found with ID {pokemon_id}.")

    conn.commit()
    conn.close()

# User menu for updating or deleting Pokémon
if __name__ == "__main__":
    choice = input("Do you want to Update (1) or Delete (2) a Pokémon? ")

    if choice == "1":
        pokemon_id = input("Enter Pokémon ID to update: ")
        new_height = input("Enter new height: ")
        new_weight = input("Enter new weight: ")
        new_type = input("Enter new type (comma-separated if multiple): ")

        update_pokemon(int(pokemon_id), int(new_height), int(new_weight), new_type)

    elif choice == "2":
        pokemon_id = input("Enter Pokémon ID to delete: ")
        confirm = input(f"Are you sure you want to delete Pokémon ID {pokemon_id}? (yes/no): ")

        if confirm.lower() == "yes":
            delete_pokemon(int(pokemon_id))
        else:
            print("❌ Deletion cancelled.")

    else:
        print("Invalid choice.")
