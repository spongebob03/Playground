f= open("numbers.txt","r")
f2=open("output.txt","w")
data=f.readlines()
sum=0
print(data)
# for i in data:
#     sum+=int(i)
# avg=sum/len(data)
# print(sum,avg)
# f2.write(str(sum)+" "+str(avg))
f.close()
f2.close()