def bubblesort(array):
	if len(array)<1:
		return [False, array]
	while True:
		t = False
		for i in range(len(array)-1):
			
			if array[i] > array[i+1]:
				c = array[i]
				array[i] = array[i+1]
				array[i+1] = c
				t = True
		if t == False:
			return [True, array]
	
