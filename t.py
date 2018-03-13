import sys
for l in xrange(15):
	f=sys.stdin.readline()
	s= "img/" + f.rstrip() + ".jpg"
	print s
