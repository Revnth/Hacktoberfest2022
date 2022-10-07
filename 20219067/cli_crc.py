# First of all import the socket library
import socket


def xor(a, b):

	# initialize result
	result = []

	# Traverse all bits, if bits are
	# same, then XOR is 0, else 1
	for i in range(1, len(b)):
		if a[i] == b[i]:
			result.append('0')
		else:
			result.append('1')

	return ''.join(result)


# Performs Modulo-2 division
def mod2div(divident, divisor):

	# Number of bits to be XORed at a time.
	pick = len(divisor)

	# Slicing the divident to appropriate
	# length for particular step
	tmp = divident[0: pick]

	while pick < len(divident):

		if tmp[0] == '1':

			# replace the divident by the result
			# of XOR and pull 1 bit down
			tmp = xor(divisor, tmp) + divident[pick]

		else: # If leftmost bit is '0'
			# If the leftmost bit of the dividend (or the
			# part used in each step) is 0, the step cannot
			# use the regular divisor; we need to use an
			# all-0s divisor.
			tmp = xor('0'*pick, tmp) + divident[pick]

		# increment pick to move further
		pick += 1

	# For the last n bits, we have to carry it out
	# normally as increased value of pick will cause
	# Index Out of Bounds.
	if tmp[0] == '1':
		tmp = xor(divisor, tmp)
	else:
		tmp = xor('0'*pick, tmp)

	checkword = tmp
	return checkword

# Function used at the receiver side to decode
# data received by sender


def decodeData(data, key):

	l_key = len(key)

	
	appended_data = data.decode() + '0'*(l_key-1)
	remainder = mod2div(appended_data, key)

	return remainder



s = socket.socket()
print("Socket successfully created")


port = 12345

s.bind(('', port))
print("socket binded to %s" % (port))

s.listen(5)
print("socket is listening")


while True:
	
	c, addr = s.accept()
	print('Got connection from', addr)

	
	data = c.recv(1024)

	print("Received encoded data in binary format :", data.decode())

	if not data:
		break
	key =input("Enter key: ")
	#key = "1001"

	ans = decodeData(data, key)
	print("Remainder after decoding is->"+ans)

	
	temp = "0" * (len(key) - 1)
	if ans == temp:
		c.sendto(("THANK you Data ->"+data.decode() +
				" Received No error FOUND").encode(), ('127.0.0.1', 12345))
	else:
		c.sendto(("Error in data").encode(), ('127.0.0.1', 12345))

	c.close()

