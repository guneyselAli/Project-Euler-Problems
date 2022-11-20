def factorial(n):
	product=1
	for i in range(1,n+1):
		product *= i

	product=list(str(product))

	product=[int(i) for i in product]

	print(sum(product))



factorial(100)