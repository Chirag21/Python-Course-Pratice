""" OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
old_macdonald('macdonald') --> MacDonald
Note: 'macdonald'.capitalize() returns 'Macdonald' """

def old_macdonald(name):
    first_half = name[:3]
    second_half = name[3:]

    return first_half.capitalize() + second_half.capitalize()

print(old_macdonald('macdonald'))


""" MASTER YODA: Given a sentence, return a sentence with the words reversed
master_yoda('I am home') --> 'home am I'
master_yoda('We are ready') --> 'ready are We' """

def master_yoda(text):
    wordlist = text.split()
    reversed_wordlist = wordlist[::-1]
    return ' '.join(reversed_wordlist) 

print(master_yoda('I am home'))
print(master_yoda('We are ready'))


""" ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
almost_there(90) --> True
almost_there(104) --> True
almost_there(150) --> False
almost_there(209) --> True """

def almost_there(n):
    return abs(n-100) <= 10 or abs(n-200) <= 10

print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))