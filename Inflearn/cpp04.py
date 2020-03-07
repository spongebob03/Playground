#나이 계산
x=input()
print(x[:2])
if x[7]=='2':
    g='W'
    year=int("19"+x[:2])
elif x[7]=='4':
    g='W'
    year=int("20"+x[:2])
elif x[7]=='1':
    g='M'
    year=int("19"+x[:2])
elif x[7]=='3':
    g='M'
    year=int("20"+x[:2])

print(2019-year+1,g)
    
        
