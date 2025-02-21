import sqlite3
from datetime import datetime

conn = sqlite3.connect("access_logs.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    access_time TEXT,
    status TEXT
)
""")

def log_entry(name, status):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO logs (name, access_time, status) VALUES (?, ?, ?)", (name, timestamp, status))
    conn.commit()
