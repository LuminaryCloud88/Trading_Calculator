'''import sqlite3
import bcrypt

DB_PATH = "users.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL,
            subscribed INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

def add_user(username, password, subscribed=False):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("INSERT INTO users VALUES (?, ?, ?)", 
                (username, password, int(subscribed)))
    conn.commit()
    conn.close()

def get_user(username, password):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT username, subscribed FROM users WHERE username=? AND password=?", 
                (username, password))
    row = cur.fetchone()
    conn.close()
    if row:
        return {"username": row[0], "subscribed": bool(row[1])}
    return None

def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def check_password(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed)
'''