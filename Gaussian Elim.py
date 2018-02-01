



def ge_fw(matrix):
	#permute to the top
	for aa in range(min(len(matrix), len(matrix[0]))):
		for i in range(len(matrix)-aa):
			if matrix[i+aa][aa] != 0:
				#swap
				matrix[aa], matrix[i+aa] = matrix[i+aa], matrix[aa]
				#try removing this for loop and see if anything changes
				for p in range(len(matrix[aa])-aa):
					matrix[aa][p+aa] /= matrix[aa][aa]
				break
		#add multiples
		#print matrix[0][0]
		for i in range(len(matrix)-1-aa):
			j = i+1+aa
			dif = matrix[j][aa]/matrix[aa][aa]
			#print "diff: ", dif
			for x in range(len(matrix[j])-aa):
				matrix[j][x+aa] -=dif*matrix[aa][x+aa]
				
		#print matrix
	return matrix
		#matrix = matrix[1:]
		#for i in range(len(matrix)):
			#matrix[i] = matrix[i][1:]
		#print matrix


def ge_bw(matrix):
	m = min(len(matrix), len(matrix[0]))
	for bb in range(m):
		aa = m-bb-1
		#normalize
		yy = 0
		yes = 0
		for x in range(len(matrix[aa])-aa):
			if yes == 0:
				yes = matrix[aa][x+aa]
				if yes!= 0:
					yy = x+aa
			if yes != 0:
				matrix[aa][x+aa] /= yes
		if yes == 0:
			continue

		for i in range(aa):
			 j = aa-i-1 # col
			 diff = matrix[j][yy]
			 #print diff
			 for k in range(len(matrix[j])-aa):
			 	p = k + aa
			 	matrix[j][p] -= diff*matrix[aa][p]
	return matrix
			 