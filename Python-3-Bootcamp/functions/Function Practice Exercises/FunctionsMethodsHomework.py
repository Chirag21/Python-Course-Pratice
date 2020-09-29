""" Write a function that computes the volume of a sphere given its radius.
Formula is 4/3 pi r^3 """

from math import pi
def vol(rad):
    return (4/3)*pi*(rad**3)
print(vol(2))


""" Write a function that checks whether a number is in a given range (inclusive of high and low) """

def ran_check(num,low,high):
    return num>=low and num<=high

def ran_check1(num,low,high):
    return num in range(low,high+1)

print(ran_check(3,2,7))
print(ran_check1(3,2,7))


""" Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters. """

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'

def up_low(s):
    print(f'Original string : {s}')
    u,l = 0,0
    for char in s:
        if char.isupper():
            u+=1
        elif char.islower():
            l+=1
        else:
            pass
    return u,l

count = up_low(s)
print(f'No. of Lower case Characters : {count[0]}')
print(f'No. of Lower case Characters : {count[1]}') 


def up_low1(s):
    print(f'Original string : {s}')
    dict = {'upper':0, 'lower':0}
    for char in s:
        if char.isupper():
            dict['upper']+=1
        elif char.islower():    
            dict['lower']+=1
        else:
            pass
    return dict

count = up_low1(s)
print(f'No. of Lower case Characters : {count["upper"]}')
print(f'No. of Lower case Characters : {count["lower"]}')


""" Write a Python function that takes a list and returns a new list with unique elements of the first list. """

sample_list = [1,1,1,1,2,2,3,3,3,3,4,5]
def unique_list(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique

print( unique_list(sample_list) )

def unique_list1(lst):
    return list(set(lst))

print( unique_list1(sample_list) )


""" Write a Python function to multiply all the numbers in a list. """

sample_list = [1, 2, 3, -4]
def multiply(lst):
    prod = 1
    for num in sample_list:
        prod *= num
    return prod

print( multiply(sample_list) )


""" Write a Python function that checks whether a word or phrase is palindrome or not. """


def palindrome(s):
    s = s.replace(' ','')
    half_length = int(len(s)/2)
    for i in range(0, half_length):
        for j in range(len(s)-1, half_length+2, -1):
            if s[i].lower() != s[j].lower():
                return False
    return True

print(palindrome('madam madam'))

def palindrome1(s):
    s = s.replace(' ','')
    return s==s[::-1]

print(palindrome1('madam madam'))


""" Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation) """

import string
def ispangram(str1, alphabet = string.ascii_lowercase):
    alphaset = set(alphabet)
    str1 = str1.replace(' ','')
    str1 = str1.lower()
    str1 = set(str1)
    return str1 == alphaset

print(ispangram('The quick brown fox jumps over the lazy dog'))
print(ispangram('This is random'))