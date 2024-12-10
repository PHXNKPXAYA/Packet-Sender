# Packet Sender & Port Scanner App - **Version 1.2**

This is the **Packet Sender & Port Scanner App**, a tool designed to send custom UDP packets and scan ports on a target IP address. This new version (1.2) introduces major improvements, including the ability to scan ports, customize packet size, and more!

---

## Features of Packet Sender & Port Scanner App

### 1. **Packet Sending**
- Send custom-sized **UDP packets** to a target IP address and port.
- Specify the **message** to include in the packet.
- Control the **number of threads** for faster packet sending.
- **Packet Size Customization**: Choose the packet size, from small packets to large ones (up to **1MB**).

### 2. **Speedometer**
- Real-time visualization of the packet sending **speed** (packets per second).
- **Dynamic needle color** changes based on speed:
  - Green for low speed (up to 5000 packets/sec).
  - Orange for medium speed (5000 to 8000 packets/sec).
  - Red for high speed (above 8000 packets/sec).
- Displays **packets sent per second** with real-time updates.

### 3. **Real-Time Statistics**
- **Total packets sent** and **failed packets** are displayed in real-time.
- Statistics update every second to reflect the **current packet sending status**.

### 4. **Port Scanning**
- **Scan a range of ports** on a target IP address.
- Displays **open ports** within the scanned range.
- Provides **real-time feedback** during the port scan process.

### 5. **Multithreaded Packet Sending**
- Supports **multiple threads** for concurrent packet sending.
- Increases the speed and **effectiveness** of the packet sending process.

### 6. **Graphical User Interface (GUI)**
- **User-friendly interface** built with **PyQt5**.
- Real-time updates for the **speedometer** and **statistics**.
- Easily navigable UI for **sending packets**, **scanning ports**, and monitoring results.

### 7. **Error Handling**
- Tracks **failed packets** and displays relevant **error messages**.
- Handles **invalid inputs** for packet size and port scanning.

### 8. **Real-Time Feedback**
- Displays **real-time status** of the packet sender (sending packets, stopped, etc.).
- Provides **visual feedback** on packet sending rates and success/failure statistics.

### 9. **Cross-Platform**
- Built with **Python** and **PyQt5**, making it compatible with multiple operating systems:
  - **Windows**
  - **macOS**
  - **Linux**

---

## Requirements

To run **Packet Sender & Port Scanner** app, you need to have **Python 3.x** installed. You can install the required dependencies by running the following command:

```bash
pip install PyQt5 requests
