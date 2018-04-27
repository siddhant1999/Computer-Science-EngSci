a =[8,7,6,5,4,5,9,9,9,9,6]
#a=[2,3]
def q(arr):
	#print arr
	#print arr
	if len(arr) == 1:
		return [arr[0]] 
	if len(arr) < 1:
		return []
	piv = arr[-1]
	#print piv

	i =0

	for x in range(len(arr)):
		if arr[x] <= piv:
			abc= arr[i]
			arr[i]= arr[x]
			arr[x] = abc

			i+=1
			
	return q(arr[0:i-1]) + q(arr[i-1:])

print q(a)