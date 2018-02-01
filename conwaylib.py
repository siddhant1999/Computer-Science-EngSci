import random

class conway:
        def __init__(self, a, b, c):
                self.a = a
                self.b = b
                self.c = c
                self.store = []
                self.p = []
                self.y = 0

                if self.c == 'zeros':
                        for i in range (0,self.a):
                                for t in range (0,self.b):
                                        self.p.append(0)

                                self.store.append(self.p)
                                self.p = []
                elif c == 'random':
                        for i in range (0,self.a):
                                for t in range (0,self.b):
                                        self.y = random.randint(0,1)
                                        self.p.append(self.y)

                                self.store.append(self.p)
                                self.p = []
                #print self.store
        '''def rule(self, val, l):
                #print sum(l)
                if val == 1:
                        if  sum == 3 or sum == 2:
                                return 1
                        return 0
                if sum == 3:
                        return 1
                return 0
        '''
        def getDisp(self):
                s = ""
                for i in range(len(self.store)):
                        for j in range(len(self.store[i])):
                                if self.store[i][j]:
                                        s+="*"
                                else:
                                        s+=" "
                        s+="\n"

                return s
        def printDisp(self):
                print self.getDisp()
                return True;

        def setPos(self, row,col,val):
                if val == 1 or val == 0:
                        self.store[row][col] = val;
                        return True
                return False

        def getNeighbours(self, row,col):
                s=[]
                for i in range(-1,2,1):
                        for j in range(-1,2,1):
                                if i == 0 and j == 0:
                                        continue
                                s.append(self.store[(row+i)%(self.a)][(col+j)%(self.b)])
                return s

        def evolve(self, r):
                x=[]
                p =[]
                for i in range (0,self.a):
                                for t in range (0,self.b):
                                        p.append(0)

                                x.append(p)
                                p = []
                #print x
                
                #self.printDisp() 
                for i in range (0,self.a):
                        for t in range (0,self.b):
                                x[i][t] = r(self.store[i][t], self.getNeighbours(i,t))
                                #if i == 12 and t==0:
                                #print self.getNeighbours(i,t)


                #self.store = x
                for i in range (0,self.a):
                        for t in range (0,self.b):
                                self.store[i][t] = x[i][t]

                #print x
                #self.printDisp()
                #print x
                #return x
                #self.printDisp()
                #print ""
                #print (x)



#x.printDisp()