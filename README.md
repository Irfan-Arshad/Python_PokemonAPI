# Python_PokemonAPI
This Pokémon Database Integration System is a Python project that fetches Pokémon data from the PokéAPI, stores it in an SQLite database, and provides a simple command-line interface to perform CRUD operations. You can view, search, update, and delete Pokémon records, all while interacting with the data seamlessly.

# Database Structure
All of the Pokémon data fetched from the API is saved into an SQLite database. The main table, pokemon, includes the following columns:

id: A unique ID for each Pokémon (e.g., 1 for Bulbasaur).
name: The name of the Pokémon (e.g., "pikachu").
height: The Pokémon's height in decimeters (e.g., 4 for Pikachu).
weight: The Pokémon's weight in hectograms (e.g., 6 for Pikachu).
types: A list of types (e.g., "electric" for Pikachu).

# CRUD Functions
This system is built with modularity in mind, which means I’ve created functions that you can re-use for interacting with the database. Here are the main functions:

fetch_pokemon(pokemon_name_or_id): Fetches Pokémon data from the PokéAPI by name or ID.
store_pokemon(pokemon_name_or_id): Adds a new Pokémon record to the database.
view_pokemon(): Fetches a Pokémon record by its ID.
manage_pokemon(pokemon_id): Updates or deletes an existing Pokémon's data using its ID.

# Command-Line Interface (CLI)
The user-friendly CLI allows you to interact with your Pokémon database in several ways. Here’s what you can do:

View all records: Displays all the Pokémon stored in your database.
Search by Name or ID: Look up a specific Pokémon by its Name or ID.
Add from PokeAPI by name: Add a Pokémon by typing its name from API.
Manually add a Pokemon: Add your own custom pokemon.
Update a record: Change a Pokémon's information by providing its ID.
Delete a record: Remove a Pokémon from the database by its ID.
Exit: Close the program.
Once you’re done with one task, the system will ask you what to do next. It keeps looping until you choose to exit.
