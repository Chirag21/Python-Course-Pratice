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
    flag= True
    sum = 0
    for num in arr:
        while flag:
            if num != 6:
                sum += num
                break
            else:
                flag = False
            while not flag:
                if num != 9:
                    break
                else:
                    flag = True
    return sum

print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))

print(summer69([1, 3, 5]))
print(summer69([4, 5, 6, 7, 8, 9]))
print(summer69([2, 1, 6, 9, 11]))