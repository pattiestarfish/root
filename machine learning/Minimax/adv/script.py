from connect_four import *

def two_ai_game():
    my_board = make_board()
    while not game_is_over(my_board):
        # The "X" player finds their best move.
        result = minimax(my_board, True, 5, -float("Inf"), float("Inf"), my_evaluate_board)
        print("X Turn\nX selected ", result[1])
        print(result[1])
        select_space(my_board, result[1], "X")
        print_board(my_board)

        if not game_is_over(my_board):
            # The "O" player finds their best move
            result = minimax(my_board, False, 4, -float("Inf"), float("Inf"), codecademy_evaluate_board)
            print("O Turn\nO selected ", result[1])
            print(result[1])
            select_space(my_board, result[1], "O")
            print_board(my_board)
    if has_won(my_board, "X"):
        print("X won!")
    elif has_won(my_board, "O"):
        print("O won!")
    else:
        print("It's a tie!")

#update to check for streaks in all 8 directions, weight streaks of 3 > 2, only count "unblocked" streaks, and only count
#streaks that have enough space to actually connect 4
def my_evaluate_board(board):
    if has_won(board, 'X'):
        return float("Inf")
    elif has_won(board, 'O'):
        return -float("Inf")
    else:
        x_two_streak = 0
        x_three_streak = 0
        o_two_streak = 0
        o_three_streak = 0
        weighted_x_streaks = 0
        weighted_o_streaks = 0

        #horizonatally checks for 2 and 3 in a rows from L-->R (skips last 3 columns)
        for col in range(len(board) - 3):
            for row in range(len(board[0])):
                if board[col][row] == 'X' and board[col + 1][row] == 'X':
                    if board[col + 2][row] != 'O' and board[col + 3][row] != 'O':
                        if board[col + 2][row] == 'X':
                            x_three_streak += 1
                        elif col > 0 and board[col][row] == 'X':
                            continue
                        else:
                            x_two_streak += 1
                elif board[col][row] == 'O' and board[col + 1][row] == 'O':
                    if board[col + 2][row] != 'X' and board[col + 3][row] != 'X':
                        if board[col + 2][row] == 'O':
                            o_three_streak += 1
                        elif col > 0 and board[col][row] == 'O':
                            continue
                        else:
                            o_two_streak += 1
        #horizontally checks for 2 and 3 in a rows from R --> L, skips first 3 col
        for col in range(len(board) - 3):
            j = len(board)-1
            for row in range(len(board[0])):
                if board[j - col][row] == 'X' and board[j - col - 1][row] == 'X':
                    if board[j - col - 2][row] != 'O' and board[j - col - 3][row] != 'O':
                        if board[j - col - 2][row] == 'X':
                            x_three_streak += 1
                        elif col > 0 and board[j - col][row] == 'X':
                            continue
                        else:
                            x_two_streak += 1
                elif board[j - col][row] == 'O' and board[j - col - 1][row] == 'O':
                    if board[j - col - 2][row] != 'X' and board[j - col - 3][row] != 'X':
                        if board[j - col - 2][row] == 'O':
                            o_three_streak += 1
                        elif col > 0 and board[j - col][row] == 'O':
                            continue
                        else:
                            o_two_streak += 1

        #vertically checks for 2 and 3 in columns from Bot-->Top
        for col in range(len(board)):
            for row in range(len(board[0]) - 3):
                if board[col][row] == 'X' and board[col][row + 1] == 'X':
                    if board[col][row + 2] != 'O' and board[col][row + 3] != 'O':
                        if board[col][row + 2] == 'X':
                            x_three_streak += 1
                        elif row > 0 and board[col][row] == 'X':
                            continue
                        else:
                            x_two_streak += 1
                elif board[col][row] == 'O' and board[col][row + 1] == 'O':
                    if board[col][row + 2] != 'X' and board[col][row + 3] != 'X':
                        if board[col][row + 2] == 'O':
                            o_three_streak += 1
                        elif row > 0 and board[col][row] == 'O':
                            continue
                        else:
                            o_two_streak += 1
        #vertically checks for 2 and 3 in columns from Top --> Bot
        for col in range(len(board)):
            i = len(board[0])-1
            for row in range(len(board[0]) - 3):
                if board[col][i - row] == 'X' and board[col][i - row - 1] == 'X':
                    if board[col][i - row - 2] != 'O' and board[col][i - row - 3] != 'O':
                        if board[col][i - row - 2] == 'X':
                            x_three_streak += 1
                        elif row > 0 and board[col][i - row] == 'X':
                            continue
                        else:
                            x_two_streak += 1
                elif board[col][i - row] == 'O' and board[col][i - row - 1] == 'O':
                    if board[col][i - row - 2] != 'X' and board[col][i - row - 3] != 'X':
                        if board[col][i - row - 2] == 'O':
                            o_three_streak += 1
                        elif row > 0 and board[col][i - row] == 'O':
                            continue
                        else:
                            o_two_streak += 1

        #diagonally finds X streaks Topleft to Botright
        for col in range(len(board) - 3):
            for row in range(len(board[0]) - 2):
                if board[col][row] == 'X' and board[col + 1][row + 1] == 'X':
                    if board[col + 2][row + 2] != 'O' and board[col + 3][row + 3] != 'O':
                        if board[col + 2][row + 2] == 'X':
                            x_three_streak += 1
                        elif col > 0 and board[col][row] == 'X':
                            continue
                        else:
                            x_two_streak += 1
                elif board[col][row + 1] == 'X' and board[col + 1][row + 2] == 'X':
                    if board[col + 2][row + 3] != 'O' and board[col + 3][row + 4] != 'O':
                        if board[col + 2][row + 3] == 'X':
                            x_three_streak += 1
                        elif col > 0 and board[col][row] == 'X':
                            continue
                        else:
                            x_two_streak += 1
        #diagonally finds O streaks Topleft to Botright
        for col in range(len(board) - 3):
            for row in range(len(board[0]) - 2):
                if board[col][row] == 'O' and board[col + 1][row + 1] == 'O':
                    if board[col + 2][row + 2] != 'X' and board[col + 3][row + 3] != 'X':
                        if board[col + 2][row + 2] == 'O':
                            o_three_streak += 1
                        elif col > 0 and board[col][row] == 'O':
                            continue
                        else:
                            o_two_streak += 1
                elif board[col][row + 1] == 'O' and board[col + 1][row + 2] == 'O':
                    if board[col + 2][row + 3] != 'X' and board[col + 3][row + 4] != 'X':
                        if board[col + 2][row + 3] == 'O':
                            o_three_streak += 1
                        elif col > 0 and board[col][row] == 'O':
                            continue
                        else:
                            o_two_streak += 1

        #diagonally finds X streaks bottom row to Topright for col 0-1
        for col in range(0,2):
            i = len(board[0])
            for row in range(len(board[0]) - 3):
                if board[col][i - row - 1] == 'X' and board[col + 1][i - row - 2] == 'X':
                    if board[col + 2][i - row - 3] != 'O' and board[col + 3][i - row - 4] != 'O':
                        if board[col + 2][i - row - 2] == 'X':
                            x_three_streak += 1
                        elif col > 0 and board[col][i - row] == 'X':
                            continue
                        else:
                            x_two_streak += 1
        #diagonally finds X streaks bottom row to Topright for col 2
        for col in range(2,3):
            i = len(board[0])
            for row in range(len(board[0]) - 4):
                if board[col][i - row - 1] == 'X' and board[col + 1][i - row - 2] == 'X':
                    if board[col + 2][i - row - 3] != 'O' and board[col + 3][i - row - 4] != 'O':
                        if board[col + 2][i - row - 3] == 'X':
                            x_three_streak += 1
                        elif col > 0 and board[col][i - row - 1] == 'X':
                            continue
                        else:
                            x_two_streak += 1
        #diagonally finds O streaks bottom row to Topright for col 0-1
        for col in range(0,2):
            i = len(board[0])
            for row in range(len(board[0]) - 3):
                if board[col][i - row - 1] == 'O' and board[col + 1][i - row - 2] == 'O':
                    if board[col + 2][i - row - 3] != 'X' and board[col + 3][i - row - 4] != 'X':
                        if board[col + 2][i - row - 2] == 'O':
                            o_three_streak += 1
                        elif col > 0 and board[col][i - row] == 'O':
                            continue
                        else:
                            o_two_streak += 1
        #diagonally finds O streaks bottom row to Topright for col 2
        for col in range(2,3):
            i = len(board[0])
            for row in range(len(board[0]) - 4):
                if board[col][i - row - 1] == 'O' and board[col + 1][i - row - 2] == 'O':
                    if board[col + 2][i - row - 3] != 'X' and board[col + 3][i - row - 4] != 'X':
                        if board[col + 2][i - row - 3] == 'O':
                            o_three_streak += 1
                        elif col > 0 and board[col][i - row - 1] == 'O':
                            continue
                        else:
                            o_two_streak += 1



        #weights 2 in row @ 0.5x, 3 in row @ 1.25x
        print("Printing streaks:")
        print("X 2 in a row: " + str(x_two_streak))
        print("X 3 in a row: " + str(x_three_streak))
        print("O 2 in a row: " + str(o_two_streak))
        print("O 3 in a row: " + str(o_three_streak))
        weighted_x_streaks = (0.5 * x_two_streak) + (x_three_streak * 1.25)
        weighted_o_streaks = (0.5 * o_two_streak) + (o_three_streak * 1.25)
        print("X player standings: " + str(weighted_x_streaks))
        print("O player standings: " + str(weighted_o_streaks))
        return weighted_x_streaks - weighted_o_streaks


