from PySide6.QtCore import QThread, Signal
import nmap

class ScanThread(QThread):
    scanFinished = Signal(dict)
    scanCancelled = Signal()

    def __init__(self, ip_range):
        super().__init__()
        self.ip_range = ip_range
        self.is_cancelled = False

    def run(self):
        nm = nmap.PortScanner()
        if(self.is_cancelled):
            self.scanCancelled.emit()
            return
        
        scan_output = nm.scan(hosts=self.ip_range, arguments="")
        self.scanFinished.emit(scan_output)
    
    def cancel(self):
        self.is_cancelled = True