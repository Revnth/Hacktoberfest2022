# Python3 program for Efficient Huffman Coding
# for Sorted input

# Class for the nodes of the Huffman tree
class QueueNode:
	
	def __init__(self, data = None, freq = None,
				left = None, right = None):
		self.data = data
		self.freq = freq
		self.left = left
		self.right = right

	# Function to check if the following
	# node is a leaf node
	def isLeaf(self):
		return (self.left == None and
				self.right == None)

# Class for the two Queues
class Queue:
	
	def __init__(self):
		self.queue = []

	# Function for checking if the
	# queue has only 1 node
	def isSizeOne(self):
		return len(self.queue) == 1

	# Function for checking if
	# the queue is empty
	def isEmpty(self):
		return self.queue == []

	# Function to add item to the queue
	def enqueue(self, x):
		self.queue.append(x)

	# Function to remove item from the queue
	def dequeue(self):
		return self.queue.pop(0)

# Function to get minimum item from two queues
def findMin(firstQueue, secondQueue):
	
	# Step 3.1: If second queue is empty,
	# dequeue from first queue
	if secondQueue.isEmpty():
		return firstQueue.dequeue()

	# Step 3.2: If first queue is empty,
	# dequeue from second queue
	if firstQueue.isEmpty():
		return secondQueue.dequeue()

	# Step 3.3: Else, compare the front of
	# two queues and dequeue minimum
	if (firstQueue.queue[0].freq <
		secondQueue.queue[0].freq):
		return firstQueue.dequeue()

	return secondQueue.dequeue()

# The main function that builds Huffman tree
def buildHuffmanTree(data, freq, size):
	
	# Step 1: Create two empty queues
	firstQueue = Queue()
	secondQueue = Queue()

	# Step 2: Create a leaf node for each unique
	# character and Enqueue it to the first queue
	# in non-decreasing order of frequency.
	# Initially second queue is empty.
	for i in range(size):
		firstQueue.enqueue(QueueNode(data[i], freq[i]))

	# Run while Queues contain more than one node.
	# Finally, first queue will be empty and
	# second queue will contain only one node
	while not (firstQueue.isEmpty() and
			secondQueue.isSizeOne()):
					
		# Step 3: Dequeue two nodes with the minimum
		# frequency by examining the front of both queues
		left = findMin(firstQueue, secondQueue)
		right = findMin(firstQueue, secondQueue)

		# Step 4: Create a new internal node with
		# frequency equal to the sum of the two
		# nodes frequencies. Enqueue this node
		# to second queue.
		top = QueueNode("$", left.freq + right.freq,
						left, right)
		secondQueue.enqueue(top)

	return secondQueue.dequeue()

# Prints huffman codes from the root of
# Huffman tree. It uses arr[] to store codes
def printCodes(root, arr):
	
	# Assign 0 to left edge and recur
	if root.left:
		arr.append(0)
		printCodes(root.left, arr)
		arr.pop(-1)

	# Assign 1 to right edge and recur
	if root.right:
		arr.append(1)
		printCodes(root.right, arr)
		arr.pop(-1)

	# If this is a leaf node, then it contains
	# one of the input characters, print the
	# character and its code from arr[]
	if root.isLeaf():
		print(f"{root.data}: ", end = "")
		for i in arr:
			print(i, end = "")
			
		print()

# The main function that builds a Huffman
# tree and print codes by traversing the
# built Huffman tree
def HuffmanCodes(data, freq, size):
	
	# Construct Huffman Tree
	root = buildHuffmanTree(data, freq, size)

	# Print Huffman codes using the Huffman
	# tree built above
	arr = []
	printCodes(root, arr)

# Driver code
arr = ["a", "b", "c", "d", "e", "f"]
freq = [5, 9, 12, 13, 16, 45]
size = len(arr)

HuffmanCodes(arr, freq, size)

# This code is contributed bymathew
