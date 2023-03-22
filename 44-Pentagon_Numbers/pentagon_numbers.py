def pentagon_generator():
	n = 0
	while True:
		n += 1
		result = n * (3 * n - 1) / 2
		yield result

def solution():
	pentagon_list = []
	for j in pentagon_generator():
		pentagon_list.append(j)
		for k in pentagon_generator():
			if k == j:
				break
			if (j - k) in pentagon_list:
				for summation in pentagon_generator():
					if summation == (j + k):
						print (j - k)
						return (1)
					if summation > (j + k):
						break

solution()