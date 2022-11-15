summary = 0
a = 1
b = 1
while b <= 4000000:
    b = b + a #new fibonacci number
    a = b - a   #new previous fibonacci number
    if b % 2 == 0:
        summary += b

print(summary)
