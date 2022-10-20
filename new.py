# Python 3 program to find
# possibility to sort by
# multiple subarray reverse
# operation

def ifPossible(arr, n):

	cp = [0] * n

	# making the copy of
	# the original array
	cp = arr

	# sorting the copied array
	cp.sort()

	for i in range(0 , n) :

		# checking mirror image of
		# elements of sorted copy
		# array and equivalent element
		# of original array
		if (not(arr[i] == cp[i]) and not
			(arr[n - 1 - i] == cp[i])):
			return False

	return True

# Driver code
arr = [1, 7, 6, 4, 5, 3, 2, 8]
n = len(arr)
if (ifPossible(arr, n)):
	print("Yes")
else:
	print("No")

# This code is contributed by mathew
