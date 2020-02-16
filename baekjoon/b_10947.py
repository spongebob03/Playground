import random

lotto=list()
for i in range(0,6):
    r=random.randrange(1,45)
    if r not in lotto:
        lotto.append(r)
        
for i in lotto:
    print(i,end=' ')

