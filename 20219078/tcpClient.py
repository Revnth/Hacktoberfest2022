"""
Sharun E Rajeev
20219078
echo-client.py
"""

import socket

HOST = "192.168.10.126"  			# The server's hostname or IP address
PORT = 4455  				# The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))		# connecting to the server using HOST ID and PORT number
    s.sendall(b"Hello, world")		# Sends data to the server
    data = s.recv(1024)			# Collect the recieved the data from the server

print(f"Received {data!r}")		# Print the recieved data

