import socket

host = '127.0.0.1'
port = 1234

s = socket.socket()

s.bind((host,port))

s.listen(2)

conn,addr = s.accept()
print("Connection from: " + str(addr))
#while True:
data=conn.recv(1024).decode()
#if not data:
#	break
	
print("from connected user: " +str(data))
if int(data)%2==0:
	res="Number is even"
else:
	res="Number is odd"
conn.send(res.encode())
	
conn.close()
