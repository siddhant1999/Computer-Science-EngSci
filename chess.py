'''Write the function GetPlayerPositions(board,player)
   where board is the list data struct that represents the chess board
   (described above) and player is 10 (for white) and 20 (for black).
   It should return a list of all positions that the player occupies.'''


def GetPlayerPositions(board,player):
	l =[]
	for x in range(len(board)):
		if board[x] >= player and board[x] <= player+10:
			l.append(x)

	return l

'''Write the function GetPieceLegalMoves(board,position)
   which will return a list of all legal positions that the piece in
   the given position can take.'''
def isWhite(n):
	if n >= 10 and n < 20:
		return True
	return False

def isValid(num):
	if num>= 0 and num<64:
		return True
	return False


def GetPieceLegalMoves(board,position):
	'''
	okay this section will not be easy
	let's do it one type of piece at a time
	'''

	p = board[position]%10 #this is the piece
	l=[]
	if p == 0:
		#pawn

		if isWhite:
			if position>=56:
				return
			if board[position+8]==0:
				l.append(position+8)

			#capture
			if position+7 < 64:
				if board[position+7]>=20:
					l.append(position+7)

			if position+9 < 64:
				if board[position+9]>=20:
					l.append(position+9)	
		else:
			if position<=7:
				return
			if board[position-8]==0:
				l.append(position-8)
			#capture
			if position-7 >= 0:
				if board[position-7]>=10 and board[position-7] < 20:
					l.append(position-7)

			if position-9 >= 0:
				if board[position-9]>=10 and board[position-9] < 20:
					l.append(position-9)

		return l

	if p == 3:
		#rook
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
		return l

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
		

			

s = [13, 11, 12, 14, 15, 12, 11, 13,
	10,10,10,10,10,10,10,10,
	0,0,0,0,0,0,0,0,
	0,0,0,0,0,0,0,0,
	0,0,0,0,0,0,0,0,
	0,0,0,0,0,0,0,0,
	20,20,20,20,20,20,20,20,
	23, 21, 22, 24, 25, 22, 21, 23,
	]
print GetPieceLegalMoves(s,1)

