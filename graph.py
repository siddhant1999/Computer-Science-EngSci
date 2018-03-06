class graph:
	edges =[[None] * 5 for i in range(5)]
	line=[]
	visited =[]
	tot=[]
	def __init__(self):
		self.vertices=0

	def addVertex(self, n):
		self.vertices+= n
		return self.vertices

	def addEdge(self, from_idx, to_idx, directed, weight):
		#print from_idx, to_idx, weight
		self.edges[from_idx][to_idx] = weight
		if not directed:
			self.edges[to_idx][from_idx] = weight
		#print self.edges

	def BFS(self, start, visited):
		t= []
		line = [start]
		for i in range(100000):
			if i==len(self.line):
				break
			if line[i] in visited:
				continue
			#print self.line[i]
			t += [line[i]]
			visited += [line[i]]
			for j in range(self.vertices):
				if self.edges[line[i]][j] != 0 and self.edges[line[i]][j] != None:
					line += [j]
		return t


	def traverse(self, start, typeBreadth):
		#print self.edges
		#still need to make sure start can be None
		#also make sure you check indices that are not connected
		if start == None:
			start = 0

		self.line = [start]
		visited = []
		if typeBreadth:
			self.tot= []
			for i in range(100000):
				if i==len(self.line):
					break
				if self.line[i] in visited:
					continue

				#print self.line[i]
				self.tot += [self.line[i]]
				visited += [self.line[i]]
				for j in range(self.vertices):
					if self.edges[self.line[i]][j] != 0 and self.edges[self.line[i]][j] != None:
						self.line += [j]
				#print self.line
				
		else:
			self.visited =[]
			self.tot=[]
			self.dfs(start)
			
		if start == None:
			for i in range(len(self.vertices)):
				if i not in self.tot:
					if typeBreadth:
						self.tot+=BFS(i, visited)
					else:
						self.dfs(i)
		print self.tot

	def dfs(self, index):
		if index in self.visited:
			return
		self.visited += [index]
		self.tot+=[index]
		#print index
		for i in range(self.vertices):
			if self.edges[index][i] != 0 and self.edges[index][i] != None:
				self.dfs(i)

	def atob(self, a, b):
		if a==b:
			return True
		for i in range(self.vertices):
			if self.edges[self.line[a]][i] != 0 and self.edges[self.line[a]][i] != None:
				self.totpath.append(i)
				isO = self.atob(i, b)

				if isO:
					return True
				self.totpath = self.totpath[:-1]
		return False


	def connectivity(self, vx, vy):

		return [self.atob(vx, vy), self.atob(vy,vx)]

	def path(self, vx, vy):
		ret = []
		self.totpath =[vx]
		if self.atob(vx,vy):
			ret += [self.totpath]
		else:
			ret += [[]]

		self.totpath =[vy]
		if self.atob(vy,vx):
			ret += [self.totpath]
		else:
			ret += [[]]

		return ret



		

x = graph()

x.addVertex(4)
x.addEdge(0, 1, True, 1)
x.addEdge(0, 3, True, 1)
x.addEdge(3, 2, True, 1)
x.addEdge(3, 1, True, 1)
x.traverse(None, False)
