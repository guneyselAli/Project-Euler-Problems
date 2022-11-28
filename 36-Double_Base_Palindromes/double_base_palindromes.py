import time
start = time.time()
#Function that converts a decimal number to binary number.
def decimal2binary(number):
	while number > 0 :
		yield number % 2
		number =int(number / 2)

#Function that checks the list if it is equal backwards.
def check_palindrome(number_list):
	if number_list == number_list[::-1]:
		return 1
	else :
		return 0
summation = 0
for i in range(1000000):
	if check_palindrome(list(str(i))) == 1:
		if check_palindrome(list(decimal2binary(i))) == 1:
			summation += i
print(summation)
print(f"Elapsed time: {time.time() - start}")
