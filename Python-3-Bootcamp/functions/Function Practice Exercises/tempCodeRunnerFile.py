def palindrome(s):
    half_length = int(len(s)/2)
    for i in range(0,half_length):
        for j in range(len(s)-1,half_length+2,-1):
            if s[i].lower() != s[j].lower():
                return False
    return True

print(palindrome('madam'))