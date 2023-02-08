#with this function we check the product if it has duplicates or zeros
#it speeds up the process
def check_duplicates(mystring):
    mylist = list(mystring)
    myset = set(mylist)
    if len(myset) == len(mylist) and ('0' not in mylist):
        return (1)
    return (0)

#In this function we check if the given list of numbers are 1 to 9
#and there is not any duplicates
#and also length must be 9
def pandigital_check(mylist):
    new_list = set(mylist)
    if len(new_list) != len(mylist):
        return(0)
    for i in range(1,10):
        if str(i) in new_list:
            continue
        return(0)
    if len(new_list) == 9:
        return(1)
    else:
        return(0)

#this function checks number and the multiplier if the products exceeds the 9 digit
def breakcheck(number, i):
    product = ''
    for multiplier in range(1,i + 1):
        product = product + str(number * multiplier)
    if len(product) > 9:
        return 1
    return 0

listofpandigitals = []
for i in range(2,10):
    number = 0
    while True:
        number+=1
        if breakcheck(number, i) == 1:
            break
        listofnumber = []
        for a in range(1,i+1):
            mystr = str(number * a)
            if check_duplicates(mystr) == 0:
                break
            for item in mystr:
                listofnumber.append(item)
        if pandigital_check(listofnumber) == 1:
            listofpandigitals.append(listofnumber)


myinteger = 0
for i in range(len(listofpandigitals)):
    for number in listofpandigitals[i]:
        myinteger = myinteger*10 + int(number)
    listofpandigitals[i] = myinteger
    myinteger = 0

print(max(listofpandigitals))

