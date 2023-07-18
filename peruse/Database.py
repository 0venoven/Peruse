import sqlite3
from sqlite3 import Error

class Database():
    def __init__(self, arg):
        super(Database,self).__init__()
        self.arg = arg

    def create_connection(db_path):
        conn = None
        try:
            conn = sqlite3.connect(db_path)
        except Error as e:
            print(e)

        return conn

    def create_table(conn, stmt):
        try:
            c = conn.cursor()
            c.execute(stmt)
        except Error as e:
            print(e)

    def main(db_path):
        create_result_table = """ CREATE TABLE IF NOT EXISTS result (
                                        SCAN_NO INTEGER PRIMARY KEY AUTOINCREMENT,
                                        PW_CRACKED TEXT NOT NULL,
                                        FINAL_SCORE INTEGER NOT NULL,
                                        DATE_TIME TEXT NOT NULL);"""
        conn = Database.create_connection(db_path)
        if conn is not None:
            Database.create_table(conn, create_result_table)
        else:
            print("Error! cannot create the database connection.")
    
    def get_results(db_path):
        conn = Database.create_connection(db_path)
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM result")
            return cur
        except Error as e:
            print("Error: failed to get scan results")
            print(e)
    
    def insert_result(db_path, pw_cracked, final_score):
        conn = Database.create_connection(db_path)
        try:
            cur = conn.cursor()
            cur.execute("INSERT INTO result (PW_CRACKED, FINAL_SCORE, DATE_TIME) VALUES (?, ?, datetime('now'))", (pw_cracked, final_score))
            conn.commit()
        except Error as e:
            print("Error: failed to insert scan result")
            print(e)
    
    def delete_result(db_path, scan_no):
        conn = Database.create_connection(db_path)
        try:
            cur = conn.cursor()
            cur.execute("DELETE FROM result WHERE SCAN_NO = ?", [scan_no])
            conn.commit()
        except Error as e:
            print("Error: failed to delete scan result")
            print(e)