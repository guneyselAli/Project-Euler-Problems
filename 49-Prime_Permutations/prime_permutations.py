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
i = 1000
prime_list = []
while True:
    a = next_prime(i)
    if a > 9999:
        break
    prime_list.append(a)
    i = a

sequence_list = []
for prime in prime_list:
    if (prime + 3330) in prime_list:
        if (prime + 6660) in prime_list:
            sequence_list.append([prime, prime+3330, prime+6660])

sorted_list = []
#Since our sequence list is a nested list
#I need to copy all the lists inside of the sequence list to sorted list
#Because I dont want to change the original list
for item in sequence_list:
    sorted_list.append(item[:])

for item in sorted_list:
    for i in range(len(item)):
        item[i] = sorted(str(item[i]))

for i in range(len(sorted_list)):
    if (sorted_list[i][0] == sorted_list[i][1] and sorted_list[i][1] == sorted_list[i][2]):
        print(sequence_list[i])
        if sequence_list[i][0] != 1487:
            print("\nThe answer:")
            print(str(sequence_list[i][0]) + str(sequence_list[i][1]) + str(sequence_list[i][2]))
    

