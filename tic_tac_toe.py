#Danial Syed
#The main function find_winner calls on its helper functions to see if three elements have the same value horizontally, diagonally, or vertically. If found, retun that element
#Each function takes the parameter of the board which is a 3x3 Matrix(tic-tac-toe board)
#The winning element(a letter, number, or symbol) is returned or a string "Draw" is returned if nobody wins
def find_winner(board):
    winner = 0
    #Checks to see if any of the helper functions caught a winner
    if horizontal(board) != None:
        return(horizontal(board))
    else:
        winner += 1
    if vertical(board) != None:
        return(vertical(board))
    else:
        winner += 1
    if diagonal(board) != None:
        return(diagonal(board))
    else:
        winner += 1
    #If all three helper functions return nothing, it is a draw
    if winner == 3:
        result = "Draw"
        return result
def horizontal(board):
    #Every horizontal pairing
    for ele in board:
        #Every element in each row
        if ele[0] == ele[1] and ele[0] == ele[2]:
            return ele[0]
        else:
            return None
def vertical(board):
    #Every vertical pairing
    for i in range(0,3):
        y = []
        #Every element in each column
        for ele in board:
            y += ele[i]
        if y[0] == y[1] and y[1] == y[2]:
            return y[0]
        else:
            return None
def diagonal(board):
    #A key that is used for each value of each needed position on the board to be compared
    a = board[0][0]
    b = board[1][1]
    c = board[2][2]
    d = board[0][2]
    e = board[2][0]
    if(a == b and b == c) or (e == b and b == d):
        return a
    else:
        return None
print(find_winner([['a', 'B', 'a'],
 ['a', 'B', 'B'],
 ['a', 'a', 'B']]))
 




