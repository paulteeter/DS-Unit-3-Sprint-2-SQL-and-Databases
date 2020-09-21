import psycopg2

DB_NAME = 'afmpwomg'
DB_USER = 'afmpwomg'
DB_PASS = 'm-gwVX4taX1mR-elkxVqPyfeTRnEKE0i'
DB_HOST = 'lallah.db.elephantsql.com'

conn = psycopg2.connect(dbname=DB_NAME,
                        user=DB_USER,
                        password=DB_PASS,
                        host=DB_HOST)

cursor = conn.cursor()

cursor.execute('SELECT * FROM test_table;')

results = cursor.fetchall()

#############
import sqlite3
sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_cursor = sl_conn.cursor()
characters = sl_cursor.execute('SELECT * FROM charactercreator_character').fetchall()

# Create table in PostGres and insert data:

create_character_table_query = '''
CREATE TABLE IF NOT EXISTS rpg_characters (
    character_id SERIAL PRIMARY KEY,
    name VARCHAR(30),
    level INT,
    exp INT,
    hp INT,
    strength INT, 
    intelligence INT,
    dexterity INT,
    wisdom INT
)
'''

cursor.execute(create_character_table_query)
conn.commit()

# for character in characters:
#     insert_query = f'''INSERT INTO rpg_characters
#     (character_id, name, level, exp, hp, strength, intelligence, dexterity, wisdom) VALUES
#     {character}
#     '''
#     cursor.execute(insert_query)

# conn.commit()


# # faster case to insert:

big_query = f'''INSERT INTO rpg_characters
    (character_id, name, level, exp, hp, strength, intelligence, dexterity, wisdom) VALUES'''

for character in characters:
    big_query += f' {character},'

cursor.execute(big_query.strip(','))
conn.commit()