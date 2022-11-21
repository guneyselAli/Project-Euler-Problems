def isprime(nb):
	if nb < 1:
		return 0
	elif nb <= 3:
		return 1
	for i in range(2, int(nb**0.5) + 1):
		if nb % i == 0:
			return 0
	return 1

def function(a,b,n):
	return n**2 + a*n + b 

results = {}
for a in range (-999,1000):
	for b in range(-1000,1001):
		n = 0
		while isprime(function(a,b,n)) == 1:
			n += 1
		results.update({n : [a,b,n]})	

print(results[max(list(results.keys()))])