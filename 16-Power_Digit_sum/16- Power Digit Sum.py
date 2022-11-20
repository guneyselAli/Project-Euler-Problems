number=2**1000

listofdigits=list(str(number))

summary=0

for i in listofdigits:
	summary += int(i)

print(summary)