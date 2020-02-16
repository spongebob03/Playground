#Knuth-Morris-Pratt -->KMP
import sys

x=input().split('-')
result=''
for i in range(0,len(x)):
    result+=(x[i][0])
print(result)
