import socket
import threading

port= 5050
add = ('127.0.0.1', port)
leave_msg = "bye"
active = True

server = socket.socket()

server.bind(add)

client_list = []

def serverside():
	server.listen(5)
	print(f"Server is listening...")
	while active:
		conn, addr = server.accept()
		client_list.append(conn)
		name=conn.recv(1024).decode()
		thread = threading.Thread(target=handle_client, args=(conn, name))
		thread.start()
		print(f"Number of active connections: {threading.active_count() - 1}")

def sendToAllClients(msg,conn):
	for client in client_list:
		if conn!=client:
			client.send(msg.encode())

def handle_client(conn, name):
	try:
		msg=f"{name} has joined the chat!"
		print(msg)
		sendToAllClients(msg,conn)
		while True:
			msg = conn.recv(1024).decode()

			if msg == leave_msg:
				break
			msg = (f"{name}:{msg}")
			print(msg)
			sendToAllClients(msg,conn)
		msg=f"{name} has left the chat!"
		print(msg)
		
		sendToAllClients(msg,conn)
		client_list.remove(conn)
		conn.close()
	
	except:
		return

serverside()
