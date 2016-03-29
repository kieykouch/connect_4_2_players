import sys


Row = 6 #Row of Board
Column = 7 #Column of Board
Size = 6*7 #Total piece

def main():
	"""
	main program, where game is start.

	"""
	First = ChooseX_O()
	Second = ""
	Turn = First 
	TheWinner = None
	numberpiece = 0 # for count tie game

	if First == "X":	
		Second = "O"
	else:
		Second = "X"

	board = get_new_board()
	#printboard(board)

	while True:
		printboard(board)
		index = move(Turn)
		if valid_move(index, board, Turn):
			print ("Place a Piece of "+ Turn + " To " + str(index))
			numberpiece += 1
			TheWinner = winner(board, Turn)
			Turn = change_turn(Turn)
		else:
			print ("Invalid Move, please try again, player "+ Turn)
	 	
		if TheWinner != None:
			printboard(board)
			print (TheWinner)
			break
		if numberpiece == Size:
			printboard(board)
			print ("Tie Game")
			break

 	

def move(turn):
	"""
	get input from player, in term of available index.

	@param turn: player either "X" or "O"
	"""
	index = -1
	while not (0 <= index <= 6):
		print("Where you desire to play a piece player "+turn+", from 0 to 6?")
		try:
			index = int(input())
		except ValueError:
			print ("Invalid Input")
			continue
		else:
			continue
	return index

def valid_move(index, board, Turn):
	"""
	check if this is valid move.

	@param turn: player either "X" or "O"
	@param index: index that just get form user
	@param board: board game
	"""


	for k in board:
		if k[index] == "*":
			k[index] = Turn
			#Size -= 1
			return True
	return False

def change_turn(Turn):
	"""
	Switch player after they completed their valid move.

	@param turn: player either "X" or "O"
	"""
	if Turn == "X":
		return "O"
	return "X"

def winner(board, turn):
	"""
	Check if the board have a winner based on 4 conditions.

	@param turn: player either "X" or "O"
	@param board: board game
	"""
	#4 Condition
	#Horizontal
	for x in range(Row):
		for y in range(Column - 3):
			# print (board[x][y])
			# print (board[x][y+1])
			# print (board[x][y+2])
			# print (board[x][y+3])
			# print()
			if board[x][y] == turn and board[x][y+1] == turn and board[x][y+2] == turn and board[x][y+3] == turn:
				return "Winner is " + turn

	#Vertical
	for y in range(Column):
		for x in range(Row - 3):
			if board[x][y] == turn and board[x+1][y] == turn and board[x+2][y] == turn and board[x+3][y] == turn:
				return "Winner is " + turn


	#Diagonal \
	for x in range(Column - 3):
		for y in range(Row - 3):
			if board[x][y] == turn and board[x+1][y+1] == turn and board[x+2][y+2] == turn and board[x+3][y+3] == turn:
				return "Winner is " + turn

	#Diagonal /
	for x in range(Column - 3):
		for y in range(3, Row):
			if board[x][y] == turn and board[x+1][y-1] == turn and board[x+2][y-2] == turn and board[x+3][y-3] == turn:
				return "Winner is " + turn
	return None

def get_new_board():
	"""
	initialize the board for the first time with *.
	"""
	board = []
	for i in range(Row):
		board.append(["*"]*Column)
	return board

def printboard(board):
	"""
	Print the board every turn user has played.

	@param board: board game
	"""
	for k in range(Row-1, -1, -1):
		print (str(k) + " "+ ' '.join(board[k]))
	for k in range(Column):
		if k == 0:
			print("  "+ str(k) + " ", end='')
		else:
			print(str(k) + " ", end='')
	print()


def ChooseX_O():
	"""
	Prompt user to select a piece to start the game.
	
	"""
	myturn = ""
	while (myturn != "X" and myturn != "O"):
		print ("Choose X or O to start the game?")
		myturn = input().upper()

	return myturn

if __name__ == '__main__':
    main()