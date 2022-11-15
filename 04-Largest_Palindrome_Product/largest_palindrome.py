listof_pal = []

for x in range(100, 1000):
    for y in range(100, 1000):
        a = x*y
        b = list(str(a))
        for i in range(int(len(b) / 2)):
           if b[i] != b[len(b) - 1 - i]:
                break
        else:
            listof_pal.append(b)

listof_pal = [int("".join(listof_pal[i])) for i in range(len(listof_pal))] 

print(max(listof_pal))

"""  Explanation of line 13:
our list consists of list of strings before the statement in line 13.
i.e it was [['1',2','3','2','1'], ['2','5','2','5','2'], [,,,], etc].
In our statement we joined every strings in each sublist and we converted them to integers."""
 
