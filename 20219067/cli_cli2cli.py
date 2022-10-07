import socket
import select
import sys
port = 5050
add = ('127.0.0.1', port)
leave_msg = "bye"
active = True

client = socket.socket()
client.connect(add)
client.send(input("Enter name:").encode())
print("Sucessfully joined the chat!\nEnter 'bye' to leave\n")

def send(msg):
	msg = msg.encode()
	client.send(msg)

def receive():
	msg = client.recv(1024).decode()
	print(msg)

while active:
	rlist, wlist, errlist = select.select([client, sys.stdin], [], [])
	for s in rlist:

		if s == client:
			receive()
		else:
			msg = input()
			if msg == leave_msg:
				active = False
			send(msg)

send(msg)
