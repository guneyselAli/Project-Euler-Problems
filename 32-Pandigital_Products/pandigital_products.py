import time
start = time.time()
#This functions checks 
#If the numbers an the product contain same digits
#If the total length is 9
#If they contain 0.
def product_check(number1,number2,product):
	mylist = list(str(number1) + str(number2) + str(product))
	if len(set(mylist)) != len(mylist) or len(mylist) != 9 or "0" in mylist:
		return 0
	return 1

#This function  checks the number if it contains same digits or 0 in it.
def num_check(number):
	if len(set(list(str(number)))) != len(list(str(number))) or "0" in list(str(number)):
		return 0

listofproducts = []
for a in range(0,9877):
	if num_check(a) == 0: #This line makes the solution faster.
		continue
	for b in range(0,98):
		if product_check(a,b,a*b) == 1:
			listofproducts.append(a*b)
print(sum(set(listofproducts)))
print(f"Elapsed time: {time.time() - start}")

