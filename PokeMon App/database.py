import sqlite3

# Connect to SQLite (creates 'pokemon.db' if not exists)
conn = sqlite3.connect("pokemon.db")
cursor = conn.cursor()

# Create table for storing Pokémon data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS pokemon (
        id INTEGER PRIMARY KEY,
        name TEXT UNIQUE,
        height INTEGER,
        weight INTEGER,
        type TEXT
    )
''')

conn.commit()
conn.close()

print("Database and table created successfully.")
