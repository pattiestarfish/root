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
                        x_two_streak += 1
                        if board[col + 2][row] == 'X':
                            x_three_streak += 1
                elif board[col][row] == 'O' and board[col + 1][row] == 'O':
                    if board[col + 2][row] != 'X' and board[col + 3][row] != 'X':
                        o_two_streak += 1
                        if board[col + 2][row] == 'O':
                            o_three_streak += 1
        #horizontally checks for 2 and 3 in a rows from R --> L, skips first 3 col
        for col in range(len(board) - 3):
            for row in range(len(board[0])):
                if board[col - 1][row] == 'X' and board[col - 2][row] == 'X':
                    if board[col - 3][row] != 'O' and board[col - 4][row] != 'O':
                        x_two_streak += 1
                        if board[col - 3][row] == 'X':
                            x_three_streak += 1
                elif board[col - 1][row] == 'O' and board[col - 2][row] == 'O':
                    if board[col - 3][row] != 'X' and board[col - 4][row] != 'X':
                        o_two_streak += 1
                        if board[col - 3][row] == 'O':
                            o_three_streak += 1
        #vertically checks for 2 and 3 in columns from Top-->Bot (skips last 3 rows)
        for col in range(len(board) - 3):
            for row in range(len(board[0])):
                if board[col][row] == 'X' and board[col][row + 1] == 'X':
                    if board[col][row + 2] != 'O' and board[col][row + 3] != 'O':
                        x_two_streak += 1
                        if board[col][row + 2] == 'X':
                            x_three_streak += 1
                elif board[col][row] == 'O' and board[col][row + 1] == 'O':
                    if board[col][row + 2] != 'X' and board[col][row + 3] != 'X':
                        o_two_streak += 1
                        if board[col][row + 2] == 'O':
                            o_three_streak += 1
        #vertically checks for 2 and 3 in columns from Bot --> Top, skips last 3 rows
        for col in range(len(board) - 3):
            for row in range(len(board[0])):
                if board[col][row - 1] == 'X' and board[col][row - 2] == 'X':
                    if board[col][row - 3] != 'O' and board[col][row - 4] != 'O':
                        x_two_streak += 1
                        if board[col][row - 3] == 'X':
                            x_three_streak += 1
                elif board[col][row - 1] == 'O' and board[col][row - 2] == 'O':
                    if board[col][row - 3] != 'X' and board[col][row - 4] != 'X':
                        o_two_streak += 1
                        if board[col][row - 3] == 'O':
                            o_three_streak += 1


        #weights 2 in row @ 0.5x, 3 in row @ 1.25x
        weighted_x_streaks = (0.5 * x_two_streak) + (x_three_streak * 1.25)
        weighted_o_streaks = (0.5 * o_two_streak) + (o_three_streak * 1.25)
        print(weighted_x_streaks)
        print(weighted_o_streaks)
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
select_space(new_board, 7, "X")
select_space(new_board, 6, "X")
select_space(new_board, 7, "X")
select_space(new_board, 6, "X")
select_space(new_board, 7, "X")
select_space(new_board, 1, "X")
select_space(new_board, 2, "X")
select_space(new_board, 1, "X")
select_space(new_board, 2, "X")
print_board(new_board)

print(my_evaluate_board(new_board))
