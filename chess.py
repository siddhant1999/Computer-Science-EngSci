'''Write the function GetPlayerPositions(board,player)
   where board is the list data struct that represents the chess board
   (described above) and player is 10 (for white) and 20 (for black).
   It should return a list of all positions that the player occupies.'''

#need to implement a alpha beta pruning method of determining successful moves

def printBoard(board):
	for i in range(len(board)):
		if i%8==0:
			print "\n"
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
	print "\n"

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
					l.append(position+7)

			if position+9 < 64:
				if isWhite(board[position+9]) != isWhite(board[position]) and board[position+9] != 0:
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
					l.append(position-7)

			if position-9 >= 0:
				if isWhite(board[position-9]) != isWhite(board[position]) and board[position-9] != 0:
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
				l.append(position-17)
		#left top
		if isValid(position-10):
			if board[position-10] == 0 or (isWhite(board[position]) != isWhite(board[position-10])):
				l.append(position-10)
		#left bottom
		if isValid(position+6):
			if board[position+6] == 0 or (isWhite(board[position]) != isWhite(board[position+6])):
				l.append(position+6)
		#bottom left
		if isValid(position+15):
			if board[position+15] == 0 or (isWhite(board[position]) != isWhite(board[position+15])):
				l.append(position+15)
		#bottom right
		if isValid(position+17):
			if board[position+17] == 0 or (isWhite(board[position]) != isWhite(board[position+17])):
				l.append(position+17)
		#right bottom
		if isValid(position+10):
			if board[position+10] == 0 or (isWhite(board[position]) != isWhite(board[position+10])):
				l.append(position+10)
		#right top
		if isValid(position-6):
			if board[position-6] == 0 or (isWhite(board[position]) != isWhite(board[position-6])):
				l.append(position-6)
		#top right
		if isValid(position-15):
			if board[position-15] == 0 or (isWhite(board[position]) != isWhite(board[position-15])):
				l.append(position-15)
		return l
		
	if p==2 or p==4:
		#bishop or queen
		pos = position+9
		row=position/8
		while(isValid(pos)):
			#right down

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
lookup[15] = 900
lookup[25] = -900

'''
Pawn:   +0
Knight: +1
Bishop: +2
Rook:   +3
Queen:  +4
King:   +5
'''

def boardValue(board):
	s = 0
	for i in board:
		s+= lookup[i]
	return s

def bestMove(board, player, isMain, prevValue, level):
	if level == 0:
		return boardValue(board)
	#idk yet if we even need player
	#start with a simple 2 level implementation
	#if the level is divisible by 2 return min

	#check all possible moves and check to see if a piece is being captured

	a = GetPlayerPositions(board, player)

	if level%2:
		globalmaxmin = 1000000
	else:
		globalmaxmin = -1000000

	#print a
	'''for i in a:
		print i
		print GetPieceLegalMoves(board, i)
	return 1
	'''
	listofmoves = []
	for piece in a:
		allmoves = GetPieceLegalMoves(board, piece)
		for move in allmoves:
			#piece is the position the piece was in, move is where it wants to go
			#boardVal = prevValue - lookup[board[move]] #you may only need to evaluate this at the end
			t = list(board)
			t[move] = board[piece]
			t[piece] = 0
			if isWhite(player):
				ret = bestMove(t, 20, isMain, prevValue, level-1)
			else:
				ret = bestMove(t, 10, isMain, prevValue, level-1)
			if level%2:
				globalmaxmin = min(globalmaxmin, ret)
			else:
				globalmaxmin = max(globalmaxmin, ret)
			if level == 4:
				listofmoves.append([ret, piece, move])
		#check the validity of the moves themselves
	if level == 4:
		return listofmoves #change this later
	return globalmaxmin

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
	for i in range(len(board)):
		if isWhite(board[i]) != isWhite(board[pos]):
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

def isWhite(n):
	if n >= 10 and n < 20:
		return True
	return False

def isValid(num):
	if num>= 0 and num<64:
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

				if position/8 != (position+i)/8:
					continue#so that lateral movement doesn't put you on the other side of the board
				
				if (j == 0 and i ==0) or not isValid(pos):
					continue
				if isWhite(board[pos]) == isWhite(board[position]):
					continue
				t= list(board)
				t[position] =0
				t[pos] = board[position]
				if not inCheck(t, board[position]-5):
					l.append(pos)
		return l
	else:

		l = Helper(board, position)
		#print l
	#check if by setting the value of board[position] to 0 and then set board[l[i]] to board[position] and check if in check
	#return l

	#issue is here
	actual_l = []
	for i in range(len(l)):
		t= list(board)
		t[position] =0
		t[l[i]]=board[position]

		if(not inCheck(t, (board[position]/10)*10)):
			actual_l.append(l[i])
	return actual_l


def letsPlay(board, player):
	printBoard(board)
	if isWhite(player):
		#use AI
		l =bestMove(board, 10, True, 1, 4)
		l.sort()
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
	#print 8*t+s
	#print board[8*t+s], player
	#print isWhite(board[8*t+s])
	#print isWhite(player)

	if isWhite(board[8*t+s]) != isWhite(player):
		letsPlay(board, player)
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

s = [
	13, 11, 12, 14, 15, 12, 11, 13,
	10, 10, 10, 10, 10, 10, 10, 10,
	 0,  0,  0,  0,  0,  0,  0,  0,
	 0,  0,  0,  0,  0,  0,  0,  0,
	 0,  0,  0,  0,  0,  0,  0,  0,
	 0,  0,  0,  0,  0,  0,  0,  0,
	20, 20, 20, 20, 20, 20, 20, 20,
	23, 21, 22, 24, 25, 22, 21, 23,
	]

t = [
	13, 11, 12, 15, 14, 12, 11, 13,
	10, 10, 10, 12, 10, 10, 10, 10,
	 0,  0,  0,  0,  0,  0,  0,  0,
	 0,  0,  0,  0,  0,  0,  0,  0,
	 0,  0,  0,  0,  0,  0,  0,  0,
	 0,  0,  0,  0,  0,  0,  0,  0,
	20, 20, 20,  0, 20, 20, 20, 20,
	23, 21, 22, 24, 25, 22, 21, 23,
	]
#print GetPieceLegalMoves(s,4)
#printBoard(s)
# if a move puts you, or keeps you in check you cannot make that move
letsPlay(s, 10)
#printBoard(t)


#print bestMove(s, 10, True, 1, 4)
#all in range(len(board)): can be optimized