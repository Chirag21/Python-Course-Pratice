""" Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False """

def has_33(nums):
    check = False
    count = 0
    for i in range(0,len(nums)-1):
        if(nums[i] == 3 and nums[i+1] == 3):  # OR if nums[i:i+2] == [3,3]
            return True
    
    return False

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))


""" PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
paper_doll('Hello') --> 'HHHeeellllllooo'
paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii' """

def paper_doll(text):
    result = ''
    for c in text:
        result += c*3
    
    return result

print(paper_doll('Hello'))
print(paper_doll('Mississippi'))


""" BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
blackjack(5,6,7) --> 18
blackjack(9,9,9) --> 'BUST'
blackjack(9,9,11) --> 19 """

def blackjack(a,b,c):
    if sum([a,b,c]) <= 21:
        return sum([a,b,c])
    elif 11 in [a,b,c] and sum([a,b,c]) <= 31:
        return sum([a,b,c])-10

    return 'BUST'

print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))


""" SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.¶
summer_69([1, 3, 5]) --> 9
summer_69([4, 5, 6, 7, 8, 9]) --> 9
summer_69([2, 1, 6, 9, 11]) --> 14 """

def summer_69(arr):
    flag = True
    sum = 0
    for num in arr:
        if num==6:
            flag = False
        elif num==9:
            flag = True
            continue
        if flag:
            sum += num
    return sum

def summer69(arr):
    total = 0
    flag = True
    for num in arr:
        while flag:
            if num != 6:
                total += num
                break
            else:
                flag = False
        while not flag:
            if num != 9:
                break
            else:
                flag = True
                break
    return total

print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))

print(summer69([1, 3, 5]))
print(summer69([4, 5, 6, 7, 8, 9]))
print(summer69([2, 1, 6, 9, 11]))