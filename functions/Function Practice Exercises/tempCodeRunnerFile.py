def almost_there(n):
    return abs(n-100) <= 10 or abs(n-200) <= 10

print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))