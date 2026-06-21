import sqlite3

conn = sqlite3.connect("todo.db")


cur = conn.cursor()

# cur.execute("""CREATE TABLE todos (
#                id INTEGER PRIMARY KEY ,
#                 todo TEXT,
#                 is_completed INTEGER NOT NULL DEFAULT 0
#
#
#                )""")
