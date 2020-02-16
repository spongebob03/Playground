def chan(a):
    y=0
    for i in range(0,len(a)-1):
        y=y+int(a[i])*(-10)**(len(a)-1-i)
        return y

print(chan('12345'))
#몰라 안풀려ㅜ
