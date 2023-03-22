
def solution():
#I did the order below because hexagon increments more than penta
#and penta increments more than triangle
	i,j,k = 1,1,1
	while True:
		i += 1
		hexagon = i * (2 * i - 1)
		while True:
			j += 1
			penta = j * (3 * j - 1) / 2
			if penta == hexagon:
				while True:
					k += 1
					triangle = k * (k + 1) / 2
					if triangle == penta and triangle != 40755:
						print(triangle)
						return (1)
					if triangle > penta:
						break
			if penta > hexagon:
				break

solution()