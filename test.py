# Python3 code to count the change required to
# convert the array into non-increasing array
from queue import PriorityQueue

def DecreasingArray(a, n):
	
	ss, dif = (0,0)
	
	# min heap
	pq = PriorityQueue()

	# Here in the loop we will
	# check that whether the upcoming
	# element of array is less than top
	# of priority queue. If yes then we
	# calculate the difference. After
	# that we will remove that element
	# and push the current element in
	# queue. And the sum is incremented
	# by the value of difference
	for i in range(n):
		tmp = 0
		
		if not pq.empty():
			tmp = pq.get()
			pq.put(tmp)
		
		if not pq.empty() and tmp < a[i]:
			dif = a[i] - tmp
			ss += dif
			pq.get()
			pq.put(a[i])
		
		pq.put(a[i])
	
	return ss
	
# Driver code
if __name__=="__main__":
	
	a = [ 3, 1, 2, 1 ]
	n = len(a)

	print(DecreasingArray(a, n))
	
# This code is contributed by mathew
