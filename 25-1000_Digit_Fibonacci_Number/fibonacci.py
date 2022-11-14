index = 3
b = 1
c = 2
while (c / 10**999 < 1):
	index += 1
	c = c + b
	b = c - b
print(index)
