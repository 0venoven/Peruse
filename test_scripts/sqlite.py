import sqlite3
from sqlite3 import Error

class Database():
    def __init__(self, arg):
        super(Database,self).__init__()
        self.arg = arg

    def create_connection():
        conn = None
        try:
            conn = sqlite3.connect(r"results.db")
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

    def main():
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
                                        port_no INTEGER NOT NULL,
                                        pw_crakced BOOLEAN NOT NULL,
                                        FOREIGN KEY (host_id) REFERENCES host (host_id));"""

        conn = Database.create_connection()
        if conn is not None:
            Database.create_table(conn, create_scan_table)
            Database.create_table(conn, create_host_table)
            Database.create_table(conn, create_service_table)
        else:
            print("Error: cannot create the database connection.")
    
    def get_all_scans():
        conn = Database.create_connection()
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM scan")
            return cur
        except Error as e:
            print("Error: failed to get scan results")
            print(e)
    
    def get_hosts(scan_no):
        conn = Database.create_connection()
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM host WHERE scan_id = ?", [scan_no])
            return cur
        except Error as e:
            print("Error: failed to get host results")
            print(e)
    
    def get_services(host_no):
        conn = Database.create_connection()
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM service WHERE host_id = ?", [host_no])
            return cur
        except Error as e:
            print("Error: failed to get service results")
            print(e)
    
    def insert_scan(network_name):
        conn = Database.create_connection()
        try:
            cur = conn.cursor()
            # insert into scan table
            cur.execute("INSERT INTO scan (network_name, date_time) VALUES (?, datetime('now','localtime'))", [network_name])
            conn.commit()
            # get latest scan no
            scan_id = cur.execute("SELECT MAX(scan_id) FROM scan").fetchone()[0]
            # then check if scan_no is not none and insert into host table
            # we need a for loop for this part for each host
            host_ip = "192.168.0.108" # this is a placeholder for now
            cur.execute("INSERT INTO host (scan_id, host_ip) VALUES (?, ?)", [scan_id, host_ip])
            conn.commit()
            # get latest host no
            host_id = cur.execute("SELECT MAX(host_id) FROM host").fetchone()[0]
            # then check if host_id is not none and insert into service table
            # we need a for loop for this part for each service
            # the vars below are placeholders for now
            service_name = "ssh"
            port_no = 22
            pw_cracked = False
            cur.execute("INSERT INTO service (host_id, service_name, port_no, pw_crakced) VALUES (?, ?, ?, ?)", [host_id, service_name, port_no, pw_cracked])
            conn.commit()
        except Error as e:
            print("Error: failed to insert scan result")
            print(e)
    
    def delete_result(scan_id):
        conn = Database.create_connection()
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
    
    def get_all_hosts(): # for testing purposes
        conn = Database.create_connection()
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM host")
            return cur
        except Error as e:
            print("Error: failed to get host results")
            print(e)
    
    def get_all_services(): # for testing purposes
        conn = Database.create_connection()
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM service")
            return cur
        except Error as e:
            print("Error: failed to get service results")
            print(e)

Database.main()
Database.insert_scan("wifi name")
Database.insert_scan("wifi name")
Database.delete_result(2)
Database.insert_scan("wifi name")
final = Database.get_all_scans()
final2 = Database.get_all_hosts()
final3 = Database.get_all_services()
for row in final:
    print(row)
print("-------------------")
for row in final2:
    print(row)
print("-------------------")
for row in final3:
    print(row)
"""
key the following into https://dbdiagram.io/d to get the ER diagram:
TABLE scan {
    scan_id INTEGER [pk, increment]
    network_name TEXT
    date_time TEXT
}

TABLE host{
    host_id INTEGER [pk, increment]
    scan_id INTEGER
    host_ip TEXT
}

TABLE service{
    service_id INTEGER [pk, increment]
    host_id INTEGER
    service_name TEXT
    port_no INT
    pw_crakced BOOLEAN
}

Ref: host.scan_id > scan.scan_id

Ref: service.host_id > host.host_id
"""