from copy import deepcopy
import random
random.seed(108)

def print_board(board):
    print()
    print(' ', end='')
    for x in range(1, len(board) + 1):
        print(' %s  ' % x, end='')
    print()

    print('+---+' + ('---+' * (len(board) - 1)))

    for y in range(len(board[0])):

        print('|', end='')
        for x in range(len(board)):
            print(' %s |' % board[x][y], end='')
        print()

        print('+---+' + ('---+' * (len(board) - 1)))

def select_space(board, column, player):
    if not move_is_valid(board, column):
        return False
    if player != "X" and player != "O":
        return False
    for y in range(len(board[0])-1, -1, -1):
        if board[column-1][y] == ' ':
            board[column-1][y] = player
            return True
    return False

def board_is_full(board):
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] == ' ':
                return False
    return True

def move_is_valid(board, move):
    if move < 1 or move > (len(board)):
        return False

    if board[move-1][0] != ' ':
        return False

    return True

def available_moves(board):
    moves = []
    for i in range(1, len(board)+1):
        if move_is_valid(board, i):
            moves.append(i)
    return moves

def has_won(board, symbol):
    # check horizontal spaces
    for y in range(len(board[0])):
        for x in range(len(board) - 3):
            if board[x][y] == symbol and board[x+1][y] == symbol and board[x+2][y] == symbol and board[x+3][y] == symbol:
                return True

    # check vertical spaces
    for x in range(len(board)):
        for y in range(len(board[0]) - 3):
            if board[x][y] == symbol and board[x][y+1] == symbol and board[x][y+2] == symbol and board[x][y+3] == symbol:
                return True

    # check / diagonal spaces
    for x in range(len(board) - 3):
        for y in range(3, len(board[0])):
            if board[x][y] == symbol and board[x+1][y-1] == symbol and board[x+2][y-2] == symbol and board[x+3][y-3] == symbol:
                return True

    # check \ diagonal spaces
    for x in range(len(board) - 3):
        for y in range(len(board[0]) - 3):
            if board[x][y] == symbol and board[x+1][y+1] == symbol and board[x+2][y+2] == symbol and board[x+3][y+3] == symbol:
                return True

    return False


def game_is_over(board):
  return has_won(board, "X") or has_won(board, "O") or len(available_moves(board)) == 0


#updated function with support to search in 6 out of 8 directions, added weighting
#doesn't count streaks that are blocked off/impossible for 4 in row
def evaluate_board(board):
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
            for row in range(len(board[0]) - 4):
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
            for row in range(len(board[0]) - 4):
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
                        elif col > 0 and board[col][i - row - 1] == 'X':
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
                        elif col > 0 and board[col][i - row - 1] == 'O':
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


def count_streaks(board, symbol):
    count = 0
    for col in range(len(board)):
        for row in range(len(board[0])):
            if board[col][row] != symbol:
                continue
            # right
            if col < len(board) - 3:
                num_in_streak = 0
                for i in range(4):
                    if board[col + i][row] == symbol:
                        num_in_streak += 1
                    elif board[col + i][row] != " ":
                        num_in_streak = 0
                        break
                count += num_in_streak
            #left
            if col > 2:
                num_in_streak = 0
                for i in range(4):
                    if board[col - i][row] == symbol:
                        num_in_streak += 1
                    elif board[col - i][row] != " ":
                        num_in_streak = 0
                        break
                count += num_in_streak
            #up-right
            if col < len(board) - 3 and row > 2:
                num_in_streak = 0
                for i in range(4):
                    if board[col + i][row - i] == symbol:
                        num_in_streak += 1
                    elif board[col + i][row - i] != " ":
                        num_in_streak = 0
                        break
                count += num_in_streak
            #down-right
            if col < len(board) - 3 and row < len(board[0]) - 3:
                num_in_streak = 0
                for i in range(4):
                    if board[col + i][row + i] == symbol:
                        num_in_streak += 1
                    elif board[col + i][row + i] != " ":
                        num_in_streak = 0
                        break
                count += num_in_streak
            #down-left
            if col > 2 and row < len(board[0]) - 3:
                num_in_streak = 0
                for i in range(4):
                    if board[col - i][row + i] == symbol:
                        num_in_streak += 1
                    elif board[col - i][row + i] != " ":
                        num_in_streak = 0
                        break
                count += num_in_streak
            #up-left
            if col > 2 and row > 2:
                num_in_streak = 0
                for i in range(4):
                    if board[col - i][row - i] == symbol:
                        num_in_streak += 1
                    elif board[col - i][row - i] != " ":
                        num_in_streak = 0
                        break
                count += num_in_streak
            #down-left
            if col > 2 and row < len(board[0]) - 3:
                num_in_streak = 0
                for i in range(4):
                    if board[col - i][row + i] == symbol:
                        num_in_streak += 1
                    elif board[col - i][row + i] != " ":
                        num_in_streak = 0
                        break
                count += num_in_streak
            #down
            num_in_streak = 0
            if row < len(board[0]) - 3:
                for i in range(4):
                    if row + i < len(board[0]):
                        if board[col][row + i] == symbol:
                            num_in_streak += 1
                        else:
                            break
            for i in range(4):
                if row - i > 0:
                    if board[col][row - i] == symbol:
                        num_in_streak += 1
                    elif board[col][row - i] == " ":
                        break
                    else:
                        num_in_streak == 0
            if row < 3:
                if num_in_streak + row < 4:
                    num_in_streak = 0
            count += num_in_streak
    return count

