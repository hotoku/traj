import sqlite3

dbname = 'db.sqlite'

with sqlite3.connect(dbname) as conn:
    c = conn.cursor()
    c.executescript("""

insert into 
positions(user_id, lattitude, longtitude)
values(1, 35.681382, 139.76608399999998);

insert into 
positions(user_id, lattitude, longtitude)
values(2, 35.681382, 139.76608399999998);

insert into 
positions(user_id, lattitude, longtitude)
values(2, 35.674596, 139.762013);

""")
    conn.commit()
