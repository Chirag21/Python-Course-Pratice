def display(lst):
    print('Here is the current list')
    print(lst)

def user_input():
    choice = 'wrong'
    while choice not in ['0','1','2','3','4']:
        choice = input('Pick a position (0,1,2,3,4) : ')

        if choice not in ['0','1','2','3','4']:
            print('Invalid choice!!! Try again.')

    return int(choice)

def replace(lst , index):
    choice = input('Enter a value : ')
    lst[index] = choice

    return lst

def to_continue():
    choice = 'wrong'
    while choice not in ['Y','N','y','n']:
        choice = input('Do you want to continue ?(Y or N) : ')
        if choice not in ['Y','N','y','n']:
            print('Invalid!! Try again.')
    
    if choice.lower() == 'y':
        return True
    else:
        return False

if __name__ == "__main__":
    lst = [1,2,3,4,5]
    choice = True
    while(choice):
        index = user_input()
        lst = replace(lst, index)
        display(lst)
        choice = to_continue()
