import random

# Global variables


theBoard = [' '] * 10  # a list of empty spaces
available = [str(num) for num in range(0, 10)]  # a List Comprehension
players = [0, 'X', 'O']  # note that players[1] == 'X' and players[-1] == 'O'


def display_board(a, b):
    print(
        f'Available   TIC-TAC-TOE\n  moves\n\n  {a[7]}|{a[8]}|{a[9]}        {b[7]}|{b[8]}|{b[9]}\n -------      -------\n  {a[4]}|{a[5]}|{a[6]}        {b[4]}|{b[5]}|{b[6]}\n -------      -------\n  {a[1]}|{a[2]}|{a[3]}        {b[1]}|{b[2]}|{b[3]}\n')


def place_marker(avail, board, marker, position):
    board[position] = marker
    avail[position] = ' '


def win_check(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or  # first row
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # second row
            (board[7] == mark and board[8] == mark and board[9] == mark) or  # third row
            (board[1] == mark and board[4] == mark and board[7] == mark) or  # first column
            (board[2] == mark and board[5] == mark and board[8] == mark) or  # second column
            (board[3] == mark and board[6] == mark and board[9] == mark) or  # third column
            (board[1] == mark and board[5] == mark and board[9] == mark) or  # diagonal
            (board[3] == mark and board[5] == mark and board[7] == mark))  # diagonal


def random_player():
    return random.choice((1, -1))


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    return ' ' not in board[1:]


def player_choice(board, player):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        try:
            position = int(input('Player %s, choose your next position(1-9) :' % (player)))
        except:
            print('Wrong input! Try again.')
    return position


def replay():
    return input('Do you want to play again?(y/n) : ').lower().startswith('y')


while True:
    # clear output
    print('\n' * 3)
    print('Welcome to Tic Tac Toe')
    toggle = random_player()
    player = players[toggle]
    print('For this round player %s, will go first' % player)
    while True:
        display_board(available, theBoard)
        position = player_choice(theBoard, player)
        place_marker(available, theBoard, player, position)
        if win_check(theBoard, player):
            display_board(available, theBoard)
            print(f'Player {player} wins!!!')
            break
        else:
            if full_board_check(theBoard):
                display_board(available, theBoard)
                print('This game is a draw!!!')
                break
            else:
                toggle *= -1
                player = players[toggle]
                print('\n' * 3)

    if not replay():
        break
