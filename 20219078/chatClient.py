import socket, select, string, sys

#Helper function (formatting)
def display() :
	you="You: "
	sys.stdout.write(you)
	sys.stdout.flush()

def main():
	# Provide the Host IP address
	host = "192.168.10.127"
	port = 5678

	# Asks for a new username
	name=input("\nCREATING NEW ID:\nEnter Username: ")
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(2)

	# connecting host
	try:
		s.connect((host, port))
	except :
		print("Can't connect to the server")
		sys.exit()

	# if connected
	s.send(name.encode("utf-8"))
	display()
	while 1:
		socket_list = [sys.stdin, s]

		# Get the list of sockets which are readable
		rList, wList, error_list = select.select(socket_list , [], [])

		for sock in rList:
			# incoming message from server
			if sock == s:
				data = sock.recv(4096)
				if not data :
					print('DISCONNECTED!')
					sys.exit()
				else :
					sys.stdout.write(data)
					display()

			# user entered a message
			else :
				msg=sys.stdin.readline()
				s.send(msg)
				display()

if __name__ == "__main__":
    main()
