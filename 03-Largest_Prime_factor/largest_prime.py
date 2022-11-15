def isprime(nbr):
    if nbr <= 1:
        return 0
    if nbr == 2:
        return 1
    i = 2
    while i < nbr ** 0.5 + 1:
        if nbr % i == 0:
            return 0
        i += 1
    return 1

number = 600851475144

i = 1
while i <= number ** 0.5:
    if number % i == 0 and isprime(i) == 1:
        print(i)
    if number % i == 0 and isprime(number / i) == 1:
        print(int(number / i))
    i += 1

"""since we are checking prime factors until square foot of the number,
we also need to check the dividers above the square foot of the number.
so the second if condition is checking the prime factors above the square foot of the number
i.e; if the number is 34 the prime factors will be 2 and 17, if we check prime factors until the square root of the number we won't find 17 if we didnt build the second if condition."""
