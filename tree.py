class binary_tree:
	def __init__(self,x):
		self.s = [x, None, None]

	def AddLeft(self, x):
		self.s[1] = [x]

	def AddRight(self, x):
		self.s[2] = [x] 

	

class tree:
    def __init__(self,x):
        self.store = [x,[]]
        self.l = [[]]

    def AddSuccessor(self,x):
        self.store[1] = self.store[1] + [x]
		# print x.store[1][1].store
        return True

    def P(self, x, num):
    	if len(self.l) < num:
    		self.l.append([])
    	# print x
    	# print x[1]
    	# print x[1][0].store
    	y=x[1]
    	print x[0]
    	self.l[num-1]+= [x[0]]
    	# print self.P(y[0].store)
    	for i in range(len(y)):
    		for j in range(num):
    			print "->",
    		self.P(y[i].store, num+1)

    def hel(self, val, left_tree, right_tree):
		print val, "<<>>" , left_tree, "<<>>", right_tree 
		x= [val, None, None]
		y=left_tree[1]#this is a list of list of trees
		z= right_tree
		if (y):
			x[1] = self.hel(y[0].store[0], y[0].store, y[1:])

		if len(z) == 0:
			x[2] = None;
		else:
			x[2] = self.hel(z[0].store[0], z[0].store, z[1:])
		return x



x=tree(1000)
y=tree(2000)
z=tree(3000)
x.AddSuccessor(y)
x.AddSuccessor(z)
c=tree(5)
z.AddSuccessor(c)

# x.Print_DepthFirst()
x.P(x.store, 1)
print x.l

t= x.store
q= tree(1)
w=tree(2)
e=tree(3)
r=tree(4)
t=tree(5)
l=tree(6)
s=tree(7)

w.AddSuccessor(t)
w.AddSuccessor(l)
e.AddSuccessor(s)

q.AddSuccessor(w)
q.AddSuccessor(e)
q.AddSuccessor(r)


q.P(q.store, 1)
print q.l
print reduce(lambda x,y :x+y ,q.l)

k= tree(1)
p = k.hel(q.store[0], q.store, [])
print "Here -->: ", p


