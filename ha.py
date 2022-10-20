# Python3 Program to count
# swaps required to balance
# string

# Function to calculate
# swaps required
def swapCount(s):

	# Keep track of '['
	pos = []

	for i in range(len(s)):
		if(s[i] == '['):
			pos.append(i)

	# To count number
	# of encountered '['		
	count = 0
	
	# To track position
	# of next '[' in pos
	p = 0
	
	# To store result
	sum = 0	
	s = list(s)
	
	for i in range(len(s)):

		# Increment count and
		# move p to next position
		if(s[i] == '['):
			count += 1
			p += 1
		elif(s[i] == ']'):
			count -= 1

		# We have encountered an
		# unbalanced part of string
		if(count < 0):
		
			# Increment sum by number
			# of swaps required
			# i.e. position of next
			# '[' - current position
			sum += pos[p] - i
			s[i], s[pos[p]] = (s[pos[p]],
							s[i])
			p += 1

			# Reset count to 1
			count = 1
	return sum

# Driver code
s = "[]][]["
print(swapCount(s))

s = "[[][]]"
print(swapCount(s))

# This code is contributed by jsdf
