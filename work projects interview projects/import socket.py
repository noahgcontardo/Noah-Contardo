import socket
import re

def calculate_tax(income, state):
    # Federal tax brackets for 2024 (single filer)
    brackets = [
        (11600, 0.10),
        (47150, 0.12),
        (100525, 0.22),
        (191950, 0.24),
        (243725, 0.32),
        (609350, 0.35),
        (float('inf'), 0.37)
    ]

    federal_tax = 0
    prev_bracket = 0
    for bracket, rate in brackets:
        if income > bracket:
            federal_tax += (bracket - prev_bracket) * rate
        else:
            federal_tax += (income - prev_bracket) * rate
            break
        prev_bracket = bracket


FICA tax (7.65% of income)
        fica_tax = income * 0.0765

Total tax (federal + FICA)
    total_tax = federal_tax + fica_tax

Round to 2 decimal places
    return round(total_tax, 2)

Connect to the server
server_address = ('192.168.10.129', 4321)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(server_address)

Receive and parse the tax form data
data = sock.recv(1024).decode()
income = float(re.search(r'Income: $(\d+)', data).group(1))
state = re.search(r'State: (\w+)', data).group(1)

Calculate the tax
tax = calculate_tax(income, state)

Send the result back to the server
sock.sendall(str(tax).encode())

Close the socket
sock.close()