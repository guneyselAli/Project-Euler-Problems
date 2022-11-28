def isprime(number):
	if number < 2:
		return 0
	if number <= 3:
		return 1
	for i in range(2,int(number**0.5)+1):
		if number % i == 0:
			return 0
	return 1

def makelist(number):
	a = list(str(number))
	b = a[:]
	for i in range(len(a)-1):
		a.pop()
		yield int("".join(a[:]))
	for i in range(len(b)-1):
		b.pop(0)
		yield int("".join(b[:]))

truncatable_list = []
i = 10
while True:
	if isprime(i) == 1:
		mylist = list(makelist(i))
		for number in mylist:
			if isprime(number) == 0:
				break
		else:
			truncatable_list.append(i)
	if len(truncatable_list) == 11:
		break
	i += 1

print(truncatable_list)
print(sum(truncatable_list))
