import socket, select

#Function to send message to all connected clients
def send_to_all (sock, message):
	#Message not forwarded to server and sender itself
	for socket in connected_list:
		if socket != server_socket and socket != sock :
			try :
				socket.send(message)
			except :
				# if connection not available
				socket.close()
				connected_list.remove(socket)

if __name__ == "__main__":
	name=""
	# Dictionary to store address corresponding to username
	record={}
	# List to keep track of socket descriptors
	connected_list = []
	# Size of the message to be send
	buffer = 4096
	port = 5678
	# Create socket
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	server_socket.bind(("192.168.10.127", port))
	server_socket.listen(10) #listen atmost 10 connection at one time

	# Add server socket to the list of readable connections
	connected_list.append(server_socket)

	print("\tSERVER WORKING")

	while 1:
        # Get the list sockets which are ready to be read through select
		rList,wList,error_sockets = select.select(connected_list,[],[])

		for sock in rList:
			#New connection
			if sock == server_socket:
				# Handle the case in which there is a new connection recieved through server_socket
				sockfd, addr = server_socket.accept()
				name=sockfd.recv(buffer)
				connected_list.append(sockfd)
				record[addr]=""
				#print "record and conn list ",record,connected_list
                
                		#if repeated username
				if name in record.values():
					sockfd.send("Username already taken!\n")
					del record[addr]
					connected_list.remove(sockfd)
					sockfd.close()
					continue
				else:
                    			#add name and address
					record[addr]=name
					print(f"Client ({addr}, [{record[addr]}]) connected")
					sockfd.send("Welcome to chat room. Enter 'exit' anytime to exit\n".encode("utf-8"))
					send_to_all(sockfd, name+" joined the conversation \n")

			#Some incoming message from a client
			else:
				# Data from client
				try:
					data1 = sock.recv(buffer)
					#print "sock is: ",sock
					data=data1[:data1.index("\n")]
					#print "\ndata received: ",data
                    
                    			#get addr of client sending the message
					i,p=sock.getpeername()
					if data == "exit":
						msg=record[(i,p)]+" left the conversation\n"
						send_to_all(sock,msg)
						print(f"Client ({(i.p)}, [{record[(i,p)]}]) is offline")
						del record[(i,p)]
						connected_list.remove(sock)
						sock.close()
						continue

					else:
						msg=record[(i,p)]+": "+data+"\n"
						send_to_all(sock,msg)
            
                		#abrupt user exit
				except:
					(i,p)=sock.getpeername()
					send_to_all(sock, record[(i,p)]+" left the conversation unexpectedly\n")
					print(f"Client ({(i.p)}, [{record[(i,p)]}]) is offline (error)")
					del record[(i,p)]
					connected_list.remove(sock)
					sock.close()
					continue

	server_socket.close()

