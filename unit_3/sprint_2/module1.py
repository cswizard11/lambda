import sqlite3

def connect_to_db(db="rpg_db.sqlite3"):
    conn = sqlite3.connect(db)
    return conn

def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()

ALL_CHARS = '''
    SELECT COUNT(*)
    FROM charactercreator_character;
'''

ITEMS = '''
    SELECT COUNT(*)
    FROM armory_item
'''

CHAR_ITEMS = '''
    SELECT character_id, count(*)
    FROM charactercreator_character_inventory
	GROUP BY character_id
	LIMIT 20;
'''

if __name__ == '__main__':
    conn = connect_to_db()
    curs = conn.cursor()
    num_chars = execute_query(curs, ALL_CHARS)
    num_items = execute_query(curs, ITEMS)
    character_items = execute_query(curs, CHAR_ITEMS)
    print(num_chars)
    print(num_items)
    print(character_items)
    avg_items = 0
    for i in character_items:
        avg_items += i[1]

    print(avg_items/len(num_items))