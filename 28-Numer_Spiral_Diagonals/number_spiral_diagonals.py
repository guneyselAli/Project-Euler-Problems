#Instead of trying to create the whole spiral, I came up with this logic below.

#First : Numbers in the direction of up right. 
#They go up with squares of odd numbers 3^2 5^2 7^2
#You can check it by writing the spiral down to a paper.
#In a spiral 5 by 5 the top right value is 5^2. So in 1001 by 1001 spiral it will be 1001^2 
rightup = 0
for i in range(3,1002,2):
	rightup += i**2


#Second : Numbers in the direction of up left.
#The formula is n^2 - (n-1) with the increment of odd numbers.
#So it will go like this. "3^2 - 2" , "5^2 - 4" , "7^2 - 6"
leftup = 0
for i in range(3,1002,2):
	leftup += i**2 - (i - 1)

#Third : Numbers in the direction of down left.
#The formula is n^2 + 1. But this time the n is even numbers 
#So it will go like this. "2^2 + 1" , "4^2 + 1" , "6^2 + 1" limit of n is 1001 - 1 = 1000
leftdown = 0
for i in range(2,1001,2):
	leftdown += i**2 + 1

#Fourth : Numbers in the direction of down right.
#The formula is n^2 - (n - 1). N is even numbers starting from 2. And goes on until 1000.
#So it will go like this. "2^2 - 1" , "4^2 - 3" , "6^2 - 5".
rightdown = 0
for i in range(2,1001,2):
	rightdown += i**2 - (i - 1)

#Lastly we are going to calculate sum of diagonals and add "1" that we didnt include before.
result = rightup + leftup + leftdown + rightdown + 1
print(result)


