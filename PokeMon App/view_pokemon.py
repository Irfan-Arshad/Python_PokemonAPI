import sqlite3

# Function to display all Pokémon in the database
def view_all_pokemon():
    conn = sqlite3.connect("pokemon.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM pokemon")
    records = cursor.fetchall()

    conn.close()

    if records:
        print("\nStored Pokémon:")
        for row in records:
            print(f"ID: {row[0]}, Name: {row[1]}, Height: {row[2]}, Weight: {row[3]}, Type: {row[4]}")
    else:
        print("No Pokémon found in the database.")

# Function to search for a Pokémon by ID or name
def search_pokemon(identifier):
    conn = sqlite3.connect("pokemon.db")
    cursor = conn.cursor()

    if identifier.isdigit():  # If input is a number, search by ID
        cursor.execute("SELECT * FROM pokemon WHERE id = ?", (int(identifier),))
    else:  # Otherwise, search by name
        cursor.execute("SELECT * FROM pokemon WHERE name LIKE ?", (identifier.lower(),))

    record = cursor.fetchone()
    conn.close()

    if record:
        print(f"\nFound Pokémon:")
        print(f"ID: {record[0]}, Name: {record[1]}, Height: {record[2]}, Weight: {record[3]}, Type: {record[4]}")
    else:
        print("No Pokémon found with that ID or name.")

# Test the functions
if __name__ == "__main__":
    choice = input("View all Pokémon (1) or Search by Name/ID (2)? ")
    if choice == "1":
        view_all_pokemon()
    elif choice == "2":
        identifier = input("Enter Pokémon Name or ID: ")
        search_pokemon(identifier)
    else:
        print("Invalid choice.")
