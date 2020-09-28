mylist = list(range(0,11,2))
print(mylist)

for num in range(0,11,2) :
    print(f'{num}')

###################################################################################

mylist2 = [ num for num in range(1,51) if num%3 == 0 ]
print(mylist2)

###################################################################################

#FizBuzz
for num in range(1,101) :
    if num%3 == 0 and num%5 == 0:
        print(f'{num} FizzBuzz')
    elif num%3 == 0 :
        print(f'{num} Fizz')
    elif num%5 == 0 :
        print(f'{num} Buzz')
    else:
        print(num)

###################################################################################

st1 = 'Print only words that starts with s in this sentence'
list_st1 = st1.split()
for word in list_st1 : # for word in st1.spli()
    if word[0].lower() == 's':
        print(f'{word}',end=', ')

###################################################################################

st2 = 'Print every word in this sentence that has an even number of letters'
for word in st2.split() :
    if len(word) % 2 == 0:
        print(f'{word}',end=', ')

###################################################################################

st3 = 'Create a list of the first letters of every word in this string'
list_str = [word[0] for word in st3.split()]
print(list_str)

####################################################################################