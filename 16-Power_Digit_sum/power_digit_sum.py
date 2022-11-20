number=2**1000

listofdigits=list(str(number))

summation=0

for i in listofdigits:
	summation += int(i)

print(summation)