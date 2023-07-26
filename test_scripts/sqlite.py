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
                                        device_type TEXT NOT NULL,
                                        mac_address TEXT,
                                        vendor TEXT,
                                        device_status TEXT NOT NULL,
                                        FOREIGN KEY (scan_id) REFERENCES scan (scan_id));"""
        create_service_table = """ CREATE TABLE IF NOT EXISTS service (
                                        service_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        host_id INTEGER NOT NULL,
                                        service_name TEXT NOT NULL,
                                        service_port INTEGER NOT NULL,
                                        state TEXT NOT NULL,
                                        software_product TEXT,
                                        service_version TEXT,
                                        version_information TEXT,
                                        cpe TEXT,
                                        script TEXT,
                                        pw_cracked TEXT,
                                        recommendation TEXT,
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
    
    def insert_scan(network_name, scan_dict):
        conn = Database.create_connection()
        try:
            cur = conn.cursor()
            # insert into scan table
            cur.execute("INSERT INTO scan (network_name, date_time) VALUES (?, ?)", [network_name, scan_dict['nmap']['scanstats']['timestr']])
            conn.commit()
            # get latest scan no
            scan_id = cur.execute("SELECT MAX(scan_id) FROM scan").fetchone()[0]
            # insert into host table
            for host in scan_dict['scan']:
                device_ip = scan_dict['scan'][host]['addresses']['ipv4']

                # Device Type
                if 'osmatch' in scan_dict['scan'][host]:
                    device_type = scan_dict['scan'][host]['osmatch'][0]['name']
                else:
                    device_type = "N.A."

                # Mac Address
                if 'mac' in scan_dict['scan'][host]['addresses']:
                    mac_address = scan_dict['scan'][host]['addresses']['mac']
                else:
                    mac_address = "N.A."

                # Vendor
                if 'vendor' in scan_dict['scan'][host]:
                    if scan_dict['scan'][host]['vendor'] == {}:
                        vendor = "N.A."
                    else:
                        vendor = scan_dict['scan'][host]['vendor'][mac_address]

                # Device Status remove brackets
                device_status = scan_dict['scan'][host]['status']['state'] + " due to " + scan_dict['scan'][host]['status']['reason']

                # insert into host table
                cur.execute("INSERT INTO host (scan_id, host_ip, device_type, mac_address, vendor, device_status) VALUES (?, ?, ?, ?, ?, ?)", [scan_id, device_ip, device_type, mac_address, vendor, device_status])
                conn.commit()

                if 'tcp' in scan_dict['scan'][host]:
                    # get latest host no
                    host_id = cur.execute("SELECT MAX(host_id) FROM host").fetchone()[0]

                    for service in scan_dict['scan'][host]['tcp']:
                        # Service Name
                        service_name = scan_dict['scan'][host]['tcp'][service]['name']

                        # Service Port
                        service_port = service

                        # State
                        state = scan_dict['scan'][host]['tcp'][service]['state']

                        # Software Product
                        if 'product' in scan_dict['scan'][host]['tcp'][service]:
                            software_product = scan_dict['scan'][host]['tcp'][service]['product']
                        else:
                            software_product = "N.A."

                        # Service Version
                        if 'version' in scan_dict['scan'][host]['tcp'][service]:
                            service_version = scan_dict['scan'][host]['tcp'][service]['version']
                        else:
                            service_version = "N.A."

                        # version information
                        if 'extrainfo' in scan_dict['scan'][host]['tcp'][service]:
                            version_information = scan_dict['scan'][host]['tcp'][service]['extrainfo']
                        else:
                            version_information = "N.A."

                        # cpe
                        if 'cpe' in scan_dict['scan'][host]['tcp'][service]:
                            cpe = scan_dict['scan'][host]['tcp'][service]['cpe']
                        else:
                            cpe = "N.A."

                        # script
                        if 'script' in scan_dict['scan'][host]['tcp'][service]:
                            script = str(scan_dict['scan'][host]['tcp'][service]['script'])
                        else:
                            script = "N.A."

                        # is pw cracked or not
                        is_cracked = scan_dict['scan'][host]['tcp'][service]['is_cracked']

                        # TODO: Reccomendation
                        recommendation = "placeholder"

                        # insert into service table
                        cur.execute("INSERT INTO service (host_id, service_name, service_port, state, software_product, service_version, version_information, cpe, script, pw_cracked, recommendation) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", [host_id, service_name, service_port, state, software_product, service_version, version_information, cpe, script, is_cracked, recommendation])
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

sample_dict = {
  'nmap': {
    'command_line': 'nmap -oX - -A -T4 192.168.158.0/24',
    'scaninfo': {
      'tcp': {
        'method': 'syn'
      }
    },
    'scanstats': {
      'timestr': 'Tue Jul 25 13:00:15 2023',
      'elapsed': '77.20',
      'uphosts': '3',
      'downhosts': '253',
      'totalhosts': '256'
    }
  },
  'scan': {
    '192.168.158.146': {
      'hostnames': [
        {
          'name': '',
          'type': ''
        }
      ],
      'addresses': {
        'ipv4': '192.168.158.146',
        'mac': '00:0C:29:50:CD:DB'
      },
      'vendor': {
        '00:0C:29:50:CD:DB': 'VMware'
      },
      'status': {
        'state': 'up',
        'reason': 'arp-response'
      },
      'uptime': {
        'seconds': '3038809',
        'lastboot': 'Tue Jun 20 08:52:45 2023'
      },
      'tcp': {
        21: {
          'is_cracked': "yes",
          'state': 'open',
          'reason': 'syn-ack',
          'name': 'ftp',
          'product': 'vsftpd',
          'version': '3.0.3',
          'extrainfo': '',
          'conf': '10',
          'cpe': 'cpe:/a:vsftpd:vsftpd:3.0.3',
          'script': {
            'ftp-syst': 'blablablabla'
          }
        },
        22: {
          'is_cracked': "yes",
          'state': 'open',
          'reason': 'syn-ack',
          'name': 'ssh',
          'product': 'OpenSSH',
          'version': '7.9p1 Debian 10+deb10u2',
          'extrainfo': 'protocol 2.0',
          'conf': '10',
          'cpe': 'cpe:/o:linux:linux_kernel',
          'script': {
            'ssh-hostkey': 'blabla'
          }
        },
        80: {
          'is_cracked': "yes",
          'state': 'open',
          'reason': 'syn-ack',
          'name': 'http',
          'product': 'Apache httpd',
          'version': '2.4.38',
          'extrainfo': '(Debian)',
          'conf': '10',
          'cpe': 'cpe:/a:apache:http_server:2.4.38',
          'script': {
            'http-apache-server-status': 'blabla'
          }
        }
      },
      'osmatch': [
        {
          'name': 'Linux 4.15 - 5.8',
          'accuracy': '100',
          'line': '67250',
          'osclass': [
            {
              'type': 'general purpose',
              'vendor': 'Linux',
              'osfamily': 'Linux',
              'osgen': '4.X',
              'accuracy': '100',
              'cpe': [
                'cpe:/o:linux:linux_kernel:4'
              ]
            },
            {
              'type': 'general purpose',
              'vendor': 'Linux',
              'osfamily': 'Linux',
              'osgen': '5.X',
              'accuracy': '100',
              'cpe': [
                'cpe:/o:linux:linux_kernel:5'
              ]
            }
          ]
        }
      ]
    }
  }
}

Database.main()
Database.insert_scan("wifi name", sample_dict)
Database.insert_scan("wifi name", sample_dict)
Database.delete_result(2)
Database.insert_scan("wifi name", sample_dict)
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
    scan_id INTEGER [ref: > scan.scan_id]
    host_ip TEXT
    device_type TEXT
    mac_address TEXT
    vendor TEXT
    device_status TEXT
}

TABLE service{
    service_id INTEGER [pk, increment]
    host_id INTEGER [ref: > host.host_id]
    service_name TEXT
    port_no INTEGER
    status TEXT
    software_product TEXT
    service_version TEXT
    version_information TEXT
    cpe TEXT
    script TEXT
    recommendation TEXT
    pw_cracked TEXT
}
"""