#정수 2진수로 바꾸고
#몇승 자리가 1인지 작은 수부터출력
def idx(s):
    for i in range(len(s)-1,-1,-1):
        if(s[i]=='1'):
            print(len(s)-1-i,end=' ')
            
tc=int(input())
for j in range(0,tc):
    n=int(input())
    n=format(n,'b')

    idx(n)
    print()
