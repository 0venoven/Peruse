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
            conn.execute("PRAGMA foreign_keys = 1")
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
        create_scan_table = """ CREATE TABLE IF NOT EXISTS scan (
                                        scan_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        network_name TEXT NOT NULL,
                                        date_time TEXT NOT NULL);"""
        create_host_table = """ CREATE TABLE IF NOT EXISTS host (
                                        host_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        scan_id INTEGER NOT NULL,
                                        host_ip TEXT NOT NULL,
                                        FOREIGN KEY (scan_id) REFERENCES scan (scan_id));"""
        create_service_table = """ CREATE TABLE IF NOT EXISTS service (
                                        service_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        host_id INTEGER NOT NULL,
                                        service_name TEXT NOT NULL,
                                        port_no INT NOT NULL,
                                        pw_crakced BOOLEAN NOT NULL,
                                        FOREIGN KEY (host_id) REFERENCES host (host_id));"""
        
        conn = Database.create_connection(db_path)
        if conn is not None:
            Database.create_table(conn, create_scan_table)
            Database.create_table(conn, create_host_table)
            Database.create_table(conn, create_service_table)
        else:
            print("Error! cannot create the database connection.")
    
    def get_all_scans(db_path):
        conn = Database.create_connection(db_path)
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM scan")
            return cur
        except Error as e:
            print("Error: failed to get scan results")
            print(e)
    
    def get_hosts(db_path, scan_no):
        conn = Database.create_connection(db_path)
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM host WHERE scan_id = ?", [scan_no])
            return cur
        except Error as e:
            print("Error: failed to get host results")
            print(e)
    
    def get_services(db_path, host_no):
        conn = Database.create_connection(db_path)
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM service WHERE host_id = ?", [host_no])
            return cur
        except Error as e:
            print("Error: failed to get service results")
            print(e)

    def insert_scan(db_path, network_name):
        # prob nd to edit this fn later
        # maybe accept more params (those that are placeholders for now)
        conn = Database.create_connection(db_path)
        try:
            cur = conn.cursor()
            # insert into scan table
            cur.execute("INSERT INTO scan (network_name, date_time) VALUES (?, datetime('now','localtime'))", [network_name])
            conn.commit()
            # get latest scan no
            scan_id = cur.execute("SELECT MAX(scan_id) FROM scan").fetchone()[0]
            # insert each host into host table
            host_ip = "192.168.0.108" # this is a placeholder for now
            cur.execute("INSERT INTO host (scan_id, host_ip) VALUES (?, ?)", [scan_id, host_ip])
            conn.commit()
            # get latest host no
            host_id = cur.execute("SELECT MAX(host_id) FROM host").fetchone()[0]
            # insert each service into service table
            # the vars below are placeholders for now
            service_name = "ssh"
            port_no = 22
            pw_cracked = False
            cur.execute("INSERT INTO service (host_id, service_name, port_no, pw_crakced) VALUES (?, ?, ?, ?)", [host_id, service_name, port_no, pw_cracked])
            conn.commit()
        except Error as e:
            print("Error: failed to insert scan result")
            print(e)
    
    def delete_result(db_path, scan_id):
        conn = Database.create_connection(db_path)
        try:
            cur = conn.cursor()
            # get corresponding list of host ids
            host_ids = cur.execute("SELECT host_id FROM host WHERE scan_id = ?", [scan_id]).fetchall() # this returns a list of tuples
            # delete all services with host_id in host_ids
            for host_id in host_ids:
                cur.execute("DELETE FROM service WHERE host_id = ?", [host_id[0]])
            conn.commit()
            # delete all hosts with scan_id
            cur.execute("DELETE FROM host WHERE scan_id = ?", [scan_id])
            # delete scan with scan_id
            cur.execute("DELETE FROM scan WHERE scan_id = ?", [scan_id])
            conn.commit()
        except Error as e:
            print("Error: failed to delete scan result")
            print(e)