from operator import truediv


board=['-','-','-','-','-','-','-','-','-',]
def display():
    print('|'+board[0]+'|'+board[1]+'|'+board[2]+'|')
    print('|'+board[3]+'|'+board[4]+'|'+board[5]+'|')
    print('|'+board[6]+'|'+board[7]+'|'+board[8]+'|')
def check(board):
    p1='x'
    p2='o'
    if board[0] == board[1]==board[2]==p1 or board[0] == board[1]==board[2]==p2:
       return True
    elif board[3] == board[4]==board[5]==p1 or board[3] == board[4]==board[5]==p2:
        return True 
    elif board[6] == board[7]==board[8]==p1 or board[6] == board[7]==board[8]==p2:
        return True
    elif board[3] == board[0]==board[6]==p1 or board[3] == board[0]==board[6]==p1:
        return True
    elif board[1] == board[4]==board[7]==p1 or  board[1] == board[4]==board[7]==p2:
        return True       
    elif board[2] == board[5]==board[8]==p1 or board[2] == board[5]==board[8]==p2:   
        return True
    elif board[0] == board[4]==board[8]==p1 or board[0] == board[4]==board[8]==p2:
        return True
    elif board[2] == board[4]==board[6]==p1 or board[2] == board[4]==board[6]==p2:
        return True
    else:    
        return False

def inp(board):
    x=int(input("enter the position"))
    if board[x-1]!='-':
         print("value already exist")
         return inp(board)
    else:
        return x     

player1 =input("palyer 1 name :")        
player2 =input("palyer 2 name :") 
display()
for i in range(9):
    if i%2==0:
        x = inp(board)   
        board[x-1]='x'
        if check(board):
            print('player 1 wins')
            break
    else:
        x = inp(board)
        board[x-1]='o'
        display()
        if check(board):
            print('player 2 wins')
            break
print   ('over')     

