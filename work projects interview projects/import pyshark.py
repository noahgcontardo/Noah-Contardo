import pyshark
import os

# File path for ttl_values.txt on Desktop
file_path = 'C:\\Users\\User\\Desktop\\ttl_values.txt'

# Ensure the pcap file path is correct
pcap_file = 'C:\\Users\\User\\Downloads\\a5e81bd8-964d-4bdb-8265-afce3fdf076b.pcap'

# Check if the pcap file exists
if os.path.exists(pcap_file):
    print(f"File found: {pcap_file}")
else:
    print(f"File not found: {pcap_file}")

# Load the pcap file and apply the TTL display filter
cap = pyshark.FileCapture(pcap_file, display_filter='ip.ttl')

# Open a file on the Desktop to write TTL values
with open(file_path, 'w') as f:
    for packet in cap:
        ttl_value = packet.ip.ttl
        f.write(f'{ttl_value}\n')

print(f"TTL values have been written to {file_path}")
