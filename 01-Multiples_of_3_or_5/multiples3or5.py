summary = 0
a = 0
while a < 1000:
    if a % 5 == 0 or a % 3 == 0:
        summary += a
    a += 1

print(summary)
