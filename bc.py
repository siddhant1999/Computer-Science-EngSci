from stackLib import stackLib

def opp(x):
	if x==')':
		return '('
	if x=='}':
		return '{'
	if x==']':
		return '['
	return x

def bc(inp):
	fail = -1
	x=stackLib()
	cnt = 0
	for c in inp:
		#print x.lis
		cnt+=1
		if not x.lis:
			if c=='(' or c=='{' or c=='[':
				x.push(c)
			elif c==')' or c==']' or c=='}':
				return [False, cnt]
			else:
				continue
		elif opp(c)==x.lis[-1]:
			x.pop()
		else:
			if c==')' or c==']' or c=='}':
				fail = cnt
			elif c=='(' or c=='{' or c=='[':
				x.push(c)
	
	if x.lis :
		if fail==-1:
			fail=cnt
		return [False, fail]
	return [True]

print bc("()({})[][]")

