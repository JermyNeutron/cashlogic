import sqlite3

def create_table(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS config (
            script_name TEXT PRIMARY KEY,
            status TEXT
        )    
    ''')
    
def insert_config(cursor, script_name, status):
    cursor.execute('INSERT OR REPLACE INTO config (script_name, status) VALUES (?, ?)', (script_name, status))

def get_config(cursor, script_name):
    cursor.execute('SELECT status FROM config WHERE script_name = ?', (script_name,))
    result = cursor.fetchone()
    return result[0] if result else None