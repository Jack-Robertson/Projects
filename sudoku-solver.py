def my_sudoku_solver(board):
    def is_valid_move(row, col, num):
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False

        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if board[i + start_row][j + start_col] == num:
                    return False
        return True

    def solve_sudoku():
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    for num in range(1, 10):
                        if is_valid_move(row, col, num):
                            board[row][col] = num
                            if solve_sudoku():
                                return True
                            board[row][col] = 0
                    return False
        return True

    if solve_sudoku():
        for row in board:
            print(" ".join(map(str, row)))
    else:
        print("No solution exists.")

# Initialize the Sudoku board
sudoku_board = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
               [0, 1, 0, 0, 0, 4, 0, 0, 0],
               [4, 0, 7, 0, 0, 0, 2, 0, 8],
               [0, 0, 5, 2, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 9, 8, 1, 0, 0],
               [0, 4, 0, 0, 0, 3, 0, 0, 0],
               [0, 0, 0, 3, 6, 0, 0, 7, 2],
               [0, 7, 0, 0, 0, 0, 0, 0, 3],
               [9, 0, 3, 0, 0, 0, 6, 0, 4]]

my_sudoku_solver(sudoku_board)
