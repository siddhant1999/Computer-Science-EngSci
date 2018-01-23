import math
def pal(x):
	return x+ x[:-1][::-1]
print pal("abc")

#just remember that you cannot take input in the sublime text

num=900.0
def bab(p, i):
	print "N:", p, i
	if i>10:
		return p
	return bab((num/p + p)/2.0, i+1)
print bab(1.0,1)

#print math.sqrt(500.0)-bab(1.0, 1)
def LeibnizPi(n):
	num = 0.0;
	for x in range(n+1):
		if x%2:
			num-=1.0/(2.0*x+1.0);
		else:
			num+=1.0/(2.0*x+1.0);
	return num*4.0
print(LeibnizPi(10000))