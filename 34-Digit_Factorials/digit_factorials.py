#Maximum number can be written with the sum of its digit's factorials is 9999999 (ten million)
#Its a total brute force and takes a lot of time.
#But I couldnt come up with differen idea to find the upper limit.

limit = 362880 * 7 #9! = 362880

def factorial(number):
	if number == 0:
		return 1
	if number == 1:
		return 1
	return number*factorial(number-1)

curiouslist = []
for i in range(3, limit + 1):
	mylist = [factorial(int(i)) for i in str(i)]
	if i == sum(mylist):
		curiouslist.append(i)
print(sum(curiouslist))
