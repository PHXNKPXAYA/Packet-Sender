import sys
import socket
import threading
import time
import math
from PyQt5 import QtWidgets, QtCore, QtGui

class Speedometer(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Speedometer, self).__init__(parent)
        self.current_speed = 0
        self.max_speed = 10000
        self.setMinimumSize(200, 200)

    def set_speed(self, speed):
        self.current_speed = speed
        self.update()

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        rect = self.rect()
        painter.setRenderHint(QtGui.QPainter.Antialiasing)

        # Background Circle
        painter.setBrush(QtGui.QColor("#444"))
        painter.setPen(QtCore.Qt.NoPen)
        painter.drawEllipse(rect)

        # Draw Speedometer Tick Marks
        painter.setPen(QtGui.QColor("#FFF"))
        for i in range(0, 11):  # 0 to 10 (10,000 packets/sec)
            angle = 240 - (i * 24)  # Spread over 240 degrees
            x = rect.center().x() + 80 * math.cos(math.radians(angle))
            y = rect.center().y() - 80 * math.sin(math.radians(angle))
            painter.drawText(QtCore.QPointF(x - 10, y + 5), f"{i * 1000}")

        # Dynamic Speed Needle
        painter.setBrush(QtCore.Qt.NoBrush)
        color = "#4CAF50" if self.current_speed <= 5000 else "#FFA500" if self.current_speed <= 8000 else "#FF0000"
        painter.setPen(QtGui.QPen(QtGui.QColor(color), 5))
        angle = 240 - (self.current_speed / self.max_speed * 240)
        x = rect.center().x() + 80 * math.cos(math.radians(angle))
        y = rect.center().y() - 80 * math.sin(math.radians(angle))
        painter.drawLine(rect.center(), QtCore.QPointF(x, y))


class PacketSenderApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Packet Sender & Port Scanner")
        self.setGeometry(100, 100, 600, 700)
        self.setStyleSheet("background-color: #2E2E2E; color: #FFFFFF;")

        self.main_layout = QtWidgets.QVBoxLayout()

        # Input fields for packet sending
        self.ip_entry = self.create_input_field("Target IP Address:")
        self.port_entry = self.create_input_field("Target Port Number:")
        self.message_entry = self.create_input_field("Message to Send:")
        self.thread_count_entry = self.create_input_field("Number of Threads:")

        # Speedometer Widget
        self.speedometer = Speedometer()
        self.main_layout.addWidget(self.speedometer)

        # Label for speedometer
        self.speedometer_label = QtWidgets.QLabel("Packets per second: 0")
        self.speedometer_label.setAlignment(QtCore.Qt.AlignCenter)
        self.speedometer_label.setStyleSheet("color: #FFFFFF; font-size: 18px;")
        self.main_layout.addWidget(self.speedometer_label)

        # Start/Stop Buttons for packet sending
        start_button = QtWidgets.QPushButton("Start Sending")
        start_button.setStyleSheet("background-color: #4CAF50; color: white;")
        start_button.clicked.connect(self.start_sending)
        self.main_layout.addWidget(start_button)

        stop_button = QtWidgets.QPushButton("Stop Sending")
        stop_button.setStyleSheet("background-color: #FF0000; color: white;")
        stop_button.clicked.connect(self.stop_sending)
        self.main_layout.addWidget(stop_button)

        # Port scanning inputs
        self.scan_start_entry = self.create_input_field("Scan Start Port:")
        self.scan_end_entry = self.create_input_field("Scan End Port:")

        # Port scanning button
        scan_button = QtWidgets.QPushButton("Start Port Scan")
        scan_button.setStyleSheet("background-color: #FFA500; color: white;")
        scan_button.clicked.connect(self.start_port_scan)
        self.main_layout.addWidget(scan_button)

        # Output area for port scan results
        self.scan_results = QtWidgets.QTextEdit()
        self.scan_results.setReadOnly(True)
        self.scan_results.setStyleSheet("background-color: #1E1E1E; color: #00FF00;")
        self.main_layout.addWidget(self.scan_results)

        self.main_layout.addStretch()
        self.setLayout(self.main_layout)

        # Initialize variables
        self.sending = False
        self.packet_rate = 0
        self.packets_sent = 0
        self.last_update_time = time.time()

    def create_input_field(self, label_text):
        label = QtWidgets.QLabel(label_text)
        label.setStyleSheet("color: #FFFFFF;")
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(label)
        entry = QtWidgets.QLineEdit()
        entry.setStyleSheet("background-color: #3E3E3E; color: #FFFFFF; border: 1px solid #4CAF50;")
        layout.addWidget(entry)
        self.main_layout.addLayout(layout)
        return entry

    def send_packet(self, ip, port, message):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(message.encode(), (ip, port))
            self.packets_sent += 1
        except Exception as e:
            print(f"Error: {e}")

    def thread_function(self, ip, port, message):
        while self.sending:
            self.send_packet(ip, port, message)

    def start_sending(self):
        self.sending = True
        ip = self.ip_entry.text()
        port = int(self.port_entry.text())
        message = self.message_entry.text()
        thread_count = int(self.thread_count_entry.text())

        threads = []
        for i in range(thread_count):
            thread = threading.Thread(target=self.thread_function, args=(ip, port, message))
            thread.start()
            threads.append(thread)

        self.update_packet_rate()

    def stop_sending(self):
        self.sending = False

    def start_port_scan(self):
        ip = self.ip_entry.text()
        start_port = int(self.scan_start_entry.text())
        end_port = int(self.scan_end_entry.text())

        self.scan_results.clear()
        self.scan_results.append(f"Scanning {ip} from port {start_port} to {end_port}...\n")

        thread = threading.Thread(target=self.port_scan, args=(ip, start_port, end_port))
        thread.start()

    def port_scan(self, ip, start_port, end_port):
        for port in range(start_port, end_port + 1):
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    sock.settimeout(0.5)
                    result = sock.connect_ex((ip, port))
                    if result == 0:
                        self.scan_results.append(f"Port {port} is OPEN.")
            except Exception as e:
                self.scan_results.append(f"Error scanning port {port}: {e}")

    def update_packet_rate(self):
        current_time = time.time()
        time_diff = current_time - self.last_update_time
        self.packet_rate = self.packets_sent / time_diff if time_diff > 0 else 0

        # Update Speedometer
        self.speedometer.set_speed(min(int(self.packet_rate), 10000))
        self.speedometer_label.setText(f"Packets per second: {int(self.packet_rate)}")

        self.last_update_time = current_time
        self.packets_sent = 0

        if self.sending:
            QtCore.QTimer.singleShot(1000, self.update_packet_rate)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    window = PacketSenderApp()
    window.show()
    sys.exit(app.exec_())
