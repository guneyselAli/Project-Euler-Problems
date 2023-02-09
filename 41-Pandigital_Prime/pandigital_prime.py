def pandigital_check(mylist):
    new_list = set(mylist)
    if len(new_list) != len(mylist):
        return(0)
    for i in range(1,len(mylist) + 1):
        if str(i) in new_list:
            continue
        return(0)
    return(1)

def isprime(number):
	if number < 2:
		return 0
	elif number == 2:
		return 1
	for i in range(2, int(number**0.5) + 1):
		if number % i == 0:
			return 0
	return 1

def pandigital_generator():
    i = 987654322
    while True:
        i -= 1
        if pandigital_check(list(str(i))):
            yield i

num = pandigital_generator()

for i in num:
    if isprime(i): 
        print(i)
        break


