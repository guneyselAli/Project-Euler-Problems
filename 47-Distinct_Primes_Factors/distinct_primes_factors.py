import time
st = time.time()

def next_prime(number):
    if number < 2:
        return 2
    while True:
        number += 1
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                break
        else:
            return number

def distinct_pf_calculator(number, prime_list):
    count = 0
    for prime in prime_list:
        if number % prime == 0:
            count += 1
            while number % prime == 0:
                number = number / prime
        if number == 1:
            return count


def solution(quantity, prime_factors):
    number = 1
    prime_list = [2]
    #I have made a list of prime so I wont create prime numbers from scratch everytime
    while True:
        #If the last number in prime list smaller than the half of the number
        #The loop below will append the prime values until it reaches half of the number
        while prime_list[-1] < ((number / 2) - 1):
            prime_list.append(next_prime(prime_list[-1]))
        count = 0
        while distinct_pf_calculator(number, prime_list) == prime_factors:
            count += 1
            number += 1
            if count == quantity:
                print(f"Answer = {number - quantity}" )
                return 1
        number += 1

solution(4,4)

et = time.time()

print(f"Elapsed time {round((et - st),2)} seconds")