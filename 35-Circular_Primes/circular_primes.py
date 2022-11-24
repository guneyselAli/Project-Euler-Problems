def isprime(number):
	if number == 2 or number == 3:
		return 1
	for i in range(2, int(number**0.5) + 1):
		if number % i == 0:
			return 0
	return 1


circularprimes = []
for i in range(2,1000000):
	if isprime(i) == 1:
		a = list(str(i))
		len_a = len(a)
		for times in range(len_a - 1):
			first = a[0]
			a[:len_a - 1] = a[1:len_a]
			a[len_a - 1] = first
			number = int("".join(a))
			if isprime(number) == 0:
				break
		else:
			circularprimes.append(i)
print(len(circularprimes))
