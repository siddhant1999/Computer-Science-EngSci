def search(lst, target):
  min = 0
  max = len(lst)-1
  avg = (min+max)/2
  # uncomment next line for traces
  # print lst, target, avg  
  while (min < max):
    if (lst[avg] == target):
      return avg
    elif (lst[avg] < target):
      return avg + 1 + search(lst[avg+1:], target)
    else:
      return search(lst[:avg], target)

  # avg may be a partial offset so no need to print it here
  # print "The location of the number in the array is", avg 
  return avg

def best(used, se, p, cache={}):
	ooo = tuple(used)
	if ooo in cache:
		return cache[ooo]
	
	g=[]
	for i in used:
		w = se[i]
		a= []
		b = []
		a= [w[0], 1]
		b = [w[1], 0]
		g.append(a)
		g.append(b)
	g.sort()
	
	count = 0

	for i in range(len(g)):
		if g[i][1] == 1:
			count +=1
		if g[i][1] == 0:
			count -=1
		if count>3:
			cache[ooo] = -1
			return 0
	
	'''
	for i in range(p):
		c=0
		for k in used:#j is an array of 2
			j= se[k]
			if i>= j[0] and i <j[1]:
				c+=1
		if c>3:
			cache[tuple(used)] = -1
			return 0;#or -1

	'''
	m = 0
	pp= used

	for qw in range(len(se)):
		if len(used):
			i = used[len(used)-1] + qw +1
			if i >= len(se):
				break;
		else:
			i = qw

		r = used
		used.insert(search(used, i)+1, i)
		#used.append(i)
		#used.sort()
		pp = used

		y = best(used, se, p)
		if y > m:
			m = y
			
		used= r
	cache[tuple(pp)] = m+1
	return m+1

def  max_florists(path_length, florist_intervals):
	x= []
	for i in range(len(florist_intervals)):
		w= florist_intervals[i]
		if w[0] >= path_length:
			continue
		if w[1] >= path_length:
			florist_intervals[i][1] = path_length
			w= florist_intervals[i]
		x.append(w)
	return best([], x, path_length)-1

print max_florists(5, [[0, 1], [0, 1], [0, 1], [1, 2], [1, 2], [0, 3]])
