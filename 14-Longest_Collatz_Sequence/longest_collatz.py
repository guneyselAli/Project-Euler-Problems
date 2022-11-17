#A recursive function that calculates sequence counts of given number.
"""In second code block we created a dict. 
So when we reach for a number we already claculated before,
it will automatically get the result for that number and save time."""
def collatz_seq(current_count, number):
	if number in dict_seq:  
		return current_count + dict_seq[number] 
	if number == 1:
		return current_count + 1
	if number % 2 == 0:
		return collatz_seq(current_count + 1, number/2)
	else:
		return collatz_seq(current_count + 1, 3 * number + 1)


dict_seq = {} #We created a dictionary so we can store sequence for every number.
for i in range(1,1000000):
	dict_seq[i] = collatz_seq(0,i)
max_chain = max(list(dict_seq.values()))
number_for_max_chain = [key for key,value in dict_seq.items() if value == max_chain]
print(number_for_max_chain[0])
		

