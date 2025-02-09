import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QHBoxLayout, QProgressBar
from PyQt5.QtCore import QThread, pyqtSignal
import subprocess


class PingThread(QThread):
    result = pyqtSignal(str)
    progress = pyqtSignal(int)

    def __init__(self, ip_address, ping_count):
        super().__init__()
        self.ip_address = ip_address
        self.ping_count = int(ping_count)

    def run(self):
        command = ["ping", "-c", str(self.ping_count), self.ip_address] if sys.platform != "win32" else ["ping", "-n", str(self.ping_count), self.ip_address]
        try:
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
            ping_responses = 0
            while True:
                output = process.stdout.readline()
                if output == "" and process.poll() is not None:
                    break
                if output:
                    ping_responses += 1
                    progress_value = int((ping_responses / self.ping_count) * 100)
                    self.progress.emit(progress_value)
                    self.result.emit(output.strip())
            process.stdout.close()
        except subprocess.CalledProcessError as e:
            self.result.emit(f"Error: {e}")
        except FileNotFoundError:
            self.result.emit("Error: Command not found.")

class PingTab(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.ip_label = QLabel("Enter IP Address:")
        self.ip_input = QLineEdit()
        self.ping_count_label = QLabel("Enter Number of Pings:")
        self.ping_count_input = QLineEdit()
        self.ping_button = QPushButton("Ping")
        self.ping_button.clicked.connect(self.ping_ip)
        self.output_area = QTextEdit()
        self.output_area.setReadOnly(True)
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.ip_label)
        input_layout.addWidget(self.ip_input)
        input_layout.addWidget(self.ping_count_label)
        input_layout.addWidget(self.ping_count_input)
        self.layout.addLayout(input_layout)
        self.layout.addWidget(self.ping_button)
        self.layout.addWidget(self.output_area)
        self.layout.addWidget(self.progress_bar)
        self.setLayout(self.layout)

    def ping_ip(self):
        ip_address = self.ip_input.text()
        ping_count = self.ping_count_input.text()

        if not ip_address or not ping_count.isdigit():
            self.output_area.setText("Please enter valid IP address and number of pings.")
            return
        self.output_area.clear()
        self.progress_bar.setValue(0)
        self.ping_thread = PingThread(ip_address, ping_count)
        self.ping_thread.result.connect(self.display_ping_result)
        self.ping_thread.progress.connect(self.update_progress)
        self.ping_thread.start()

    def display_ping_result(self, result):
        self.output_area.append(result)

    def update_progress(self, value):
        self.progress_bar.setValue(value)

    def get_state(self):
        return {'ip': self.ip_input.text(), 'ping_count': self.ping_count_input.text()}

    def load_state(self, state):
        self.ip_input.setText(state['ip'])
        self.ping_count_input.setText(state['ping_count'])
