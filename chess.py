'''
Pawn:   +0
Knight: +1
Bishop: +2
Rook:   +3
Queen:  +4
King:   +5
'''
import random
import time

def isWhite(n):
	if n >= 10 and n < 20:
		return True
	return False

def isValid(num):
	if num>= 0 and num<64:
		return True
	return False

def HorseValid(a, b):
	if abs(a/8 - b/8)>2 or abs(a%8-b%8)>2:
		return False
	return True

def printBoard(board):
	for i in range(len(board)-1, -1, -1):
		
		if board[i] == 0:
			if (i/8)%2:
				if i%2:
					print "#",
				else:
					print ".",
			else:
				if i%2:
					print ".",
				else:
					print "#",

		elif board[i]%10 == 0:
			if isWhite(board[i]):
				print "P",
			else:
				print "p",

		elif board[i]%10 == 1:
			if isWhite(board[i]):
				print "H",
			else:
				print "h",

		elif board[i]%10 == 2:
			if isWhite(board[i]):
				print "B",
			else:
				print "b",

		elif board[i]%10 == 3:
			if isWhite(board[i]):
				print "R",
			else:
				print "r",

		elif board[i]%10 == 4:
			if isWhite(board[i]):
				print "Q",
			else:
				print "q",

		elif board[i]%10 == 5:
			if isWhite(board[i]):
				print "K",
			else:
				print "k",
		if i%8==0:
			print "\n"
	print "\n"

def IsPositionUnderThreat(board,position,player):
	play = GetPlayerPositions(board, player)
	for i in play:
		l =GetPieceLegalMoves(board, i)
		if position in l:
			return True
	return False

def inCheck(board, colour):
	#let's us first check if white king is in danger
	#first determine where the white king is

	king = colour+5

	#can speed this up by not having to itterate over the entire board state
	for i in range(len(board)):
		if board[i] == king:
			pos = i
			break
	#print pos
	#pos is the position of my king
	if isWhite(king):
		abc =GetPlayerPositions(board, 20)
	else:
		abc =GetPlayerPositions(board, 10)
	for i in abc:
		if GetHit(board, i, pos):
			return True
		#meaning if the king is here it will be taken

	
	for i in range(len(board)):
		if isWhite(board[i]) == isWhite(king):
			continue
		if board[i]%10 == 5:
			#found the other king
			for z in range(-1, 2):
				for q in range(-1, 2):
					k = 8*q
					possi = i+z+q
					if i/8 != (i+z)/8:
						continue#so that lateral movement doesn't put you on the other side of the board
					
					if (q == 0 and z ==0) or not isValid(possi):
						continue
					if possi == pos:
						return True
					#thus the other king
					#check if in my minesweeper
	return False

def GetPlayerPositions(board,player):
	l =[]
	for x in range(len(board)):
		if (isWhite(board[x]) == isWhite(player)) and board[x] != 0:
			l.append(x)

	return l

