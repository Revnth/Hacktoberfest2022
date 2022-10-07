import socket
import random

def calRedundantBits(m):
	for i in range(m):
		if(2**i >= m):
			return i

def detectError(arr, nr):
	n = len(arr)
	res = 0
	for i in range(nr):
		val = 0
		for j in range(1, n + 1):
			if(j & (2**i) == (2**i)):
				val = val ^ int(arr[-1 * j])
		res = res + val*(10**i)
	if (res==0):
		return (int(str(res),2))
	else:
		return (n-int(str(res), 2)+1)

s=socket.socket()
port=12345
s.bind(('127.0.0.1',port))
print (f"Connected to port {port}")
s.listen(5)

while True:
	k,a=s.accept()
	print (f"Connected to {a}")
	data=k.recv(1024).decode()
	print("When no disturbance occured during transmission\nMessage from client:", data)
	m=len(data)
	nr=calRedundantBits(m)
	correction = detectError(data, nr)
	if (correction==0):
		msg=f"Data received : {data} ; No error"
		k.send(msg.encode())
	else:
		data1=''
		if (data[correction-1]=='0'):
			data1=data[:correction-1]+"1"+data[correction:]
		else:
			data1=data[:correction-1]+"0"+data[correction:]
		msg=f"Data received is {data} ; Error found at position {correction} ; Corrected data is {data1}"
		k.send(msg.encode())
	rand=random.randint(1,m)
	ndata=''
	if (data[rand-1]=='0'):
		ndata=data[:rand-1]+"1"+data[rand:]
	else:
		ndata=data[:rand-1]+"0"+data[rand:]
	print(f"When disturbance occured during transmission\nMessage from client: {data}")
	correction = detectError(ndata, nr)
	if (correction==0):
		msg=f"Data received is {ndata} ; No error"
		k.send(msg.encode())
	else:
		data1=''
		if (ndata[correction-1]=='0'):
			data1=ndata[:correction-1]+"1"+ndata[correction:]
		else:
			data1=ndata[:correction-1]+"0"+ndata[correction:]
		msg=f"Data received : {ndata} ; Error found at position {correction} ; Corrected data is {data1}"
		k.send(msg.encode())
