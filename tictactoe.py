def check_winner_pythonic(board):
    #check rows
    # ['O', 'X', 'X'], -> set(['x','x','x']) -> {'x'} 
    # (this will return the how many different elements it contain)
    # ['X', 'X', 'O'],
    #['O', 'X', 'X']
    for row in board:
        if len(set(row)) == 1:
            #if there is only one symbol
            return row[0]
        #then the row already has a winner
   
   
    # check columns
     # ['O', 'X', 'X']
     # ['X', 'X', 'O']
     # ['O', 'X', 'X']
    
    for i in range(len(board)):
        # len(board)=3
        column = [board[i][j] for j in range(len(board))]
        if len(set(column)) == 1:
            return board[0][1]
        
    # check diagnols
    tl_to_br = [board[i][i] for i in range(len(board))]
    if len(set(tl_to_br)) == 1:
        return board[0][0]
    
    # the other orientation
    bl_to_tr = [board[i][len(board)-i-1] for i in range(len(board))]
    if len(set(bl_to_tr)) == 1:
        return board[0][0]