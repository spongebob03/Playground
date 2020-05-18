s=input()

nlist=list()

#문자다이얼->숫자로 
for i in s:
    if i in ('A','B','C'):
        nlist.append(2+1)
    elif i in ('D','E','F'):
        nlist.append(3+1)
    elif i in ('G','H','I'):
        nlist.append(4+1)
    elif i in ('J','K','L'):
        nlist.append(5+1)
    elif i in ('M','N','O'):
        nlist.append(6+1)
    elif i in ('P','Q','R','S'):
        nlist.append(7+1)
    elif i in ('T','U','V'):
        nlist.append(8+1)
    elif i in ('W','X','Y','Z'):
        nlist.append(9+1)
#총 걸리는 시간
sum=0
for i in nlist:
    sum+=i
print(sum)
