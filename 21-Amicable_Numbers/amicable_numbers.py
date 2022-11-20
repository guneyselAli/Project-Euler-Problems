listofamicable=[]

def sumofdiv(n):
	summation=0
	for i in range(1,int(n**0.5+1)):
		if n%i==0 and i**2!=n:
			summation+=i
			if i!=1:
				summation+=int(n/i)
		elif i**2==i:
			summation+=i
	return summation

for i in range(1,10000):
	a=sumofdiv(i)
	if sumofdiv(a)==i and a!=i:
		listofamicable.append(i)
print(listofamicable)
print(sum(listofamicable))