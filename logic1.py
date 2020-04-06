from random import *
board= 	['_']*9
def print_board():
	print(board[0] + '|' + board[1] + '|' + board[2] )
	print(board[3] + '|' + board[4] + '|' + board[5] )
	print(board[6] + '|' + board[7] + '|' + board[8] )
print_board()
def play():
	while True:
		x = input('Pick a number from 0-8 =')
		x = int(x)
		board[x] = 'X'
		print_board()
		o = randint(0,8)
		#o = int(0)
		print(o)
		board[o] = '$'
		print_board()
	
def rule():	
	if board[0]==board[1]==board[2]=='x or $':
		print ("GAMEOVER")
	elif board[3]==board[4]==board[5]:
		print ("GAMEOVER")
	elif board[6]==board[7]==board[8]:
		print ("GAMEOVER")
	elif board[0]==board[4]==board[8]:
		print ("GAMEOVER")
	elif board[2]==board[4]==board[6]:
		print ("GAMEOVER")
		
play()
if rule()==True:
	print("end")
