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

board2=[
    [".",".","4",".",".",".","6","3","."],
    [".",".",".",".",".",".",".",".","."],
    ["5",".",".",".",".",".",".","9","."],
    [".",".",".","5","6",".",".",".","."],
    ["4",".","3",".",".",".",".",".","1"],
    [".",".",".","7",".",".",".",".","."],
    [".",".",".","5",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."]]

def isValidSudoku(board: list[str]) -> bool:
    box_hash={}
    for i in range(9):
        row_hash=set()
        column_hash=set()
        for j in range(9):
            print(i,j, board[i][j],board[j][i])
            print(row_hash)
            print(column_hash)
            print(box_hash)
            '''if(board[i][j]=="." or board[j][i]=='.'):
                continue'''
            
            if(board[i][j] in row_hash and board[i][j]!="."):
                print("row repetida")
                return False
    
            if(board[j][i] in column_hash and board[j][i]!='.'):
                print("column repetida char: ",board[j][i])
                return False
            
            position=[int(i/3),int(j/3)]
            position=str(position)

            if(position not in box_hash):
                box_hash[position]=[]

            if(board[i][j] in box_hash[position] and board[i][j]!="."):
                print("box repetida")
                return False
            
            row_hash.add(board[i][j])
            column_hash.add(board[j][i])
            box_hash[position].append(board[i][j])

    return True
                
        


print(isValidSudoku(board2))