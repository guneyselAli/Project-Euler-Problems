#Solution of this problem is a bit long
#So I created a solution file that covers the solution of the problem.
def findcycle(numerator, denominator):
	remainderindex = {}
	division = []
	if numerator / denominator < 1:
		division.extend(["0", "."])
	#since our numerator will always be "1" this part is unnecessary.
	#but I wanted my function to work with all numbers
	elif numerator / denominator >= 1:
		division.extend([str(int(numerator/denominator)), "."])
		if numerator % denominator != 0:
			numerator = numerator - int(numerator / denominator)*denominator 
		else:
			return "0"
	index = 2
	while numerator % denominator != 0:
		remainderindex.update({numerator % denominator : index})
		numerator *= 10
		#remainderindex.update({numerator % denominator : index})
		division.append(str(int(numerator/denominator)))
		numerator = numerator % denominator
		index += 1
		if numerator % denominator == 0:
			return "0"
		if numerator % denominator in list(remainderindex.keys()):
			first = ("".join(division[:remainderindex[numerator % denominator]]))
			cycle = ("".join(division[remainderindex[numerator % denominator]:index+1]))
			final = f'{first}({cycle})' #You can print this if you want full number.
			return(cycle)			
			break

dictofcycles = {}
for i in range(2,1000):
	dictofcycles.update({findcycle(1,i): i})
longestcycle = max(list(dictofcycles.keys()), key=len)
print(f"Longest cycle is: {longestcycle}")
print(f"Denominator is : {dictofcycles[longestcycle]}")

