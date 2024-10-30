'''
9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:
    Each row must contain the digits 1-9 without duplicates.
    Each column must contain the digits 1-9 without duplicates.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.

Return true if the Sudoku board is valid, otherwise return false

Note: A board does not need to be full or be solvable to be valid.
'''
valid = [["1","2",".",".","3",".",".",".","."],
        ["4",".",".","5",".",".",".",".","."],
        [".","9","8",".",".",".",".",".","3"],
        ["5",".",".",".","6",".",".",".","4"],
        [".",".",".","8",".","3",".",".","5"],
        ["7",".",".",".","2",".",".",".","6"],
        [".",".",".",".",".",".","2",".","."],
        [".",".",".","4","1","9",".",".","8"],
        [".",".",".",".","8",".",".","7","9"]]

invalid=[["1","2",".",".","3",".",".",".","."],
        ["4",".",".","5",".",".",".",".","."],
        [".","9","1",".",".",".",".",".","3"],
        ["5",".",".",".","6",".",".",".","4"],
        [".",".",".","8",".","3",".",".","5"],
        ["7",".",".",".","2",".",".",".","6"],
        [".",".",".",".",".",".","2",".","."],
        [".",".",".","4","1","9",".",".","8"],
        [".",".",".",".","8",".",".","7","9"]]

test_row=[["1","2",".",".","3",".",".",".","."]]
test_row2=[["1","2",".","3","3",".",".",".","."]]
test_column=[["1"],["2"],["."],["4"],["."],["6"],["."],["8"],["9"]]
test_column2=[["1","3"],["3","3"],["2","4"],["4","8"],[".","9"],["6","5"],[".","7"],["8","2"],["9","6"]]
def isValidSudoku(board: list[str]) -> bool:
    #validate rows
    #validate columns
    #validate grids
    isValid=True
    digits=[1,2,3,4,5,6,7,8,9]

    for row in board:
        row_hash=set()
        for element in row:
            if(element in row_hash and element != "."):
                isValid=False
                return isValid
            row_hash.add(element)
    counter=1
    for i in range(len(board[0])):
        column_hash=set()
        for j in range(len(board)):
            if(board[j][i] in column_hash and board[j][i] != "."):
                isValid=False
                return isValid
            column_hash.add(board[j][i])
    
    square=int(len(digits)**(1/2))
    
    
    for i in range(0,square,1):
        sub_boxes=set()
        for j in range(0,square,1):
            if(board[i][j] in sub_boxes and board[i][j] != "."):
                isValid=False
                return isValid
            sub_boxes.add(board[i][j])
            print(sub_boxes)
    return isValid




print(isValidSudoku(invalid))