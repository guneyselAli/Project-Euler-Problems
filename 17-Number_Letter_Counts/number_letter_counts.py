import math

letterdict={1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten'}
letterdict.update({11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen'})
letterdict.update({20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety' })


def numberprinter(number):

	if number<=10 or (number%10==0 and number<100): #for 0-10 and multiples of 10
		return letterdict[number]

	elif number<20: #for 11-19
		return letterdict[number]

	elif number<100 and number%10!=0: #for 21-99 without multiples of 10
		return letterdict[number-number%10]+letterdict[number%10]

	elif 1000>number>=100 and number%100==0: #for multiples of 100
		return letterdict[number/100]+'hundred'

	elif 1000>number>=100 and number%100!=0: #for 101-999
		hundreds=math.floor(number/100)
		tens=math.floor((number-hundreds*100)/10)
		ones=math.floor(number-hundreds*100-tens*10)

		if tens==1 and ones!=0:  #X11-#X19
			return letterdict[hundreds]+'hundredand'+letterdict[number-hundreds*100]

		elif tens==0 and ones!=0: #X0X 
			return letterdict[hundreds]+'hundredand'+letterdict[ones]

		elif tens>0 and ones==0: #XX0
			return letterdict[hundreds]+'hundredand'+letterdict[tens*10]

		elif tens>1 and ones!=0: #XXX
			return letterdict[hundreds]+'hundredand'+letterdict[tens*10]+letterdict[ones]
	elif number==1000:
			return 'onethousand'


listofletters=[]
fulltsring=''
for number in range(1,1001):
	listofletters.append(numberprinter(number))

fullstring=''.join(listofletters)
print(len(fullstring))
