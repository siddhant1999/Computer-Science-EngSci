class binary_tree:
	def __init__(self,x):
		self.s = [x, None, None]
		self.l = [[]]

	def AddLeft(self, x):
		self.s[1] = x

	def AddRight(self, x):
		self.s[2] = x

	def P(self, x, num):
		if len(self.l) < num:
			self.l.append([])
		
		self.l[num-1]+= [x[0]]
		
		if x[1] is not None:
			self.P(x[1].s, num+1)

		if x[2] is not None:
			self.P(x[2].s, num+1)

	def Get_LevelOrder(self):
		self.P(self.s, 1)
		return reduce(lambda x,y :x+y ,self.l)

	def sel(self, node):
		print "rec->", node
		#convert this level of the tree to a binary tree
		x=[node[0],[]]
		curnode = node[1]#lefttree
		while curnode != [] and curnode != None:
			x[1].append(self.sel(curnode.s))
			curnode=curnode.s[2]

			#meaning it has a child, therefore look for siblings
			#go right all the way down the tree

		return x
		#return the left subtree
				
	def ConvertToTree(self):
		self.store =[None,[]]
		print self.sel(self.s)

	

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
    	y=x[1]
    	print x[0]
    	self.l[num-1]+= [x[0]]

    	for i in range(len(y)):
    		for j in range(num):
    			print "->",
    		self.P(y[i].store, num+1)

    def Get_LevelOrder(self):
    	P(self.store, 1)
    	return reduce(lambda x,y :x+y ,self.l)

    def hel(self, val, left_tree, right_tree):
		#print val, "<<>>" , left_tree, "<<>>", right_tree 
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


k= tree(1)
p = k.hel(q.store[0], q.store, [])
print "Here -->: ", p

a =binary_tree(1)
b = binary_tree(2)
c = binary_tree(3)
d = binary_tree(4)
e = binary_tree(5)
f = binary_tree(6)
g = binary_tree(7)

e.AddRight(f)
b.AddLeft(e)

c.AddLeft(g)
c.AddRight(d)
b.AddRight(c)
a.AddLeft(b)

print a.Get_LevelOrder()
print "Converting to Tree"
a.ConvertToTree()

