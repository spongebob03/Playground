#2진수 -> 8진수
b='0b'+input()

#2진수 문자열->정수
b=int(b,2)
#정수->8진수(접두어 빼고)
b=format(b,'o')

print(b)
