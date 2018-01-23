class seqdetectorlib:

	def __init__(self):
		self.count = 0
	def evolve(self, word):
		

		l = ["here", "are", "the", "solutions", "to", "the", "next", "exam"]
		#print l
		if word == l[self.count]:
			self.count+=1
			if self.count == 8:
				return  True
			 return False
		else:
			self.count=0
			if l[self.count] == word:
				self.count = 1;
			return False