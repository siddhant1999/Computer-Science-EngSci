from tree import *
from binary_tree import *
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
    	#print x[0]
    	if type(x[0])!=list:
    		self.l[num-1]+= [x[0]]

    	for i in range(len(y)):
    		#for j in range(num):
    			#print "->",
    		self.P(y[i].store, num+1)

    def Get_LevelOrder(self):
    	self.P(self.store, 1)
    	return reduce(lambda x,y :x+y ,self.l)

    def ConvertToBinaryTree(self):
    	p=  self.hel(self.store[0], self.store, [])
    	y=binary_tree(p)
    	return y


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





class binary_tree:
	def __init__(self,x):
		if type(x)==list:
			self.s = [x[0], binary_tree(x[1]), binary_tree(x[2])]
		else:
			self.s = [x, None, None]
		self.l = [[]]

	def AddLeft(self, x):
		self.s[1] = x

	def AddRight(self, x):
		self.s[2] = x

	def P(self, x, num):
		if len(self.l) < num:
			self.l.append([])

		if x[0] is not None:
			self.l[num-1]+= [x[0]]
		
		if x[1] is not None:
			self.P(x[1].s, num+1)

		if x[2] is not None:
			self.P(x[2].s, num+1)

	def Get_LevelOrder(self):
		self.P(self.s, 1)
		return reduce(lambda x,y :x+y ,self.l)

	def sel(self, node):
		# print "rec->", node
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
	def makeTree(self, k):
		#you recieve a list
		# print "k:", k
		a=tree(k[0])
		for i in range(len(k[1])):
			# print "iii:", k[1][i]
			a.AddSuccessor(self.makeTree(k[1][i]))
		return a
				
	def ConvertToTree(self):
		self.store =[None,[]]
		if self.s[2]:
			return [False]
		else:
			p= self.sel(self.s)
			# print "p", p
			y= self.makeTree(p)
			return y
			#print "y", y.store[1]
			return y

	
