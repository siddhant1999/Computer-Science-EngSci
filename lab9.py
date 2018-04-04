def quick_sort(u,ini,fin):
	helper_quicksort(u,ini,fin)
	return True

def helper_quicksort(u,ini,fin):
	if ini < fin:
		splitpoint = partition(u,ini,fin)

		helper_quicksort(u,ini,splitpoint - 1)
		helper_quicksort(u,splitpoint + 1,fin)
		
def partition(u,ini,fin):
	left = ini + 1
	right = fin
	pivot = u[ini]
	run = False
	
	while not run:
		while (left <= right and u[left] <= pivot):
			left = left + 1

		while (u[right] >= pivot and right >= left):
			right = right - 1

		if right < left:
			run = True
			
		else:
			temp = u[left]
			u[left] = u[right]
			u[right] = temp

	temp = u[ini]
	u[ini] = u[right]
	u[right] = temp

	return right

# QUICK SORT TESTING CODE
# v1=[10,9,8,7,6,5,4,3,2,1,0]
# v2=[100,1,1000,9,8,7,2,2000,10]
# v3=[100,10,1000,9,8,7,2,6,5,2,3,1]

# for i in [v1,v2,v3]:
   # x=list(i)
   # quick_sort(x,0,len(x)-1)
   # print x

def hanoi(accum, n, start, tmp, final):
	if n > 0:
		hanoi(accum,n - 1, start, final, tmp)
		final.append(start.pop())
		hanoi(accum,n - 1, tmp, start, final)
		accum += [start,tmp,final]
		return True
	else:
		return True

# HANOI TESTING CODE		
# start = [5,4,3,2,1]
# final = []
# tmp = []
# accum = []
# print start, tmp, final

# hanoi(accum,len(start),start,tmp,final)

# print start, tmp, final