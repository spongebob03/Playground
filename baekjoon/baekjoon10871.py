#정수 n개
n=input()
n=n.split()
print(n)
num=n[0]
x=n[1]

result=''

a=input()
a=a.split()

for i in a:
     print(i)
     if i < x:
          result=result+i+' '

print(result)
