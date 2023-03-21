import itertools

def divisibility_checker(number):
	mylist = list(str(number))
	divider_list = [2,3,5,7,11,13,17]
	index_1 = 1
	index_2 = 2
	index_3 = 3
	divider_idx = 0
	while index_3 < 10:
		number = int(mylist[index_1] + mylist[index_2] + mylist[index_3])
		if number % divider_list[divider_idx] > 0:
			return 0
		index_1 += 1
		index_2 += 1
		index_3 += 1
		divider_idx += 1
	return 1
	

def pandigital_checker(number):
	mylist = list(str(number))
	
	for i in range(0,10):
		if str(i) not in mylist:
			return 0
	return 1


digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sum_of_all = 0
for subset in itertools.permutations(digits, 10):
    number = int(''.join(map(str, subset)))
    if pandigital_checker(number) == 1:
	    if divisibility_checker(number) == 1:
		    sum_of_all += number

print(sum_of_all)