def Helper(board, position):
	p = board[position]%10 #this is the piece
	l=[]
	if p == 0:
		#pawn

		if isWhite(board[position]):
			if position>=56:
				return l
			if board[position+8]==0:
				l.append(position+8)

			#capture
			if position+7 < 64:
				if isWhite(board[position+7]) != isWhite(board[position]) and board[position+7] != 0:
					if abs((position+7)%8 -position%8) <= 1:
						l.append(position+7)

			if position+9 < 64:
				if isWhite(board[position+9]) != isWhite(board[position]) and board[position+9] != 0:
					if abs((position+9)%8 -position%8) <= 1:
						l.append(position+9)	
		else:
			#print "I am a black pawn", position
			#printBoard(board)
			if position<=7:
				return l
			if board[position-8]==0:
				l.append(position-8)
			#capture
			if position-7 >= 0:
				if isWhite(board[position-7]) != isWhite(board[position]) and board[position-7] != 0:
					if abs((position-7)%8 -position%8) <= 1:
						l.append(position-7)

			if position-9 >= 0:
				if isWhite(board[position-9]) != isWhite(board[position]) and board[position-9] != 0:
					if abs((position-9)%8 -position%8) <= 1:
						l.append(position-9)

	if p == 3 or p == 4:
		#rook or queen
		pos = position+1
		row=position/8
		while(pos/8== row and isValid(pos)):

			#right
			if board[pos] == 0:
				l.append(pos)
				pos+=1
				continue
			if isWhite(board[position]) == isWhite(board[pos]):
				break
			else:
				l.append(pos)
				break

			pos+=1

		pos = position-1
		while(pos/8== row and isValid(pos)):
			#left
			if board[pos] == 0:
				l.append(pos)
				pos-=1
				continue
			if isWhite(board[position]) == isWhite(board[pos]):
				break
			else:
				l.append(pos)
				break

			pos-=1

		pos = position+8
		while(isValid(pos)):
			#down
			if board[pos] == 0:
				l.append(pos)
				pos+=8
				continue
			if isWhite(board[position]) == isWhite(board[pos]):
				break
			else:
				l.append(pos)
				break

			pos+=8

		pos = position-8
		while(isValid(pos)):
			#down
			if board[pos] == 0:
				l.append(pos)
				pos-=8
				continue
			if isWhite(board[position]) == isWhite(board[pos]):
				break
			else:
				l.append(pos)
				break

			pos-=8

	if p == 1:
		#knight, horsey
		#just check the 8 posible moves

		#top left
		if isValid(position-17):
			if board[position-17] == 0 or (isWhite(board[position]) != isWhite(board[position-17])):
				if HorseValid(position, position-17):
					l.append(position-17)
		#left top
		if isValid(position-10):
			if board[position-10] == 0 or (isWhite(board[position]) != isWhite(board[position-10])):
				if HorseValid(position, position-10):
					l.append(position-10)
		#left bottom
		if isValid(position+6):
			if board[position+6] == 0 or (isWhite(board[position]) != isWhite(board[position+6])):
				if HorseValid(position, position+6):
					l.append(position+6)
		#bottom left
		if isValid(position+15):
			if board[position+15] == 0 or (isWhite(board[position]) != isWhite(board[position+15])):
				if HorseValid(position, position+15):
					l.append(position+15)
		#bottom right
		if isValid(position+17):
			if board[position+17] == 0 or (isWhite(board[position]) != isWhite(board[position+17])):
				if HorseValid(position, position+17):
					l.append(position+17)
		#right bottom
		if isValid(position+10):
			if board[position+10] == 0 or (isWhite(board[position]) != isWhite(board[position+10])):
				if HorseValid(position, position+10):
					l.append(position+10)
		#right top
		if isValid(position-6):
			if board[position-6] == 0 or (isWhite(board[position]) != isWhite(board[position-6])):
				if HorseValid(position, position-6):
					l.append(position-6)
		#top right
		if isValid(position-15):
			if board[position-15] == 0 or (isWhite(board[position]) != isWhite(board[position-15])):
				if HorseValid(position, position-15):
					l.append(position-15)
		return l
		
	if p==2 or p==4:
		#bishop or queen
		pos = position+9
		row=position/8
		while(isValid(pos)):
			#right down
			if abs((pos-9)/8 - pos/8)>1 or abs((pos-9)%8-pos%8)>1:
				break

			if board[pos] == 0:
				l.append(pos)
				pos+=9
				continue
			if isWhite(board[position]) == isWhite(board[pos]):
				break
			else:
				l.append(pos)
				break

			pos+=9

		pos = position-9
		while(isValid(pos)):
			if abs((pos+9)/8 - pos/8)>1 or abs((pos+9)%8-pos%8)>1:
				break
			#left up
			if board[pos] == 0:
				l.append(pos)
				pos-=9
				continue
			if isWhite(board[position]) == isWhite(board[pos]):
				break
			else:
				l.append(pos)
				break

			pos-=9

		pos = position+7
		while(isValid(pos)):
			#left down
			if abs((pos-7)/8 - pos/8)>1 or abs((pos-7)%8-pos%8)>1:
				break

			if board[pos] == 0:
				l.append(pos)
				pos+=7
				continue
			if isWhite(board[position]) == isWhite(board[pos]):
				break
			else:
				l.append(pos)
				break

			pos+=7

		pos = position-7
		while(isValid(pos)):
			#down
			if abs((pos+7)/8 - pos/8)>1 or abs((pos+7)%8-pos%8)>1:
				break
			if board[pos] == 0:
				l.append(pos)
				pos-=7
				continue
			if isWhite(board[position]) == isWhite(board[pos]):
				break
			else:
				l.append(pos)
				break

			pos-=7

	
	return l

