# Packet Sender & Port Scanner (v1.3)

Packet Sender & Port Scanner is a comprehensive network tool designed for packet sending, port scanning, and network performance analysis.

---

## 📢 What's New in v1.3:
- **Added Installer**: A new, user-friendly installer is available! Simply run it to install the app—no manual file handling required.
- **Port Scanning Returns**: Enhanced functionality for scanning open ports within a specified range.
- **Major UI Update**: Improved user interface for a better experience.
- **Improved Speedometer**: Real-time updates with dynamic color coding for speed visualization.
- **Custom Packet Size**: Control the exact size of packets sent, up to 1MB.
- **Multithreaded Operations**: Optimized for high-performance packet sending with multiple threads.
- **Error Handling**: Displays clear error messages for invalid inputs or connection issues.

---

## 🚀 Getting Started
### Step 1: Install Required Python Packages
Ensure Python is installed on your system, and then run the following command in your terminal to install the necessary libraries:

```bash
pip install PyQt5 requests
```

### Step 2: Download and Run the Installer
- Download the installer from the [Releases page](https://github.com/PHXNKPXAYA/PacketSender/releases).
- Run the installer and follow the on-screen instructions to set up the application.

### Step 3: Launch the Application
After installation, start the app via the desktop shortcut or from the Start Menu.

---

## Features of Packet Sender v1.2:
### Packet Sending:
- Send custom-sized UDP packets to a target IP address and port.
- Specify the message to include in the packet.
- Multithreaded for faster packet sending.

### Speedometer:
- Visualize the packet sending speed in real time.
- Dynamic needle color change based on speed:
  - Green: Low speed (up to 5000 packets/sec).
  - Orange: Medium speed (5000 to 8000 packets/sec).
  - Red: High speed (above 8000 packets/sec).
- Display packets sent per second with live updates.

### Port Scanning:
- Scan a range of ports on a target IP.
- Display open ports during the scanning process.

### Real-Time Statistics:
- Monitor total packets sent and failed packets in real time.
- Updated every second for accurate status.

### Graphical User Interface (GUI):
- Built with PyQt5 for a clean, user-friendly design.
- Easily navigate between packet sending, port scanning, and results monitoring.

### Error Handling:
- Displays error messages for invalid inputs or network issues.
- Tracks failed packets for troubleshooting.

---

## 🖍️ Note on Port Scanning
### Port scanning functionality has been improved in this version.  
It may still be affected by system firewalls or permissions. Adjust network and security settings if you encounter issues.

---

## ⚠️ Disclaimer
This tool is intended for **educational and cybersecurity purposes only**.  
The creator is **not responsible** for any misuse or consequences of using this software.

---

## 📨 Support & Contributions
- **Report Issues**: If you encounter any problems, submit them via the [Issues](https://github.com/PHXNKPXAYA/Packet-Sender/issues) section.
- **Contribute**: Contributions to improve or expand this project are always welcome! Fork the repository and submit a pull request.

---
