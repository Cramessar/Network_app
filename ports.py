import sys
import socket
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QHBoxLayout, QProgressBar

class PortsTab(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.ip_label = QLabel("Enter IP Address:")
        self.ip_input = QLineEdit()
        self.port_range_label = QLabel("Enter Port Range (e.g., 20-80):")
        self.port_range_input = QLineEdit()
        self.netstat_button = QPushButton("Run Port Scan")
        self.netstat_button.clicked.connect(self.run_netstat)
        self.telnet_port_label = QLabel("Enter Port for Telnet:")
        self.telnet_port_input = QLineEdit()
        self.telnet_button = QPushButton("Run Telnet")
        self.telnet_button.clicked.connect(self.run_telnet)
        self.output_area = QTextEdit()
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        netstat_layout = QHBoxLayout()
        netstat_layout.addWidget(self.port_range_label)
        netstat_layout.addWidget(self.port_range_input)
        telnet_layout = QHBoxLayout()
        telnet_layout.addWidget(self.telnet_port_label)
        telnet_layout.addWidget(self.telnet_port_input)
        self.layout.addWidget(self.ip_label)
        self.layout.addWidget(self.ip_input)
        self.layout.addLayout(netstat_layout)
        self.layout.addWidget(self.netstat_button)
        self.layout.addLayout(telnet_layout)
        self.layout.addWidget(self.telnet_button)
        self.layout.addWidget(self.output_area)
        self.layout.addWidget(self.progress_bar)
        self.setLayout(self.layout)

    def run_netstat(self):
        ip_address = self.ip_input.text()
        port_range = self.port_range_input.text()
        if not ip_address or not port_range or "-" not in port_range:
            self.output_area.setText("Please enter a valid IP address and port range (e.g., 20-80).")
            return
        start_port, end_port = port_range.split("-")
        try:
            start_port = int(start_port)
            end_port = int(end_port)
        except ValueError:
            self.output_area.setText("Invalid port range. Please enter numbers (e.g., 20-80).")
            return
        total_ports = end_port - start_port + 1
        self.progress_bar.setValue(0)  
        self.progress_bar.setMaximum(total_ports)
        self.output_area.clear()
        self.output_area.append(f"Scanning IP: {ip_address} for open ports between {start_port} and {end_port}...\n")
        for count, port in enumerate(range(start_port, end_port + 1), start=1):
            self.output_area.append(f"Checking port {port}...")
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((ip_address, port))

                if result == 0:
                    self.output_area.append(f"Port {port}: Open")
                else:
                    self.output_area.append(f"Port {port}: Closed")

                sock.close()
            except socket.error as e:
                self.output_area.append(f"Error checking port {port}: {e}")
            self.progress_bar.setValue(count)

    def run_telnet(self):
        ip_address = self.ip_input.text()
        port = self.telnet_port_input.text()
        if not ip_address or not port.isdigit():
            self.output_area.setText("Please enter a valid IP address and port number.")
            return
        port = int(port)
        try:
            self.output_area.append(f"Attempting to connect to {ip_address} on port {port}...")
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            result = sock.connect_ex((ip_address, port))
            if result == 0:
                self.output_area.append(f"Connection to {ip_address} on port {port} succeeded.")
            else:
                self.output_area.append(f"Connection to {ip_address} on port {port} failed. Error code: {result}")
            if result != 0:
                self.output_area.append(f"Connection attempt resulted in error code {result}. "
                                        "Make sure the IP address and port are reachable, and check for any firewalls or network issues.")
            sock.close()
        except socket.error as e:
            self.output_area.append(f"Socket error: {e}")

    def get_state(self):
        return {'ip': self.ip_input.text(), 'port_range': self.port_range_input.text(), 'telnet_port': self.telnet_port_input.text()}

    def load_state(self, state):
        self.ip_input.setText(state['ip'])
        self.port_range_input.setText(state['port_range'])
        self.telnet_port_input.setText(state['telnet_port'])