def GetHit(board, position, target):
	#it is very important to note that this a line of fire problem, as actually making this move may put the opponent in check themselves
	#can board[target] be hit by board[position]
	lis = Helper(board, position)#everything that the board[position] piece can hit
	if target in lis:
		return True
	return False

def GetPieceLegalMoves(board,position):
	'''if board[position] < 10 or board[position] > 25:
		print "ERROR", board[position], position'''

	l=[]
	if board[position]%10 == 5:
		#make sure to check if this king move puts the king in danger
		for i in range(-1, 2):
			for j in range(-1, 2):
				k = 8*j
				pos = position+i+k

				if abs(position/8 - (pos)/8) > 1:
					continue#so that lateral movement doesn't put you on the other side of the board
				if abs(position%8 - (pos)%8) > 1:
					continue

				if (j == 0 and i ==0) or not isValid(pos):
					continue

				if (isWhite(board[pos]) != isWhite(board[position])) or board[pos] == 0:
					t= list(board)
					t[position] =0
					t[pos] = board[position]
	
					if not inCheck(t, board[position]-5):
						l.append(pos)
		return l
	else:

		l = Helper(board, position)
		#print l
		#print l
	#check if by setting the value of board[position] to 0 and then set board[l[i]] to board[position] and check if in check
	#return l

	#issue is here
	actual_l = []
	for i in range(len(l)):
		t= list(board)
		t[position] =0
		t[l[i]]=board[position]
		#printBoard(t)
		#print (board[position]/10)*10
		if(not inCheck(t, (board[position]/10)*10)):
			actual_l.append(l[i])
	return actual_l

def boardValue(board):
	lookup = [None]*30
	lookup[0] = 0
	lookup[10] = 10
	lookup[20] = -10
	lookup[11] = 30
	lookup[21] = -30
	lookup[12] = 30
	lookup[22] = -30
	lookup[13] = 50
	lookup[23] = -50
	lookup[14] = 90
	lookup[24] = -90
	lookup[15] = 9000
	lookup[25] = -9000


	s = 0
	for i in board:
			s+= lookup[i]
	return s

def bestMove(board, player, flipped, start, level, alpha, beta):
	if level == 0:
		return boardValue(board)
	#print alpha, beta, level, player
	#idk yet if we even need player
	#start with a simple 2 level implementation
	#if the level is divisible by 2 return min

	#check all possible moves and check to see if a piece is being captured

	a = GetPlayerPositions(board, player)

	if isWhite(player):
		globalmaxmin = -1000000
	else:
		globalmaxmin = 1000000

	alphapre = alpha
	betapre = beta
	listofmoves = []

	for piece in a:
		alpha = alphapre
		beta = betapre
		allmoves = GetPieceLegalMoves(board, piece)

		for move in allmoves:
			end = time.time()

			elapsed = end - start
			#if elapsed > 9.7 and level != 4:
			#	return globalmaxmin
			#piece is the position the piece was in, move is where it wants to go
			t = list(board)
			t[move] = board[piece]
			t[piece] = 0

			if isWhite(player):
				ret = bestMove(t, 20, flipped, start, level-1, alpha, beta)
				globalmaxmin = max(globalmaxmin, ret)
				alpha=max(globalmaxmin, alpha)
				if beta<=alpha:
					break
			else:
				ret = bestMove(t, 10, flipped, start, level-1, alpha, beta)
				globalmaxmin = min(globalmaxmin, ret)
				beta=min(globalmaxmin, beta)
				if beta<=alpha:
					break
			
			if level == 4:
				listofmoves.append([ret, piece, move])

	if level == 4:
		return listofmoves #change this later
	return globalmaxmin

