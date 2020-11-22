from random import randint


def display_position():
    print("Following are the positions for 'X' and 'O' You have to choose between these numbers only")
    print(' 1 ' + ' | ' + ' 2 ' + ' | ' + ' 3 ')
    print('---' + ' | ' + '---' + ' | ' + '---')
    print(' 4 ' + ' | ' + ' 5 ' + ' | ' + ' 6 ')
    print('---' + ' | ' + '---' + ' | ' + '---')
    print(' 7 ' + ' | ' + ' 8 ' + ' | ' + ' 9 ')


def display_board(board):
    print('\n')
    print(' ' + board[1] + '  ' + '|' + '  ' + board[2] + '  ' + '|' + '  ' + board[3])
    print('----' + '|' + '-----' + '|' + '----')
    print(' ' + board[4] + '  ' + '|' + '  ' + board[5] + '  ' + '|' + '  ' + board[6])
    print('----' + '|' + '-----' + '|' + '----')
    print(' ' + board[7] + '  ' + '|' + '  ' + board[8] + '  ' + '|' + '  ' + board[9])


def choose_first():
    flip = randint(0, 1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':  # OR  if not (marker == 'X' or marker == 'O'):
        marker = input("Select marker 'X' or 'O' : ").upper()
    if marker == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


def place_marker(board, marker, position):
    board[position] = marker


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    return ' ' not in board[1:]


def replay():
    return input("Do you want to play again('Y/N')  : ").upper() == 'Y'


def win_check(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or  # first row
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # second row
            (board[7] == mark and board[8] == mark and board[9] == mark) or  # third row
            (board[1] == mark and board[4] == mark and board[7] == mark) or  # first column
            (board[2] == mark and board[5] == mark and board[8] == mark) or  # second column
            (board[3] == mark and board[6] == mark and board[9] == mark) or  # third column
            (board[1] == mark and board[5] == mark and board[9] == mark) or  # diagonal
            (board[3] == mark and board[5] == mark and board[7] == mark))  # diagonal


def board_full_check(board):
    for i in range(1, 10):  # Skip space at 0th index. So start with 1
        if board[i] == ' ':  # or if space_check(board,i):
            return False
    return True


def player_choice():
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Enter a position (1-9) : '))
    return position


print('Welcome to Tic Tac Toe!')
while True:
    # Reset the board
    print('\n' * 7)
    board = [' '] * 10
    game_on = True
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first')
    display_position()
    while game_on:  # Or while True:
        if turn == 'Player 1':
            # Player1's turn.

            display_board(board)
            position = player_choice()
            place_marker(board, player1_marker, position)
            if win_check(board, player1_marker):
                display_board(board)
                print(turn + " with marker '" + player1_marker + "' Won!!!")
                game_on = False  # OR break
            else:
                if board_full_check(board):
                    display_board(board)
                    print('Match drawn!!!')
                    break
                else:
                    turn = 'Player 2'
        else:
            # Player2's turn.

            display_board(board)
            position = player_choice()
            place_marker(board, player2_marker, position)
            if win_check(board, player2_marker):
                display_board(board)
                print(turn + " with marker '" + player2_marker + "' Won!!!")
                game_on = False  # OR break
            else:
                if board_full_check(board):
                    display_board(board)
                    print('Match drawn!!!')
                    break
                else:
                    turn = 'Player 1'
    if not replay():
        break
