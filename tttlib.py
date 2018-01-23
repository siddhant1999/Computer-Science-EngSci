from random import randint
class ttt:
	def __init__(self):
		self.T=[0 for i in range(0,9)]

	def analyzeBoard(self):
	        #b print "printing board: "
	        #printBoard(self.T)
	        #perhaps an error could be significantly more x's than o's and vice versa
	        #return str.join(self.T)
	        if len(self.T) != 9:
	                return -1
	
	        n = 3
	        t = [self.T[i:i+3] for i in range(0, len(self.T), 3)]
	        a = [1,1,1]
	        o = [2,2,2]
	
	        if (t[0] == a) or (t[1] == a) or (t[2] == a):
	                return 1
	
	        if ([t[0][0], t[1][0], t[2][0]] == a) or ([t[0][1], t[1][1], t[2][1]] == a) or ([t[0][2], t[1][2], t[2][2]] == a):
	                return 1
	
	        if ([t[0][0], t[1][1], t[2][2]] == a) or ([t[2][0], t[1][1], t[0][2]] == a):
	                return 1
	
	        if (t[0] == o) or (t[1] == o) or (t[2] == o):
	                return 2
	
	        if ([t[0][0], t[1][0], t[2][0]] == o) or ([t[0][1], t[1][1], t[2][1]] == o) or ([t[0][2], t[1][2], t[2][2]] == o):
	                return 2
	
	        if ([t[0][0], t[1][1], t[2][2]] == o) or ([t[2][0], t[1][1], t[0][2]] == o):
	                return 2
	        for i in xrange(0,9):
	                if self.T[i] == 0:
	                        return 0
	
	        return 3
	def helper(self, l):
	        #b print "printing board: "
	        #printBoard(self.T)
	        #perhaps an error could be significantly more x's than o's and vice versa
	        #return str.join(self.T)
	        if len(l) != 9:
	                return -1
	
	        n = 3
	        t = [l[i:i+3] for i in range(0, len(l), 3)]
	        a = [1,1,1]
	        o = [2,2,2]
	
	        if (t[0] == a) or (t[1] == a) or (t[2] == a):
	                return 1
	
	        if ([t[0][0], t[1][0], t[2][0]] == a) or ([t[0][1], t[1][1], t[2][1]] == a) or ([t[0][2], t[1][2], t[2][2]] == a):
	                return 1
	
	        if ([t[0][0], t[1][1], t[2][2]] == a) or ([t[2][0], t[1][1], t[0][2]] == a):
	                return 1
	
	        if (t[0] == o) or (t[1] == o) or (t[2] == o):
	                return 2
	
	        if ([t[0][0], t[1][0], t[2][0]] == o) or ([t[0][1], t[1][1], t[2][1]] == o) or ([t[0][2], t[1][2], t[2][2]] == o):
	                return 2
	
	        if ([t[0][0], t[1][1], t[2][2]] == o) or ([t[2][0], t[1][1], t[0][2]] == o):
	                return 2
	        for i in xrange(0,9):
	                if l[i] == 0:
	                        return 0
	
	        return 3
	def Move(self, m, player):
	        if self.T[m] == 0:
	        	self.T[m] = player;
	        	return True
	        return False
	
	def printBoard(self):
	        l = list(self.T)
	        if len(l) != 9:
	                return False
	
	        for m in xrange(0,9):
	                if l[m]==1:
	                        l[m]= 'X'
	                elif l[m]==2:
	                        l[m]= 'O'
	                elif l[m] == 0:
	                        l[m] = m
	                else:
	                        return False
	
	        print "", l[0] , "|" , l[1] , "|" , l[2]
	        print "---|---|---"
	        print "",l[3] , "|" , l[4] , "|" , l[5]
	        print "---|---|---"
	        print "",l[6] , "|" , l[7] , "|" , l[8]
	
	        return True
	
	def genRandomMove(self,player):
	        if len(self.T) != 9:
	                return -1
	        if 0 not in self.T:
	                return -1
	
	        s = 0
	        while self.T[s] != 0:
	                s +=1
	        return s
	
	def genWinningMove(self,player):
	        if len(self.T) != 9:
	                return -1
	        for o in xrange(0,9):
	                if self.T[o] != 1 and self.T[o] != 2 and  self.T[o] != 0:
	                        return -1
	        l = list(self.T)
	        for m in xrange(0,9):
	                if l[m] == 0:
	                        l[m] = player;
	                        if self.helper(l) == player:
	                                return m
	                        l[m] = 0
	
	        return -1
	
	def genNonLoser(self, player):
	        if len(self.T) != 9:
	                return -1
	        l = list(self.T)
	        for o in xrange(0,9):
	        	if self.T[o] != 1 and self.T[o] != 2 and  self.T[o] != 0:
	                        return -1
	
	        if player == 1:
	                player = 2
	        else:
	                player = 1
	
	        for m in xrange(0,9):
	                if l[m] == 0:
	                        l[m] = player;
	                        if self.helper(l) == player:
	                                return m
	                        l[m] = 0
	
	        return -1

'''x=ttt()
x.genWinningMove(1)
x.printBoard()'''