Lets try to explain how to find recurring decimal for a fraction.

1/24 will be our fraction. 

Dividing 1 by 24, 1 cant be divided by 24 in conventional way. So we multiply it with 10 and place a dot on our divison. Division = "0."
So the next operation will be 10/24.
Again, we cant divide 10 by 24 so we multiply it with 10 and put another zero to our division
So the division = "0.0" and we are going to operate 100/24

100/24 = 4 with 4 remainder
Division = "0.04"

Now we are going to take remainder and divide it again and again

4/24 --> 40/24 = 1 with 16 remainder
Division = "0.041"

16/24 --> 160/24 = 6 with 16 remainder

Now we get to the point where we now what is the result of 16/24 because we have done it before. After this point the cycling decimal is going to repeat infinitely. So we should find where we first operated 16/24 and take the result between that point and last point. That will be our recurring decimal. At our example it is only one number which is 6.
So 1/24 = 0.041(6)

If we had more than one number after the start of the recurring point. It will be our whole recurring decimal part.

So this was the mathematical explanation of what we actually do in our python code.


Lets try to explain what I did in the code:
In first function (findcycle) I created a function takes the numerator and the denominator. Which in our example these were 1 and 24.
I created a list called division to store every digit in division.
And created a remainderindex dictionary to store every remainder and its index in the division list.
I kept doing the iteration above until I find the remainder that I have already calculated.

For the result I created a dictionary which consist of the keys = cycles and values = denominators. So I can store which cycle has which denominator. At the end of the code we find longest cycle and its fraction's denominator.

I know I explanied this a bit long. But I wanted you to understand everything like I did :) 
