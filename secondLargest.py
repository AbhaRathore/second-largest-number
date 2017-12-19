#Program to find second largest number:

import sys
def secondLargestNumber(arr):
	if len(arr)<2:
		return "Only single element in array. No Second largest number!"

	first = second = -(sys.maxint)-1
	for i in arr:
		if i > first:
			second = first
			first = i
		elif i > second and i != first:
			second = i
	
	if second == -(sys.maxint)-1:
		return "No Second Lagrest Number!"
	else:
		return second

num_arr = []
x= raw_input("Enter the array size: ")
print "Enter array elements: "

for i in range(int(x)):
	n = raw_input("")
	num_arr.append(int(n))

print num_arr 
print secondLargestNumber(num_arr)