def minimax(input_board, is_maximizing, depth, alpha, beta):
  if game_is_over(input_board) or depth == 0:
        return [evaluate_board(input_board), ""]
  if is_maximizing:
    best_value = -float("Inf")
    moves = available_moves(input_board)
    random.shuffle(moves)
    best_move = moves[0]
    for move in moves:
      new_board = deepcopy(input_board)
      select_space(new_board, move, "X")
      hypothetical_value = minimax(new_board, False, depth - 1, alpha, beta)[0]
      if hypothetical_value > best_value:
        best_value = hypothetical_value
        best_move = move
      alpha = max(alpha, best_value)
      if alpha >= beta:
        break
    return [best_value, best_move]
  else:
    best_value = float("Inf")
    moves = available_moves(input_board)
    random.shuffle(moves)
    best_move = moves[0]
    for move in moves:
      new_board = deepcopy(input_board)
      select_space(new_board, move, "O")
      hypothetical_value = minimax(new_board, True, depth - 1, alpha, beta)[0]
      if hypothetical_value < best_value:
        best_value = hypothetical_value
        best_move = move
      beta = min(beta, best_value)
      if alpha >= beta:
        break
    return [best_value, best_move]


def play_game(ai):
    BOARDWIDTH = 7
    BOARDHEIGHT = 6
    board = []
    for x in range(BOARDWIDTH):
      board.append([' '] * BOARDHEIGHT)
    while not game_is_over(board):
        print_board(board)
        moves = available_moves(board)
        print("Available moves: " , moves)
        choice = 100
        good_move = False
        while not good_move:
            choice = input("Select a move:\n")
            try:
                move = int(choice)
            except ValueError:
                continue
            if move in moves:
                good_move = True
        select_space(board, int(choice), "X")
        if not game_is_over(board):
          result = minimax(board, False, ai, -float("Inf"), float("Inf"))
          print("Computer chose: ", result[1])
          select_space(board, result[1], "O")
    print_board(board)
    if has_won(board, "X"):
        print("X won!")
    elif has_won(board, "O"):
        print("O won!")
    else:
        print("It's a tie!")

def two_ai_game(ai1, ai2):
    BOARDWIDTH = 7
    BOARDHEIGHT = 6
    my_board = []
    for x in range(BOARDWIDTH):
      my_board.append([' '] * BOARDHEIGHT)
    while not game_is_over(my_board):
      result = minimax(my_board, True, ai1, -float("Inf"), float("Inf"))
      print( "X Turn\nX selected ", result[1])
      print(result[1])
      select_space(my_board, result[1], "X")
      print_board(my_board)

      if not game_is_over(my_board):
        result = minimax(my_board, False, ai2, -float("Inf"), float("Inf"))
        print( "O Turn\nO selected ", result[1])
        select_space(my_board, result[1], "O")
        print_board(my_board)
    if has_won(my_board, "X"):
        print("X won!")
    elif has_won(my_board, "O"):
        print("O won!")
    else:
        print("It's a tie!")

#--------------------------------

