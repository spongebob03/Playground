#백준에서는 한줄에 두 수를 입력받기때문에
#파이썬에서는 문자열로 받은 두 수를 나눠서 저장
num=input()
num_split=num.split()

a=int(num_split[0])
b=int(num_split[1])

print(a/b)

