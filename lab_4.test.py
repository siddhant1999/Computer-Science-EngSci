from tttlib import *

print "INFO: sample auto tester"
print "INFO: tester MUST complete to receive a score"

errcnt = 0
tot    = 0

def copyList(T,L):
   for i in range(0,len(L)):
      if L[i] != 0:
         T.Move(i,L[i])
   return True

print "INFO: testing analyzeBoard: win cases"
for t in [ \
   [ 1,1,1, 0,0,0, 0,0,0 ], \
   [ 0,0,0, 1,1,1, 0,0,0 ], \
   [ 0,0,0, 0,0,0, 1,1,1 ], \
   [ 1,0,0, 1,0,0, 1,0,0 ], \
   [ 0,1,0, 0,1,0, 0,1,0 ], \
   [ 0,0,1, 0,0,1, 0,0,1 ], \
   [ 1,0,0, 0,1,0, 0,0,1 ], \
   [ 0,0,1, 0,1,0, 1,0,0 ]]:
   for player in [1,2]:
      x=ttt()
      u=map(lambda x: player if x==1 else 0,t)
      copyList(x,u)
      err = False
      dut = x.analyzeBoard()
      tot +=1
      if dut != player:
         errcnt += 1
         err = True
         print "ERR: analyzeBoard [win]",u,dut,player

print "INFO: testing analyzeBoard: play cases"
for i in range(0,9):
   for p in [1,2]:
      T=[0 for k in range(0,9)]
      T[i]=p
      x=ttt()
      copyList(x,T)
      err = False
      tot += 1
      if x.analyzeBoard() != 0:
         err=True
         errcnt += 1
         print "ERR: analyseBoard [play]",T

print "INFO: testing analyzeBoard: draw cases"
for t in [\
   [ 1,1,2, 2,2,1, 1,1,2 ], \
   [ 2,2,1, 1,1,2, 2,2,1 ], \
   [ 1,2,1, 2,1,2, 2,1,2 ], \
   [ 2,1,2, 1,2,1, 1,2,1 ] ]:
   err = False
   tot += 1
   x=ttt()
   copyList(x,t)
   if x.analyzeBoard() != 3:
      err=True
      errcnt += 1
      print "ERR: analyzeBoard [ draw]",t

print "INFO: testing genWinningMove & genNonLoser"
for (t,gold) in [\
   ([0,1,1,0,0,0,0,0,0], 0),\
   ([1,0,1,0,0,0,0,0,0], 1),\
   ([1,1,0,0,0,0,0,0,0], 2),\
   ([0,0,0,0,1,1,0,0,0], 3),\
   ([0,0,0,1,0,1,0,0,0], 4),\
   ([0,0,0,1,1,0,0,0,0], 5),\
   ([0,0,0,0,0,0,0,1,1], 6),\
   ([0,0,0,0,0,0,1,0,1], 7),\
   ([0,0,0,0,0,0,1,1,0], 8),\
   ([1,0,0,0,1,0,0,0,0], 8),\
   ([1,0,0,0,0,0,0,0,1], 4),\
   ([0,0,0,0,1,0,0,0,1], 0),\
   ([0,0,1,0,1,0,0,0,0], 6),\
   ([0,0,0,0,1,0,1,0,0], 2),\
   ([0,0,1,0,0,0,1,0,0], 4,),\
   ([0,1,0,0,0,0,0,0,0], -1),\
   ([1,0,0,0,0,0,0,0,0], -1),\
   ([1,0,0,0,0,0,0,0,0], -1),\
   ([0,0,0,0,1,0,0,0,0], -1),\
   ([0,0,0,0,0,1,0,0,0], -1),\
   ([0,0,0,1,0,0,0,0,0], -1),\
   ([0,0,0,0,0,0,0,0,1], -1),\
   ([0,0,0,0,0,0,0,0,1], -1),\
   ([0,0,0,0,0,0,1,0,0], -1),\
   ([1,0,0,0,0,0,0,0,0], -1),\
   ([0,0,0,0,0,0,0,0,1], -1),\
   ([0,0,0,0,1,0,0,0,0], -1),\
   ([0,0,1,0,0,0,0,0,0], -1),\
   ([0,0,0,0,0,0,1,0,0], -1),\
   ([0,0,1,0,0,0,0,0,0], -1)\
   ]:
   for player in [1,2]:
      tot += 5
      T=map(lambda x:player if x==1 else 0,t)
      x=ttt()
      copyList(x,T)
      r=x.genWinningMove(player)
      if r != gold:
         print "ERR: genWinningMove:",T,"player:",player,"you:",r,"gold:",gold
         errcnt += 5
      tot += 5
      opponent=1 if player==2 else 2
      T=map(lambda x:opponent if x==1 else 0,t)
      x=ttt()
      copyList(x,T)
      r=x.genNonLoser(player)
      if r != gold:
         print "ERR: genNonLoser:",T,"player:",player,"you:",r,"gold:",gold
         errcnt += 5

print "INFO: testing genRandomMove"
for i in [\
   [0,0,0,0,0,0,0,0,0],\
   [1,0,0,0,1,0,1,0,0],\
   [0,1,0,0,0,0,0,0,0],\
   [0,1,1,0,1,1,0,0,0],\
   [0,1,1,1,0,0,1,0,0],\
   [0,1,0,1,1,0,0,0,0],\
   [0,0,1,0,1,1,0,0,0],\
   [0,0,1,1,0,1,1,0,0],\
   [0,0,0,1,1,0,1,1,0],\
   [0,0,0,0,1,1,0,1,1],\
   [2,0,0,0,2,0,2,0,0],\
   [0,2,0,0,0,0,0,0,0],\
   [0,2,2,0,2,2,0,0,0],\
   [0,2,2,2,0,0,2,0,0],\
   [0,2,0,2,2,0,0,0,0],\
   [0,0,2,0,2,2,0,0,0],\
   [0,0,2,2,0,2,2,0,0],\
   [0,0,0,2,2,0,2,2,0],\
   [0,0,0,0,2,2,0,0,2]]:
   x=ttt()
   copyList(x,i)
   u=x.genRandomMove(1)
   tot += 3
   if type(u) != int or u == -1:
      print "ERR: genRandomMove returned an erroneous result",i,u
      errcnt += 3
   elif i[u] != 0:
      print "ERR: genRandomMove returned occupied location, or board was modified",i,u
      errcnt += 3

print "INFO: testing genRandomMove"
for i in [\
   [1,1,1,1,1,1,1,1,1],\
   [1,2,1,2,1,2,1,2,1],\
   [2,2,2,2,1,2,2,2,2]]:
   tot += 3
   x=ttt()
   copyList(x,i)
   u=x.genRandomMove(2)
   if not(u == -1):
      print "ERR: genRandomMove didn't return -1 for full board",i,u
      errcnt += 3

#print "You scored:",errcnt,"out of maximum badness",tot
print "GRADE:",tot-errcnt,"out of",tot