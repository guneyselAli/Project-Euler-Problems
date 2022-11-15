sumofsquares = 0
for i in range(101):
	sumofsquares += i**2

squareofsum = 0
for i in range(101):
	squareofsum += i
squareofsum = squareofsum**2

print(squareofsum - sumofsquares)
