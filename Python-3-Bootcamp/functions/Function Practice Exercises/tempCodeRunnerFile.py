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