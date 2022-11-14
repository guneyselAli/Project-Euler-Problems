def gridcalculator(size, mylist):
	sublist = []
	for x in range(size+1):
		for y in range(size+1):
			sublist.append(1)
		mylist.append(sublist)
		sublist = []
	for x in range(size+1):
		for y in range(size+1):
			if x == 0 and y == 0:
				pass
			elif x > 0 and y == 0:
				mylist[x][y] = mylist[x-1][y]
			elif x == 0 and y > 0:
				mylist[x][y] = mylist[x][y-1]
			else:
				mylist[x][y] = mylist[x-1][y] + mylist[x][y-1]

mylist = []
gridcalculator(20, mylist)
print(mylist[20][20])  