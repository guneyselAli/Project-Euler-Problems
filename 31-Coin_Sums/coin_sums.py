#This problem solved with total brute force.
#There are way more clever solutions out there.
#But since this is the only solution I came up with at my first try,
#I wanted to post this one.
possibilities = 0
count = 0
for twohundredp in range(0,2):
	for onehundredp in range(0,3):
		for fiftyp in range (0,5):
			for twentyp in range(0,11):
				for tenp in range(0,21):
					for fivep in range(0,41):
						for twop in range(0,101):
							if twohundredp*200 + onehundredp*100 + fiftyp*50 + twentyp*20 + tenp*10 + fivep*5 + twop*2 <= 200:
								onep = 200 - (twohundredp*200 + onehundredp*100 + fiftyp*50 + twentyp*20 + tenp*10 + fivep*5 + twop*2)
							if (twohundredp*200 + onehundredp*100 + fiftyp*50 + twentyp*20 + tenp*10 + fivep*5 + twop*2 + onep) == 200:
								possibilities += 1
							count +=1

print(possibilities)
	
