from time import perf_counter


def sudoku_sovler(board):
    if not search_blank(board):
        print_board(board)
        return True
    else:
        row, col = search_blank(board)

    for number in range(1, 10):
        if check_row(board, number, row) and check_col(board, number, col) and check_square(board, number, row, col):
            board[row][col] = number
            if sudoku_sovler(board):
                return True
            board[row][col] = ' '
    return False


def search_blank(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == ' ':
                return i, j
    return False


def check_row(board, number, row):
    if number in board[row]:
        return False
    else:
        return True


def check_col(board, number, col):
    temp_col = []
    for i in range(len(board)):
        temp_col.append(board[i][col])
    if number in temp_col:
        return False
    else:
        return True


def check_square(board, number, row, col):
    square_x = row // 3
    square_y = col // 3
    temp_col = []
    for i in range(square_x * 3, square_x * 3 + 3):
        for j in range(square_y * 3, square_y * 3 + 3):
                temp_col.append(board[i][j])
    if number in temp_col:
        return False
    else:
        return True


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print('-'*22)
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print('| ', end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


random_board = \
         [['4', '9', '6', '8', ' ', '2', ' ', ' ', ' ']
        , [' ', ' ', ' ', ' ', ' ', '5', ' ', ' ', ' ']
        , ['7', ' ', ' ', ' ', '9', ' ', ' ', ' ', ' ']
        , [' ', '3', '1', ' ', '8', ' ', ' ', '7', ' ']
        , ['6', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8']
        , [' ', '2', ' ', ' ', ' ', '3', ' ', '4', '5']
        , [' ', ' ', ' ', ' ', ' ', '9', '3', ' ', ' ']
        , [' ', '7', '4', ' ', '6', ' ', ' ', '2', ' ']
        , ['9', ' ', ' ', ' ', '7', ' ', '5', '1', '4']]

for i in range(len(random_board)):
    for j in range(len(random_board[0])):
        if random_board[i][j] != ' ':
            random_board[i][j] = int(random_board[i][j])

start_time = perf_counter()
print_board(random_board)
print("@"*20)
sudoku_sovler(random_board)
end_time = perf_counter()
print('Time: {:.1f}'.format(end_time - start_time))
print("Done!")
