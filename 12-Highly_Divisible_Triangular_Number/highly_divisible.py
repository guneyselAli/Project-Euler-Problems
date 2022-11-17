def divisor_count(number):
	divisor_list = []
	for i in range(1,int(number**0.5 + 1)):
		if number % i == 0:
			divisor_list.append(i)
			divisor_list.append(number/i)
	divisor_list = set(divisor_list)
	#We have converted the list to set because the square root of number may be an integer.
	#So in that case we would have had the square root of the number twice.
	return len(divisor_list)

count = 1
number = 1

while divisor_count(number) < 500:
	count += 1
	number += count
print(number)