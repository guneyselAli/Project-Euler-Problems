import time

st = time.time()

def prime_generator():
	yield 2
	yield 3
	number = 3
	while True:
		number += 2
		for i in range(2, int(number**0.5) + 1):
			if number % i == 0:
				break
		else:
			yield number

list_of_primes = []
prime = 0
for prime in prime_generator():
	if prime >= 1000000:
		break
	list_of_primes.append(prime)

max_sum = 0
max_len = 0
for i in range(len(list_of_primes)):
	current_sum = list_of_primes[i]
	current_len = 1
	for j in range(i + 1, len(list_of_primes)):
		if current_sum + list_of_primes[j] >= 1000000:
			break
		current_sum += list_of_primes[j]
		current_len += 1
		if current_len > max_len and (current_sum in list_of_primes):
			max_sum = current_sum
			max_len = current_len

print(max_sum, max_len)
print(round((time.time() - st),2))