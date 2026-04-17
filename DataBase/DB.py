import sqlite3

class DB:
    def __init__(self):
        self.start_connection()

    def start_connection(self):
        self.con = sqlite3.connect("FEP.db")
        self.cursor = self.con.cursor()

    def close_connection(self):
        self.con.close()




