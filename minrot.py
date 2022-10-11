# Python3 program for min rotation to unlock

# function for min rotation
def minRotation(input, unlock_code):

	rotation = 0;

	# iterate till input and unlock
	# code become 0
	while (input > 0 or unlock_code > 0):

		# input and unlock last digit
		# as reminder
		input_digit = input % 10;
		code_digit = unlock_code % 10;

		# find min rotation
		rotation += min(abs(input_digit - code_digit),
					10 - abs(input_digit - code_digit));

		# update code and input
		input = int(input / 10);
		unlock_code = int(unlock_code / 10);

	return rotation;

# Driver Code
input = 333666;
unlock_code = 2476;
print("Minimum Rotation =",
	minRotation(input, unlock_code));
	
# This code is contributed by Mathew Saju
