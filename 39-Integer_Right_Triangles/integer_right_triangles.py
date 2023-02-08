import math

def perimeter_calc(a,b):
    perimeter = a + b + (a**2 + b**2)**0.5
    if math.floor(perimeter) == perimeter:
        return (perimeter)
    return 0


mydict = {}
for one_side in range(1,400):
    for other_side in range(one_side + 1, 400):
        if perimeter_calc(one_side, other_side) > 1:
            perimeter = perimeter_calc(one_side, other_side)
            if str(perimeter) in mydict:
                mydict[str(perimeter)] += 1
            else:
                mydict[str(perimeter)] = 1

#Its just for getting rid of perimeters above 1000
to_delete =[]
for key in mydict:
    if float(key) > 1000:
        to_delete.append(key)
for item in to_delete:
    del mydict[item]


print(sorted(mydict.items(), key=lambda x:x[1], reverse=True))
