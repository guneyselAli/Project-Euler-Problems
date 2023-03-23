import time
st = time.time()

def is_prime(nbr):
    if nbr < 2:
        return 0
    if nbr == 2:
        return 1
    for i in range(2, int(nbr**0.5) + 1):
        if nbr % i == 0:
            return 0
    return 1

def conjecture_check(nbr, prime_set):
    square = 0
    while True:
        square += 1
        if (nbr - 2 * (square ** 2)) in prime_set:
            return 1
        if nbr < 2 * (square ** 2):
            return 0

prime_set = {2}
nbr = 3
#I made a list of primes so I can keep previous prime numbers in memory
#So there will be no need to create or check prime numbers in conjecture check function
while True:
    if is_prime(nbr) == 1:
        prime_set.add(nbr)
    elif (conjecture_check(nbr, prime_set) != 1):
        print(nbr)
        break
    nbr += 2

et = time.time()
print((et - st)*1000)
#Its the fastest solution I have come up with