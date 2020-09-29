check_list = [1, 2, 3, 4, 5]
def display():
    check_digit = False
    check_range = False
    index = int(input(f'Enter a index to change number(0-{len(check_list-1)}'))
    while(not check_digit or not check_range):
        if not check_digit:
            print('Please enter a number only')
        if index not in range(0, len(check_list)-1):
            print(f'Please enter a number between(0-{0})',len(check_list-1))
    return index

print(display())