""" 
Sharun E Rajeev
20219078
echo-server.py
"""

import socket							# Importing socket module

HOST = "192.168.10.127" 						# HOST here is the localhost

""" Port here is an non-privileged port ie port > 1023 and < 65535
It represent the TCP port number from where the connections are accepted. """
PORT = 6543

ADDR = (HOST, PORT) 					# Address tuple for binding

""" 
with in python is used to  wrap the execution of a block with methods defined by a context manager
AF_INET is the Internet address family for IPv4
SOCK_STREAM is the socket type for TCP
"""
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	"""
	Bind() binds the server to the given host and port address.
	Bind() here used IPv4 so it requires two tuples : HOST and PORT.
    """
	s.bind(ADDR)						# Server binds the address
	s.listen()
	conn, addr = s.accept()				# On accepting the connection from the client it stores the client connection details and the address.
	with conn:							# If connection is established then 
		print(f"Connected by {addr}")	# We are going to print the address of the client
		while True:						# Until the data is recieved
			data = conn.recv(1024)		# Collect the data from the client
			if not data:				# If data is not recieved end the while loop else send all data.
				break
			conn.sendall(data)

