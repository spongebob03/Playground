#비타알고 9월1주차 시공의 폭풍속으로
a=input().split()
b=input().split()

cnt=0

for i in b:
    if i not in a:
        cnt+=1

print(cnt)
    
