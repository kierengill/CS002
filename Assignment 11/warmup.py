import random


board = [['.','.','.'],
         ['.','.','.'],
         ['.','.','.']]

def print_board():
    for i in board:
        for c in i:
            print(c,end=' ')
        print()


##def has_empty_space(x,y):
##    counter = 0
##    if board[x][y]=='.':
##        return True
##    else:
##        return False

def has_empty_space():
    for i in board:
        if '.' in i:
            return True
        else:
            return False

        

def has_winner():
    winner = 0
    for i in board:
        if (i[0] == i[1]) and (i[1] == i[2]) and ('.' not in i):
            winner += 1
            
    if (board[0][0] == board[1][0]) and (board[1][0] == board[2][0]) and (board[0][0]!='.'):
        winner +=1
    elif (board[0][1] == board[1][1]) and (board[1][1] == board[2][1]) and (board[0][1]!='.'):
        winner +=1
    elif (board[0][2] == board[1][2]) and (board[1][2] == board[2][2]) and (board[0][2]!='.'):
        winner +=1
    elif (board[0][0] == board[1][1]) and (board[1][1] == board[2][2]) and (board[0][0]!='.'):
        winner +=1
    elif (board[0][2] == board[1][1]) and (board[1][1] == board[2][0]) and (board[0][2]!='.'):
        winner +=1

    if winner != 0:
        print("Winner is player "+board[x][y]+"!")
        return True
    else:
        return False

while has_empty_space():            
    while True:
        user = input("Enter a coordinate (i.e. 0,0): ")
        coords = user.split(',')
        x=int(coords[0])
        y=int(coords[1])
        if board[x][y]=='.':
            board[x][y] = 'x'
            break
        else:
            print("Sorry! This space is taken.")
    print()

    while True:
        computer_x = random.randint(0,2)
        computer_y = random.randint(0,2)
        if board[computer_x][computer_y]=='.':
            board[computer_x][computer_y] = 'o'
            break
        else:
            continue
        
    print_board()
    print()


    if has_winner():
        break