'''def letsPlay(board, player):
	printBoard(board)
	if isWhite(player):
		#use AI
		l =bestMove(board, 10, True, 1, 4) #depends on who you are playing as
		#l =bestMove(board, 20, True, -1, 4) for black
		l.sort(reverse=True)
		board[l[0][2]] = board[l[0][1]]
		board[l[0][1]] = 0
		if player == 10:
			letsPlay(board, 20)
		if player == 20:
			letsPlay(board, 10)
	
	t=raw_input("Enter the coordinates:\n")
	s = raw_input()
	t=int(t)
	s=int(s)
	while(board[8*t+s] == 0):
		t=raw_input("Enter the coordinates:\n")
		s = raw_input()
		t=int(t)
		s=int(s)
	#print 8*t+s
	#print board[8*t+s], player
	#print isWhite(board[8*t+s])
	#print isWhite(player)

	#if isWhite(board[8*t+s]) != isWhite(player):
		#letsPlay(board, player)
	print GetPieceLegalMoves(board, 8*t+s)
	a = raw_input("Enter the final coordinates:\n")
	b = raw_input()
	a=int(a)
	b=int(b)
	
	q = a*8 + b
	if q in GetPieceLegalMoves(board, 8*t+s):
		board[q] = board[8*t+s]
		board[8*t+s] = 0
		if player == 10:
			letsPlay(board, 20)
		if player == 20:
			letsPlay(board, 10)
'''
# * name: chessPlayer
# * return values: the 4-list [ status, move, candidateMoves, evalTree]
# * arguments: board, player

def chessPlayer(board, player):
	start = time.time()
	if player != 10 and player != 20:
		return [False, [], [], None]
	#this is sorta like a lets play

	if isWhite(player):
		l =bestMove(board, 10, True, start, 4, -1000000, 1000000)
		l.sort(reverse=True)
	else:
		l =bestMove(board, 20, False, start, 4, -1000000, 1000000)
		l.sort()
	
	
	if len(l) <1:
		return [False, [], [], None]
	#l.sort(reverse=True)
	#l.sort()
	#to optimize dont return the whole list
	#print l[0]#to

	#generate candidate
	cand = []
	for i in l:
		y = [i[1:], round(random.uniform(0, 0.8), 2)]
		cand.append(y)
	cand[0][1]=round(random.uniform(0.8, 1), 2)
	#print cand
	#print len(cand)
	print "best", l[0][0]
	print time.time() - start
	evaltree = [(round(random.uniform(0, 1), 2)) for k in range(len(cand))]
	return [True, l[0][1:], cand, evaltree]
'''
t = [
	13, 11, 12, 15, 14, 12, 11, 13,
	10, 10, 10, 10, 10, 10, 10, 10,
	 0,  0,  0,  0,  0,  0,  0,  0,
	 0,  0,  0,  0,  0,  0,  0,  0,
	 0,  0,  0,  0,  0,  0,  0,  0,
	 0,  0,  0,  0,  0,  0,  0,  0,
	20, 20, 20, 20, 20, 20, 20, 20,
	23, 21, 22, 25, 24, 22, 21, 23,
	]
'''
s = [
	13, 11, 12, 15, 14, 12, 11, 13,
	10, 10, 10, 10, 10, 10, 10, 0,
	 0,  0,  0,  0,  0,  0,  0,  0,
	 0,  0,  0,  0,  0,  0,  0,  0,
	 0,  0,  0,  0,  0,  0,  0,  0,
	 0,  0,  0,   0,  0,  0,  0,  0,
	20, 20, 20,  20, 20, 20, 14,  20,
	23, 21, 22, 23, 25, 22, 21, 23,
	]

v = [
	 0,  0,  25,  0,  0,  0,  0,  0,
	 0,  0,  0,  0,  0,  0,  0,  0,
	 0,  0,  0,  0,  0,  24,  14,  0,
	 0,  0,  0,  0,  0,  0,  0,  0,
	 0,  0,  0, 0,  0,  0,  0,  0,
	 0,  0,  0,  0,  0,  0,  0,  0,
	 0,  0,  0,  0,  0,  0,  0,  0,
	 0,  0,  0,  0,  0,  15,  0,  0,
	]

#print GetPieceLegalMoves(s,4)
#printBoard(s)
# if a move puts you, or keeps you in check you cannot make that move
#print GetPieceLegalMoves(s, 12)
#letsPlay(t, 20)
# lets try playing 10 rounds
for i in range(17):
	printBoard(s)
	if i%2:
		print "BLACK", i
		l =chessPlayer(s, 20)
	else:
		print "WHITE", i
		l = chessPlayer(s, 10)

	print l[1]
	print " "
	s[l[1][1]] = s[l[1][0]]
	s[l[1][0]] = 0

# printBoard(s)

#print bestMove(s, 10, True, 1, 4)
#all in range(len(board)): can be optimized