Basic Network Sniffer

Building a network sniffer like "The Sniffer" typically involves using a Python library such as Scapy, which is essential for tasks involving network analysis. Scapy allows precise control over packet handling, making it possible to directly inspect and manipulate network traffic. Running such tools generally requires administrator privileges. It’s also crucial to be aware of and comply with ethical and legal guidelines when intercepting network traffic. "The Sniffer" is intended to be a simple yet effective solution for tracking and examining network activity, offering valuable insights into the data moving through a network. Always ensure you have proper authorization and are respecting legal and privacy considerations before using this tool for packet capture.

📄 Project Task 1: Basic Network Sniffer (Windows Environment)
🔧 System Requirements and Setup Guide
This document outlines the system requirements and setup steps for building a Basic Network Sniffer in Python using Visual Studio Code on a Windows environment.

✅ 1. System Requirements
🖥️ Hardware Requirements
Component	Minimum	Recommended
Processor	Dual-core 2.0 GHz	Quad-core 2.5 GHz or faster
RAM	4 GB	8 GB or more
Storage	2 GB free space	SSD with 5+ GB free space
Network	Standard NIC	NIC supporting promiscuous mode

💻 Operating System
Windows 10 or Windows 11 (64-bit preferred)

🧰 2. Software Requirements
a. Visual Studio Code
Download from: https://code.visualstudio.com/

Install with the Python extension from Microsoft for coding support.

b. Python
Version: Python 3.8 or higher

Download from: https://www.python.org/downloads/windows/

During installation:

✅ Ensure “Add Python to PATH” is checked.

📦 3. Python Packages
Install the necessary Python libraries via Command Prompt or the VS Code terminal:

bash
Copy
Edit
pip install scapy
Optional (for logging or enhancements):

bash
Copy
Edit
pip install colorama psutil
📡 4. Npcap Installation (Essential for Packet Capturing on Windows)
Windows requires Npcap to capture low-level network traffic.

Download from: https://nmap.org/npcap/

During installation:

✅ Select “Install Npcap in WinPcap API-compatible Mode”

✅ Enable “Support raw 802.11 traffic (and monitor mode)”
