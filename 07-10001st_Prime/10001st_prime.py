def isprime(nb):
	if nb <= 1:
		return 0
	if nb == 2:
		return 1
	for i in range (2, int(nb ** 0.5 + 1)):
		if nb % i == 0:
			return 0
	return 1
i = 0
count = 0
while True:
	i += 1
	if isprime(i) == 1:
		count += 1
	if count == 10001:
		print(i)
		break
