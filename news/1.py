y = 0
total = []
for x in range(0,999):
    if x%3 ==0 or x%5==0:
        total.append(x)

for x in total:
    y=y+x
print y
