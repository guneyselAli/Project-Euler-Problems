mystr = ''

for i in range(1,10000001):
    mystr += (str(i))
    if len(mystr) > 1000000:
        break


result = int(mystr[0]) * int(mystr[9]) * int(mystr[99])
result *= int(mystr[999]) * int(mystr[9999]) * int(mystr[99999])
result *= int(mystr[999999])

print(result)