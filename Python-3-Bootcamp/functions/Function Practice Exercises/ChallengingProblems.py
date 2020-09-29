""" SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
 spy_game([1,2,4,0,0,7,5]) --> True
 spy_game([1,0,2,4,0,5,7]) --> True
 spy_game([1,7,2,0,4,5,0]) --> False """

from os import truncate


def spy_game(nums):
    code = [0,0,7,'x']
    for num in nums:
        if num == code[0]:
            code.pop(0)

    return len(code) == 1
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))


""" COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
count_primes(100) --> 25 """

import time
start_time = time.time()

def count_primes(num):
    primes = [2]  # already added 2 to prime list. Can chack only for odd prime numbers then
    x = 3
    if num < 2:  # for the case of num = 0 or 1
        return 0
    while x <= num:
        for y in primes:  # test all odd factors up to x-1   TRICK
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)

print(count_primes(100))
print("Process finished --- %s seconds ---" % (time.time() - start_time))


""" PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter¶
print_big('a')

out:   *  
      * *
     *****
     *   *
     *   *
HINT: Consider making a dictionary of possible patterns, and mapping the alphabet to specific 5-line combinations of patterns.
For purposes of this exercise, it's ok if your dictionary stops at "E". """

def print_big(letter):
    patterns = {1:'  *  ', 2:' * * ', 3:'*   *', 4:'*****', 5:'**** ', 6:'   * ', 7:' *   ', 8:'*   * ', 9:'*    '}
    alphabet = {'A':[1,2,4,3,3], 'B':[5,3,5,3,5], 'C':[4,9,9,9,4], 'D':[5,3,3,3,5], 'E':[4,9,4,9,4]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])

print_big('b')