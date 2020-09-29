from random import shuffle

position = ['','c','']

def user_input():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input('Enter a choice 0,1, or 2 : ')
    return int(guess)   # IMP

def shuffle_list(lst):
    return shuffle(lst)

def check(lst,guess):
    if lst[guess] == 'c':
        print('Crrect!')
    else:
        print('Wrong!!!')
        print(lst)

guess = user_input()
shuffle_list(position)
check(position,guess)