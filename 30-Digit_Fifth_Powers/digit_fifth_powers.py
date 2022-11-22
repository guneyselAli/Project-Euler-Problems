#I know this is not the perfect solution.
#I firstly calculated what is the maximum number that can be written of their digit's fifth powers.
#9999 >>> 9^5 * 4 = 236196 that means we can go over 9999
#99999 >>> 9^5 * 5 = 295245
#999999 >>> 9^5 * 6 = 354294
#Now our limit is probably between 99999 and 354294
#So I took 354294.

correctlist = []
for i in range(2,354295):
	digitlist = [int(a) for a in str(i)]
	sumof_powers = 0
	for digit in digitlist:
		sumof_powers += digit**5
	if sumof_powers == i:
		correctlist.append(i)
print(f"List of numbers are: {correctlist}")
print(f"Sum of numbers = {sum(correctlist)}")
