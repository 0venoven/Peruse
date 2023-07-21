from PySide6.QtCore import QThread, Signal
import nmap

class ScanThread(QThread):
    scanFinished = Signal(dict)

    def __init__(self, ip_range):
        super().__init__()
        self.ip_range = ip_range

    def run(self):
        nm = nmap.PortScanner()
        scan_output = nm.scan(hosts=self.ip_range, arguments="")
        print(scan_output)
        print(type(scan_output))
        print(scan_output['nmap']['command_line'])
        self.scanFinished.emit(scan_output)