#two_ai_game()

#-----------------
#TESTING
new_board = make_board()
print(len(new_board[0]))

select_space(new_board, 5, "X")
select_space(new_board, 6, "X")
select_space(new_board, 7, "X")
select_space(new_board, 6, "O")
select_space(new_board, 7, "O")
select_space(new_board, 6, "X")
select_space(new_board, 7, "O")
select_space(new_board, 6, "X")
select_space(new_board, 7, "X")
select_space(new_board, 6, "X")
select_space(new_board, 7, "X")
select_space(new_board, 1, "X")
select_space(new_board, 2, "X")
select_space(new_board, 1, "X")
select_space(new_board, 2, "X")
select_space(new_board, 1, "X")
select_space(new_board, 2, "X")
select_space(new_board, 5, "X")
select_space(new_board, 5, "X")
select_space(new_board, 3, "O")
select_space(new_board, 4, "O")
select_space(new_board, 3, "O")
select_space(new_board, 3, "O")
select_space(new_board, 4, "O")
select_space(new_board, 5, "O")
select_space(new_board, 5, "X")
select_space(new_board, 3, "X")
select_space(new_board, 1, "O")
select_space(new_board, 2, "O")
select_space(new_board, 1, "X")
select_space(new_board, 2, "X")
select_space(new_board, 1, "X")


print_board(new_board[0][3])
print(new_board[0][5])

print_board(new_board)

print(my_evaluate_board(new_board))
