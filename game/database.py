import sqlite3

DB_PATH = "../database/playerData.db"

def createTable():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS player (
        name TEXT,
        hp INTEGER,
        xp INTEGER
    )''')
    conn.commit()
    conn.close()
    

def savePlayer(player):
    createTable()
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("DELETE FROM player")
    c.execute("INSERT INTO player VALUES (?, ?, ?)", 
              (player['name'], player['hp'], player['xp']))
    conn.commit()
    conn.close()

def loadPlayer():
    createTable()
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM player LIMIT 1")
    row = c.fetchone()
    conn.close()
    if row:
        return {"name": row[0], "hp": row[1], "xp": row[2]}
    return None