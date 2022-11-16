#First we build a function that checks if the number is prime.
def isprime(number):
	if number < 2:
		return 0
	elif number == 2:
		return 1
	for i in range(2, int(number**0.5) + 1):
		if number % i == 0:
			return 0
	return 1

#Calculation of sum of prime numbers below two million.
sumofprimes = 0
for a in range(2000000):
	if isprime(a) == 1:
		sumofprimes += a

print(sumofprimes)