import sqlite3

dbname = 'db.sqlite'

with sqlite3.connect(dbname) as conn:
    c = conn.cursor()
    c.executescript("""
create table positions(
  id primary key, 
  user_id text,
  lattitude real,
  longtitude real
);
""")
    conn.commit()
