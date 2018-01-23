class stack:
	store=[]
	def push(self, x):
		self.store=self.store+[x]
	def disp(self):
		for i in range(0, len(self.store)):
			print self.store[i]
	def pop(self):
		if len(self.store):
			rval=self.store[len(self.store)-1]
			self.store=self.store[0:len(self.store)-1]
			return rval
		return False


x=stack()
x.push(1)
x.push(2)
x.push("sdf")
x.push(4)

x.disp()
print ""
print x.pop()
print ""
x.disp()
print ""
print x.pop()
print ""
x.disp()
print ""
print x.pop()
print ""
x.disp()
print ""
print x.pop()
print ""
x.disp()
print ""
print x.pop()
print ""
x.disp()
print ""
print x.pop()
print ""
x.disp()
print ""
print x.pop()
print ""
x.disp()