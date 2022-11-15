# Number which is evenly divisible by all of the numbers between 1 and 20 is actually called
# smallest multiple of 1 2 3 4 5 .... 19 20. 

def isprime(nb):  #Function checks whether given number is prime or not
	if nb <= 1:
		return 0
	if nb == 2:
		return 1
	i = 2
	while i < nb**0.5 +1:
		if nb % i == 0:
			return 0
		i += 1
	return 1

def primefactor(nb):  #Returns list of primefactors of given number with repetition
	primefactors = []
	i = 2
	while i <= nb:
		if nb % i == 0 and isprime(i) == 1:
			while nb % i == 0:
				nb /= i
				primefactors.append(i)
		i += 1
	return primefactors[:]

union_of_multiples = [] 

""" In this line of code below we are trying to find the common prime factors of given numbers
for example	prime factors of 160 = (2^5) * 5
		prime factors of 30 = 2 * 3 * 5
So our smallest multiple of 160 and 30 is (2^5) * 3 * 5 = 480
In a range of numbers between 1 and 20 we first checked current number's prime factors
and after that we check the next number's prime factors and compared their each prime factor counts.
if the next one has more times of currently checked prime number, count of prime factor is changed
as next one's count"""

for i in range(1, 21):
	b = primefactor(i)
	for item in b:
		countx = 0
		for x in range(len(b)):
			if item == b[x]:
				countx += 1
		county = 0
		for y in range(len(union_of_multiples)):
			if item == union_of_multiples[y]:
				county += 1
		if countx > county:
			union_of_multiples += [item]*(countx - county)

print(f"List of common prime factors are: {sorted(union_of_multiples)}")
a = 1
for x in union_of_multiples:
	a *= x		
print(f"Smallest multiple is: {a}")
