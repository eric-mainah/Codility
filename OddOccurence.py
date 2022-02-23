def solution(A):

	# Initialize result
	res = 0
	
	# Traverse the array
	for element in A:
		# XOR with the result
		res = res ^ element

	return res
	
exam = [9,3,9,3,9,7,9]

print("%d" %solution(exam))
