import socket

host='127.0.0.1'
port=1234

s=socket.socket()
s.connect((host,port))

msg=input("Enter number: ")
s.send(msg.encode())
d=s.recv(1024).decode()

print("Received from the server: " + d)

s.close()
