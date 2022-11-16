a = 1
search = True
while search and a < 1000:
	b = a + 1
	while search and b < 1000:
		c = (a**2 + b**2)**0.5 
		if a + b + c == 1000:
			print(f"a={a}, b={b}, c={c}")
			print(a*b*c)
			search = False
		b += 1
	a += 1

"""At line 22 we found c via calculating the square root of a**2 + b**2
But there is a flaw in this line that we can ignore. Line 22 may return an irrational value
i.e. if a = 4 and b = 6, a**2 + b**2 will be equal to 52 and square root of 52 is irrational.
Although this flaw, we trust in the problem description.
It tells us there is an exact three number that has a sum of 1000, and it provides the pythagorean rule.
"""