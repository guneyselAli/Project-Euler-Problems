a_b_list = []

for a in range(10,99):
	for b in range(a+1,100):
		if "0" in str(a) + str(b):
			continue
		if str(a)[0] in list(str(b)):
			new_b = int(str(b)[1 - str(b).index(str(a)[0])])
			new_a = int(str(a)[1])
		elif str(a)[1] in list(str(b)):
			new_b = int(str(b)[1 - str(b).index(str(a)[1])])
			new_a = int(str(a)[0])
		else:
			continue
		if a/b == new_a / new_b:
			a_b_list.append([new_a,new_b])
denominator = 1
for i in range(len(a_b_list)):
	denominator *= a_b_list[i][1]

numerator = 1
for i in range(len(a_b_list)):
	numerator *= a_b_list[i][0]

for i in range(1,numerator+1):
	if numerator % i == 0 and denominator % i == 0:
		numerator /= i
		denominator /= i

print(numerator, denominator)
