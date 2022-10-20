# Python3 code to find
# winner of game

# function to find the winner
def winner( a, n, k):

	# if the number of steps is
	# more than n-1
	if k >= n - 1:
		return n
	
	# initially the best is 0
	# and no of wins is 0.
	best = 0
	times = 0
	
	# traverse through all the numbers
	for i in range(n):
	
		# if the value of array is more
		# than that of previous best
		if a[i] > best:
		
			# best is replaced by a[i]
			best = a[i]
			
			# if not the first index
			if i == True:
				
				# no of wins is 1 now
				times = 1
		else:
			times += 1 # if it wins
			
		# if any position has more
		# than k wins then return
		if times >= k:
			return best
			
	# Maximum element will be winner
	# because we move smaller element
	# at end and repeat the process.
	return best
	
	
# driver code
a = [ 2, 1, 3, 4, 5 ]
n = len(a)
k = 2
print(winner(a, n, k))

# This code is contributed by jhasd
