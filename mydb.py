import sqlite3

class News:
    def __init__(self):
        self.con = sqlite3.connect('test.db')
        self.cur = self.con.cursor()

    def create_table(self):
        #self.cur.execute("""DROP TABLE newssdb""")
       self.cur.execute("""REATE TABLE IF NOT EXISTS newsdb(
       date DATE PRIMARY KEY,
       category TEXT,
       newstext TEXT,
       title TEXT,
       authors TEXT,
       keyword TEXT,
       link TEXT
        )""")

    def insert(self, item):
        self.cur.execute("""INSERT OR IGNORE INTO newsdb VALUES(?,?,?,?,?,?)""",
                item)
        self.con.commit()

