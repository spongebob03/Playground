n=int(input())

nlist=list()
nlist.append(1)

for i in range(1,n):
    for j in nlist:
        if(j==1):
            nlist.append(0)
        else:
            nlist.append(1)
print(nlist)
