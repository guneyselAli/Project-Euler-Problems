permlist = []
def perm(templist, head, mylist):
	if head != None:
		templist[:] = templist[:] + [head]
	if len(mylist) == 0:
		permlist.append(templist[:])
		templist.clear()
	for i in range(0, len(mylist)):
		if i != len(mylist):
			perm(templist[:],mylist[i], mylist[:i] + mylist[i+1:])
		else:
			perm(templist[:],mylist[i], [])

mylist = [0,1,2,3,4,5,6,7,8,9]
perm([],None,mylist)

print(int("".join(map(str,permlist[999999]))))