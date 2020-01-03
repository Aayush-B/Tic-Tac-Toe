print("Welcome to Tic Tac Toe \n")
print("Player 1, please select your marker : X or O\n")
player1=input()
player2=None

player1=player1.upper()

if(player1=='X'):
	player2='O'
else:
	player2='X'

board=[1,2,3,4,5,6,7,8,9]

print(f"Player 1 has chosen {player1} \n")

turn=0
ans='Y'

def show_board(board):
	print("\n"*100)

	print(f"                                       ___ ___ ___\n                                      |   |   |   |\n                                      | {board[0]} | {board[1]} | {board[2]} |\n                                      |___|___|___|\n                                      |   |   |   |\n                                      | {board[3]} | {board[4]} | {board[5]} |\n                                      |___|___|___|")
	
	print(f"                                      |   |   |   |\n                                      | {board[6]} | {board[7]} | {board[8]} |\n                                      |___|___|___|\n")
	print("\n")


def update_board(board,choice,player):
	res=board
	res[choice-1]=player
	return res
    
def check_win(board):

	if((board[0]==board[1]) and (board[1]==board[2])):
		if(board[0]==player1):
			print("Player 1 has won \n")
			return True
		else:
			print("Player 2 has won \n")
			return True

	elif((board[3]==board[4]) and (board[4]==board[5])):
		if(board[3]==player1):
			print("Player 1 has won \n")
			return True
		else:
			print("Player 2 has won \n")
			return True

	elif((board[6]==board[7]) and (board[7]==board[8])):
		if(board[6]==player1):
			print("Player 1 has won \n")
			return True
		else:
			print("Player 2 has won \n")
			return True

	elif((board[0]==board[3]) and (board[3]==board[6])):
		if(board[0]==player1):
			print("Player 1 has won \n")
			return True
		else:
			print("Player 2 has won \n")
			return True

	elif((board[1]==board[4]) and (board[4]==board[7])):
		if(board[1]==player1):
			print("Player 1 has won \n")
			return True
		else:
			print("Player 2 has won \n")
			return True

	elif((board[2]==board[5]) and (board[5]==board[8])):
		if(board[2]==player1):
			print("Player 1 has won \n")
			return True
		else:
			print("Player 2 has won \n")
			return True

	elif((board[0]==board[4]) and (board[4]==board[8])):
		if(board[0]==player1):
			print("Player 1 has won \n")
			return True
		else:
			print("Player 2 has won \n")
			return True

	elif((board[2]==board[4]) and (board[4]==board[6])):
		if(board[2]==player1):
			print("Player 1 has won \n")
			return True
		else:
			print("Player 2 has won \n")
			return True

	else:
		return False

def check_draw(board):
	for i in board:
		if((i!='X') and (i!='O')):
			return False

	print("The game has resulted in a draw. \n")

	return True

while(ans.upper()=='Y'):
	show_board(board)

	print(f"Player {(turn%2)+1}'s turn to choose the cell \n")

	choice=int(input())

	if(((turn%2)+1)==1):
		board=update_board(board,choice,player1)

	else:
		board=update_board(board,choice,player2)

	show_board(board)
	turn+=1

	if(check_win(board) or check_draw(board)):
		turn=0
		board=[1,2,3,4,5,6,7,8,9]
		print("Do you want to play again ? (Y/N) : ")
		ans=input()






