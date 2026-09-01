import sqlite3
from datetime import datetime
from pathlib import Path
DB_PATH=Path(__file__).resolve().parents[1]/'wingman.db'
def _connect():
    c=sqlite3.connect(DB_PATH); c.row_factory=sqlite3.Row; return c
def initialize_database():
    c=_connect()
    c.execute('CREATE TABLE IF NOT EXISTS saved_items(id INTEGER PRIMARY KEY AUTOINCREMENT,created_at TEXT NOT NULL,category TEXT NOT NULL,title TEXT NOT NULL,content TEXT NOT NULL)')
    c.execute('CREATE TABLE IF NOT EXISTS history(id INTEGER PRIMARY KEY AUTOINCREMENT,created_at TEXT NOT NULL,input_type TEXT NOT NULL,source_preview TEXT NOT NULL,vibe TEXT,confidence INTEGER)')
    c.commit(); c.close()
def save_item(category,title,content):
    c=_connect(); c.execute('INSERT INTO saved_items(created_at,category,title,content) VALUES(?,?,?,?)',(datetime.now().isoformat(timespec='seconds'),category,title,content)); c.commit(); c.close()
def get_saved():
    c=_connect(); rows=c.execute('SELECT * FROM saved_items ORDER BY id DESC').fetchall(); c.close(); return rows
def delete_saved(item_id):
    c=_connect(); c.execute('DELETE FROM saved_items WHERE id=?',(int(item_id),)); c.commit(); c.close()
def save_history(input_type,source_preview,vibe,confidence):
    c=_connect(); c.execute('INSERT INTO history(created_at,input_type,source_preview,vibe,confidence) VALUES(?,?,?,?,?)',(datetime.now().isoformat(timespec='seconds'),input_type,str(source_preview)[:700],vibe,int(confidence))); c.commit(); c.close()
def get_history(limit=50):
    c=_connect(); rows=c.execute('SELECT * FROM history ORDER BY id DESC LIMIT ?',(int(limit),)).fetchall(); c.close(); return rows
initialize_database()
